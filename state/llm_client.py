#!/usr/bin/env python3
"""Minimal LLM client used by state/kernel.py.

Design goals:
- stdlib-only (no extra dependencies)
- provider-agnostic, but with pragmatic support for:
  - OpenAI-compatible Chat Completions API
  - Ollama /api/chat
- returns token-usage when the provider supplies it

This module deliberately does not attempt retries/backoff; the kernel remains
sovereign and should decide stop/iterate behavior.
"""

from __future__ import annotations

import asyncio
import importlib
import json
import os
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Any, Literal


Provider = Literal["openai_compatible", "ollama", "mock"]


class LLMClientError(RuntimeError):
    pass


@dataclass(frozen=True)
class LLMUsage:
    prompt_tokens: int = 0
    completion_tokens: int = 0


@dataclass(frozen=True)
class LLMResponse:
    content: str
    usage: LLMUsage
    raw: dict[str, Any] | None = None


class LLMClient:
    def __init__(
        self,
        *,
        provider: Provider,
        model: str,
        base_url: str | None = None,
        api_key_env: str = "OPENAI_API_KEY",
        timeout_s: int = 90,
    ) -> None:
        self._provider: Provider = provider
        self._model = model
        self._base_url = (base_url or "").rstrip("/")
        self._api_key_env = api_key_env
        self._timeout_s = int(timeout_s)
        self._sdk_client: Any | None = None
        self._sdk_session: Any | None = None

        if self._provider == "openai_compatible" and not self._base_url:
            self._base_url = "https://api.openai.com/v1"
        if self._provider == "ollama" and not self._base_url:
            self._base_url = "http://localhost:11434"

    @property
    def provider(self) -> Provider:
        return self._provider

    def close(self) -> None:
        """Compatibility shutdown hook for kernel-managed lifecycle."""
        if self._sdk_client is not None:
            stop_fn = getattr(self._sdk_client, "stop", None)
            if callable(stop_fn):
                self._run_async(stop_fn())
            force_stop_fn = getattr(self._sdk_client, "force_stop", None)
            if callable(force_stop_fn):
                self._run_async(force_stop_fn())
        return None

    def chat(
        self,
        *,
        messages: list[dict[str, str]],
        temperature: float = 0.0,
        max_tokens: int | None = None,
    ) -> LLMResponse:
        if self._provider == "mock":
            return self._chat_mock(messages=messages)
        sdk_response = self._chat_copilot_sdk(messages=messages, temperature=temperature, max_tokens=max_tokens)
        if sdk_response is not None:
            return sdk_response
        if self._provider == "openai_compatible":
            return self._chat_openai_compatible(messages=messages, temperature=temperature, max_tokens=max_tokens)
        if self._provider == "ollama":
            return self._chat_ollama(messages=messages, temperature=temperature, max_tokens=max_tokens)
        raise LLMClientError(f"Unknown provider: {self._provider}")

    def _run_async(self, awaitable: Any) -> Any:
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            return asyncio.run(awaitable)
        if not loop.is_running():
            return loop.run_until_complete(awaitable)
        fresh = asyncio.new_event_loop()
        try:
            return fresh.run_until_complete(awaitable)
        finally:
            fresh.close()

    def _chat_copilot_sdk(
        self,
        *,
        messages: list[dict[str, str]],
        temperature: float,
        max_tokens: int | None,
    ) -> LLMResponse | None:
        if os.environ.get("KERNEL_LLM_USE_COPILOT_SDK", "1").strip().lower() in {"0", "false", "no"}:
            return None
        try:
            sdk_mod = importlib.import_module("copilot")
        except ImportError:
            return None

        copilot_client_cls = getattr(sdk_mod, "CopilotClient", None)
        client_options_cls = getattr(sdk_mod, "CopilotClientOptions", None)
        session_config_cls = getattr(sdk_mod, "SessionConfig", None)
        if not callable(copilot_client_cls):
            return None

        async def _send() -> LLMResponse:
            if self._sdk_client is None:
                options: Any | None = None
                if callable(client_options_cls):
                    options_kwargs: dict[str, Any] = {}
                    if self._base_url:
                        options_kwargs["base_url"] = self._base_url
                    if self._provider:
                        options_kwargs["provider"] = self._provider
                    api_key = os.environ.get(self._api_key_env, "").strip()
                    if api_key:
                        options_kwargs["api_key"] = api_key
                    options = client_options_cls(**options_kwargs)
                self._sdk_client = copilot_client_cls(options) if options is not None else copilot_client_cls()
                await self._sdk_client.start()
            if self._sdk_session is None:
                session_cfg = session_config_cls(model=self._model, provider=self._provider) if callable(session_config_cls) else None
                create_session = getattr(self._sdk_client, "create_session", None)
                if not callable(create_session):
                    raise LLMClientError("Copilot SDK client does not expose create_session()")
                self._sdk_session = (
                    await create_session(session_cfg) if session_cfg is not None else await create_session()
                )
            payload: dict[str, Any] = {"messages": messages, "temperature": float(temperature)}
            if max_tokens is not None:
                payload["max_tokens"] = int(max_tokens)
            send = getattr(self._sdk_session, "send", None)
            if not callable(send):
                raise LLMClientError("Copilot SDK session does not expose send()")
            result = await send(**payload)
            return self._normalize_sdk_response(result)

        try:
            return self._run_async(_send())
        except Exception as exc:
            raise LLMClientError(f"Copilot SDK chat failed: {exc}") from exc

    def _normalize_sdk_response(self, result: Any) -> LLMResponse:
        raw: dict[str, Any] | None = result if isinstance(result, dict) else None
        content = ""
        usage = self._extract_sdk_usage(result)
        if isinstance(result, dict):
            if isinstance(result.get("content"), str):
                content = result["content"]
            elif isinstance(result.get("message"), dict):
                content = str(result["message"].get("content", ""))
        if not content:
            content_attr = getattr(result, "content", None)
            if isinstance(content_attr, str):
                content = content_attr
        return LLMResponse(content=str(content), usage=usage, raw=raw)

    def _extract_sdk_usage(self, result: Any) -> LLMUsage:
        direct = self._usage_from_any(result)
        if direct is not None:
            return direct

        events: Any = None
        if isinstance(result, dict):
            events = result.get("events")
        if events is None:
            events = getattr(result, "events", None)
        if isinstance(events, list):
            prompt_tokens = 0
            completion_tokens = 0
            for event in events:
                if not isinstance(event, dict):
                    continue
                event_name = str(event.get("type") or event.get("event") or "")
                if event_name and event_name != "assistant.usage":
                    continue
                usage = self._usage_from_any(event.get("usage"))
                if usage is None:
                    usage = self._usage_from_any(event.get("data"))
                if usage is None:
                    continue
                prompt_tokens += usage.prompt_tokens
                completion_tokens += usage.completion_tokens
            return LLMUsage(prompt_tokens=prompt_tokens, completion_tokens=completion_tokens)
        return LLMUsage()

    def _usage_from_any(self, payload: Any) -> LLMUsage | None:
        if isinstance(payload, dict):
            usage_raw = payload.get("usage") if isinstance(payload.get("usage"), dict) else payload
            token_keys = {"prompt_tokens", "completion_tokens", "input_tokens", "output_tokens"}
            if not any(key in usage_raw for key in token_keys):
                return None
            prompt = usage_raw.get("prompt_tokens", usage_raw.get("input_tokens", 0))
            completion = usage_raw.get("completion_tokens", usage_raw.get("output_tokens", 0))
            return LLMUsage(prompt_tokens=int(prompt or 0), completion_tokens=int(completion or 0))
        usage_attr = getattr(payload, "usage", None)
        if isinstance(usage_attr, dict):
            return self._usage_from_any(usage_attr)
        if isinstance(getattr(payload, "prompt_tokens", None), int) or isinstance(
            getattr(payload, "completion_tokens", None), int
        ):
            return LLMUsage(
                prompt_tokens=int(getattr(payload, "prompt_tokens", 0) or 0),
                completion_tokens=int(getattr(payload, "completion_tokens", 0) or 0),
            )
        return None

    def _http_json(self, *, url: str, payload: dict[str, Any], headers: dict[str, str] | None = None) -> dict[str, Any]:
        body = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            url=url,
            data=body,
            headers={"Content-Type": "application/json", **(headers or {})},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=self._timeout_s) as resp:
                raw = resp.read().decode("utf-8")
        except urllib.error.HTTPError as exc:
            details = ""
            try:
                details = exc.read().decode("utf-8")
            except Exception:
                details = ""
            raise LLMClientError(f"HTTP {exc.code} from LLM provider: {details or exc}") from exc
        except urllib.error.URLError as exc:
            raise LLMClientError(f"LLM provider connection error: {exc}") from exc

        try:
            out = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise LLMClientError(f"LLM provider returned non-JSON response: {raw[:500]}") from exc

        if not isinstance(out, dict):
            raise LLMClientError("LLM provider returned unexpected JSON shape (expected object)")
        return out

    def _chat_openai_compatible(
        self,
        *,
        messages: list[dict[str, str]],
        temperature: float,
        max_tokens: int | None,
    ) -> LLMResponse:
        api_key = os.environ.get(self._api_key_env, "").strip()
        if not api_key:
            raise LLMClientError(
                f"Missing API key env var {self._api_key_env}. "
                "Set it or use --llm-provider ollama (local) or --llm-provider mock."
            )

        payload: dict[str, Any] = {
            "model": self._model,
            "messages": messages,
            "temperature": float(temperature),
        }
        if max_tokens is not None:
            payload["max_tokens"] = int(max_tokens)

        out = self._http_json(
            url=f"{self._base_url}/chat/completions",
            payload=payload,
            headers={"Authorization": f"Bearer {api_key}"},
        )

        try:
            content = out["choices"][0]["message"]["content"]
        except Exception as exc:
            raise LLMClientError("OpenAI-compatible response missing choices[0].message.content") from exc

        usage_raw = out.get("usage")
        usage = LLMUsage(
            prompt_tokens=int(usage_raw.get("prompt_tokens", 0) or 0) if isinstance(usage_raw, dict) else 0,
            completion_tokens=int(usage_raw.get("completion_tokens", 0) or 0) if isinstance(usage_raw, dict) else 0,
        )
        return LLMResponse(content=str(content), usage=usage, raw=out)

    def _chat_ollama(
        self,
        *,
        messages: list[dict[str, str]],
        temperature: float,
        max_tokens: int | None,
    ) -> LLMResponse:
        payload: dict[str, Any] = {
            "model": self._model,
            "messages": messages,
            "stream": False,
            "options": {
                "temperature": float(temperature),
            },
        }
        if max_tokens is not None:
            payload["options"]["num_predict"] = int(max_tokens)

        out = self._http_json(url=f"{self._base_url}/api/chat", payload=payload)

        try:
            content = out["message"]["content"]
        except Exception as exc:
            raise LLMClientError("Ollama response missing message.content") from exc

        # Ollama usage fields vary by version; normalize best-effort.
        prompt_tokens = int(out.get("prompt_eval_count", 0) or 0)
        completion_tokens = int(out.get("eval_count", 0) or 0)
        usage = LLMUsage(prompt_tokens=prompt_tokens, completion_tokens=completion_tokens)
        return LLMResponse(content=str(content), usage=usage, raw=out)

    def _chat_mock(self, *, messages: list[dict[str, str]]) -> LLMResponse:
        # Deterministic, safe mock: always produces schema-conforming outputs that
        # force the kernel to keep iterating (critic decision=refine).
        joined = "\n".join(m.get("content", "") for m in messages)

        if "Planner" in joined and "target_word_delta" in joined:
            content = json.dumps(
                {
                    "focus_areas": ["## Thesis: tighten scope"],
                    "structural_changes": [],
                    "risk_flags": ["possible repetition"],
                    "target_word_delta": "+0",
                },
                sort_keys=True,
            )
            return LLMResponse(content=content, usage=LLMUsage())

        if "===CHAPTER_START===" in joined and "===CHAPTER_END===" in joined:
            lo = joined.find("===CHAPTER_START===")
            hi = joined.find("===CHAPTER_END===")
            if lo != -1 and hi != -1 and hi > lo:
                chapter = joined[lo + len("===CHAPTER_START===") : hi]
                return LLMResponse(content=chapter.strip() + "\n", usage=LLMUsage())
            return LLMResponse(content="\n", usage=LLMUsage())

        if "Critic" in joined and "violations" in joined:
            content = json.dumps(
                {
                    "structure_score": 0.0,
                    "clarity_score": 0.0,
                    "example_density": 0.0,
                    "tradeoff_presence": False,
                    "failure_modes_present": False,
                    "drift_score": 1.0,
                    "violations": ["MOCK: not a real evaluation"],
                    "decision": "refine",
                },
                sort_keys=True,
            )
            return LLMResponse(content=content, usage=LLMUsage())

        return LLMResponse(content="", usage=LLMUsage())

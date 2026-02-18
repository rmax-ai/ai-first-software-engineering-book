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

        if self._provider == "openai_compatible" and not self._base_url:
            self._base_url = "https://api.openai.com/v1"
        if self._provider == "ollama" and not self._base_url:
            self._base_url = "http://localhost:11434"

    @property
    def provider(self) -> Provider:
        return self._provider

    def chat(
        self,
        *,
        messages: list[dict[str, str]],
        temperature: float = 0.0,
        max_tokens: int | None = None,
    ) -> LLMResponse:
        if self._provider == "openai_compatible":
            return self._chat_openai_compatible(messages=messages, temperature=temperature, max_tokens=max_tokens)
        if self._provider == "ollama":
            return self._chat_ollama(messages=messages, temperature=temperature, max_tokens=max_tokens)
        if self._provider == "mock":
            return self._chat_mock(messages=messages)
        raise LLMClientError(f"Unknown provider: {self._provider}")

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

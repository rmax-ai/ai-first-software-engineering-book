#!/usr/bin/env python3
"""Minimal LLM client used by state/kernel.py.

Design goals:
- stdlib-only (no extra dependencies)
- Copilot SDK backed (with deterministic mock fallback)
- returns token-usage when the provider supplies it

This module deliberately does not attempt retries/backoff; the kernel remains
sovereign and should decide stop/iterate behavior.
"""

from __future__ import annotations

import asyncio
import importlib
import json
import os
import threading
from dataclasses import dataclass
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, ValidationError


Provider = Literal["copilot", "mock"]


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


class ChatMessagePayload(BaseModel):
    model_config = ConfigDict(extra="forbid")

    role: str = Field(default="user")
    content: str


class ChatMessagesPayload(BaseModel):
    model_config = ConfigDict(extra="forbid")

    messages: list[ChatMessagePayload]


class SDKUsagePayload(BaseModel):
    model_config = ConfigDict(extra="allow")

    prompt_tokens: int | None = None
    completion_tokens: int | None = None
    input_tokens: int | None = None
    output_tokens: int | None = None

    def to_usage(self) -> LLMUsage:
        prompt = self.prompt_tokens if self.prompt_tokens is not None else self.input_tokens
        completion = self.completion_tokens if self.completion_tokens is not None else self.output_tokens
        return LLMUsage(prompt_tokens=int(prompt or 0), completion_tokens=int(completion or 0))


class SDKMessagePayload(BaseModel):
    model_config = ConfigDict(extra="allow")

    content: str | None = None


class SDKChatResponsePayload(BaseModel):
    model_config = ConfigDict(extra="allow")

    content: str | None = None
    message: SDKMessagePayload | None = None
    usage: SDKUsagePayload | None = None


@dataclass(frozen=True)
class ChatMessagesTransit:
    payload: ChatMessagesPayload

    @classmethod
    def from_raw(cls, messages: list[dict[str, str]]) -> "ChatMessagesTransit":
        return cls(payload=ChatMessagesPayload.model_validate({"messages": messages}))

    @property
    def message_payloads(self) -> list[ChatMessagePayload]:
        return self.payload.messages


@dataclass(frozen=True)
class SDKChatResponseTransit:
    raw: dict[str, Any]
    payload: SDKChatResponsePayload

    @classmethod
    def from_raw(cls, raw: dict[str, Any]) -> "SDKChatResponseTransit":
        return cls(raw=raw, payload=SDKChatResponsePayload.model_validate(raw))

    def content_text(self) -> str:
        if isinstance(self.payload.content, str):
            return self.payload.content
        if self.payload.message and isinstance(self.payload.message.content, str):
            return self.payload.message.content
        return ""

    def usage(self) -> LLMUsage | None:
        if self.payload.usage is None:
            return None
        return self.payload.usage.to_usage()


class LLMClient:
    def __init__(
        self,
        *,
        provider: Provider,
        model: str,
        base_url: str | None = None,
        api_key_env: str = "COPILOT_API_KEY",
        timeout_s: int = 90,
    ) -> None:
        self._provider: Provider = provider
        self._model = model
        self._base_url = (base_url or "").rstrip("/")
        self._api_key_env = api_key_env
        self._timeout_s = int(timeout_s)
        self._sdk_client: Any | None = None
        self._sdk_session: Any | None = None
        self._sdk_loop: asyncio.AbstractEventLoop | None = None
        self._sdk_thread_loop: asyncio.AbstractEventLoop | None = None
        self._sdk_thread: threading.Thread | None = None


    @property
    def provider(self) -> Provider:
        return self._provider

    def close(self) -> None:
        """Compatibility shutdown hook for kernel-managed lifecycle."""
        shutdown_errors: list[str] = []
        try:
            if self._sdk_session is not None:
                destroy_fn = getattr(self._sdk_session, "destroy", None)
                if callable(destroy_fn):
                    try:
                        self._run_async(destroy_fn())
                    except Exception as destroy_exc:
                        detail = str(destroy_exc).strip() or destroy_exc.__class__.__name__
                        shutdown_errors.append(f"session.destroy()={detail}")

            if self._sdk_client is not None:
                stop_fn = getattr(self._sdk_client, "stop", None)
                if callable(stop_fn):
                    try:
                        self._run_async(stop_fn())
                    except Exception as stop_exc:
                        stop_detail = str(stop_exc).strip() or stop_exc.__class__.__name__
                        force_stop_fn = getattr(self._sdk_client, "force_stop", None)
                        if callable(force_stop_fn):
                            try:
                                self._run_async(force_stop_fn())
                            except Exception as force_exc:
                                force_detail = str(force_exc).strip() or force_exc.__class__.__name__
                                shutdown_errors.append(f"stop()={stop_detail}; force_stop()={force_detail}")
                        else:
                            shutdown_errors.append(f"stop()={stop_detail}; force_stop() unavailable")
                else:
                    shutdown_errors.append("stop() unavailable")
        finally:
            self._sdk_session = None
            self._sdk_client = None
            self._close_sdk_loop()

        if shutdown_errors:
            raise LLMClientError("Copilot SDK shutdown failed: " + "; ".join(shutdown_errors))
        return None

    def _close_sdk_loop(self) -> None:
        if self._sdk_loop is not None and not self._sdk_loop.is_closed():
            self._sdk_loop.close()
        if self._sdk_thread_loop is not None:
            if self._sdk_thread_loop.is_running():
                self._sdk_thread_loop.call_soon_threadsafe(self._sdk_thread_loop.stop)
            if self._sdk_thread is not None and self._sdk_thread.is_alive():
                self._sdk_thread.join(timeout=1.0)
            if not self._sdk_thread_loop.is_running() and not self._sdk_thread_loop.is_closed():
                self._sdk_thread_loop.close()
        self._sdk_loop = None
        self._sdk_thread_loop = None
        self._sdk_thread = None

    def _ensure_sdk_thread_loop(self) -> asyncio.AbstractEventLoop:
        if self._sdk_thread_loop is not None and self._sdk_thread_loop.is_running():
            return self._sdk_thread_loop

        ready = threading.Event()
        startup: dict[str, Any] = {}

        def _runner() -> None:
            loop: asyncio.AbstractEventLoop | None = None
            try:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                startup["loop"] = loop
            except Exception as exc:
                startup["error"] = exc
            finally:
                ready.set()

            if loop is not None:
                loop.run_forever()
                loop.close()

        thread = threading.Thread(target=_runner, name="llm-client-sdk-loop", daemon=True)
        thread.start()
        startup_timeout_s = max(1.0, min(float(self._timeout_s), 10.0))
        if not ready.wait(timeout=startup_timeout_s):
            raise LLMClientError(
                f"Copilot SDK worker-loop bootstrap failed: startup timeout after {startup_timeout_s:.1f}s"
            )
        if "error" in startup:
            raise self._sdk_stage_error("worker-loop bootstrap", startup["error"])
        loop = startup.get("loop")
        if not isinstance(loop, asyncio.AbstractEventLoop):
            raise LLMClientError("Copilot SDK worker-loop bootstrap failed: loop was not created")
        self._sdk_thread = thread
        self._sdk_thread_loop = loop
        return self._sdk_thread_loop

    def chat(
        self,
        *,
        messages: list[dict[str, str]],
        temperature: float = 0.0,
        max_tokens: int | None = None,
    ) -> LLMResponse:
        try:
            transit = ChatMessagesTransit.from_raw(messages)
        except ValidationError as exc:
            raise LLMClientError(f"Invalid chat messages payload: {exc}") from exc
        if self._provider == "mock":
            return self._chat_mock(messages=transit.message_payloads)
        if self._provider != "copilot":
            raise LLMClientError(f"Unknown provider: {self._provider}")
        return self._chat_copilot_sdk(
            messages=transit.message_payloads,
            temperature=temperature,
            max_tokens=max_tokens,
        )

    def _run_async(self, awaitable: Any) -> Any:
        """Run coroutine from sync code; nested-loop calls use a dedicated SDK worker loop."""
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            if self._sdk_loop is None or self._sdk_loop.is_closed():
                self._sdk_loop = asyncio.new_event_loop()
            return self._sdk_loop.run_until_complete(awaitable)
        if not loop.is_running():
            return loop.run_until_complete(awaitable)
        worker_loop = self._ensure_sdk_thread_loop()
        future = asyncio.run_coroutine_threadsafe(awaitable, worker_loop)
        return future.result()

    def _chat_copilot_sdk(
        self,
        *,
        messages: list[ChatMessagePayload],
        temperature: float,
        max_tokens: int | None,
    ) -> LLMResponse:
        try:
            sdk_mod = importlib.import_module("copilot")
        except ImportError as exc:
            raise LLMClientError(
                "Copilot SDK unavailable: install `github-copilot-sdk` to use provider='copilot'"
            ) from exc

        copilot_client_cls = getattr(sdk_mod, "CopilotClient", None)
        client_options_cls = getattr(sdk_mod, "CopilotClientOptions", None)
        session_config_cls = getattr(sdk_mod, "SessionConfig", None)
        if not callable(copilot_client_cls):
            raise LLMClientError("Copilot SDK module missing required CopilotClient class")

        async def _send() -> LLMResponse:
            if self._sdk_client is None:
                options: Any | None = None
                if callable(client_options_cls):
                    options_kwargs: dict[str, Any] = {}
                    if self._base_url:
                        options_kwargs["base_url"] = self._base_url
                    api_key = os.environ.get(self._api_key_env, "").strip()
                    if api_key:
                        options_kwargs["api_key"] = api_key
                    try:
                        options = client_options_cls(**options_kwargs)
                    except Exception as exc:
                        raise self._sdk_stage_error("options initialization", exc) from exc
                try:
                    self._sdk_client = copilot_client_cls(options) if options is not None else copilot_client_cls()
                except Exception as exc:
                    raise self._sdk_stage_error("client initialization", exc) from exc
                try:
                    await self._sdk_client.start()
                except Exception as exc:
                    raise self._sdk_stage_error("client startup", exc) from exc
            if self._sdk_session is None:
                session_cfg_obj: Any | None = None
                session_cfg_dict: dict[str, Any] = {"model": self._model}
                if callable(session_config_cls):
                    try:
                        session_cfg_obj = session_config_cls(model=self._model)
                    except Exception:
                        session_cfg_obj = None
                create_session = getattr(self._sdk_client, "create_session", None)
                if not callable(create_session):
                    raise LLMClientError("Copilot SDK client does not expose create_session()")
                try:
                    if session_cfg_obj is not None:
                        self._sdk_session = await create_session(session_cfg_obj)
                    else:
                        self._sdk_session = await create_session(session_cfg_dict)
                except Exception as exc:
                    try:
                        self._sdk_session = await create_session(session_cfg_dict)
                    except Exception:
                        raise self._sdk_stage_error("session creation", exc) from exc
            payload: dict[str, Any] = {
                "messages": [message.model_dump() for message in messages],
                "temperature": float(temperature),
            }
            if max_tokens is not None:
                payload["max_tokens"] = int(max_tokens)
            send_and_wait = getattr(self._sdk_session, "send_and_wait", None)
            if callable(send_and_wait):
                prompt_text = self._messages_to_prompt(messages)
                try:
                    result = await send_and_wait({"prompt": prompt_text}, timeout=float(self._timeout_s))
                    return await self._normalize_sdk_session_result(result, self._sdk_session)
                except Exception as exc:
                    raise self._sdk_stage_error("message send", exc) from exc
            send = getattr(self._sdk_session, "send", None)
            if not callable(send):
                raise LLMClientError("Copilot SDK session does not expose send()")
            try:
                result = await send(**payload)
            except Exception as exc:
                prompt_text = self._messages_to_prompt(messages)
                try:
                    message_id = await send({"prompt": prompt_text})
                    get_messages = getattr(self._sdk_session, "get_messages", None)
                    if callable(get_messages):
                        events = await get_messages()
                        return self._response_from_sdk_events(events, message_id=message_id)
                    raise self._sdk_stage_error("message send", exc)
                except Exception:
                    raise self._sdk_stage_error("message send", exc) from exc
            return self._normalize_sdk_response(result)

        try:
            return self._run_async(_send())
        except LLMClientError:
            raise
        except Exception as exc:
            raise LLMClientError(f"Copilot SDK chat failed: {exc}") from exc

    def _sdk_stage_error(self, stage: str, exc: Exception) -> LLMClientError:
        detail = str(exc).strip() or exc.__class__.__name__
        return LLMClientError(f"Copilot SDK {stage} failed: {detail}")

    def _messages_to_prompt(self, messages: list[ChatMessagePayload]) -> str:
        rendered: list[str] = []
        for item in messages:
            role = item.role.strip().lower() or "user"
            content = item.content
            rendered.append(f"[{role}]\n{content}")
        return "\n\n".join(rendered).strip()

    async def _normalize_sdk_session_result(self, result: Any, session: Any) -> LLMResponse:
        if result is not None:
            event_type = self._sdk_event_type_name(getattr(result, "type", ""))
            data = getattr(result, "data", None)
            if event_type in {"assistant.message", "assistant_message"}:
                content = str(getattr(data, "content", "") or "")
                usage = self._usage_from_any(data)
                if usage is None:
                    get_messages = getattr(session, "get_messages", None)
                    if callable(get_messages):
                        events = await get_messages()
                        fallback = self._response_from_sdk_events(events, message_id=getattr(data, "message_id", None))
                        usage = fallback.usage
                usage = usage or LLMUsage()
                return LLMResponse(content=content, usage=usage, raw=None)
            if event_type in {"session.error", "session_error"}:
                message = str(getattr(data, "message", "unknown session error"))
                raise LLMClientError(f"Copilot SDK session error: {message}")

        get_messages = getattr(session, "get_messages", None)
        if callable(get_messages):
            events = await get_messages()
            return self._response_from_sdk_events(events)
        return LLMResponse(content="", usage=LLMUsage(), raw=None)

    def _response_from_sdk_events(self, events: Any, message_id: str | None = None) -> LLMResponse:
        if isinstance(events, list):
            prompt_tokens = 0
            completion_tokens = 0

            for event in events:
                event_type = self._sdk_event_type_name(getattr(event, "type", ""))
                data = getattr(event, "data", None)
                if event_type not in {"assistant.usage", "assistant_usage"}:
                    continue
                usage = self._usage_from_any(data)
                if usage is None:
                    continue
                prompt_tokens += usage.prompt_tokens
                completion_tokens += usage.completion_tokens

            for event in reversed(events):
                event_type = self._sdk_event_type_name(getattr(event, "type", ""))
                data = getattr(event, "data", None)
                if event_type in {"assistant.message", "assistant_message"}:
                    if message_id is not None:
                        event_message_id = getattr(data, "message_id", None)
                        if event_message_id and event_message_id != message_id:
                            continue
                    content = str(getattr(data, "content", "") or "")
                    usage = self._usage_from_any(data)
                    if usage is None:
                        usage = LLMUsage(prompt_tokens=prompt_tokens, completion_tokens=completion_tokens)
                    return LLMResponse(content=content, usage=usage, raw=None)
                if event_type in {"session.error", "session_error"}:
                    message = str(getattr(data, "message", "unknown session error"))
                    raise LLMClientError(f"Copilot SDK session error: {message}")

            if prompt_tokens or completion_tokens:
                return LLMResponse(content="", usage=LLMUsage(prompt_tokens=prompt_tokens, completion_tokens=completion_tokens), raw=None)
        return LLMResponse(content="", usage=LLMUsage(), raw=None)

    def _sdk_event_type_name(self, value: Any) -> str:
        normalized = getattr(value, "value", value)
        text = str(normalized).strip().lower()
        if text.startswith("sessioneventtype."):
            text = text.split(".", 1)[1]
        return text

    def _normalize_sdk_response(self, result: Any) -> LLMResponse:
        raw: dict[str, Any] | None = result if isinstance(result, dict) else None
        transit: SDKChatResponseTransit | None = None
        if raw is not None:
            try:
                transit = SDKChatResponseTransit.from_raw(raw)
            except ValidationError as exc:
                raise LLMClientError(f"Invalid Copilot SDK response payload: {exc}") from exc
        content = transit.content_text() if transit is not None else ""
        usage = self._extract_sdk_usage(result)
        if transit is not None:
            payload_usage = transit.usage()
            if payload_usage is not None:
                usage = payload_usage
        if not content:
            content_attr = getattr(result, "content", None)
            if isinstance(content_attr, str):
                content = content_attr
        return LLMResponse(content=str(content), usage=usage, raw=transit.raw if transit is not None else raw)

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
                event_name = self._sdk_event_type_name(
                    event.get("type") if isinstance(event, dict) else getattr(event, "type", "")
                )
                if event_name not in {"assistant.usage", "assistant_usage"}:
                    continue
                usage = self._usage_from_any(event.get("usage") if isinstance(event, dict) else None)
                if usage is None:
                    usage = self._usage_from_any(event.get("data") if isinstance(event, dict) else getattr(event, "data", None))
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
        prompt_attr = getattr(payload, "prompt_tokens", getattr(payload, "input_tokens", None))
        completion_attr = getattr(payload, "completion_tokens", getattr(payload, "output_tokens", None))
        if prompt_attr is not None or completion_attr is not None:
            return LLMUsage(
                prompt_tokens=int(prompt_attr or 0),
                completion_tokens=int(completion_attr or 0),
            )
        return None

    def _chat_mock(self, *, messages: list[ChatMessagePayload]) -> LLMResponse:
        # Deterministic, safe mock: always produces schema-conforming outputs that
        # force the kernel to keep iterating (critic decision=refine).
        joined = "\n".join(message.content for message in messages)

        if "===CHAPTER_START===" in joined and "===CHAPTER_END===" in joined:
            lo = joined.find("===CHAPTER_START===")
            hi = joined.find("===CHAPTER_END===")
            if lo != -1 and hi != -1 and hi > lo:
                chapter = joined[lo + len("===CHAPTER_START===") : hi]
                return LLMResponse(content=chapter.strip() + "\n", usage=LLMUsage())
            return LLMResponse(content="\n", usage=LLMUsage())

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

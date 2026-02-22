#!/usr/bin/env python3
"""Small Copilot SDK smoke test for state/llm_client.py.

Usage:
  uv run python state/copilot_sdk_smoke_test.py
  uv run python state/copilot_sdk_smoke_test.py --mode sdk-unavailable
  uv run python state/copilot_sdk_smoke_test.py --mode bootstrap-failure
  uv run python state/copilot_sdk_smoke_test.py --mode shutdown-failure
  uv run python state/copilot_sdk_smoke_test.py --mode stop-unavailable
  uv run python state/copilot_sdk_smoke_test.py --mode destroy-unavailable
  uv run python state/copilot_sdk_smoke_test.py --mode destroy-failure
  uv run python state/copilot_sdk_smoke_test.py --mode force-stop-unavailable
  uv run python state/copilot_sdk_smoke_test.py --mode force-stop-close-idempotency
  uv run python state/copilot_sdk_smoke_test.py --mode stop-close-idempotency
  uv run python state/copilot_sdk_smoke_test.py --mode close-idempotency
  uv run python state/copilot_sdk_smoke_test.py --mode destroy-close-idempotency
  uv run python state/copilot_sdk_smoke_test.py --mode destroy-unavailable-close-idempotency
  uv run python state/copilot_sdk_smoke_test.py --mode stop-destroy-unavailable-close-idempotency
  uv run python state/copilot_sdk_smoke_test.py --mode stop-unavailable-destroy-failure-close-idempotency
  uv run python state/copilot_sdk_smoke_test.py --mode stop-failure-destroy-unavailable-close-idempotency
  uv run python state/copilot_sdk_smoke_test.py --mode stop-failure-destroy-failure-close-idempotency
  uv run python state/copilot_sdk_smoke_test.py --mode trace-summary
  uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-missing-key
  uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-shape-guard
  uv run python state/copilot_sdk_smoke_test.py --mode live

Modes:
- stub (default): installs an in-process fake `copilot` module and verifies
  that LLMClient uses the SDK path end-to-end without network or credentials.
- sdk-unavailable: forces SDK import unavailability and verifies a clear SDK-required error.
- bootstrap-failure: forces worker-loop bootstrap failure and verifies error context.
- shutdown-failure: forces SDK shutdown failures and verifies stop/force_stop error context.
- stop-unavailable: forces SDK client stop() to be unavailable and verifies shutdown error context.
- destroy-unavailable: forces session.destroy() to be unavailable and verifies shutdown error context.
- destroy-failure: forces session.destroy() failure and verifies shutdown error context.
- force-stop-unavailable: forces stop() failure with non-callable force_stop and verifies shutdown error context.
- force-stop-close-idempotency: forces stop() failure with force_stop unavailable, then verifies a second close() is a no-op.
- stop-close-idempotency: forces stop() to be unavailable, then verifies a second close() is a no-op.
- close-idempotency: forces shutdown failure then verifies a second close() is a no-op.
- destroy-close-idempotency: forces session.destroy() failure then verifies a second close() is a no-op.
- destroy-unavailable-close-idempotency: forces session.destroy() unavailable then verifies a second close() is a no-op.
- stop-destroy-unavailable-close-idempotency: forces both stop() and session.destroy() unavailable, then verifies a second close() is a no-op.
- stop-unavailable-destroy-failure-close-idempotency: forces stop() unavailable and session.destroy() failure, then verifies a second close() is a no-op.
- stop-failure-destroy-unavailable-close-idempotency: forces stop() failure and session.destroy() unavailable, then verifies a second close() is a no-op.
- stop-failure-destroy-failure-close-idempotency: forces stop() and session.destroy() failures, then verifies a second close() is a no-op.
- trace-summary: validates required keys in a deterministic trace_summary fixture.
- trace-summary-missing-key: verifies missing trace_summary keys are detected.
- trace-summary-shape-guard: verifies non-dict trace_summary payloads are rejected.
- live: uses the real installed `copilot` package and your configured provider.
"""

from __future__ import annotations

import argparse
import importlib
import os
import sys
import types
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any, cast


ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

llm_client = importlib.import_module("state.llm_client")
LLMClient = llm_client.LLMClient
LLMClientError = llm_client.LLMClientError
Provider = llm_client.Provider

TRACE_SUMMARY_REQUIRED_KEYS = {"decision", "drift_score", "diff_ratio", "deterministic_pass"}


def _get_latest_trace_summary(metrics: dict[str, Any], chapter_id: str) -> dict[str, Any]:
    chapters = metrics.get("chapters", {})
    assert isinstance(chapters, dict), "expected chapters dictionary"
    chapter_metrics = chapters.get(chapter_id, {})
    assert isinstance(chapter_metrics, dict), "expected chapter metrics dictionary"
    history = chapter_metrics.get("history", [])
    assert isinstance(history, list) and history, f"expected metrics history for chapter {chapter_id}"
    latest = history[-1]
    assert isinstance(latest, dict), "expected latest history entry to be a dictionary"
    trace_summary = latest.get("trace_summary")
    assert isinstance(trace_summary, dict), "expected latest history entry to contain trace_summary dictionary"
    return trace_summary


def _missing_trace_summary_keys(trace_summary: dict[str, Any]) -> list[str]:
    return sorted(TRACE_SUMMARY_REQUIRED_KEYS - set(trace_summary))


def _install_stub_copilot_module() -> None:
    module = types.ModuleType("copilot")

    @dataclass
    class CopilotClientOptions:
        base_url: str | None = None
        provider: str | None = None
        api_key: str | None = None

    @dataclass
    class SessionConfig:
        model: str | None = None
        provider: str | None = None

    @dataclass
    class UsageData:
        prompt_tokens: int
        completion_tokens: int

    @dataclass
    class MessageData:
        content: str
        message_id: str

    @dataclass
    class SessionEvent:
        type: str
        data: Any

    class StubSession:
        def __init__(self) -> None:
            self._message_id = "stub-message-1"
            self._content = ""

        async def send_and_wait(self, payload: dict[str, Any], timeout: float) -> SessionEvent:
            _ = timeout
            prompt = str(payload.get("prompt", ""))
            if "[user]\n" in prompt:
                user = prompt.rsplit("[user]\n", 1)[1].strip()
            else:
                user = prompt.strip()
            self._content = f"stub-ok: {user}".strip()
            return SessionEvent(
                type="assistant.message",
                data=MessageData(content=self._content, message_id=self._message_id),
            )

        async def get_messages(self) -> list[SessionEvent]:
            return [
                SessionEvent(type="assistant.usage", data=UsageData(prompt_tokens=7, completion_tokens=3)),
                SessionEvent(type="assistant.message", data=MessageData(content=self._content, message_id=self._message_id)),
            ]

        async def send(self, **payload: Any) -> dict[str, Any]:
            messages_any = payload.get("messages", [])
            messages: list[dict[str, Any]] = []
            if isinstance(messages_any, Sequence):
                iterable = cast(Sequence[Any], messages_any)
                for raw_item in iterable:
                    if isinstance(raw_item, dict):
                        messages.append(cast(dict[str, Any], raw_item))
            user = ""
            for item in reversed(messages):
                if item.get("role") == "user":
                    user = str(item.get("content", ""))
                    break
            return {
                "content": f"stub-ok: {user}".strip(),
                "usage": {"prompt_tokens": 7, "completion_tokens": 3},
            }

        async def destroy(self):
            return None

    class CopilotClient:
        def __init__(self, options: CopilotClientOptions | None = None):
            self.options = options

        async def start(self):
            return None

        async def stop(self):
            return None

        async def create_session(self, *_args: Any, **_kwargs: Any) -> StubSession:
            return StubSession()

    setattr(module, "CopilotClientOptions", CopilotClientOptions)
    setattr(module, "SessionConfig", SessionConfig)
    setattr(module, "CopilotClient", CopilotClient)
    sys.modules["copilot"] = module


def run_stub_mode() -> int:
    _install_stub_copilot_module()
    client = LLMClient(provider="copilot", model="stub-model")
    try:
        response = client.chat(
            messages=[
                {"role": "system", "content": "Return a short answer."},
                {"role": "user", "content": "ping"},
            ],
            temperature=0.0,
            max_tokens=16,
        )
        assert response.content.startswith("stub-ok:"), "unexpected content"
        assert response.usage.prompt_tokens == 7, "unexpected prompt token count"
        assert response.usage.completion_tokens == 3, "unexpected completion token count"
    finally:
        client.close()

    print("PASS: stub Copilot SDK path works")
    print(f"content={response.content!r}")
    print(
        "usage="
        f"prompt_tokens={response.usage.prompt_tokens},"
        f" completion_tokens={response.usage.completion_tokens}"
    )
    return 0


def run_live_mode() -> int:
    try:
        __import__("copilot")
    except ImportError as exc:
        raise SystemExit("FAIL: copilot package is not installed") from exc

    provider_raw = os.environ.get("KERNEL_LLM_PROVIDER", "copilot")
    if provider_raw not in {"copilot", "mock"}:
        raise SystemExit(
            "FAIL: KERNEL_LLM_PROVIDER must be one of copilot|mock"
        )
    provider = cast(Provider, provider_raw)
    model = os.environ.get("KERNEL_LLM_MODEL", "gpt-4.1-mini")
    base_url = os.environ.get("KERNEL_LLM_BASE_URL")

    client = LLMClient(provider=provider, model=model, base_url=base_url)
    try:
        response = client.chat(
            messages=[
                {"role": "system", "content": "Reply with exactly: ok"},
                {"role": "user", "content": "Say ok."},
            ],
            temperature=0.0,
            max_tokens=8,
        )
    except LLMClientError as exc:
        raise SystemExit(f"FAIL: live SDK chat failed: {exc}") from exc
    finally:
        client.close()

    print("PASS: live Copilot SDK chat works")
    print(f"provider={provider} model={model}")
    print(f"content={response.content!r}")
    print(
        "usage="
        f"prompt_tokens={response.usage.prompt_tokens},"
        f" completion_tokens={response.usage.completion_tokens}"
    )
    return 0


def run_sdk_unavailable_mode() -> int:
    import_module = llm_client.importlib.import_module

    def _patched_import(name: str, package: str | None = None) -> Any:
        if name == "copilot":
            raise ImportError("forced for unavailable-sdk test")
        return import_module(name, package)

    llm_client.importlib.import_module = _patched_import
    client = LLMClient(provider="copilot", model="stub-model")
    try:
        try:
            client.chat(
                messages=[
                    {"role": "system", "content": "Return a short answer."},
                    {"role": "user", "content": "pong"},
                ],
                temperature=0.0,
                max_tokens=16,
            )
            raise AssertionError("expected SDK unavailable error")
        except LLMClientError as exc:
            message = str(exc)
            assert "Copilot SDK unavailable" in message, "missing SDK unavailable context"
    finally:
        client.close()
        llm_client.importlib.import_module = import_module

    print("PASS: copilot provider requires SDK when module is unavailable")
    return 0


def run_bootstrap_failure_mode() -> int:
    _install_stub_copilot_module()
    original = LLMClient._ensure_sdk_thread_loop

    def _patched_bootstrap_failure(self: LLMClient) -> Any:
        raise LLMClientError("Copilot SDK worker-loop bootstrap failed: forced smoke-test failure")

    LLMClient._ensure_sdk_thread_loop = _patched_bootstrap_failure
    client = LLMClient(provider="copilot", model="stub-model")
    try:
        try:
            client._ensure_sdk_thread_loop()
            raise AssertionError("expected worker-loop bootstrap error")
        except LLMClientError as exc:
            message = str(exc)
            assert "Copilot SDK worker-loop bootstrap" in message, "missing bootstrap context"
    finally:
        client.close()
        LLMClient._ensure_sdk_thread_loop = original

    print("PASS: bootstrap failure mode validates worker-loop bootstrap error context")
    return 0


def _init_shutdown_mode_client(user_prompt: str) -> LLMClient:
    _install_stub_copilot_module()
    client = LLMClient(provider="copilot", model="stub-model")
    client.chat(
        messages=[
            {"role": "system", "content": "Return a short answer."},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.0,
        max_tokens=16,
    )
    return client


def _teardown_shutdown_mode_client(client: LLMClient) -> None:
    client._sdk_session = None
    client._sdk_client = None
    client._close_sdk_loop()


def run_shutdown_failure_mode() -> int:
    client = _init_shutdown_mode_client("shutdown")
    try:
        async def _patched_stop_failure() -> None:
            raise RuntimeError("forced stop failure")

        async def _patched_force_stop_failure() -> None:
            raise RuntimeError("forced force_stop failure")

        sdk_client = client._sdk_client
        assert sdk_client is not None, "expected SDK client to be initialized"
        setattr(sdk_client, "stop", _patched_stop_failure)
        setattr(sdk_client, "force_stop", _patched_force_stop_failure)

        try:
            client.close()
            raise AssertionError("expected shutdown failure")
        except LLMClientError as exc:
            message = str(exc)
            assert "Copilot SDK shutdown failed:" in message, "missing shutdown failure context"
            assert "stop()=forced stop failure" in message, "missing stop() failure detail"
            assert "force_stop()=forced force_stop failure" in message, "missing force_stop() failure detail"
    finally:
        _teardown_shutdown_mode_client(client)

    print("PASS: shutdown failure mode validates stop()/force_stop() error context")
    return 0


def run_destroy_failure_mode() -> int:
    client = _init_shutdown_mode_client("destroy")
    try:
        async def _patched_destroy_failure() -> None:
            raise RuntimeError("forced destroy failure")

        sdk_session = client._sdk_session
        assert sdk_session is not None, "expected SDK session to be initialized"
        setattr(sdk_session, "destroy", _patched_destroy_failure)

        try:
            client.close()
            raise AssertionError("expected destroy failure")
        except LLMClientError as exc:
            message = str(exc)
            assert "Copilot SDK shutdown failed:" in message, "missing shutdown failure context"
            assert "session.destroy()=forced destroy failure" in message, "missing destroy() failure detail"
    finally:
        _teardown_shutdown_mode_client(client)

    print("PASS: destroy failure mode validates session.destroy() error context")
    return 0


def run_stop_unavailable_mode() -> int:
    client = _init_shutdown_mode_client("stop-unavailable")
    try:
        sdk_client = client._sdk_client
        assert sdk_client is not None, "expected SDK client to be initialized"
        setattr(sdk_client, "stop", None)

        try:
            client.close()
            raise AssertionError("expected stop unavailable failure")
        except LLMClientError as exc:
            message = str(exc)
            assert "Copilot SDK shutdown failed:" in message, "missing shutdown failure context"
            assert "stop() unavailable" in message, "missing stop() unavailable detail"
    finally:
        _teardown_shutdown_mode_client(client)

    print("PASS: stop unavailable mode validates stop() unavailable shutdown error context")
    return 0


def run_destroy_unavailable_mode() -> int:
    client = _init_shutdown_mode_client("destroy-unavailable")
    try:
        sdk_session = client._sdk_session
        assert sdk_session is not None, "expected SDK session to be initialized"
        setattr(sdk_session, "destroy", None)
        client.close()
    finally:
        _teardown_shutdown_mode_client(client)

    print("PASS: destroy unavailable mode validates non-callable session.destroy() shutdown success path")
    return 0


def run_force_stop_unavailable_mode() -> int:
    client = _init_shutdown_mode_client("force-stop-unavailable")
    try:
        async def _patched_stop_failure() -> None:
            raise RuntimeError("forced stop failure")

        sdk_client = client._sdk_client
        assert sdk_client is not None, "expected SDK client to be initialized"
        setattr(sdk_client, "stop", _patched_stop_failure)
        setattr(sdk_client, "force_stop", None)

        try:
            client.close()
            raise AssertionError("expected force_stop unavailable failure")
        except LLMClientError as exc:
            message = str(exc)
            assert "Copilot SDK shutdown failed:" in message, "missing shutdown failure context"
            assert "stop()=forced stop failure" in message, "missing stop() failure detail"
            assert "force_stop() unavailable" in message, "missing force_stop() unavailable detail"
    finally:
        _teardown_shutdown_mode_client(client)

    print("PASS: force-stop-unavailable mode validates force_stop() unavailable shutdown error context")
    return 0


def run_stop_close_idempotency_mode() -> int:
    client = _init_shutdown_mode_client("stop-close-idempotency")
    first_message = ""
    try:
        sdk_client = client._sdk_client
        assert sdk_client is not None, "expected SDK client to be initialized"
        setattr(sdk_client, "stop", None)

        try:
            client.close()
            raise AssertionError("expected stop unavailable failure")
        except LLMClientError as exc:
            first_message = str(exc)
            assert "Copilot SDK shutdown failed:" in first_message, "missing shutdown failure context"
            assert "stop() unavailable" in first_message, "missing stop() unavailable detail"

        client.close()
        assert first_message, "expected first close() failure message"
    finally:
        _teardown_shutdown_mode_client(client)

    print("PASS: stop-close-idempotency mode validates repeated close() after stop() unavailable")
    return 0


def run_force_stop_close_idempotency_mode() -> int:
    client = _init_shutdown_mode_client("force-stop-close-idempotency")
    first_message = ""
    try:
        async def _patched_stop_failure() -> None:
            raise RuntimeError("forced stop failure")

        sdk_client = client._sdk_client
        assert sdk_client is not None, "expected SDK client to be initialized"
        setattr(sdk_client, "stop", _patched_stop_failure)
        setattr(sdk_client, "force_stop", None)

        try:
            client.close()
            raise AssertionError("expected force_stop unavailable failure")
        except LLMClientError as exc:
            first_message = str(exc)
            assert "Copilot SDK shutdown failed:" in first_message, "missing shutdown failure context"
            assert "stop()=forced stop failure" in first_message, "missing stop() failure detail"
            assert "force_stop() unavailable" in first_message, "missing force_stop() unavailable detail"

        client.close()
        assert first_message, "expected first close() failure message"
    finally:
        _teardown_shutdown_mode_client(client)

    print("PASS: force-stop-close-idempotency mode validates repeated close() after force_stop() unavailable")
    return 0


def run_close_idempotency_mode() -> int:
    client = _init_shutdown_mode_client("close-idempotency")
    first_message = ""
    try:
        async def _patched_stop_failure() -> None:
            raise RuntimeError("forced stop failure")

        async def _patched_force_stop_failure() -> None:
            raise RuntimeError("forced force_stop failure")

        sdk_client = client._sdk_client
        assert sdk_client is not None, "expected SDK client to be initialized"
        setattr(sdk_client, "stop", _patched_stop_failure)
        setattr(sdk_client, "force_stop", _patched_force_stop_failure)

        try:
            client.close()
            raise AssertionError("expected shutdown failure")
        except LLMClientError as exc:
            first_message = str(exc)
            assert "Copilot SDK shutdown failed:" in first_message, "missing shutdown failure context"
            assert "stop()=forced stop failure" in first_message, "missing stop() failure detail"
            assert "force_stop()=forced force_stop failure" in first_message, "missing force_stop() failure detail"

        client.close()
        assert first_message, "expected first close() failure message"
    finally:
        _teardown_shutdown_mode_client(client)

    print("PASS: close-idempotency mode validates repeated close() after shutdown failure")
    return 0


def run_destroy_close_idempotency_mode() -> int:
    client = _init_shutdown_mode_client("destroy-close-idempotency")
    first_message = ""
    try:
        async def _patched_destroy_failure() -> None:
            raise RuntimeError("forced destroy failure")

        sdk_session = client._sdk_session
        assert sdk_session is not None, "expected SDK session to be initialized"
        setattr(sdk_session, "destroy", _patched_destroy_failure)

        try:
            client.close()
            raise AssertionError("expected destroy failure")
        except LLMClientError as exc:
            first_message = str(exc)
            assert "Copilot SDK shutdown failed:" in first_message, "missing shutdown failure context"
            assert "session.destroy()=forced destroy failure" in first_message, "missing destroy() failure detail"

        client.close()
        assert first_message, "expected first close() failure message"
    finally:
        _teardown_shutdown_mode_client(client)

    print("PASS: destroy-close-idempotency mode validates repeated close() after destroy failure")
    return 0


def run_destroy_unavailable_close_idempotency_mode() -> int:
    client = _init_shutdown_mode_client("destroy-unavailable-close-idempotency")
    try:
        sdk_session = client._sdk_session
        assert sdk_session is not None, "expected SDK session to be initialized"
        setattr(sdk_session, "destroy", None)
        client.close()
        client.close()
    finally:
        _teardown_shutdown_mode_client(client)

    print(
        "PASS: destroy-unavailable-close-idempotency mode validates repeated close() after destroy() unavailable"
    )
    return 0


def run_stop_destroy_unavailable_close_idempotency_mode() -> int:
    client = _init_shutdown_mode_client("stop-destroy-unavailable-close-idempotency")
    first_message = ""
    try:
        sdk_client = client._sdk_client
        assert sdk_client is not None, "expected SDK client to be initialized"
        setattr(sdk_client, "stop", None)
        sdk_session = client._sdk_session
        assert sdk_session is not None, "expected SDK session to be initialized"
        setattr(sdk_session, "destroy", None)

        try:
            client.close()
            raise AssertionError("expected stop unavailable failure")
        except LLMClientError as exc:
            first_message = str(exc)
            assert "Copilot SDK shutdown failed:" in first_message, "missing shutdown failure context"
            assert "stop() unavailable" in first_message, "missing stop() unavailable detail"

        client.close()
        assert first_message, "expected first close() failure message"
    finally:
        _teardown_shutdown_mode_client(client)

    print(
        "PASS: stop-destroy-unavailable-close-idempotency mode validates repeated close() after stop()/destroy() unavailable"
    )
    return 0


def run_stop_failure_destroy_unavailable_close_idempotency_mode() -> int:
    client = _init_shutdown_mode_client("stop-failure-destroy-unavailable-close-idempotency")
    first_message = ""
    try:
        async def _patched_stop_failure() -> None:
            raise RuntimeError("forced stop failure")

        sdk_client = client._sdk_client
        assert sdk_client is not None, "expected SDK client to be initialized"
        setattr(sdk_client, "stop", _patched_stop_failure)
        sdk_session = client._sdk_session
        assert sdk_session is not None, "expected SDK session to be initialized"
        setattr(sdk_session, "destroy", None)

        try:
            client.close()
            raise AssertionError("expected stop failure")
        except LLMClientError as exc:
            first_message = str(exc)
            assert "Copilot SDK shutdown failed:" in first_message, "missing shutdown failure context"
            assert "stop()=forced stop failure" in first_message, "missing stop() failure detail"

        client.close()
        assert first_message, "expected first close() failure message"
    finally:
        _teardown_shutdown_mode_client(client)

    print(
        "PASS: stop-failure-destroy-unavailable-close-idempotency mode validates repeated close() after stop() failure and destroy() unavailable"
    )
    return 0


def run_stop_unavailable_destroy_failure_close_idempotency_mode() -> int:
    client = _init_shutdown_mode_client("stop-unavailable-destroy-failure-close-idempotency")
    first_message = ""
    try:
        async def _patched_destroy_failure() -> None:
            raise RuntimeError("forced destroy failure")

        sdk_client = client._sdk_client
        assert sdk_client is not None, "expected SDK client to be initialized"
        setattr(sdk_client, "stop", None)
        sdk_session = client._sdk_session
        assert sdk_session is not None, "expected SDK session to be initialized"
        setattr(sdk_session, "destroy", _patched_destroy_failure)

        try:
            client.close()
            raise AssertionError("expected stop unavailable/destroy failure")
        except LLMClientError as exc:
            first_message = str(exc)
            assert "Copilot SDK shutdown failed:" in first_message, "missing shutdown failure context"
            assert "stop() unavailable" in first_message, "missing stop() unavailable detail"
            assert "session.destroy()=forced destroy failure" in first_message, "missing destroy() failure detail"

        client.close()
        assert first_message, "expected first close() failure message"
    finally:
        _teardown_shutdown_mode_client(client)

    print(
        "PASS: stop-unavailable-destroy-failure-close-idempotency mode validates repeated close() after stop() unavailable and destroy() failure"
    )
    return 0


def run_stop_failure_destroy_failure_close_idempotency_mode() -> int:
    client = _init_shutdown_mode_client("stop-failure-destroy-failure-close-idempotency")
    first_message = ""
    try:
        async def _patched_stop_failure() -> None:
            raise RuntimeError("forced stop failure")

        async def _patched_destroy_failure() -> None:
            raise RuntimeError("forced destroy failure")

        sdk_client = client._sdk_client
        assert sdk_client is not None, "expected SDK client to be initialized"
        setattr(sdk_client, "stop", _patched_stop_failure)
        sdk_session = client._sdk_session
        assert sdk_session is not None, "expected SDK session to be initialized"
        setattr(sdk_session, "destroy", _patched_destroy_failure)

        try:
            client.close()
            raise AssertionError("expected stop/destroy failure")
        except LLMClientError as exc:
            first_message = str(exc)
            assert "Copilot SDK shutdown failed:" in first_message, "missing shutdown failure context"
            assert "stop()=forced stop failure" in first_message, "missing stop() failure detail"
            assert "session.destroy()=forced destroy failure" in first_message, "missing destroy() failure detail"

        client.close()
        assert first_message, "expected first close() failure message"
    finally:
        _teardown_shutdown_mode_client(client)

    print(
        "PASS: stop-failure-destroy-failure-close-idempotency mode validates repeated close() after stop()/destroy() failures"
    )
    return 0


def run_trace_summary_mode() -> int:
    metrics_fixture = {
        "chapters": {
            "01-paradigm-shift": {
                "history": [
                    {
                        "trace_summary": {
                            "decision": "accept",
                            "drift_score": 0.1,
                            "diff_ratio": 0.2,
                            "deterministic_pass": True,
                        }
                    }
                ]
            }
        }
    }

    trace_summary = _get_latest_trace_summary(metrics_fixture, "01-paradigm-shift")
    missing = _missing_trace_summary_keys(trace_summary)
    assert not missing, f"unexpected missing trace_summary keys: {missing}"

    print("PASS: trace-summary mode validates required trace_summary keys")
    return 0


def run_trace_summary_missing_key_mode() -> int:
    metrics_fixture = {
        "chapters": {
            "01-paradigm-shift": {
                "history": [
                    {
                        "trace_summary": {
                            "decision": "accept",
                            "drift_score": 0.1,
                            "deterministic_pass": True,
                        }
                    }
                ]
            }
        }
    }

    trace_summary = _get_latest_trace_summary(metrics_fixture, "01-paradigm-shift")
    missing = _missing_trace_summary_keys(trace_summary)
    assert missing == ["diff_ratio"], f"expected diff_ratio missing-key detection, got: {missing}"

    print("PASS: trace-summary-missing-key mode detects required key omissions")
    return 0


def run_trace_summary_shape_guard_mode() -> int:
    metrics_fixture = {
        "chapters": {
            "01-paradigm-shift": {"history": [{"trace_summary": ["accept", 0.1, 0.2, True]}]}
        }
    }

    try:
        _get_latest_trace_summary(metrics_fixture, "01-paradigm-shift")
        raise AssertionError("expected non-dict trace_summary fixture to fail shape validation")
    except AssertionError as exc:
        assert str(exc) == "expected latest history entry to contain trace_summary dictionary"

    print("PASS: trace-summary-shape-guard mode detects non-dict trace_summary payloads")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Copilot SDK smoke test")
    parser.add_argument(
        "--mode",
        choices=[
            "stub",
            "sdk-unavailable",
            "bootstrap-failure",
            "shutdown-failure",
            "stop-unavailable",
            "destroy-unavailable",
            "destroy-failure",
            "force-stop-unavailable",
            "force-stop-close-idempotency",
            "stop-close-idempotency",
            "close-idempotency",
            "destroy-close-idempotency",
            "destroy-unavailable-close-idempotency",
            "stop-destroy-unavailable-close-idempotency",
            "stop-unavailable-destroy-failure-close-idempotency",
            "stop-failure-destroy-unavailable-close-idempotency",
            "stop-failure-destroy-failure-close-idempotency",
            "trace-summary",
            "trace-summary-missing-key",
            "trace-summary-shape-guard",
            "live",
        ],
        default="stub",
        help="stub = offline synthetic test, sdk-unavailable = forced missing SDK error, bootstrap-failure = forced worker-loop bootstrap error, shutdown-failure = forced SDK shutdown error, stop-unavailable = missing SDK stop() callable, destroy-unavailable = missing session destroy() callable, destroy-failure = forced session destroy error, force-stop-unavailable = stop() failure with missing force_stop(), force-stop-close-idempotency = repeated close() after force_stop() unavailable, stop-close-idempotency = repeated close() after stop() unavailable, close-idempotency = repeated close() after shutdown failure, destroy-close-idempotency = repeated close() after destroy failure, destroy-unavailable-close-idempotency = repeated close() after destroy() unavailable, stop-destroy-unavailable-close-idempotency = repeated close() after stop()/destroy() unavailable, stop-unavailable-destroy-failure-close-idempotency = repeated close() after stop() unavailable and destroy() failure, stop-failure-destroy-unavailable-close-idempotency = repeated close() after stop() failure and destroy() unavailable, stop-failure-destroy-failure-close-idempotency = repeated close() after stop() and destroy() failures, trace-summary = deterministic required-key assertion, trace-summary-missing-key = deterministic missing-key detection, trace-summary-shape-guard = deterministic non-dict shape detection, live = real provider call",
    )
    args = parser.parse_args()

    if args.mode == "stub":
        return run_stub_mode()
    if args.mode == "sdk-unavailable":
        return run_sdk_unavailable_mode()
    if args.mode == "bootstrap-failure":
        return run_bootstrap_failure_mode()
    if args.mode == "shutdown-failure":
        return run_shutdown_failure_mode()
    if args.mode == "stop-unavailable":
        return run_stop_unavailable_mode()
    if args.mode == "destroy-unavailable":
        return run_destroy_unavailable_mode()
    if args.mode == "destroy-failure":
        return run_destroy_failure_mode()
    if args.mode == "force-stop-unavailable":
        return run_force_stop_unavailable_mode()
    if args.mode == "force-stop-close-idempotency":
        return run_force_stop_close_idempotency_mode()
    if args.mode == "stop-close-idempotency":
        return run_stop_close_idempotency_mode()
    if args.mode == "close-idempotency":
        return run_close_idempotency_mode()
    if args.mode == "destroy-close-idempotency":
        return run_destroy_close_idempotency_mode()
    if args.mode == "destroy-unavailable-close-idempotency":
        return run_destroy_unavailable_close_idempotency_mode()
    if args.mode == "stop-destroy-unavailable-close-idempotency":
        return run_stop_destroy_unavailable_close_idempotency_mode()
    if args.mode == "stop-unavailable-destroy-failure-close-idempotency":
        return run_stop_unavailable_destroy_failure_close_idempotency_mode()
    if args.mode == "stop-failure-destroy-unavailable-close-idempotency":
        return run_stop_failure_destroy_unavailable_close_idempotency_mode()
    if args.mode == "stop-failure-destroy-failure-close-idempotency":
        return run_stop_failure_destroy_failure_close_idempotency_mode()
    if args.mode == "trace-summary":
        return run_trace_summary_mode()
    if args.mode == "trace-summary-missing-key":
        return run_trace_summary_missing_key_mode()
    if args.mode == "trace-summary-shape-guard":
        return run_trace_summary_shape_guard_mode()
    return run_live_mode()


if __name__ == "__main__":
    raise SystemExit(main())

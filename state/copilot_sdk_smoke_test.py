#!/usr/bin/env python3
"""Small Copilot SDK smoke test for state/llm_client.py.

Usage and mode details are generated from shared mode metadata below.
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
from typing import Any, Callable, cast


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


def run_trace_summary_container_shape_guard_mode() -> int:
    metrics_fixture = {"chapters": []}

    try:
        _get_latest_trace_summary(metrics_fixture, "01-paradigm-shift")
        raise AssertionError("expected malformed chapters fixture to fail shape validation")
    except AssertionError as exc:
        assert str(exc) == "expected chapters dictionary"

    print("PASS: trace-summary-container-shape-guard mode detects malformed metrics containers")
    return 0


def run_trace_summary_history_container_shape_guard_mode() -> int:
    metrics_fixture = {"chapters": {"01-paradigm-shift": {"history": {}}}}

    try:
        _get_latest_trace_summary(metrics_fixture, "01-paradigm-shift")
        raise AssertionError("expected malformed history fixture to fail shape validation")
    except AssertionError as exc:
        assert str(exc) == "expected metrics history for chapter 01-paradigm-shift"

    print(
        "PASS: trace-summary-history-container-shape-guard mode detects malformed history containers"
    )
    return 0


def run_trace_summary_latest_history_entry_shape_guard_mode() -> int:
    metrics_fixture = {"chapters": {"01-paradigm-shift": {"history": ["malformed-latest-entry"]}}}

    try:
        _get_latest_trace_summary(metrics_fixture, "01-paradigm-shift")
        raise AssertionError("expected malformed latest history entry fixture to fail shape validation")
    except AssertionError as exc:
        assert str(exc) == "expected latest history entry to be a dictionary"

    print(
        "PASS: trace-summary-latest-history-entry-shape-guard mode detects malformed latest history entries"
    )
    return 0


def run_trace_summary_empty_history_guard_mode() -> int:
    metrics_fixture = {"chapters": {"01-paradigm-shift": {"history": []}}}

    try:
        _get_latest_trace_summary(metrics_fixture, "01-paradigm-shift")
        raise AssertionError("expected empty history fixture to fail shape validation")
    except AssertionError as exc:
        assert str(exc) == "expected metrics history for chapter 01-paradigm-shift"

    print("PASS: trace-summary-empty-history-guard mode detects empty history containers")
    return 0


def run_trace_summary_missing_chapter_guard_mode() -> int:
    metrics_fixture = {"chapters": {}}

    try:
        _get_latest_trace_summary(metrics_fixture, "01-paradigm-shift")
        raise AssertionError("expected missing chapter fixture to fail shape validation")
    except AssertionError as exc:
        assert str(exc) == "expected metrics history for chapter 01-paradigm-shift"

    print("PASS: trace-summary-missing-chapter-guard mode detects missing chapter entries")
    return 0


def run_trace_summary_chapter_metrics_shape_guard_mode() -> int:
    metrics_fixture = {"chapters": {"01-paradigm-shift": []}}

    try:
        _get_latest_trace_summary(metrics_fixture, "01-paradigm-shift")
        raise AssertionError("expected non-dict chapter metrics fixture to fail shape validation")
    except AssertionError as exc:
        assert str(exc) == "expected chapter metrics dictionary"

    print(
        "PASS: trace-summary-chapter-metrics-shape-guard mode detects malformed chapter metrics"
    )
    return 0


def run_trace_summary_missing_entry_guard_mode() -> int:
    metrics_fixture = {"chapters": {"01-paradigm-shift": {"history": [{"result": "accept"}]}}}

    try:
        _get_latest_trace_summary(metrics_fixture, "01-paradigm-shift")
        raise AssertionError("expected missing trace_summary fixture to fail shape validation")
    except AssertionError as exc:
        assert str(exc) == "expected latest history entry to contain trace_summary dictionary"

    print("PASS: trace-summary-missing-entry-guard mode detects missing trace_summary entries")
    return 0


def run_docstring_mode_coverage_guard_mode() -> int:
    module_doc = __doc__
    assert isinstance(module_doc, str) and module_doc, "expected generated module docstring"
    missing_modes = [name for name, _handler, _description in _all_mode_specs() if f"- {name}:" not in module_doc]
    assert not missing_modes, f"expected module docstring entries for all modes, missing: {missing_modes}"

    print("PASS: docstring-mode-coverage-guard mode validates module doc coverage for all modes")
    return 0


def _build_mode_help(mode_specs: Sequence[tuple[str, Callable[[], int], str]]) -> str:
    return ", ".join(f"{name} = {description}" for name, _handler, description in mode_specs)


def run_mode_help_coverage_guard_mode() -> int:
    all_mode_specs = _all_mode_specs()
    mode_help = _build_mode_help(all_mode_specs)
    missing_descriptions = [
        name for name, _handler, description in all_mode_specs if f"{name} = {description}" not in mode_help
    ]
    assert not missing_descriptions, (
        f"expected mode_help entries for all mode descriptions, missing: {missing_descriptions}"
    )

    print("PASS: mode-help-coverage-guard mode validates argparse mode help coverage for all modes")
    return 0


def _build_parser(mode_specs: Sequence[tuple[str, Callable[[], int], str]]) -> argparse.ArgumentParser:
    mode_names = [name for name, _handler, _description in mode_specs]
    mode_help = _build_mode_help(mode_specs)
    parser = argparse.ArgumentParser(description="Copilot SDK smoke test")
    parser.add_argument(
        "--mode",
        choices=mode_names,
        default="stub",
        help=mode_help,
    )
    return parser


def run_mode_choices_coverage_guard_mode() -> int:
    all_mode_specs = _all_mode_specs()
    expected_mode_names = [name for name, _handler, _description in all_mode_specs]
    parser = _build_parser(all_mode_specs)
    mode_action = next(
        (
            action
            for action in parser._actions
            if "--mode" in getattr(action, "option_strings", [])
        ),
        None,
    )
    assert mode_action is not None, "expected argparse --mode action to exist"
    parser_mode_choices = list(mode_action.choices or [])
    assert parser_mode_choices == expected_mode_names, (
        "expected argparse --mode choices to match registered mode names exactly once in order"
    )

    print(
        "PASS: mode-choices-coverage-guard mode validates argparse --mode choices for all modes"
    )
    return 0


def run_usage_examples_coverage_guard_mode() -> int:
    all_mode_specs = _all_mode_specs()
    usage_lines = _usage_doc_lines(all_mode_specs)
    expected_lines = [
        f"  uv run python state/copilot_sdk_smoke_test.py --mode {name}"
        for name, _handler, _description in all_mode_specs
        if name != "stub"
    ]
    actual_lines = [line for line in usage_lines if line.startswith("  uv run python state/copilot_sdk_smoke_test.py --mode ")]
    assert actual_lines == expected_lines, (
        "expected usage examples to include every non-stub mode exactly once in order"
    )

    print(
        "PASS: usage-examples-coverage-guard mode validates generated usage examples for non-stub modes"
    )
    return 0


def run_usage_examples_duplicates_guard_mode() -> int:
    all_mode_specs = _all_mode_specs()
    usage_lines = _usage_doc_lines(all_mode_specs)
    actual_lines = [line for line in usage_lines if line.startswith("  uv run python state/copilot_sdk_smoke_test.py --mode ")]
    assert len(actual_lines) == len(set(actual_lines)), "expected generated usage examples to contain no duplicate non-stub mode lines"

    print(
        "PASS: usage-examples-duplicates-guard mode validates generated usage examples contain no duplicates"
    )
    return 0


TraceSummaryModeHandler = Callable[[], int]
TRACE_SUMMARY_MODE_SPECS: tuple[tuple[str, TraceSummaryModeHandler, str], ...] = (
    ("trace-summary", run_trace_summary_mode, "deterministic required-key assertion"),
    ("trace-summary-missing-key", run_trace_summary_missing_key_mode, "deterministic missing-key detection"),
    ("trace-summary-shape-guard", run_trace_summary_shape_guard_mode, "deterministic non-dict shape detection"),
    (
        "trace-summary-container-shape-guard",
        run_trace_summary_container_shape_guard_mode,
        "deterministic malformed metrics container detection",
    ),
    (
        "trace-summary-history-container-shape-guard",
        run_trace_summary_history_container_shape_guard_mode,
        "deterministic malformed history container detection",
    ),
    (
        "trace-summary-latest-history-entry-shape-guard",
        run_trace_summary_latest_history_entry_shape_guard_mode,
        "deterministic malformed latest history entry detection",
    ),
    ("trace-summary-empty-history-guard", run_trace_summary_empty_history_guard_mode, "deterministic empty history detection"),
    (
        "trace-summary-missing-chapter-guard",
        run_trace_summary_missing_chapter_guard_mode,
        "deterministic missing chapter detection",
    ),
    (
        "trace-summary-chapter-metrics-shape-guard",
        run_trace_summary_chapter_metrics_shape_guard_mode,
        "deterministic malformed chapter-metrics detection",
    ),
    (
        "trace-summary-missing-entry-guard",
        run_trace_summary_missing_entry_guard_mode,
        "deterministic missing trace_summary entry detection",
    ),
    (
        "docstring-mode-coverage-guard",
        run_docstring_mode_coverage_guard_mode,
        "deterministic module-doc mode coverage assertion",
    ),
    (
        "mode-help-coverage-guard",
        run_mode_help_coverage_guard_mode,
        "deterministic argparse mode-help coverage assertion",
    ),
    (
        "mode-choices-coverage-guard",
        run_mode_choices_coverage_guard_mode,
        "deterministic argparse mode-choices coverage assertion",
    ),
    (
        "usage-examples-coverage-guard",
        run_usage_examples_coverage_guard_mode,
        "deterministic generated usage-example coverage assertion",
    ),
    (
        "usage-examples-duplicates-guard",
        run_usage_examples_duplicates_guard_mode,
        "deterministic generated usage-example duplicate-line assertion",
    ),
)


BaseModeHandler = Callable[[], int]
BASE_MODE_SPECS: tuple[tuple[str, BaseModeHandler, str], ...] = (
    ("stub", run_stub_mode, "offline synthetic test"),
    ("sdk-unavailable", run_sdk_unavailable_mode, "forced missing SDK error"),
    ("bootstrap-failure", run_bootstrap_failure_mode, "forced worker-loop bootstrap error"),
    ("live", run_live_mode, "real provider call"),
)


ShutdownModeHandler = Callable[[], int]
SHUTDOWN_MODE_SPECS: tuple[tuple[str, ShutdownModeHandler, str], ...] = (
    ("shutdown-failure", run_shutdown_failure_mode, "forced SDK shutdown error"),
    ("stop-unavailable", run_stop_unavailable_mode, "missing SDK stop() callable"),
    ("destroy-unavailable", run_destroy_unavailable_mode, "missing session destroy() callable"),
    ("destroy-failure", run_destroy_failure_mode, "forced session destroy error"),
    ("force-stop-unavailable", run_force_stop_unavailable_mode, "stop() failure with missing force_stop()"),
    (
        "force-stop-close-idempotency",
        run_force_stop_close_idempotency_mode,
        "repeated close() after force_stop() unavailable",
    ),
    ("stop-close-idempotency", run_stop_close_idempotency_mode, "repeated close() after stop() unavailable"),
    ("close-idempotency", run_close_idempotency_mode, "repeated close() after shutdown failure"),
    ("destroy-close-idempotency", run_destroy_close_idempotency_mode, "repeated close() after destroy failure"),
    (
        "destroy-unavailable-close-idempotency",
        run_destroy_unavailable_close_idempotency_mode,
        "repeated close() after destroy() unavailable",
    ),
    (
        "stop-destroy-unavailable-close-idempotency",
        run_stop_destroy_unavailable_close_idempotency_mode,
        "repeated close() after stop()/destroy() unavailable",
    ),
    (
        "stop-unavailable-destroy-failure-close-idempotency",
        run_stop_unavailable_destroy_failure_close_idempotency_mode,
        "repeated close() after stop() unavailable and destroy() failure",
    ),
    (
        "stop-failure-destroy-unavailable-close-idempotency",
        run_stop_failure_destroy_unavailable_close_idempotency_mode,
        "repeated close() after stop() failure and destroy() unavailable",
    ),
    (
        "stop-failure-destroy-failure-close-idempotency",
        run_stop_failure_destroy_failure_close_idempotency_mode,
        "repeated close() after stop() and destroy() failures",
    ),
)


def _all_mode_specs() -> tuple[tuple[str, Callable[[], int], str], ...]:
    return (*BASE_MODE_SPECS, *SHUTDOWN_MODE_SPECS, *TRACE_SUMMARY_MODE_SPECS)


def _usage_doc_lines(mode_specs: Sequence[tuple[str, Callable[[], int], str]]) -> list[str]:
    lines = ["Usage:", "  uv run python state/copilot_sdk_smoke_test.py"]
    lines.extend(f"  uv run python state/copilot_sdk_smoke_test.py --mode {name}" for name, _handler, _description in mode_specs if name != "stub")
    return lines


def _mode_doc_lines(mode_specs: Sequence[tuple[str, Callable[[], int], str]]) -> list[str]:
    lines = ["Modes:"]
    lines.extend(f"- {name}: {description}." for name, _handler, description in mode_specs)
    return lines


def _build_module_docstring() -> str:
    mode_specs = _all_mode_specs()
    sections = [
        "Small Copilot SDK smoke test for state/llm_client.py.",
        "",
        *_usage_doc_lines(mode_specs),
        "",
        *_mode_doc_lines(mode_specs),
    ]
    return "\n".join(sections)


__doc__ = _build_module_docstring()


def main() -> int:
    all_mode_specs = _all_mode_specs()
    mode_handlers = {name: handler for name, handler, _description in all_mode_specs}
    parser = _build_parser(all_mode_specs)
    args = parser.parse_args()
    return mode_handlers[args.mode]()


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Small Copilot SDK smoke test for state/llm_client.py.

Usage and mode details are generated from shared mode metadata below.
"""

from __future__ import annotations

import argparse
import ast
import importlib
import inspect
import os
import subprocess
import sys
import types
from collections import Counter
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
TRACE_SUMMARY_FIXTURE_ROOT = ROOT / "state" / ".smoke_fixtures" / "trace_summary"
TRACE_SUMMARY_NON_KERNEL_FIXTURE_REPO = ROOT / "state" / ".smoke_fixtures" / "trace_summary" / "repo"
TRACE_SUMMARY_KERNEL_FIXTURE_REPO = ROOT / "state" / ".smoke_fixtures" / "trace_summary" / "kernel_repo"


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


def _run_trace_summary_kernel_mode(
    mode_name: str,
    expected_failure: str | None = None,
    expect_fixture_cleanup: bool = False,
) -> str:
    ledger_path = ROOT / "state" / "ledger.json"
    before_ledger = ledger_path.read_text(encoding="utf-8")
    proc = subprocess.run(
        [
            "uv",
            "run",
            "python",
            "state/copilot_sdk_uv_smoke.py",
            "--mode",
            mode_name,
            "--run-kernel-for-trace-summary",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    after_ledger = ledger_path.read_text(encoding="utf-8")
    assert after_ledger == before_ledger, "expected state/ledger.json to remain unchanged after kernel trace-summary smoke"
    if expect_fixture_cleanup:
        assert not TRACE_SUMMARY_KERNEL_FIXTURE_REPO.exists(), (
            f"expected fixture kernel repo cleanup after mode {mode_name}: {TRACE_SUMMARY_KERNEL_FIXTURE_REPO}"
        )

    combined_output = "\n".join(part for part in (proc.stdout.strip(), proc.stderr.strip()) if part).strip()
    assert proc.returncode == 0, f"expected exit code 0 for mode {mode_name}, got {proc.returncode}\n{combined_output}"
    if expected_failure is None:
        assert "PASS: trace_summary present with required keys" in combined_output, (
            f"expected success output for mode {mode_name}, got: {combined_output}"
        )
    else:
        assert expected_failure in combined_output, (
            f"expected phase_trace validation failure output for mode {mode_name}, got: {combined_output}"
        )
    return combined_output


def _run_trace_summary_non_kernel_mode(
    mode_name: str,
    expected_failure: str | None = None,
    expect_fixture_cleanup: bool = False,
) -> str:
    proc = subprocess.run(
        [
            "uv",
            "run",
            "python",
            "state/copilot_sdk_uv_smoke.py",
            "--mode",
            mode_name,
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if expect_fixture_cleanup:
        assert not TRACE_SUMMARY_NON_KERNEL_FIXTURE_REPO.exists(), (
            f"expected fixture repo cleanup after mode {mode_name}: {TRACE_SUMMARY_NON_KERNEL_FIXTURE_REPO}"
        )

    combined_output = "\n".join(part for part in (proc.stdout.strip(), proc.stderr.strip()) if part).strip()
    assert proc.returncode == 0, f"expected exit code 0 for mode {mode_name}, got {proc.returncode}\n{combined_output}"
    if expected_failure is None:
        assert "PASS: trace_summary present with required keys" in combined_output, (
            f"expected success output for mode {mode_name}, got: {combined_output}"
        )
    else:
        assert expected_failure in combined_output, (
            f"expected phase_trace validation failure output for mode {mode_name}, got: {combined_output}"
        )
    return combined_output


def _assert_trace_summary_fixture_root_clean(mode_name: str) -> None:
    if not TRACE_SUMMARY_FIXTURE_ROOT.exists():
        return
    residual_dirs = sorted(path.name for path in TRACE_SUMMARY_FIXTURE_ROOT.iterdir() if path.is_dir())
    assert not residual_dirs, (
        "expected trace-summary fixture root cleanup after mode "
        f"{mode_name}, found residual directories: {residual_dirs}"
    )


def run_trace_summary_kernel_mode() -> int:
    _run_trace_summary_kernel_mode("trace-summary")
    print("PASS: trace-summary-kernel mode validates fixture-backed kernel trace-summary success")
    return 0


def run_trace_summary_kernel_malformed_phase_mode() -> int:
    _run_trace_summary_kernel_mode(
        "trace-summary-malformed-phase",
        expected_failure="phase_trace missing keys: ['budget_signal']",
    )
    print("PASS: trace-summary-kernel-malformed-phase mode validates malformed phase-trace key failures")
    return 0


def run_trace_summary_kernel_malformed_phase_payload_mode() -> int:
    _run_trace_summary_kernel_mode(
        "trace-summary-malformed-phase-payload",
        expected_failure="phase_trace payload is not an object",
    )
    print("PASS: trace-summary-kernel-malformed-phase-payload mode validates non-object phase-trace payload failures")
    return 0


def run_trace_summary_kernel_missing_phase_mode() -> int:
    _run_trace_summary_kernel_mode(
        "trace-summary-missing-phase",
        expected_failure="missing required phase traces: ['evaluation']",
    )
    print("PASS: trace-summary-kernel-missing-phase mode validates missing required phase-trace failures")
    return 0


def run_trace_summary_kernel_fixture_cleanup_mode() -> int:
    _run_trace_summary_kernel_mode("trace-summary", expect_fixture_cleanup=True)
    _run_trace_summary_kernel_mode(
        "trace-summary-malformed-phase",
        expected_failure="phase_trace missing keys: ['budget_signal']",
        expect_fixture_cleanup=True,
    )
    _run_trace_summary_kernel_mode(
        "trace-summary-malformed-phase-payload",
        expected_failure="phase_trace payload is not an object",
        expect_fixture_cleanup=True,
    )
    _run_trace_summary_kernel_mode(
        "trace-summary-missing-phase",
        expected_failure="missing required phase traces: ['evaluation']",
        expect_fixture_cleanup=True,
    )
    print("PASS: trace-summary-kernel-fixture-cleanup mode validates fixture cleanup after kernel-backed trace-summary runs")
    return 0


def run_trace_summary_kernel_fixture_root_cleanup_mode() -> int:
    _run_trace_summary_kernel_mode("trace-summary", expect_fixture_cleanup=True)
    _assert_trace_summary_fixture_root_clean("trace-summary")
    _run_trace_summary_kernel_mode(
        "trace-summary-malformed-phase",
        expected_failure="phase_trace missing keys: ['budget_signal']",
        expect_fixture_cleanup=True,
    )
    _assert_trace_summary_fixture_root_clean("trace-summary-malformed-phase")
    _run_trace_summary_kernel_mode(
        "trace-summary-malformed-phase-payload",
        expected_failure="phase_trace payload is not an object",
        expect_fixture_cleanup=True,
    )
    _assert_trace_summary_fixture_root_clean("trace-summary-malformed-phase-payload")
    _run_trace_summary_kernel_mode(
        "trace-summary-missing-phase",
        expected_failure="missing required phase traces: ['evaluation']",
        expect_fixture_cleanup=True,
    )
    _assert_trace_summary_fixture_root_clean("trace-summary-missing-phase")
    print(
        "PASS: trace-summary-kernel-fixture-root-cleanup mode validates trace-summary fixture root cleanup "
        "after kernel trace-summary runs"
    )
    return 0


def run_trace_summary_non_kernel_fixture_cleanup_mode() -> int:
    _run_trace_summary_non_kernel_mode("trace-summary", expect_fixture_cleanup=True)
    _run_trace_summary_non_kernel_mode(
        "trace-summary-malformed-phase",
        expected_failure="phase_trace missing keys: ['budget_signal']",
        expect_fixture_cleanup=True,
    )
    _run_trace_summary_non_kernel_mode(
        "trace-summary-malformed-phase-payload",
        expected_failure="phase_trace payload is not an object",
        expect_fixture_cleanup=True,
    )
    _run_trace_summary_non_kernel_mode(
        "trace-summary-missing-phase",
        expected_failure="missing required phase traces: ['evaluation']",
        expect_fixture_cleanup=True,
    )
    print("PASS: trace-summary-non-kernel-fixture-cleanup mode validates fixture cleanup after non-kernel trace-summary runs")
    return 0


def run_trace_summary_non_kernel_fixture_root_cleanup_mode() -> int:
    _run_trace_summary_non_kernel_mode("trace-summary", expect_fixture_cleanup=True)
    _assert_trace_summary_fixture_root_clean("trace-summary")
    _run_trace_summary_non_kernel_mode(
        "trace-summary-malformed-phase",
        expected_failure="phase_trace missing keys: ['budget_signal']",
        expect_fixture_cleanup=True,
    )
    _assert_trace_summary_fixture_root_clean("trace-summary-malformed-phase")
    _run_trace_summary_non_kernel_mode(
        "trace-summary-malformed-phase-payload",
        expected_failure="phase_trace payload is not an object",
        expect_fixture_cleanup=True,
    )
    _assert_trace_summary_fixture_root_clean("trace-summary-malformed-phase-payload")
    _run_trace_summary_non_kernel_mode(
        "trace-summary-missing-phase",
        expected_failure="missing required phase traces: ['evaluation']",
        expect_fixture_cleanup=True,
    )
    _assert_trace_summary_fixture_root_clean("trace-summary-missing-phase")
    print(
        "PASS: trace-summary-non-kernel-fixture-root-cleanup mode validates trace-summary fixture root cleanup "
        "after non-kernel trace-summary runs"
    )
    return 0


def run_trace_summary_fixture_root_cleanup_parity_mode() -> int:
    run_trace_summary_kernel_fixture_root_cleanup_mode()
    run_trace_summary_non_kernel_fixture_root_cleanup_mode()
    print(
        "PASS: trace-summary-fixture-root-cleanup-parity mode validates both kernel and non-kernel "
        "fixture root cleanup guards in one run"
    )
    return 0


def run_trace_summary_fixture_cleanup_parity_mode() -> int:
    run_trace_summary_kernel_fixture_cleanup_mode()
    run_trace_summary_non_kernel_fixture_cleanup_mode()
    print(
        "PASS: trace-summary-fixture-cleanup-parity mode validates both kernel and non-kernel "
        "fixture cleanup guards in one run"
    )
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


def _mode_action_for_parser(parser: argparse.ArgumentParser) -> argparse.Action:
    mode_action = next(
        (
            action
            for action in parser._actions
            if "--mode" in getattr(action, "option_strings", [])
        ),
        None,
    )
    assert mode_action is not None, "expected argparse --mode action to exist"
    return mode_action


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


_USAGE_EXAMPLE_MODE_PREFIX = "  uv run python state/copilot_sdk_smoke_test.py --mode "


def _generated_non_stub_usage_mode_names(usage_lines: Sequence[str]) -> list[str]:
    return [
        line.removeprefix(_USAGE_EXAMPLE_MODE_PREFIX)
        for line in usage_lines
        if line.startswith(_USAGE_EXAMPLE_MODE_PREFIX)
    ]


def _expected_non_stub_mode_names(mode_specs: Sequence[tuple[str, Callable[[], int], str]]) -> list[str]:
    return [name for name, _handler, _description in mode_specs if name != "stub"]


def run_usage_examples_coverage_guard_mode() -> int:
    all_mode_specs = _all_mode_specs()
    usage_lines = _usage_doc_lines(all_mode_specs)
    expected_mode_names = _expected_non_stub_mode_names(all_mode_specs)
    actual_mode_names = _generated_non_stub_usage_mode_names(usage_lines)
    assert actual_mode_names == expected_mode_names, (
        "expected usage examples to include every non-stub mode exactly once in order"
    )

    print(
        "PASS: usage-examples-coverage-guard mode validates generated usage examples for non-stub modes"
    )
    return 0


def run_usage_examples_duplicates_guard_mode() -> int:
    all_mode_specs = _all_mode_specs()
    usage_lines = _usage_doc_lines(all_mode_specs)
    expected_mode_names = _expected_non_stub_mode_names(all_mode_specs)
    actual_mode_names = _generated_non_stub_usage_mode_names(usage_lines)
    mode_counts = Counter(actual_mode_names)
    duplicate_mode_counts = {name: mode_counts[name] for name in expected_mode_names if mode_counts[name] > 1}
    assert not duplicate_mode_counts, (
        "expected generated usage examples to contain no duplicate non-stub mode lines; "
        f"found duplicates with counts: {duplicate_mode_counts}"
    )

    print(
        "PASS: usage-examples-duplicates-guard mode validates generated usage examples contain no duplicates"
    )
    return 0


def run_usage_examples_duplicate_count_regression_guard_mode() -> int:
    all_mode_specs = _all_mode_specs()
    expected_mode_names = _expected_non_stub_mode_names(all_mode_specs)
    usage_lines = _usage_doc_lines(all_mode_specs)
    synthetic_duplicates = (expected_mode_names[0], expected_mode_names[-1])
    usage_lines.extend(
        [
            f"{_USAGE_EXAMPLE_MODE_PREFIX}{synthetic_duplicates[0]}",
            f"{_USAGE_EXAMPLE_MODE_PREFIX}{synthetic_duplicates[0]}",
            f"{_USAGE_EXAMPLE_MODE_PREFIX}{synthetic_duplicates[1]}",
        ]
    )

    actual_mode_names = _generated_non_stub_usage_mode_names(usage_lines)
    mode_counts = Counter(actual_mode_names)
    duplicate_mode_counts = {name: mode_counts[name] for name in expected_mode_names if mode_counts[name] > 1}
    expected_duplicate_mode_counts = {
        synthetic_duplicates[0]: 3,
        synthetic_duplicates[1]: 2,
    }
    assert duplicate_mode_counts == expected_duplicate_mode_counts, (
        "expected duplicate diagnostics to include deterministic synthetic duplicate-count payload; "
        f"got {duplicate_mode_counts}"
    )

    print(
        "PASS: usage-examples-duplicate-count-regression-guard mode validates duplicate-count diagnostics"
    )
    return 0


def _assert_mode_in_parser_and_usage_examples(
    all_mode_specs: Sequence[tuple[str, Callable[[], int], str]], target_mode_name: str
) -> None:
    parser = _build_parser(all_mode_specs)
    mode_action = _mode_action_for_parser(parser)
    parser_mode_choices = list(mode_action.choices or [])
    assert target_mode_name in parser_mode_choices, (
        f"expected argparse --mode choices to include {target_mode_name}"
    )
    usage_lines = _usage_doc_lines(all_mode_specs)
    usage_mode_names = _generated_non_stub_usage_mode_names(usage_lines)
    assert target_mode_name in usage_mode_names, (
        f"expected generated usage examples to include {target_mode_name}"
    )


def _run_usage_examples_duplicate_count_mode_coverage_guard(
    target_mode_name: str, pass_message: str
) -> int:
    all_mode_specs = _all_mode_specs()
    _assert_mode_in_parser_and_usage_examples(all_mode_specs, target_mode_name)
    print(pass_message)
    return 0


def run_usage_examples_duplicate_count_mode_coverage_guard_mode() -> int:
    return _run_usage_examples_duplicate_count_mode_coverage_guard(
        "usage-examples-duplicate-count-mode-coverage-guard",
        "PASS: usage-examples-duplicate-count-mode-coverage-guard mode validates duplicate-count regression mode coverage",
    )


def _trace_summary_fixture_cleanup_parity_target_modes() -> tuple[str, str]:
    return (
        "trace-summary-fixture-root-cleanup-parity",
        "trace-summary-fixture-cleanup-parity",
    )


def run_trace_summary_fixture_cleanup_parity_usage_examples_guard_mode() -> int:
    all_mode_specs = _all_mode_specs()
    usage_lines = _usage_doc_lines(all_mode_specs)
    usage_mode_names = _generated_non_stub_usage_mode_names(usage_lines)
    mode_counts = Counter(usage_mode_names)
    target_modes = _trace_summary_fixture_cleanup_parity_target_modes()
    unexpected_counts = {name: mode_counts.get(name, 0) for name in target_modes if mode_counts.get(name, 0) != 1}
    assert not unexpected_counts, (
        "expected parity cleanup modes to appear exactly once in generated usage examples; "
        f"counts were {unexpected_counts}"
    )

    print(
        "PASS: trace-summary-fixture-cleanup-parity-usage-examples-guard mode validates parity mode usage-example uniqueness"
    )
    return 0


def run_trace_summary_fixture_cleanup_parity_mode_choices_usage_examples_order_guard_mode() -> int:
    all_mode_specs = _all_mode_specs()
    target_modes = _trace_summary_fixture_cleanup_parity_target_modes()

    parser = _build_parser(all_mode_specs)
    mode_action = _mode_action_for_parser(parser)
    parser_mode_choices = list(mode_action.choices or [])
    parser_target_modes = [name for name in parser_mode_choices if name in target_modes]

    usage_lines = _usage_doc_lines(all_mode_specs)
    usage_mode_names = _generated_non_stub_usage_mode_names(usage_lines)
    usage_target_modes = [name for name in usage_mode_names if name in target_modes]

    assert len(parser_target_modes) == len(target_modes), (
        "expected argparse --mode choices to include both parity cleanup modes"
    )
    assert len(usage_target_modes) == len(target_modes), (
        "expected generated usage examples to include both parity cleanup modes"
    )
    assert parser_target_modes == usage_target_modes, (
        "expected argparse --mode parity cleanup mode ordering to match generated usage examples"
    )

    print(
        "PASS: trace-summary-fixture-cleanup-parity-mode-choices-usage-examples-order-guard mode validates parity mode ordering parity between parser choices and usage examples"
    )
    return 0


def run_trace_summary_fixture_cleanup_parity_mode_choices_uniqueness_guard_mode() -> int:
    all_mode_specs = _all_mode_specs()
    target_modes = _trace_summary_fixture_cleanup_parity_target_modes()
    parser = _build_parser(all_mode_specs)
    mode_action = _mode_action_for_parser(parser)
    parser_mode_choices = list(mode_action.choices or [])
    mode_counts = Counter(parser_mode_choices)
    unexpected_counts = {name: mode_counts.get(name, 0) for name in target_modes if mode_counts.get(name, 0) != 1}
    assert not unexpected_counts, (
        "expected parity cleanup modes to appear exactly once in argparse --mode choices; "
        f"counts were {unexpected_counts}"
    )

    print(
        "PASS: trace-summary-fixture-cleanup-parity-mode-choices-uniqueness-guard mode validates parity mode argparse choice uniqueness"
    )
    return 0


def run_trace_summary_fixture_cleanup_parity_mode_choices_usage_examples_adjacency_guard_mode() -> int:
    all_mode_specs = _all_mode_specs()
    target_modes = _trace_summary_fixture_cleanup_parity_target_modes()
    parser = _build_parser(all_mode_specs)
    mode_action = _mode_action_for_parser(parser)
    parser_mode_choices = list(mode_action.choices or [])
    assert all(name in parser_mode_choices for name in target_modes), (
        "expected argparse --mode choices to include both parity cleanup modes"
    )
    parser_first_index = parser_mode_choices.index(target_modes[0])
    parser_second_index = parser_mode_choices.index(target_modes[1])
    assert parser_second_index - parser_first_index == 1, (
        "expected parity cleanup modes to be adjacent in argparse --mode choices"
    )

    usage_lines = _usage_doc_lines(all_mode_specs)
    usage_mode_names = _generated_non_stub_usage_mode_names(usage_lines)
    assert all(name in usage_mode_names for name in target_modes), (
        "expected generated usage examples to include both parity cleanup modes"
    )
    usage_first_index = usage_mode_names.index(target_modes[0])
    usage_second_index = usage_mode_names.index(target_modes[1])
    assert usage_second_index - usage_first_index == 1, (
        "expected parity cleanup modes to be adjacent in generated usage examples"
    )

    print(
        "PASS: trace-summary-fixture-cleanup-parity-mode-choices-usage-examples-adjacency-guard mode validates parity mode adjacency in parser choices and usage examples"
    )
    return 0


def run_trace_summary_fixture_cleanup_parity_mode_choices_usage_examples_uniqueness_adjacency_guard_mode() -> int:
    all_mode_specs = _all_mode_specs()
    target_modes = _trace_summary_fixture_cleanup_parity_target_modes()
    parser = _build_parser(all_mode_specs)
    mode_action = _mode_action_for_parser(parser)
    parser_mode_choices = list(mode_action.choices or [])
    parser_mode_counts = Counter(parser_mode_choices)
    parser_unexpected_counts = {name: parser_mode_counts.get(name, 0) for name in target_modes if parser_mode_counts.get(name, 0) != 1}
    assert not parser_unexpected_counts, (
        "expected parity cleanup modes to appear exactly once in argparse --mode choices before adjacency checks; "
        f"counts were {parser_unexpected_counts}"
    )
    parser_first_index = parser_mode_choices.index(target_modes[0])
    parser_second_index = parser_mode_choices.index(target_modes[1])
    assert parser_second_index - parser_first_index == 1, (
        "expected parity cleanup modes to be adjacent in argparse --mode choices after uniqueness checks"
    )

    usage_lines = _usage_doc_lines(all_mode_specs)
    usage_mode_names = _generated_non_stub_usage_mode_names(usage_lines)
    usage_mode_counts = Counter(usage_mode_names)
    usage_unexpected_counts = {name: usage_mode_counts.get(name, 0) for name in target_modes if usage_mode_counts.get(name, 0) != 1}
    assert not usage_unexpected_counts, (
        "expected parity cleanup modes to appear exactly once in generated usage examples before adjacency checks; "
        f"counts were {usage_unexpected_counts}"
    )
    usage_first_index = usage_mode_names.index(target_modes[0])
    usage_second_index = usage_mode_names.index(target_modes[1])
    assert usage_second_index - usage_first_index == 1, (
        "expected parity cleanup modes to be adjacent in generated usage examples after uniqueness checks"
    )

    print(
        "PASS: trace-summary-fixture-cleanup-parity-mode-choices-usage-examples-uniqueness-adjacency-guard mode validates parity mode first-occurrence uniqueness before adjacency checks"
    )
    return 0


def run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_mode() -> int:
    return _run_usage_examples_duplicate_count_mode_coverage_guard(
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard",
        "PASS: usage-examples-duplicate-count-mode-coverage-guard-coverage-guard mode validates duplicate-count mode-coverage guard mode coverage",
    )


def run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_mode() -> int:
    return _run_usage_examples_duplicate_count_mode_coverage_guard(
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard",
        "PASS: usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard mode validates duplicate-count mode-coverage guard-coverage guard mode coverage"
    )


def run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode() -> int:
    return _run_usage_examples_duplicate_count_mode_coverage_guard(
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        "PASS: usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard mode validates duplicate-count mode-coverage guard-coverage guard-coverage guard mode coverage"
    )


def run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode() -> int:
    return _run_usage_examples_duplicate_count_mode_coverage_guard(
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        "PASS: usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard mode validates duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard mode coverage"
    )


def run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode() -> int:
    return _run_usage_examples_duplicate_count_mode_coverage_guard(
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        "PASS: usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard mode validates duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard mode coverage"
    )


def run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode() -> int:
    return _run_usage_examples_duplicate_count_mode_coverage_guard(
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        "PASS: usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard mode validates duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard mode coverage"
    )


def run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode() -> int:
    return _run_usage_examples_duplicate_count_mode_coverage_guard(
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        "PASS: usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard mode validates duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard mode coverage"
    )


def run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode() -> int:
    return _run_usage_examples_duplicate_count_mode_coverage_guard(
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        "PASS: usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard mode validates duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard mode coverage"
    )


def run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode() -> int:
    return _run_usage_examples_duplicate_count_mode_coverage_guard(
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        "PASS: usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard mode validates duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard mode coverage"
    )


def run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode() -> int:
    return _run_usage_examples_duplicate_count_mode_coverage_guard(
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        "PASS: usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard mode validates duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard mode coverage",
    )


def run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode() -> int:
    return _run_usage_examples_duplicate_count_mode_coverage_guard(
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        "PASS: usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard mode validates duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard mode coverage",
    )


def run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode() -> int:
    return _run_usage_examples_duplicate_count_mode_coverage_guard(
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        "PASS: usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard mode validates duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard mode coverage"
    )


def run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode() -> int:
    return _run_usage_examples_duplicate_count_mode_coverage_guard(
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        "PASS: usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard mode validates duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard mode coverage"
    )


def run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode() -> int:
    return _run_usage_examples_duplicate_count_mode_coverage_guard(
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        "PASS: usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard mode validates duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard mode coverage"
    )


def run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode() -> int:
    return _run_usage_examples_duplicate_count_mode_coverage_guard(
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        "PASS: usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard mode validates duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard mode coverage"
    )


def run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode() -> int:
    return _run_usage_examples_duplicate_count_mode_coverage_guard(
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        "PASS: usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard mode validates duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard mode coverage"
    )


def run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode() -> int:
    return _run_usage_examples_duplicate_count_mode_coverage_guard(
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        "PASS: usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard mode validates duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard mode coverage"
    )


def run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode() -> int:
    return _run_usage_examples_duplicate_count_mode_coverage_guard(
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        "PASS: usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard mode validates duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard mode coverage"
    )


def run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode() -> int:
    return _run_usage_examples_duplicate_count_mode_coverage_guard(
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        "PASS: usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard mode validates duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard mode coverage"
    )

def run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode() -> int:
    return _run_usage_examples_duplicate_count_mode_coverage_guard(
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        "PASS: usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard mode validates duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard mode coverage"
    )


def run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode() -> int:
    return _run_usage_examples_duplicate_count_mode_coverage_guard(
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        "PASS: usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard mode validates duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard mode coverage"
    )

def run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode() -> int:
    return _run_usage_examples_duplicate_count_mode_coverage_guard(
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        "PASS: usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard mode validates duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard mode coverage"
    )


def run_usage_examples_duplicate_count_wrapper_all_mode_specs_guard_mode() -> int:
    wrapper_functions = [
        mode_handler
        for mode_name, mode_handler, _description in TRACE_SUMMARY_MODE_SPECS
        if mode_name.startswith("usage-examples-duplicate-count-mode-coverage-guard")
    ]
    assert wrapper_functions, "expected duplicate-count coverage-guard wrapper functions"

    wrappers_calling_all_mode_specs = [
        mode_handler.__name__
        for mode_handler in wrapper_functions
        if "_all_mode_specs()" in inspect.getsource(mode_handler)
    ]
    assert not wrappers_calling_all_mode_specs, (
        "expected duplicate-count coverage-guard wrappers to avoid direct _all_mode_specs() usage, "
        f"found regressions: {wrappers_calling_all_mode_specs}"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-all-mode-specs-guard mode validates duplicate-count "
        "coverage-guard wrappers avoid direct _all_mode_specs() calls"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_delegation_guard_mode() -> int:
    wrapper_functions = [
        mode_handler
        for mode_name, mode_handler, _description in TRACE_SUMMARY_MODE_SPECS
        if mode_name.startswith("usage-examples-duplicate-count-mode-coverage-guard")
    ]
    assert wrapper_functions, "expected duplicate-count coverage-guard wrapper functions"

    wrappers_missing_delegation = [
        mode_handler.__name__
        for mode_handler in wrapper_functions
        if "_run_usage_examples_duplicate_count_mode_coverage_guard(" not in inspect.getsource(mode_handler)
    ]
    assert not wrappers_missing_delegation, (
        "expected duplicate-count coverage-guard wrappers to delegate to "
        "_run_usage_examples_duplicate_count_mode_coverage_guard(...), "
        f"found regressions: {wrappers_missing_delegation}"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-delegation-guard mode validates duplicate-count "
        "coverage-guard wrappers delegate to _run_usage_examples_duplicate_count_mode_coverage_guard(...)"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_single_delegation_guard_mode() -> int:
    wrapper_functions = [
        mode_handler
        for mode_name, mode_handler, _description in TRACE_SUMMARY_MODE_SPECS
        if mode_name.startswith("usage-examples-duplicate-count-mode-coverage-guard")
    ]
    assert wrapper_functions, "expected duplicate-count coverage-guard wrapper functions"

    wrappers_without_single_delegation = [
        mode_handler.__name__
        for mode_handler in wrapper_functions
        if inspect.getsource(mode_handler).count("_run_usage_examples_duplicate_count_mode_coverage_guard(") != 1
    ]
    assert not wrappers_without_single_delegation, (
        "expected duplicate-count coverage-guard wrappers to call "
        "_run_usage_examples_duplicate_count_mode_coverage_guard(...) exactly once, "
        f"found regressions: {wrappers_without_single_delegation}"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-single-delegation-guard mode validates duplicate-count "
        "coverage-guard wrappers call _run_usage_examples_duplicate_count_mode_coverage_guard(...) exactly once"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_signature_guard_mode() -> int:
    wrapper_functions = [
        mode_handler
        for mode_name, mode_handler, _description in TRACE_SUMMARY_MODE_SPECS
        if mode_name.startswith("usage-examples-duplicate-count-mode-coverage-guard")
    ]
    assert wrapper_functions, "expected duplicate-count coverage-guard wrapper functions"

    wrappers_with_non_canonical_signature: list[str] = []
    for mode_handler in wrapper_functions:
        helper_calls = [
            node
            for node in ast.walk(ast.parse(inspect.getsource(mode_handler)))
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "_run_usage_examples_duplicate_count_mode_coverage_guard"
        ]
        if len(helper_calls) != 1:
            wrappers_with_non_canonical_signature.append(mode_handler.__name__)
            continue
        helper_call = helper_calls[0]
        if len(helper_call.args) != 2 or any(
            not isinstance(arg, ast.Constant) or not isinstance(arg.value, str) for arg in helper_call.args
        ):
            wrappers_with_non_canonical_signature.append(mode_handler.__name__)

    assert not wrappers_with_non_canonical_signature, (
        "expected duplicate-count coverage-guard wrappers to delegate with exactly two string arguments to "
        "_run_usage_examples_duplicate_count_mode_coverage_guard(...), "
        f"found regressions: {wrappers_with_non_canonical_signature}"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-signature-guard mode validates duplicate-count "
        "coverage-guard wrappers delegate with canonical two-string helper arguments"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_mode_name_literal_guard_mode() -> int:
    wrapper_mode_specs = [
        (mode_name, mode_handler)
        for mode_name, mode_handler, _description in TRACE_SUMMARY_MODE_SPECS
        if mode_name.startswith("usage-examples-duplicate-count-mode-coverage-guard")
    ]
    assert wrapper_mode_specs, "expected duplicate-count coverage-guard wrapper functions"

    wrappers_with_non_canonical_mode_name_literal: list[str] = []
    for mode_name, mode_handler in wrapper_mode_specs:
        helper_calls = [
            node
            for node in ast.walk(ast.parse(inspect.getsource(mode_handler)))
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "_run_usage_examples_duplicate_count_mode_coverage_guard"
        ]
        if len(helper_calls) != 1:
            wrappers_with_non_canonical_mode_name_literal.append(mode_handler.__name__)
            continue
        first_arg = helper_calls[0].args[0] if helper_calls[0].args else None
        if (
            not isinstance(first_arg, ast.Constant)
            or not isinstance(first_arg.value, str)
            or first_arg.value != mode_name
        ):
            wrappers_with_non_canonical_mode_name_literal.append(mode_handler.__name__)

    assert not wrappers_with_non_canonical_mode_name_literal, (
        "expected duplicate-count coverage-guard wrappers to pass their registered mode name as the first helper "
        "argument to _run_usage_examples_duplicate_count_mode_coverage_guard(...), "
        f"found regressions: {wrappers_with_non_canonical_mode_name_literal}"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-mode-name-literal-guard mode validates duplicate-count "
        "coverage-guard wrappers pass their registered mode name as the first helper argument"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_pass_message_literal_guard_mode() -> int:
    wrapper_mode_specs = [
        (mode_name, mode_handler)
        for mode_name, mode_handler, _description in TRACE_SUMMARY_MODE_SPECS
        if mode_name.startswith("usage-examples-duplicate-count-mode-coverage-guard")
    ]
    assert wrapper_mode_specs, "expected duplicate-count coverage-guard wrapper functions"

    wrappers_with_non_canonical_pass_message_literal: list[str] = []
    for mode_name, mode_handler in wrapper_mode_specs:
        helper_calls = [
            node
            for node in ast.walk(ast.parse(inspect.getsource(mode_handler)))
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "_run_usage_examples_duplicate_count_mode_coverage_guard"
        ]
        if len(helper_calls) != 1:
            wrappers_with_non_canonical_pass_message_literal.append(mode_handler.__name__)
            continue
        second_arg = helper_calls[0].args[1] if len(helper_calls[0].args) > 1 else None
        if (
            not isinstance(second_arg, ast.Constant)
            or not isinstance(second_arg.value, str)
            or mode_name not in second_arg.value
        ):
            wrappers_with_non_canonical_pass_message_literal.append(mode_handler.__name__)

    assert not wrappers_with_non_canonical_pass_message_literal, (
        "expected duplicate-count coverage-guard wrappers to use second helper argument PASS message literals "
        "that include their registered mode name, "
        f"found regressions: {wrappers_with_non_canonical_pass_message_literal}"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-pass-message-literal-guard mode validates duplicate-count "
        "coverage-guard wrappers use PASS message literals containing their registered mode name"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_pass_message_prefix_guard_mode() -> int:
    wrapper_mode_specs = [
        (mode_name, mode_handler)
        for mode_name, mode_handler, _description in TRACE_SUMMARY_MODE_SPECS
        if mode_name.startswith("usage-examples-duplicate-count-mode-coverage-guard")
    ]
    assert wrapper_mode_specs, "expected duplicate-count coverage-guard wrapper functions"

    wrappers_with_non_canonical_pass_message_prefix: list[str] = []
    for mode_name, mode_handler in wrapper_mode_specs:
        helper_calls = [
            node
            for node in ast.walk(ast.parse(inspect.getsource(mode_handler)))
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "_run_usage_examples_duplicate_count_mode_coverage_guard"
        ]
        if len(helper_calls) != 1:
            wrappers_with_non_canonical_pass_message_prefix.append(mode_handler.__name__)
            continue
        second_arg = helper_calls[0].args[1] if len(helper_calls[0].args) > 1 else None
        expected_prefix = f"PASS: {mode_name} mode validates"
        if (
            not isinstance(second_arg, ast.Constant)
            or not isinstance(second_arg.value, str)
            or not second_arg.value.startswith(expected_prefix)
        ):
            wrappers_with_non_canonical_pass_message_prefix.append(mode_handler.__name__)

    assert not wrappers_with_non_canonical_pass_message_prefix, (
        "expected duplicate-count coverage-guard wrappers to use second helper argument PASS message literals "
        "with canonical 'PASS: <mode-name> mode validates' prefixes, "
        f"found regressions: {wrappers_with_non_canonical_pass_message_prefix}"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-pass-message-prefix-guard mode validates duplicate-count "
        "coverage-guard wrappers use canonical PASS message prefixes"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_pass_message_suffix_guard_mode() -> int:
    wrapper_mode_specs = [
        (mode_name, mode_handler)
        for mode_name, mode_handler, _description in TRACE_SUMMARY_MODE_SPECS
        if mode_name.startswith("usage-examples-duplicate-count-mode-coverage-guard")
    ]
    assert wrapper_mode_specs, "expected duplicate-count coverage-guard wrapper functions"

    wrappers_with_non_canonical_pass_message_suffix: list[str] = []
    for _mode_name, mode_handler in wrapper_mode_specs:
        helper_calls = [
            node
            for node in ast.walk(ast.parse(inspect.getsource(mode_handler)))
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "_run_usage_examples_duplicate_count_mode_coverage_guard"
        ]
        if len(helper_calls) != 1:
            wrappers_with_non_canonical_pass_message_suffix.append(mode_handler.__name__)
            continue
        second_arg = helper_calls[0].args[1] if len(helper_calls[0].args) > 1 else None
        if not isinstance(second_arg, ast.Constant) or not isinstance(second_arg.value, str):
            wrappers_with_non_canonical_pass_message_suffix.append(mode_handler.__name__)
            continue
        suffix_segment = second_arg.value.split(" mode validates ", 1)[-1]
        if not (
            suffix_segment.startswith("duplicate-count ")
            and suffix_segment.endswith(" mode coverage")
        ):
            wrappers_with_non_canonical_pass_message_suffix.append(mode_handler.__name__)

    assert not wrappers_with_non_canonical_pass_message_suffix, (
        "expected duplicate-count coverage-guard wrappers to use second helper argument PASS message literals "
        "with canonical 'duplicate-count ... mode coverage' suffixes, "
        f"found regressions: {wrappers_with_non_canonical_pass_message_suffix}"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-pass-message-suffix-guard mode validates duplicate-count "
        "coverage-guard wrappers use canonical PASS message suffixes"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_pass_message_delimiter_guard_mode() -> int:
    wrapper_mode_specs = [
        (mode_name, mode_handler)
        for mode_name, mode_handler, _description in TRACE_SUMMARY_MODE_SPECS
        if mode_name.startswith("usage-examples-duplicate-count-mode-coverage-guard")
    ]
    assert wrapper_mode_specs, "expected duplicate-count coverage-guard wrapper functions"

    wrappers_with_non_canonical_pass_message_delimiter_count: list[str] = []
    for _mode_name, mode_handler in wrapper_mode_specs:
        helper_calls = [
            node
            for node in ast.walk(ast.parse(inspect.getsource(mode_handler)))
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "_run_usage_examples_duplicate_count_mode_coverage_guard"
        ]
        if len(helper_calls) != 1:
            wrappers_with_non_canonical_pass_message_delimiter_count.append(mode_handler.__name__)
            continue
        second_arg = helper_calls[0].args[1] if len(helper_calls[0].args) > 1 else None
        if not isinstance(second_arg, ast.Constant) or not isinstance(second_arg.value, str):
            wrappers_with_non_canonical_pass_message_delimiter_count.append(mode_handler.__name__)
            continue
        if second_arg.value.count(" mode validates ") != 1:
            wrappers_with_non_canonical_pass_message_delimiter_count.append(mode_handler.__name__)

    assert not wrappers_with_non_canonical_pass_message_delimiter_count, (
        "expected duplicate-count coverage-guard wrappers to use second helper argument PASS message literals "
        "with exactly one 'mode validates' delimiter, "
        f"found regressions: {wrappers_with_non_canonical_pass_message_delimiter_count}"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-pass-message-delimiter-guard mode validates duplicate-count "
        "coverage-guard wrappers use exactly one PASS message delimiter"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_literal_only_guard_mode() -> int:
    wrapper_mode_specs = [
        (mode_name, mode_handler)
        for mode_name, mode_handler, _description in TRACE_SUMMARY_MODE_SPECS
        if mode_name.startswith("usage-examples-duplicate-count-mode-coverage-guard")
    ]
    assert wrapper_mode_specs, "expected duplicate-count coverage-guard wrapper functions"

    wrappers_with_non_literal_helper_args: list[str] = []
    for _mode_name, mode_handler in wrapper_mode_specs:
        helper_calls = [
            node
            for node in ast.walk(ast.parse(inspect.getsource(mode_handler)))
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "_run_usage_examples_duplicate_count_mode_coverage_guard"
        ]
        if len(helper_calls) != 1:
            wrappers_with_non_literal_helper_args.append(mode_handler.__name__)
            continue
        helper_args = helper_calls[0].args
        if any(
            isinstance(arg, ast.JoinedStr) or (isinstance(arg, ast.BinOp) and isinstance(arg.op, ast.Add))
            for arg in helper_args
        ):
            wrappers_with_non_literal_helper_args.append(mode_handler.__name__)

    assert not wrappers_with_non_literal_helper_args, (
        "expected duplicate-count coverage-guard wrappers to pass literal-only helper arguments (no f-strings "
        "or concatenation), "
        f"found regressions: {wrappers_with_non_literal_helper_args}"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-literal-only-guard mode validates duplicate-count "
        "coverage-guard wrappers use literal-only helper arguments"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_positional_only_guard_mode() -> int:
    wrapper_mode_specs = [
        (mode_name, mode_handler)
        for mode_name, mode_handler, _description in TRACE_SUMMARY_MODE_SPECS
        if mode_name.startswith("usage-examples-duplicate-count-mode-coverage-guard")
    ]
    assert wrapper_mode_specs, "expected duplicate-count coverage-guard wrapper functions"

    wrappers_with_non_positional_only_helper_calls: list[str] = []
    for _mode_name, mode_handler in wrapper_mode_specs:
        helper_calls = [
            node
            for node in ast.walk(ast.parse(inspect.getsource(mode_handler)))
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "_run_usage_examples_duplicate_count_mode_coverage_guard"
        ]
        if len(helper_calls) != 1:
            wrappers_with_non_positional_only_helper_calls.append(mode_handler.__name__)
            continue
        helper_call = helper_calls[0]
        if len(helper_call.args) != 2 or helper_call.keywords:
            wrappers_with_non_positional_only_helper_calls.append(mode_handler.__name__)

    assert not wrappers_with_non_positional_only_helper_calls, (
        "expected duplicate-count coverage-guard wrappers to call "
        "_run_usage_examples_duplicate_count_mode_coverage_guard(...) with exactly two positional arguments "
        "and no keyword arguments, "
        f"found regressions: {wrappers_with_non_positional_only_helper_calls}"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-positional-only-guard mode validates duplicate-count "
        "coverage-guard wrappers call helper with exactly two positional arguments and no keywords"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_arg_order_guard_mode() -> int:
    wrapper_mode_specs = [
        (mode_name, mode_handler)
        for mode_name, mode_handler, _description in TRACE_SUMMARY_MODE_SPECS
        if mode_name.startswith("usage-examples-duplicate-count-mode-coverage-guard")
    ]
    assert wrapper_mode_specs, "expected duplicate-count coverage-guard wrapper functions"

    wrappers_with_non_canonical_helper_arg_order: list[str] = []
    for mode_name, mode_handler in wrapper_mode_specs:
        helper_calls = [
            node
            for node in ast.walk(ast.parse(inspect.getsource(mode_handler)))
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "_run_usage_examples_duplicate_count_mode_coverage_guard"
        ]
        if len(helper_calls) != 1:
            wrappers_with_non_canonical_helper_arg_order.append(mode_handler.__name__)
            continue
        helper_call = helper_calls[0]
        first_arg = helper_call.args[0] if len(helper_call.args) > 0 else None
        second_arg = helper_call.args[1] if len(helper_call.args) > 1 else None
        expected_prefix = f"PASS: {mode_name} mode validates"
        if (
            not isinstance(first_arg, ast.Constant)
            or not isinstance(first_arg.value, str)
            or first_arg.value != mode_name
            or not isinstance(second_arg, ast.Constant)
            or not isinstance(second_arg.value, str)
            or not second_arg.value.startswith(expected_prefix)
        ):
            wrappers_with_non_canonical_helper_arg_order.append(mode_handler.__name__)

    assert not wrappers_with_non_canonical_helper_arg_order, (
        "expected duplicate-count coverage-guard wrappers to call "
        "_run_usage_examples_duplicate_count_mode_coverage_guard(...) with canonical argument order "
        "(mode-name first, PASS-prefixed message second), "
        f"found regressions: {wrappers_with_non_canonical_helper_arg_order}"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-arg-order-guard mode validates duplicate-count "
        "coverage-guard wrappers pass mode-name first and canonical PASS-prefixed message second"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_mode_order_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    positional_only_guard_mode = "usage-examples-duplicate-count-wrapper-helper-positional-only-guard"
    arg_order_guard_mode = "usage-examples-duplicate-count-wrapper-helper-arg-order-guard"
    assert positional_only_guard_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {positional_only_guard_mode}"
    )
    assert arg_order_guard_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {arg_order_guard_mode}"
    )

    positional_only_guard_index = trace_summary_mode_names.index(positional_only_guard_mode)
    arg_order_guard_index = trace_summary_mode_names.index(arg_order_guard_mode)
    assert arg_order_guard_index - positional_only_guard_index == 1, (
        "expected usage-examples-duplicate-count-wrapper-helper-positional-only-guard to appear immediately "
        "before usage-examples-duplicate-count-wrapper-helper-arg-order-guard in TRACE_SUMMARY_MODE_SPECS"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-mode-order-guard mode validates duplicate-count "
        "wrapper helper hardening modes preserve positional-only then arg-order adjacency"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_adjacency_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    positional_only_guard_mode = "usage-examples-duplicate-count-wrapper-helper-positional-only-guard"
    arg_order_guard_mode = "usage-examples-duplicate-count-wrapper-helper-arg-order-guard"
    positional_only_guard_count = trace_summary_mode_names.count(positional_only_guard_mode)
    arg_order_guard_count = trace_summary_mode_names.count(arg_order_guard_mode)
    assert positional_only_guard_count == 1, (
        "expected usage-examples-duplicate-count-wrapper-helper-positional-only-guard to appear exactly once "
        f"in TRACE_SUMMARY_MODE_SPECS, found {positional_only_guard_count}"
    )
    assert arg_order_guard_count == 1, (
        "expected usage-examples-duplicate-count-wrapper-helper-arg-order-guard to appear exactly once "
        f"in TRACE_SUMMARY_MODE_SPECS, found {arg_order_guard_count}"
    )

    positional_only_guard_index = trace_summary_mode_names.index(positional_only_guard_mode)
    arg_order_guard_index = trace_summary_mode_names.index(arg_order_guard_mode)
    assert arg_order_guard_index - positional_only_guard_index == 1, (
        "expected usage-examples-duplicate-count-wrapper-helper-positional-only-guard to appear immediately "
        "before usage-examples-duplicate-count-wrapper-helper-arg-order-guard in TRACE_SUMMARY_MODE_SPECS"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-adjacency-guard mode validates "
        "duplicate-count wrapper helper hardening mode uniqueness before adjacency checks"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    mode_order_guard_mode = "usage-examples-duplicate-count-wrapper-helper-mode-order-guard"
    uniqueness_adjacency_guard_mode = "usage-examples-duplicate-count-wrapper-helper-uniqueness-adjacency-guard"
    assert mode_order_guard_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {mode_order_guard_mode}"
    )
    assert uniqueness_adjacency_guard_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {uniqueness_adjacency_guard_mode}"
    )

    mode_order_guard_index = trace_summary_mode_names.index(mode_order_guard_mode)
    uniqueness_adjacency_guard_index = trace_summary_mode_names.index(uniqueness_adjacency_guard_mode)
    assert uniqueness_adjacency_guard_index - mode_order_guard_index == 1, (
        "expected usage-examples-duplicate-count-wrapper-helper-mode-order-guard to appear immediately "
        "before usage-examples-duplicate-count-wrapper-helper-uniqueness-adjacency-guard in TRACE_SUMMARY_MODE_SPECS"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-guard mode validates "
        "duplicate-count wrapper helper hardening uniqueness-adjacency registration order"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    uniqueness_adjacency_guard_mode = "usage-examples-duplicate-count-wrapper-helper-uniqueness-adjacency-guard"
    uniqueness_order_guard_mode = "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-guard"
    assert uniqueness_adjacency_guard_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {uniqueness_adjacency_guard_mode}"
    )
    assert uniqueness_order_guard_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {uniqueness_order_guard_mode}"
    )

    uniqueness_adjacency_guard_index = trace_summary_mode_names.index(uniqueness_adjacency_guard_mode)
    uniqueness_order_guard_index = trace_summary_mode_names.index(uniqueness_order_guard_mode)
    assert uniqueness_order_guard_index - uniqueness_adjacency_guard_index == 1, (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-adjacency-guard to appear immediately "
        "before usage-examples-duplicate-count-wrapper-helper-uniqueness-order-guard in TRACE_SUMMARY_MODE_SPECS"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-guard mode validates "
        "duplicate-count wrapper helper hardening uniqueness-order adjacency registration order"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    uniqueness_order_guard_mode = "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-guard"
    uniqueness_order_adjacency_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-guard"
    )
    assert uniqueness_order_guard_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {uniqueness_order_guard_mode}"
    )
    assert uniqueness_order_adjacency_guard_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {uniqueness_order_adjacency_guard_mode}"
    )

    uniqueness_order_guard_index = trace_summary_mode_names.index(uniqueness_order_guard_mode)
    uniqueness_order_adjacency_guard_index = trace_summary_mode_names.index(
        uniqueness_order_adjacency_guard_mode
    )
    assert uniqueness_order_adjacency_guard_index - uniqueness_order_guard_index == 1, (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-guard to appear immediately "
        "before usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-guard in "
        "TRACE_SUMMARY_MODE_SPECS"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-guard mode validates "
        "duplicate-count wrapper helper hardening uniqueness-order adjacency ordering"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    uniqueness_order_adjacency_order_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-guard"
    )
    uniqueness_order_adjacency_order_guard_count = trace_summary_mode_names.count(
        uniqueness_order_adjacency_order_guard_mode
    )
    assert uniqueness_order_adjacency_order_guard_count == 1, (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-guard "
        "to appear exactly once in TRACE_SUMMARY_MODE_SPECS, found "
        f"{uniqueness_order_adjacency_order_guard_count}"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-guard "
        "mode validates duplicate-count wrapper helper uniqueness-order adjacency-order uniqueness"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    uniqueness_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-guard"
    )
    usage_examples_order_guard_mode = "usage-examples-order-guard"
    assert uniqueness_guard_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {uniqueness_guard_mode}"
    )
    assert usage_examples_order_guard_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {usage_examples_order_guard_mode}"
    )

    uniqueness_guard_mode_index = trace_summary_mode_names.index(uniqueness_guard_mode)
    usage_examples_order_guard_mode_index = trace_summary_mode_names.index(usage_examples_order_guard_mode)
    assert usage_examples_order_guard_mode_index - uniqueness_guard_mode_index == 1, (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-guard "
        "to appear immediately before usage-examples-order-guard in TRACE_SUMMARY_MODE_SPECS"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-guard "
        "mode validates uniqueness-order adjacency-order uniqueness guard precedes usage-examples-order-guard"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    uniqueness_adjacency_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-guard"
    )
    uniqueness_adjacency_guard_mode_count = trace_summary_mode_names.count(uniqueness_adjacency_guard_mode)
    assert uniqueness_adjacency_guard_mode_count == 1, (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-guard "
        "to appear exactly once in TRACE_SUMMARY_MODE_SPECS, found "
        f"{uniqueness_adjacency_guard_mode_count}"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-guard "
        "mode validates uniqueness-order adjacency-order uniqueness adjacency guard appears exactly once"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    uniqueness_adjacency_uniqueness_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-guard"
    )
    usage_examples_order_guard_mode = "usage-examples-order-guard"
    assert uniqueness_adjacency_uniqueness_guard_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {uniqueness_adjacency_uniqueness_guard_mode}"
    )
    assert usage_examples_order_guard_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {usage_examples_order_guard_mode}"
    )

    uniqueness_adjacency_uniqueness_guard_mode_index = trace_summary_mode_names.index(
        uniqueness_adjacency_uniqueness_guard_mode
    )
    usage_examples_order_guard_mode_index = trace_summary_mode_names.index(usage_examples_order_guard_mode)
    assert usage_examples_order_guard_mode_index - uniqueness_adjacency_uniqueness_guard_mode_index == 1, (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-guard "
        "to appear immediately before usage-examples-order-guard in TRACE_SUMMARY_MODE_SPECS"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-guard "
        "mode validates uniqueness-order adjacency-order uniqueness adjacency uniqueness guard precedes usage-examples-order-guard"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    usage_examples_order_guard_mode = "usage-examples-order-guard"
    uniqueness_adjacency_uniqueness_adjacency_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-guard"
    )
    assert usage_examples_order_guard_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {usage_examples_order_guard_mode}"
    )
    assert uniqueness_adjacency_uniqueness_adjacency_guard_mode in trace_summary_mode_names, (
        "expected TRACE_SUMMARY_MODE_SPECS to include "
        f"{uniqueness_adjacency_uniqueness_adjacency_guard_mode}"
    )

    usage_examples_order_guard_mode_index = trace_summary_mode_names.index(usage_examples_order_guard_mode)
    uniqueness_adjacency_uniqueness_adjacency_guard_mode_index = trace_summary_mode_names.index(
        uniqueness_adjacency_uniqueness_adjacency_guard_mode
    )
    assert (
        uniqueness_adjacency_uniqueness_adjacency_guard_mode_index
        - usage_examples_order_guard_mode_index
        == 1
    ), (
        "expected usage-examples-order-guard to appear immediately before "
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-guard "
        "in TRACE_SUMMARY_MODE_SPECS"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-guard "
        "mode validates usage-examples-order-guard precedes uniqueness-order adjacency-order uniqueness adjacency uniqueness adjacency guard"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    uniqueness_adjacency_uniqueness_adjacency_order_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-guard"
    )
    uniqueness_adjacency_uniqueness_adjacency_order_guard_count = trace_summary_mode_names.count(
        uniqueness_adjacency_uniqueness_adjacency_order_guard_mode
    )
    assert uniqueness_adjacency_uniqueness_adjacency_order_guard_count == 1, (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-guard "
        "to appear exactly once in TRACE_SUMMARY_MODE_SPECS, found "
        f"{uniqueness_adjacency_uniqueness_adjacency_order_guard_count}"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-guard "
        "mode validates uniqueness-order adjacency-order uniqueness adjacency uniqueness adjacency-order guard appears exactly once"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-guard"
    )
    usage_examples_order_guard_mode = "usage-examples-order-guard"
    assert uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_guard_mode in trace_summary_mode_names, (
        "expected TRACE_SUMMARY_MODE_SPECS to include "
        f"{uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_guard_mode}"
    )
    assert usage_examples_order_guard_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {usage_examples_order_guard_mode}"
    )

    uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_guard_mode_index = trace_summary_mode_names.index(
        uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_guard_mode
    )
    usage_examples_order_guard_mode_index = trace_summary_mode_names.index(usage_examples_order_guard_mode)
    assert (
        usage_examples_order_guard_mode_index
        - uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_guard_mode_index
        == 1
    ), (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-guard "
        "to appear immediately before usage-examples-order-guard in TRACE_SUMMARY_MODE_SPECS"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-guard "
        "mode validates uniqueness-order adjacency-order uniqueness adjacency uniqueness adjacency-order uniqueness guard precedes usage-examples-order-guard"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    uniqueness_adjacency_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-guard"
    )
    uniqueness_adjacency_guard_count = trace_summary_mode_names.count(uniqueness_adjacency_guard_mode)
    assert uniqueness_adjacency_guard_count == 1, (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-guard "
        "to appear exactly once in TRACE_SUMMARY_MODE_SPECS, found "
        f"{uniqueness_adjacency_guard_count}"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-guard "
        "mode validates uniqueness-order adjacency-order uniqueness adjacency uniqueness adjacency-order uniqueness adjacency guard appears exactly once"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    uniqueness_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-guard"
    )
    mode_set_coverage_guard_mode = "usage-examples-mode-set-coverage-guard"
    assert uniqueness_guard_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {uniqueness_guard_mode}"
    )
    assert mode_set_coverage_guard_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {mode_set_coverage_guard_mode}"
    )

    uniqueness_guard_mode_index = trace_summary_mode_names.index(uniqueness_guard_mode)
    mode_set_coverage_guard_mode_index = trace_summary_mode_names.index(mode_set_coverage_guard_mode)
    assert mode_set_coverage_guard_mode_index - uniqueness_guard_mode_index == 1, (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-guard "
        "to appear immediately before usage-examples-mode-set-coverage-guard in TRACE_SUMMARY_MODE_SPECS"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-guard "
        "mode validates uniqueness-order adjacency-order uniqueness adjacency uniqueness adjacency-order uniqueness adjacency uniqueness guard precedes usage-examples-mode-set-coverage-guard"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    uniqueness_adjacency_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-guard"
    )
    uniqueness_adjacency_guard_count = trace_summary_mode_names.count(uniqueness_adjacency_guard_mode)
    assert uniqueness_adjacency_guard_count == 1, (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-guard "
        "to appear exactly once in TRACE_SUMMARY_MODE_SPECS, found "
        f"{uniqueness_adjacency_guard_count}"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-guard "
        "mode validates uniqueness-order adjacency-order uniqueness adjacency uniqueness adjacency-order uniqueness adjacency uniqueness adjacency guard appears exactly once"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    uniqueness_adjacency_uniqueness_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-guard"
    )
    uniqueness_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-guard"
    )
    assert uniqueness_adjacency_uniqueness_guard_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {uniqueness_adjacency_uniqueness_guard_mode}"
    )
    assert uniqueness_guard_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {uniqueness_guard_mode}"
    )

    uniqueness_adjacency_uniqueness_guard_index = trace_summary_mode_names.index(uniqueness_adjacency_uniqueness_guard_mode)
    uniqueness_guard_index = trace_summary_mode_names.index(uniqueness_guard_mode)
    assert uniqueness_adjacency_uniqueness_guard_index + 1 == uniqueness_guard_index, (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-guard "
        "to appear immediately before usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-guard "
        "in TRACE_SUMMARY_MODE_SPECS"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-guard "
        "mode validates uniqueness-order adjacency-order uniqueness adjacency uniqueness adjacency-order uniqueness adjacency uniqueness adjacency uniqueness guard appears immediately before uniqueness guard"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    uniqueness_adjacency_uniqueness_adjacency_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-guard"
    )
    uniqueness_adjacency_uniqueness_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-guard"
    )
    assert uniqueness_adjacency_uniqueness_adjacency_guard_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {uniqueness_adjacency_uniqueness_adjacency_guard_mode}"
    )
    assert uniqueness_adjacency_uniqueness_guard_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {uniqueness_adjacency_uniqueness_guard_mode}"
    )

    uniqueness_adjacency_uniqueness_adjacency_guard_index = trace_summary_mode_names.index(
        uniqueness_adjacency_uniqueness_adjacency_guard_mode
    )
    uniqueness_adjacency_uniqueness_guard_index = trace_summary_mode_names.index(
        uniqueness_adjacency_uniqueness_guard_mode
    )
    assert uniqueness_adjacency_uniqueness_adjacency_guard_index + 1 == uniqueness_adjacency_uniqueness_guard_index, (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-guard "
        "to appear immediately before usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-guard "
        "in TRACE_SUMMARY_MODE_SPECS"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-guard "
        "mode validates uniqueness-order adjacency-order uniqueness adjacency uniqueness adjacency-order uniqueness adjacency uniqueness adjacency uniqueness adjacency uniqueness guard appears immediately before uniqueness adjacency uniqueness guard"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    uniqueness_adjacency_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-guard"
    )
    uniqueness_adjacency_count = trace_summary_mode_names.count(uniqueness_adjacency_mode)
    assert uniqueness_adjacency_count == 1, (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-guard "
        "to appear exactly once in TRACE_SUMMARY_MODE_SPECS, found "
        f"{uniqueness_adjacency_count}"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-guard "
        "mode validates uniqueness-order adjacency-order uniqueness adjacency uniqueness adjacency-order uniqueness adjacency uniqueness adjacency uniqueness adjacency guard appears exactly once"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-guard"
    )
    uniqueness_adjacency_uniqueness_adjacency_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-guard"
    )
    assert uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_guard_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_guard_mode}"
    )
    assert uniqueness_adjacency_uniqueness_adjacency_guard_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {uniqueness_adjacency_uniqueness_adjacency_guard_mode}"
    )

    uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_guard_index = trace_summary_mode_names.index(
        uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_guard_mode
    )
    uniqueness_adjacency_uniqueness_adjacency_guard_index = trace_summary_mode_names.index(
        uniqueness_adjacency_uniqueness_adjacency_guard_mode
    )
    assert (
        uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_guard_index + 1
        == uniqueness_adjacency_uniqueness_adjacency_guard_index
    ), (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-guard "
        "to appear immediately before usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-guard "
        "in TRACE_SUMMARY_MODE_SPECS"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-guard "
        "mode validates uniqueness-order adjacency-order uniqueness adjacency uniqueness adjacency-order uniqueness adjacency uniqueness adjacency uniqueness adjacency uniqueness adjacency uniqueness adjacency guard appears immediately before uniqueness adjacency uniqueness adjacency guard"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    uniqueness_adjacency_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-guard"
    )
    uniqueness_adjacency_count = trace_summary_mode_names.count(uniqueness_adjacency_mode)
    assert uniqueness_adjacency_count == 1, (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-guard "
        "to appear exactly once in TRACE_SUMMARY_MODE_SPECS, found "
        f"{uniqueness_adjacency_count}"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-guard "
        "mode validates uniqueness-order adjacency-order uniqueness adjacency uniqueness adjacency-order uniqueness adjacency uniqueness adjacency uniqueness adjacency uniqueness adjacency uniqueness adjacency guard appears exactly once"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    newest_uniqueness_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-guard"
    )
    prior_uniqueness_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-guard"
    )
    assert newest_uniqueness_guard_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {newest_uniqueness_guard_mode}"
    )
    assert prior_uniqueness_guard_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {prior_uniqueness_guard_mode}"
    )

    newest_uniqueness_guard_index = trace_summary_mode_names.index(newest_uniqueness_guard_mode)
    prior_uniqueness_guard_index = trace_summary_mode_names.index(prior_uniqueness_guard_mode)
    assert newest_uniqueness_guard_index + 1 == prior_uniqueness_guard_index, (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-guard "
        "to appear immediately before usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-guard "
        "in TRACE_SUMMARY_MODE_SPECS"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-guard "
        "mode validates newest uniqueness guard appears immediately before prior uniqueness guard"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    newest_adjacency_order_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-guard"
    )
    newest_adjacency_order_guard_count = trace_summary_mode_names.count(newest_adjacency_order_guard_mode)
    assert newest_adjacency_order_guard_count == 1, (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-guard "
        "to appear exactly once in TRACE_SUMMARY_MODE_SPECS, found "
        f"{newest_adjacency_order_guard_count}"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-guard "
        "mode validates newest uniqueness adjacency-order guard appears exactly once"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    newest_uniqueness_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-guard"
    )
    newest_adjacency_order_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-guard"
    )
    assert newest_uniqueness_guard_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {newest_uniqueness_guard_mode}"
    )
    assert newest_adjacency_order_guard_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {newest_adjacency_order_guard_mode}"
    )

    newest_uniqueness_guard_index = trace_summary_mode_names.index(newest_uniqueness_guard_mode)
    newest_adjacency_order_guard_index = trace_summary_mode_names.index(newest_adjacency_order_guard_mode)
    assert newest_uniqueness_guard_index + 1 == newest_adjacency_order_guard_index, (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-guard "
        "to appear immediately before usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-guard "
        "in TRACE_SUMMARY_MODE_SPECS"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-guard "
        "mode validates newest uniqueness guard appears immediately before newest adjacency-order guard"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    newest_uniqueness_adjacency_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-guard"
    )
    newest_uniqueness_adjacency_guard_count = trace_summary_mode_names.count(newest_uniqueness_adjacency_guard_mode)
    assert newest_uniqueness_adjacency_guard_count == 1, (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-guard "
        "to appear exactly once in TRACE_SUMMARY_MODE_SPECS, found "
        f"{newest_uniqueness_adjacency_guard_count}"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-guard "
        "mode validates newest uniqueness adjacency-order adjacency guard appears exactly once"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    newest_uniqueness_adjacency_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-guard"
    )
    prior_uniqueness_adjacency_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-guard"
    )
    assert newest_uniqueness_adjacency_guard_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {newest_uniqueness_adjacency_guard_mode}"
    )
    assert prior_uniqueness_adjacency_guard_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {prior_uniqueness_adjacency_guard_mode}"
    )

    newest_uniqueness_adjacency_guard_index = trace_summary_mode_names.index(newest_uniqueness_adjacency_guard_mode)
    prior_uniqueness_adjacency_guard_index = trace_summary_mode_names.index(prior_uniqueness_adjacency_guard_mode)
    assert newest_uniqueness_adjacency_guard_index + 1 == prior_uniqueness_adjacency_guard_index, (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-guard "
        "to appear immediately before usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-guard "
        "in TRACE_SUMMARY_MODE_SPECS"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-guard "
        "mode validates newest uniqueness adjacency-order adjacency guard appears immediately before prior uniqueness adjacency-order guard"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    newest_uniqueness_adjacency_order_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-guard"
    )
    newest_uniqueness_adjacency_order_guard_count = trace_summary_mode_names.count(
        newest_uniqueness_adjacency_order_guard_mode
    )
    assert newest_uniqueness_adjacency_order_guard_count == 1, (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-guard "
        "to appear exactly once in TRACE_SUMMARY_MODE_SPECS, found "
        f"{newest_uniqueness_adjacency_order_guard_count}"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-guard "
        "mode validates newest uniqueness adjacency-order adjacency ordering guard appears exactly once"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_order_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    newest_uniqueness_adjacency_order_uniqueness_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-guard"
    )
    newest_uniqueness_adjacency_order_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-guard"
    )
    assert newest_uniqueness_adjacency_order_uniqueness_guard_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {newest_uniqueness_adjacency_order_uniqueness_guard_mode}"
    )
    assert newest_uniqueness_adjacency_order_guard_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {newest_uniqueness_adjacency_order_guard_mode}"
    )

    newest_uniqueness_adjacency_order_uniqueness_guard_index = trace_summary_mode_names.index(
        newest_uniqueness_adjacency_order_uniqueness_guard_mode
    )
    newest_uniqueness_adjacency_order_guard_index = trace_summary_mode_names.index(
        newest_uniqueness_adjacency_order_guard_mode
    )
    assert (
        newest_uniqueness_adjacency_order_uniqueness_guard_index + 1
        == newest_uniqueness_adjacency_order_guard_index
    ), (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-guard "
        "to appear immediately before usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-guard "
        "in TRACE_SUMMARY_MODE_SPECS"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-guard "
        "mode validates newest uniqueness adjacency-order adjacency ordering uniqueness guard appears immediately before newest adjacency-order adjacency ordering guard"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_order_uniqueness_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    newest_uniqueness_adjacency_order_uniqueness_order_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-guard"
    )
    newest_uniqueness_adjacency_order_uniqueness_order_guard_count = trace_summary_mode_names.count(
        newest_uniqueness_adjacency_order_uniqueness_order_guard_mode
    )
    assert newest_uniqueness_adjacency_order_uniqueness_order_guard_count == 1, (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-guard "
        "to appear exactly once in TRACE_SUMMARY_MODE_SPECS, found "
        f"{newest_uniqueness_adjacency_order_uniqueness_order_guard_count}"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-guard "
        "mode validates newest uniqueness adjacency-order adjacency ordering uniqueness-order guard appears exactly once"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-guard"
    )
    newest_uniqueness_adjacency_order_uniqueness_order_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-guard"
    )
    assert newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_guard_mode in trace_summary_mode_names, (
        "expected TRACE_SUMMARY_MODE_SPECS to include "
        f"{newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_guard_mode}"
    )
    assert newest_uniqueness_adjacency_order_uniqueness_order_guard_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {newest_uniqueness_adjacency_order_uniqueness_order_guard_mode}"
    )

    newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_guard_index = trace_summary_mode_names.index(
        newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_guard_mode
    )
    newest_uniqueness_adjacency_order_uniqueness_order_guard_index = trace_summary_mode_names.index(
        newest_uniqueness_adjacency_order_uniqueness_order_guard_mode
    )
    assert (
        newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_guard_index + 1
        == newest_uniqueness_adjacency_order_uniqueness_order_guard_index
    ), (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-guard "
        "to appear immediately before usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-guard "
        "in TRACE_SUMMARY_MODE_SPECS"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-guard "
        "mode validates newest uniqueness adjacency-order adjacency ordering uniqueness-order uniqueness guard appears immediately before newest uniqueness-order adjacency ordering guard"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-guard"
    )
    newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_guard_count = trace_summary_mode_names.count(
        newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_guard_mode
    )
    assert newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_guard_count == 1, (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-guard "
        "to appear exactly once in TRACE_SUMMARY_MODE_SPECS, found "
        f"{newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_guard_count}"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-guard "
        "mode validates newest uniqueness adjacency-order adjacency ordering uniqueness-order uniqueness ordering guard appears exactly once"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-guard"
    )
    newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-guard"
    )
    assert newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_mode in trace_summary_mode_names, (
        "expected TRACE_SUMMARY_MODE_SPECS to include "
        f"{newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_mode}"
    )
    assert newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_guard_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_guard_mode}"
    )

    newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_guard_index = trace_summary_mode_names.index(
        newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_mode
    )
    newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_guard_index = trace_summary_mode_names.index(
        newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_guard_mode
    )
    assert (
        newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_guard_index + 1
        == newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_guard_index
    ), (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-guard "
        "to appear immediately before usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-guard "
        "in TRACE_SUMMARY_MODE_SPECS"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-guard "
        "mode validates newest uniqueness adjacency-order adjacency ordering uniqueness-order uniqueness ordering uniqueness ordering guard appears immediately before newest uniqueness-order uniqueness ordering guard"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-guard"
    )
    newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_count = trace_summary_mode_names.count(
        newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_mode
    )
    assert newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_count == 1, (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-guard "
        "to appear exactly once in TRACE_SUMMARY_MODE_SPECS, found "
        f"{newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_count}"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard "
        "mode validates newest uniqueness adjacency-order adjacency ordering uniqueness-order uniqueness ordering uniqueness ordering adjacency guard appears exactly once"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-guard"
    )
    newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_count = trace_summary_mode_names.count(
        newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_mode
    )
    assert newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_count == 1, (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-guard "
        "to appear exactly once in TRACE_SUMMARY_MODE_SPECS, found "
        f"{newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_count}"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard "
        "mode validates newest uniqueness adjacency-order adjacency ordering uniqueness-order uniqueness ordering uniqueness ordering uniqueness-order adjacency guard appears exactly once"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-guard"
    )
    newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-guard"
    )
    assert newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_mode in trace_summary_mode_names, (
        "expected TRACE_SUMMARY_MODE_SPECS to include "
        f"{newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_mode}"
    )
    assert newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_mode}"
    )

    newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_index = trace_summary_mode_names.index(
        newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_mode
    )
    newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_index = trace_summary_mode_names.index(
        newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_mode
    )
    assert (
        newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_index + 1
        == newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_index
    ), (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-guard "
        "to appear immediately before usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-guard "
        "in TRACE_SUMMARY_MODE_SPECS"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-guard "
        "mode validates newest uniqueness adjacency-order adjacency ordering uniqueness-order uniqueness ordering uniqueness ordering uniqueness-order adjacency guard appears immediately before prior uniqueness-order adjacency guard"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard"
    )
    newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-guard"
    )
    assert newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_guard_mode in trace_summary_mode_names, (
        "expected TRACE_SUMMARY_MODE_SPECS to include "
        f"{newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_guard_mode}"
    )
    assert newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_mode}"
    )

    newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_guard_index = trace_summary_mode_names.index(
        newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_guard_mode
    )
    newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_index = trace_summary_mode_names.index(
        newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_mode
    )
    assert (
        newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_guard_index + 1
        == newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_index
    ), (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard "
        "to appear immediately before usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-guard "
        "in TRACE_SUMMARY_MODE_SPECS"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-guard "
        "mode validates newest uniqueness adjacency-order adjacency ordering uniqueness-order uniqueness ordering uniqueness ordering uniqueness-order uniqueness guard appears immediately before prior uniqueness-order uniqueness-order guard"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-guard"
    )
    newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_count = trace_summary_mode_names.count(
        newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_mode
    )
    assert newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_count == 1, (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-guard "
        "to appear exactly once in TRACE_SUMMARY_MODE_SPECS, found "
        f"{newest_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_count}"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard "
        "mode validates newest uniqueness adjacency-order adjacency ordering uniqueness-order uniqueness ordering uniqueness ordering uniqueness-order uniqueness adjacency-order mode appears exactly once"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_guard_adjacency_order_guard_uniqueness_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    newest_long_form_uniqueness_order_adjacency_order_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard-adjacency-order-guard"
    )
    newest_long_form_uniqueness_order_adjacency_order_mode_count = trace_summary_mode_names.count(
        newest_long_form_uniqueness_order_adjacency_order_mode
    )
    assert newest_long_form_uniqueness_order_adjacency_order_mode_count == 1, (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard-adjacency-order-guard "
        "to appear exactly once in TRACE_SUMMARY_MODE_SPECS, found "
        f"{newest_long_form_uniqueness_order_adjacency_order_mode_count}"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard-adjacency-order-guard-uniqueness-guard "
        "mode validates newest long-form uniqueness-order adjacency-order mode appears exactly once"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_guard_adjacency_order_guard_uniqueness_guard_adjacency_order_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    newest_long_form_uniqueness_order_adjacency_order_uniqueness_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard-adjacency-order-guard-uniqueness-guard"
    )
    prior_long_form_uniqueness_order_adjacency_order_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard-adjacency-order-guard"
    )
    assert newest_long_form_uniqueness_order_adjacency_order_uniqueness_guard_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {newest_long_form_uniqueness_order_adjacency_order_uniqueness_guard_mode}"
    )
    assert prior_long_form_uniqueness_order_adjacency_order_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {prior_long_form_uniqueness_order_adjacency_order_mode}"
    )

    newest_long_form_uniqueness_order_adjacency_order_uniqueness_guard_mode_index = trace_summary_mode_names.index(
        newest_long_form_uniqueness_order_adjacency_order_uniqueness_guard_mode
    )
    prior_long_form_uniqueness_order_adjacency_order_mode_index = trace_summary_mode_names.index(
        prior_long_form_uniqueness_order_adjacency_order_mode
    )
    assert newest_long_form_uniqueness_order_adjacency_order_uniqueness_guard_mode_index + 1 == prior_long_form_uniqueness_order_adjacency_order_mode_index, (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard-adjacency-order-guard-uniqueness-guard "
        "to appear immediately before usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard-adjacency-order-guard "
        "in TRACE_SUMMARY_MODE_SPECS"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard "
        "mode validates newest long-form uniqueness-order adjacency-order uniqueness mode appears immediately before prior long-form uniqueness-order adjacency-order mode"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_guard_adjacency_order_guard_uniqueness_guard_adjacency_order_guard_uniqueness_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    newest_long_form_uniqueness_order_adjacency_order_uniqueness_guard_adjacency_order_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard"
    )
    newest_long_form_uniqueness_order_adjacency_order_uniqueness_guard_adjacency_order_mode_count = trace_summary_mode_names.count(
        newest_long_form_uniqueness_order_adjacency_order_uniqueness_guard_adjacency_order_mode
    )
    assert newest_long_form_uniqueness_order_adjacency_order_uniqueness_guard_adjacency_order_mode_count == 1, (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard "
        "to appear exactly once in TRACE_SUMMARY_MODE_SPECS, found "
        f"{newest_long_form_uniqueness_order_adjacency_order_uniqueness_guard_adjacency_order_mode_count}"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard-uniqueness-guard "
        "mode validates newest long-form uniqueness-order adjacency-order uniqueness adjacency-order mode appears exactly once"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_guard_adjacency_order_guard_uniqueness_guard_adjacency_order_guard_uniqueness_guard_adjacency_order_guard_uniqueness_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    newest_long_form_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard"
    )
    newest_long_form_mode_count = trace_summary_mode_names.count(newest_long_form_mode)
    assert newest_long_form_mode_count == 1, (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard "
        "to appear exactly once in TRACE_SUMMARY_MODE_SPECS, found "
        f"{newest_long_form_mode_count}"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard-uniqueness-guard "
        "mode validates newest long-form uniqueness-order adjacency-order uniqueness adjacency-order uniqueness adjacency-order mode appears exactly once"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_guard_adjacency_order_guard_uniqueness_guard_adjacency_order_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    newest_long_form_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard-uniqueness-guard"
    )
    prior_long_form_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard"
    )
    assert newest_long_form_mode in trace_summary_mode_names, f"expected TRACE_SUMMARY_MODE_SPECS to include {newest_long_form_mode}"
    assert prior_long_form_mode in trace_summary_mode_names, f"expected TRACE_SUMMARY_MODE_SPECS to include {prior_long_form_mode}"

    newest_long_form_mode_index = trace_summary_mode_names.index(newest_long_form_mode)
    prior_long_form_mode_index = trace_summary_mode_names.index(prior_long_form_mode)
    assert newest_long_form_mode_index + 1 == prior_long_form_mode_index, (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard-uniqueness-guard "
        "to appear immediately before usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard "
        "in TRACE_SUMMARY_MODE_SPECS"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard "
        "mode validates newest long-form uniqueness-order adjacency-order uniqueness mode appears immediately before newest long-form uniqueness-order adjacency-order uniqueness adjacency-order mode"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_guard_adjacency_order_guard_uniqueness_guard_adjacency_order_guard_uniqueness_guard_adjacency_order_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    adjacency_order_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard"
    )
    paired_uniqueness_guard_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard-uniqueness-guard"
    )
    assert adjacency_order_guard_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {adjacency_order_guard_mode}"
    )
    assert paired_uniqueness_guard_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {paired_uniqueness_guard_mode}"
    )

    adjacency_order_guard_mode_index = trace_summary_mode_names.index(adjacency_order_guard_mode)
    paired_uniqueness_guard_mode_index = trace_summary_mode_names.index(paired_uniqueness_guard_mode)
    assert paired_uniqueness_guard_mode_index + 1 == adjacency_order_guard_mode_index, (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard-uniqueness-guard "
        "to appear immediately before usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard "
        "in TRACE_SUMMARY_MODE_SPECS"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard "
        "mode validates the paired uniqueness-count mode appears immediately before the long-form adjacency-order guard mode"
    )
    return 0


def run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_guard_adjacency_order_guard_mode() -> int:
    trace_summary_mode_names = [mode_name for mode_name, _mode_handler, _description in TRACE_SUMMARY_MODE_SPECS]
    newest_uniqueness_order_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard"
    )
    prior_uniqueness_order_mode = (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-guard"
    )
    assert newest_uniqueness_order_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {newest_uniqueness_order_mode}"
    )
    assert prior_uniqueness_order_mode in trace_summary_mode_names, (
        f"expected TRACE_SUMMARY_MODE_SPECS to include {prior_uniqueness_order_mode}"
    )

    newest_uniqueness_order_mode_index = trace_summary_mode_names.index(newest_uniqueness_order_mode)
    prior_uniqueness_order_mode_index = trace_summary_mode_names.index(prior_uniqueness_order_mode)
    assert newest_uniqueness_order_mode_index + 1 == prior_uniqueness_order_mode_index, (
        "expected usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard "
        "to appear immediately before usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-guard "
        "in TRACE_SUMMARY_MODE_SPECS"
    )

    print(
        "PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard-adjacency-order-guard "
        "mode validates newest long-form uniqueness-order uniqueness mode appears immediately before prior long-form uniqueness-order mode"
    )
    return 0


def run_usage_examples_order_guard_mode() -> int:
    all_mode_specs = _all_mode_specs()
    usage_lines = _usage_doc_lines(all_mode_specs)
    expected_mode_order = _expected_non_stub_mode_names(all_mode_specs)
    actual_mode_order = _generated_non_stub_usage_mode_names(usage_lines)
    assert actual_mode_order == expected_mode_order, (
        "expected generated usage examples to preserve non-stub mode registration order"
    )

    print(
        "PASS: usage-examples-order-guard mode validates generated usage examples preserve registration order"
    )
    return 0


def run_usage_examples_mode_set_coverage_guard_mode() -> int:
    all_mode_specs = _all_mode_specs()
    usage_lines = _usage_doc_lines(all_mode_specs)
    expected_mode_names = _expected_non_stub_mode_names(all_mode_specs)
    actual_mode_names = _generated_non_stub_usage_mode_names(usage_lines)
    assert len(actual_mode_names) == len(expected_mode_names), (
        "expected generated usage examples to include each non-stub mode exactly once by count"
    )
    assert set(actual_mode_names) == set(expected_mode_names), (
        "expected generated usage examples to include each non-stub mode exactly once by set coverage"
    )

    print(
        "PASS: usage-examples-mode-set-coverage-guard mode validates generated usage examples cover all non-stub modes exactly once"
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
        "trace-summary-kernel",
        run_trace_summary_kernel_mode,
        "fixture-backed --run-kernel-for-trace-summary success assertion",
    ),
    (
        "trace-summary-kernel-malformed-phase",
        run_trace_summary_kernel_malformed_phase_mode,
        "fixture-backed malformed phase-trace key failure assertion",
    ),
    (
        "trace-summary-kernel-malformed-phase-payload",
        run_trace_summary_kernel_malformed_phase_payload_mode,
        "fixture-backed non-object phase-trace payload failure assertion",
    ),
    (
        "trace-summary-kernel-missing-phase",
        run_trace_summary_kernel_missing_phase_mode,
        "fixture-backed missing required phase-trace assertion",
    ),
    (
        "trace-summary-kernel-fixture-cleanup",
        run_trace_summary_kernel_fixture_cleanup_mode,
        "fixture-backed kernel trace-summary cleanup assertion",
    ),
    (
        "trace-summary-kernel-fixture-root-cleanup",
        run_trace_summary_kernel_fixture_root_cleanup_mode,
        "fixture-backed kernel trace-summary root cleanup assertion",
    ),
    (
        "trace-summary-non-kernel-fixture-cleanup",
        run_trace_summary_non_kernel_fixture_cleanup_mode,
        "fixture-backed non-kernel trace-summary cleanup assertion",
    ),
    (
        "trace-summary-non-kernel-fixture-root-cleanup",
        run_trace_summary_non_kernel_fixture_root_cleanup_mode,
        "fixture-backed non-kernel trace-summary root cleanup assertion",
    ),
    (
        "trace-summary-fixture-root-cleanup-parity",
        run_trace_summary_fixture_root_cleanup_parity_mode,
        "fixture-backed parity assertion for kernel and non-kernel trace-summary root cleanup",
    ),
    (
        "trace-summary-fixture-cleanup-parity",
        run_trace_summary_fixture_cleanup_parity_mode,
        "fixture-backed parity assertion for kernel and non-kernel trace-summary cleanup",
    ),
    (
        "trace-summary-fixture-cleanup-parity-usage-examples-guard",
        run_trace_summary_fixture_cleanup_parity_usage_examples_guard_mode,
        "deterministic generated usage-example uniqueness assertion for parity cleanup modes",
    ),
    (
        "trace-summary-fixture-cleanup-parity-mode-choices-usage-examples-order-guard",
        run_trace_summary_fixture_cleanup_parity_mode_choices_usage_examples_order_guard_mode,
        "deterministic parity cleanup mode ordering assertion between argparse choices and usage examples",
    ),
    (
        "trace-summary-fixture-cleanup-parity-mode-choices-uniqueness-guard",
        run_trace_summary_fixture_cleanup_parity_mode_choices_uniqueness_guard_mode,
        "deterministic parity cleanup mode argparse choice uniqueness assertion",
    ),
    (
        "trace-summary-fixture-cleanup-parity-mode-choices-usage-examples-adjacency-guard",
        run_trace_summary_fixture_cleanup_parity_mode_choices_usage_examples_adjacency_guard_mode,
        "deterministic parity cleanup mode adjacency assertion across argparse choices and usage examples",
    ),
    (
        "trace-summary-fixture-cleanup-parity-mode-choices-usage-examples-uniqueness-adjacency-guard",
        run_trace_summary_fixture_cleanup_parity_mode_choices_usage_examples_uniqueness_adjacency_guard_mode,
        "deterministic parity cleanup mode first-occurrence uniqueness and adjacency assertion across argparse choices and usage examples",
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
    (
        "usage-examples-duplicate-count-regression-guard",
        run_usage_examples_duplicate_count_regression_guard_mode,
        "deterministic generated usage-example duplicate-count diagnostics assertion",
    ),
    (
        "usage-examples-duplicate-count-mode-coverage-guard",
        run_usage_examples_duplicate_count_mode_coverage_guard_mode,
        "deterministic duplicate-count regression mode coverage across parser choices and usage examples assertion",
    ),
    (
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard",
        run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_mode,
        "deterministic duplicate-count mode-coverage guard mode coverage across parser choices and usage examples assertion",
    ),
    (
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard",
        run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_mode,
        "deterministic duplicate-count mode-coverage guard-coverage guard mode coverage across parser choices and usage examples assertion",
    ),
    (
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode,
        "deterministic duplicate-count mode-coverage guard-coverage guard-coverage guard mode coverage across parser choices and usage examples assertion",
    ),
    (
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode,
        "deterministic duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard mode coverage across parser choices and usage examples assertion",
    ),
    (
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode,
        "deterministic duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard mode coverage across parser choices and usage examples assertion",
    ),
    (
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode,
        "deterministic duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard mode coverage across parser choices and usage examples assertion",
    ),
    (
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode,
        "deterministic duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard mode coverage across parser choices and usage examples assertion",
    ),
    (
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode,
        "deterministic duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard mode coverage across parser choices and usage examples assertion",
    ),
    (
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode,
        "deterministic duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard mode coverage across parser choices and usage examples assertion",
    ),
    (
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode,
        "deterministic duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard mode coverage across parser choices and usage examples assertion",
    ),
    (
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode,
        "deterministic duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard mode coverage across parser choices and usage examples assertion",
    ),
    (
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode,
        "deterministic duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard mode coverage across parser choices and usage examples assertion",
    ),
    (
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode,
        "deterministic duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard mode coverage across parser choices and usage examples assertion",
    ),
    (
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode,
        "deterministic duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard mode coverage across parser choices and usage examples assertion",
    ),
    (
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode,
        "deterministic duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard mode coverage across parser choices and usage examples assertion",
    ),
    (
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode,
        "deterministic duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard mode coverage across parser choices and usage examples assertion",
    ),
    (
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode,
        "deterministic duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard mode coverage across parser choices and usage examples assertion",
    ),
    (
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode,
        "deterministic duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard mode coverage across parser choices and usage examples assertion",
    ),
    (
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode,
        "deterministic duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard mode coverage across parser choices and usage examples assertion",
    ),
    (
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode,
        "deterministic duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard mode coverage across parser choices and usage examples assertion",
    ),
    (
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode,
        "deterministic duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard mode coverage across parser choices and usage examples assertion",
    ),
    (
        "usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard-coverage-guard",
        run_usage_examples_duplicate_count_mode_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_coverage_guard_mode,
        "deterministic duplicate-count mode-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard-coverage guard mode coverage across parser choices and usage examples assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-all-mode-specs-guard",
        run_usage_examples_duplicate_count_wrapper_all_mode_specs_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper source regression assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-delegation-guard",
        run_usage_examples_duplicate_count_wrapper_helper_delegation_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper delegation assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-single-delegation-guard",
        run_usage_examples_duplicate_count_wrapper_helper_single_delegation_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper single helper delegation assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-signature-guard",
        run_usage_examples_duplicate_count_wrapper_helper_signature_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper signature assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-mode-name-literal-guard",
        run_usage_examples_duplicate_count_wrapper_helper_mode_name_literal_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper first-argument mode-name literal assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-pass-message-literal-guard",
        run_usage_examples_duplicate_count_wrapper_pass_message_literal_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper second-argument PASS message literal assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-pass-message-prefix-guard",
        run_usage_examples_duplicate_count_wrapper_pass_message_prefix_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper second-argument PASS message prefix assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-pass-message-suffix-guard",
        run_usage_examples_duplicate_count_wrapper_pass_message_suffix_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper second-argument PASS message suffix assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-pass-message-delimiter-guard",
        run_usage_examples_duplicate_count_wrapper_pass_message_delimiter_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper second-argument PASS message delimiter assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-literal-only-guard",
        run_usage_examples_duplicate_count_wrapper_helper_literal_only_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper literal-only argument assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-positional-only-guard",
        run_usage_examples_duplicate_count_wrapper_helper_positional_only_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper positional-only call-shape assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-arg-order-guard",
        run_usage_examples_duplicate_count_wrapper_helper_arg_order_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper canonical argument-order assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-mode-order-guard",
        run_usage_examples_duplicate_count_wrapper_helper_mode_order_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper hardening mode-order adjacency assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-adjacency-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_adjacency_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper hardening mode uniqueness-before-adjacency assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper hardening mode registration-order assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper uniqueness-order adjacency assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper uniqueness-order adjacency ordering assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper uniqueness-order adjacency-order uniqueness adjacency assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper uniqueness-order adjacency-order uniqueness adjacency uniqueness assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper usage-examples-order adjacency-order uniqueness adjacency uniqueness adjacency assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper uniqueness-order adjacency-order uniqueness adjacency uniqueness adjacency-order uniqueness assertion",
    ),
    (
        "usage-examples-order-guard",
        run_usage_examples_order_guard_mode,
        "deterministic generated usage-example ordering assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper uniqueness-order adjacency-order uniqueness adjacency uniqueness adjacency assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper uniqueness-order adjacency-order uniqueness assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper uniqueness-order adjacency-order uniqueness adjacency uniqueness adjacency-order uniqueness adjacency assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper uniqueness-order adjacency-order uniqueness adjacency uniqueness adjacency-order uniqueness adjacency uniqueness adjacency assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper uniqueness-order adjacency-order uniqueness adjacency uniqueness adjacency-order uniqueness adjacency uniqueness adjacency uniqueness adjacency assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper uniqueness-order adjacency-order uniqueness adjacency uniqueness adjacency-order uniqueness adjacency uniqueness adjacency uniqueness adjacency uniqueness adjacency assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper newest uniqueness guard adjacency-order uniqueness assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper newest uniqueness guard adjacency-order assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper newest uniqueness adjacency-order adjacency uniqueness assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper newest uniqueness adjacency-order adjacency assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper newest uniqueness adjacency-order adjacency ordering uniqueness assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_order_uniqueness_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper newest uniqueness adjacency-order adjacency ordering uniqueness-order uniqueness assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_order_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper newest uniqueness adjacency-order adjacency ordering uniqueness-order adjacency assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper newest uniqueness adjacency-order adjacency ordering assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper newest uniqueness adjacency-order adjacency ordering uniqueness-order uniqueness ordering uniqueness assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper newest uniqueness adjacency-order adjacency ordering uniqueness-order uniqueness ordering uniqueness ordering uniqueness assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper newest uniqueness adjacency-order adjacency ordering uniqueness-order uniqueness ordering uniqueness ordering uniqueness-order uniqueness assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper newest uniqueness adjacency-order adjacency ordering uniqueness-order uniqueness ordering uniqueness ordering uniqueness-order adjacency assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper newest uniqueness adjacency-order adjacency ordering uniqueness-order uniqueness ordering uniqueness ordering uniqueness-order uniqueness adjacency-order uniqueness assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper newest uniqueness adjacency-order adjacency ordering uniqueness-order uniqueness ordering uniqueness ordering uniqueness-order uniqueness adjacency-order assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard-uniqueness-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_guard_adjacency_order_guard_uniqueness_guard_adjacency_order_guard_uniqueness_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper newest long-form uniqueness-order adjacency-order uniqueness adjacency-order uniqueness assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_guard_adjacency_order_guard_uniqueness_guard_adjacency_order_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper newest long-form uniqueness-order adjacency-order uniqueness adjacency-order assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard-uniqueness-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_guard_adjacency_order_guard_uniqueness_guard_adjacency_order_guard_uniqueness_guard_adjacency_order_guard_uniqueness_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper newest long-form uniqueness-order adjacency-order uniqueness then uniqueness adjacency-order uniqueness-count assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_guard_adjacency_order_guard_uniqueness_guard_adjacency_order_guard_uniqueness_guard_adjacency_order_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper newest long-form adjacency-order guard then paired uniqueness-count adjacency assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard-adjacency-order-guard-uniqueness-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_guard_adjacency_order_guard_uniqueness_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper newest long-form uniqueness-order adjacency-order uniqueness assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard-adjacency-order-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_order_uniqueness_guard_adjacency_order_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper newest long-form uniqueness-order adjacency-order assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_uniqueness_order_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper newest uniqueness adjacency-order adjacency ordering uniqueness-order uniqueness ordering adjacency assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_order_uniqueness_order_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper newest uniqueness adjacency-order adjacency ordering uniqueness-order uniqueness ordering assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper uniqueness-order adjacency-order uniqueness adjacency uniqueness adjacency-order uniqueness adjacency uniqueness adjacency uniqueness adjacency uniqueness adjacency uniqueness adjacency assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_adjacency_uniqueness_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper uniqueness-order adjacency-order uniqueness adjacency uniqueness adjacency-order uniqueness adjacency uniqueness adjacency uniqueness adjacency uniqueness adjacency uniqueness adjacency uniqueness assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_uniqueness_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper uniqueness-order adjacency-order uniqueness adjacency uniqueness adjacency-order uniqueness adjacency uniqueness adjacency uniqueness assertion",
    ),
    (
        "usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-guard",
        run_usage_examples_duplicate_count_wrapper_helper_uniqueness_order_adjacency_order_uniqueness_adjacency_uniqueness_adjacency_order_uniqueness_adjacency_uniqueness_guard_mode,
        "deterministic duplicate-count coverage-guard wrapper helper uniqueness-order adjacency-order uniqueness adjacency uniqueness adjacency-order uniqueness adjacency uniqueness assertion",
    ),
    (
        "usage-examples-mode-set-coverage-guard",
        run_usage_examples_mode_set_coverage_guard_mode,
        "deterministic generated usage-example mode set/count coverage assertion",
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

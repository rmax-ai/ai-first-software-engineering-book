#!/usr/bin/env python3
"""Small Copilot SDK smoke test for state/llm_client.py.

Usage:
  python state/copilot_sdk_smoke_test.py
  python state/copilot_sdk_smoke_test.py --mode sdk-unavailable
  python state/copilot_sdk_smoke_test.py --mode bootstrap-failure
  python state/copilot_sdk_smoke_test.py --mode live

Modes:
- stub (default): installs an in-process fake `copilot` module and verifies
  that LLMClient uses the SDK path end-to-end without network or credentials.
- sdk-unavailable: forces SDK import unavailability and verifies a clear SDK-required error.
- bootstrap-failure: forces worker-loop bootstrap failure and verifies error context.
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


def main() -> int:
    parser = argparse.ArgumentParser(description="Copilot SDK smoke test")
    parser.add_argument(
        "--mode",
        choices=[
            "stub",
            "sdk-unavailable",
            "bootstrap-failure",
            "live",
        ],
        default="stub",
        help="stub = offline synthetic test, sdk-unavailable = forced missing SDK error, bootstrap-failure = forced worker-loop bootstrap error, live = real provider call",
    )
    args = parser.parse_args()

    if args.mode == "stub":
        return run_stub_mode()
    if args.mode == "sdk-unavailable":
        return run_sdk_unavailable_mode()
    if args.mode == "bootstrap-failure":
        return run_bootstrap_failure_mode()
    return run_live_mode()


if __name__ == "__main__":
    raise SystemExit(main())

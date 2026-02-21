#!/usr/bin/env python3
"""Copilot SDK smoke test using uv-managed dependencies.

Run:
  uv run python state/copilot_sdk_uv_smoke.py
  uv run python state/copilot_sdk_uv_smoke.py --mode prompt --model gpt-5
"""

from __future__ import annotations

import argparse
import asyncio
import importlib
from typing import Any


def _event_type_name(event_type: Any) -> str:
    value = getattr(event_type, "value", event_type)
    return str(value).strip().lower()


async def run_ping_mode() -> int:
    sdk = importlib.import_module("copilot")
    copilot_client_cls = getattr(sdk, "CopilotClient")
    client = copilot_client_cls()
    try:
        await client.start()
        response = await client.ping("health check")
    except Exception as exc:
        print(f"FAIL: ping failed: {exc}")
        return 1
    finally:
        try:
            await client.stop()
        except Exception:
            pass

    print("PASS: Copilot SDK ping succeeded")
    print(f"response={response}")
    return 0


async def run_prompt_mode(model: str, prompt: str, timeout_s: float) -> int:
    result: dict[str, Any] = {"content": None, "error": None}
    sdk = importlib.import_module("copilot")
    copilot_client_cls = getattr(sdk, "CopilotClient")
    client = copilot_client_cls()
    session: Any | None = None

    try:
        await client.start()
        session = await client.create_session({"model": model, "streaming": False})
        assert session is not None
        response = await session.send_and_wait({"prompt": prompt}, timeout=timeout_s)
        if response is None:
            print(f"FAIL: prompt mode timed out after {timeout_s:.1f}s")
            return 1
        response_type = _event_type_name(response.type)
        if response_type in {"session.error", "sessioneventtype.session_error"}:
            result["error"] = getattr(response.data, "message", "unknown session error")
        elif response_type in {"assistant.message", "sessioneventtype.assistant_message"}:
            result["content"] = getattr(response.data, "content", "")
        else:
            events = await session.get_messages()
            for event in reversed(events):
                event_type = _event_type_name(event.type)
                if event_type in {"assistant.message", "sessioneventtype.assistant_message"}:
                    result["content"] = getattr(event.data, "content", "")
                    break
                if event_type in {"session.error", "sessioneventtype.session_error"}:
                    result["error"] = getattr(event.data, "message", "unknown session error")
                    break
    except TimeoutError:
        print(f"FAIL: prompt mode timed out after {timeout_s:.1f}s")
        return 1
    except Exception as exc:
        print(f"FAIL: prompt mode failed: {exc}")
        return 1
    finally:
        if session is not None:
            try:
                await session.destroy()
            except Exception:
                pass
        try:
            await client.stop()
        except Exception:
            pass

    if result["error"]:
        print(f"FAIL: session.error: {result['error']}")
        return 1

    content = str(result["content"] or "").strip()
    if not content:
        print("FAIL: empty assistant response")
        return 1

    print("PASS: Copilot SDK prompt round-trip succeeded")
    print(f"content={content!r}")
    return 0


async def main_async(args: argparse.Namespace) -> int:
    if args.mode == "ping":
        return await run_ping_mode()
    return await run_prompt_mode(model=args.model, prompt=args.prompt, timeout_s=args.timeout)


def main() -> int:
    parser = argparse.ArgumentParser(description="Copilot SDK smoke test")
    parser.add_argument("--mode", choices=["ping", "prompt"], default="ping")
    parser.add_argument("--model", default="gpt-5")
    parser.add_argument("--prompt", default="Reply with exactly: ok")
    parser.add_argument("--timeout", type=float, default=45.0)
    args = parser.parse_args()
    return asyncio.run(main_async(args))


if __name__ == "__main__":
    raise SystemExit(main())

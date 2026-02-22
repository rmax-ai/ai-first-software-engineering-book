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
import json
from pathlib import Path
import subprocess
import sys
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
KERNEL_PATH = REPO_ROOT / "state" / "kernel.py"
METRICS_PATH = REPO_ROOT / "state" / "metrics.json"


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


async def run_trace_summary_mode(chapter_id: str, max_iterations: int, run_kernel: bool, metrics_path: Path) -> int:
    if run_kernel:
        kernel_cmd = [
            sys.executable,
            str(KERNEL_PATH),
            "--chapter-id",
            chapter_id,
            "--llm",
            "--llm-provider",
            "mock",
            "--max-iterations",
            str(max_iterations),
        ]
        proc = subprocess.run(kernel_cmd, cwd=REPO_ROOT, capture_output=True, text=True)
        if proc.returncode != 0:
            print("FAIL: kernel run failed for trace-summary smoke")
            if proc.stdout:
                print(proc.stdout.strip())
            if proc.stderr:
                print(proc.stderr.strip())
            return 1

    metrics = json.loads(metrics_path.read_text(encoding="utf-8"))
    chapter_metrics = metrics.get("chapters", {}).get(chapter_id, {})
    history = chapter_metrics.get("history", [])
    if not history:
        print(f"FAIL: no metrics history for chapter {chapter_id}")
        return 1

    latest = history[-1]
    trace_summary = latest.get("trace_summary")
    if not isinstance(trace_summary, dict):
        print("FAIL: latest metrics history entry missing trace_summary")
        return 1

    required_keys = {"decision", "drift_score", "diff_ratio", "deterministic_pass"}
    missing = sorted(required_keys - set(trace_summary))
    if missing:
        print(f"FAIL: trace_summary missing keys: {missing}")
        return 1

    print("PASS: trace_summary present with required keys")
    print(f"trace_summary={trace_summary}")
    return 0


async def main_async(args: argparse.Namespace) -> int:
    if args.mode == "ping":
        return await run_ping_mode()
    if args.mode == "prompt":
        return await run_prompt_mode(model=args.model, prompt=args.prompt, timeout_s=args.timeout)
    return await run_trace_summary_mode(
        chapter_id=args.chapter_id,
        max_iterations=args.kernel_max_iterations,
        run_kernel=args.run_kernel_for_trace_summary,
        metrics_path=Path(args.metrics_path),
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Copilot SDK smoke test")
    parser.add_argument("--mode", choices=["ping", "prompt", "trace-summary"], default="ping")
    parser.add_argument("--model", default="gpt-5")
    parser.add_argument("--prompt", default="Reply with exactly: ok")
    parser.add_argument("--timeout", type=float, default=45.0)
    parser.add_argument("--chapter-id", default="01-paradigm-shift")
    parser.add_argument("--kernel-max-iterations", type=int, default=1)
    parser.add_argument("--run-kernel-for-trace-summary", action="store_true")
    parser.add_argument("--metrics-path", default=str(METRICS_PATH))
    args = parser.parse_args()
    return asyncio.run(main_async(args))


if __name__ == "__main__":
    raise SystemExit(main())

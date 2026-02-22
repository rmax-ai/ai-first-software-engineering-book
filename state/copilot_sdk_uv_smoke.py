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
TRACE_SUMMARY_FIXTURE_ROOT = REPO_ROOT / "state" / ".smoke_fixtures" / "trace_summary"


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


def _build_trace_summary_fixture(chapter_id: str, fixture_root: Path) -> tuple[Path, Path]:
    fixture_repo_root = fixture_root / "repo"
    metrics_path = fixture_repo_root / "state" / "metrics.json"
    trace_path = fixture_repo_root / "state" / "role_io" / chapter_id / "iter_01" / "out" / "kernel_trace.jsonl"
    trace_path.parent.mkdir(parents=True, exist_ok=True)
    metrics_path.parent.mkdir(parents=True, exist_ok=True)

    metrics_payload = {
        "chapters": {
            chapter_id: {
                "history": [
                    {
                        "iteration": 1,
                        "trace_summary": {
                            "decision": "accept",
                            "drift_score": 0.0,
                            "diff_ratio": 0.0,
                            "deterministic_pass": True,
                        },
                    }
                ]
            }
        }
    }
    metrics_path.write_text(json.dumps(metrics_payload, indent=2), encoding="utf-8")

    phase_entries = [
        {"event": "phase_trace", "payload": {"phase": "role_output_ready", "status": "ok", "duration_ms": 1, "budget_signal": "within"}},
        {"event": "phase_trace", "payload": {"phase": "evaluation", "status": "ok", "duration_ms": 1, "budget_signal": "within"}},
        {"event": "phase_trace", "payload": {"phase": "state_persistence", "status": "ok", "duration_ms": 1, "budget_signal": "within"}},
    ]
    trace_path.write_text("\n".join(json.dumps(entry) for entry in phase_entries) + "\n", encoding="utf-8")
    return metrics_path, fixture_repo_root


async def run_trace_summary_mode(
    chapter_id: str,
    max_iterations: int,
    run_kernel: bool,
    metrics_path: Path,
    fixture_root: Path,
) -> int:
    repo_root_for_trace = REPO_ROOT
    metrics_path_for_trace = metrics_path
    if not run_kernel:
        metrics_path_for_trace, repo_root_for_trace = _build_trace_summary_fixture(chapter_id=chapter_id, fixture_root=fixture_root)

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

    metrics = json.loads(metrics_path_for_trace.read_text(encoding="utf-8"))
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

    iteration = latest.get("iteration")
    if not isinstance(iteration, int):
        print("FAIL: latest metrics history entry missing integer iteration")
        return 1
    trace_path = repo_root_for_trace / "state" / "role_io" / chapter_id / f"iter_{iteration:02d}" / "out" / "kernel_trace.jsonl"
    if not trace_path.exists():
        print(f"FAIL: kernel trace file missing at {trace_path}")
        return 1

    trace_entries = [json.loads(line) for line in trace_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    phase_entries = [entry for entry in trace_entries if entry.get("event") == "phase_trace"]
    if not phase_entries:
        print("FAIL: no phase_trace events in kernel trace")
        return 1

    required_phase_payload_keys = {"phase", "status", "duration_ms", "budget_signal"}
    for entry in phase_entries:
        payload = entry.get("payload")
        if not isinstance(payload, dict):
            print("FAIL: phase_trace payload is not an object")
            return 1
        phase_missing = sorted(required_phase_payload_keys - set(payload))
        if phase_missing:
            print(f"FAIL: phase_trace missing keys: {phase_missing}")
            return 1

    phase_names = {entry.get("payload", {}).get("phase") for entry in phase_entries}
    required_phases = {"role_output_ready", "evaluation", "state_persistence"}
    missing_phases = sorted(required_phases - phase_names)
    if missing_phases:
        print(f"FAIL: missing required phase traces: {missing_phases}")
        return 1

    print("PASS: trace_summary present with required keys")
    print(f"trace_summary={trace_summary}")
    print(f"phase_trace_events={len(phase_entries)}")
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
        fixture_root=Path(args.trace_summary_fixture_root),
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
    parser.add_argument("--trace-summary-fixture-root", default=str(TRACE_SUMMARY_FIXTURE_ROOT))
    args = parser.parse_args()
    return asyncio.run(main_async(args))


if __name__ == "__main__":
    raise SystemExit(main())

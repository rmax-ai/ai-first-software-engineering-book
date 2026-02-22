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
import shutil
import subprocess
import sys
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
KERNEL_PATH = REPO_ROOT / "state" / "kernel.py"
METRICS_PATH = REPO_ROOT / "state" / "metrics.json"
TRACE_SUMMARY_FIXTURE_ROOT = REPO_ROOT / "state" / ".smoke_fixtures" / "trace_summary"
TRACE_SUMMARY_MODE_SPECS: dict[str, dict[str, bool]] = {
    "trace-summary": {},
    "trace-summary-malformed-phase": {
        "expect_phase_trace_failure": True,
        "inject_malformed_phase_trace": True,
    },
    "trace-summary-malformed-phase-payload": {
        "expect_phase_trace_failure": True,
        "inject_non_object_phase_payload": True,
    },
    "trace-summary-missing-phase": {
        "expect_phase_trace_failure": True,
        "inject_missing_required_phase_trace": True,
    },
}


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


def _build_trace_summary_fixture(
    chapter_id: str,
    fixture_root: Path,
    malformed_phase_trace: bool = False,
    non_object_phase_payload: bool = False,
    omit_evaluation_phase_trace: bool = False,
) -> tuple[Path, Path]:
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
    if malformed_phase_trace:
        phase_entries[1]["payload"].pop("budget_signal", None)
    if non_object_phase_payload:
        phase_entries[1]["payload"] = "not-an-object"
    if omit_evaluation_phase_trace:
        phase_entries = [entry for entry in phase_entries if entry.get("payload", {}).get("phase") != "evaluation"]
    trace_path.write_text("\n".join(json.dumps(entry) for entry in phase_entries) + "\n", encoding="utf-8")
    return metrics_path, fixture_repo_root


def _build_trace_summary_kernel_fixture(chapter_id: str, fixture_root: Path) -> tuple[Path, Path]:
    fixture_repo_root = fixture_root / "kernel_repo"
    if fixture_repo_root.exists():
        shutil.rmtree(fixture_repo_root)
    fixture_repo_root.mkdir(parents=True, exist_ok=True)

    source_ledger = json.loads((REPO_ROOT / "state" / "ledger.json").read_text(encoding="utf-8"))
    source_chapter = source_ledger.get("chapters", {}).get(chapter_id)
    if not isinstance(source_chapter, dict):
        raise RuntimeError(f"Unknown chapter_id for fixture: {chapter_id}")
    chapter_meta = dict(source_chapter)
    chapter_meta["status"] = "draft"
    if chapter_meta.get("lifecycle") == "frozen":
        chapter_meta["lifecycle"] = "draft"
    chapter_path = chapter_meta.get("path")
    if not isinstance(chapter_path, str) or not chapter_path:
        raise RuntimeError(f"Invalid chapter path for fixture chapter: {chapter_id}")

    (fixture_repo_root / "state").mkdir(parents=True, exist_ok=True)
    shutil.copy2(REPO_ROOT / "state" / "kernel.py", fixture_repo_root / "state" / "kernel.py")
    shutil.copy2(REPO_ROOT / "state" / "llm_client.py", fixture_repo_root / "state" / "llm_client.py")
    shutil.copytree(REPO_ROOT / "evals", fixture_repo_root / "evals")
    shutil.copytree(REPO_ROOT / "prompts", fixture_repo_root / "prompts")
    shutil.copy2(REPO_ROOT / "AGENTS.md", fixture_repo_root / "AGENTS.md")
    shutil.copy2(REPO_ROOT / "CONSTITUTION.md", fixture_repo_root / "CONSTITUTION.md")
    shutil.copy2(REPO_ROOT / "ROADMAP.md", fixture_repo_root / "ROADMAP.md")
    chapter_file = fixture_repo_root / chapter_path
    chapter_file.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(REPO_ROOT / chapter_path, chapter_file)

    fixture_ledger = {"chapters": {chapter_id: chapter_meta}, "repo_iteration_log": []}
    (fixture_repo_root / "state" / "ledger.json").write_text(json.dumps(fixture_ledger, indent=2) + "\n", encoding="utf-8")
    (fixture_repo_root / "state" / "metrics.json").write_text(json.dumps({"chapters": {}}, indent=2) + "\n", encoding="utf-8")
    source_version_map = REPO_ROOT / "state" / "version_map.json"
    if source_version_map.exists():
        shutil.copy2(source_version_map, fixture_repo_root / "state" / "version_map.json")
    else:
        (fixture_repo_root / "state" / "version_map.json").write_text("{}\n", encoding="utf-8")

    subprocess.run(["git", "init"], cwd=fixture_repo_root, check=True, capture_output=True, text=True)
    subprocess.run(["git", "add", "."], cwd=fixture_repo_root, check=True, capture_output=True, text=True)
    subprocess.run(
        ["git", "-c", "user.name=trace-smoke", "-c", "user.email=trace-smoke@example.com", "commit", "-m", "fixture"],
        cwd=fixture_repo_root,
        check=True,
        capture_output=True,
        text=True,
    )
    return fixture_repo_root / "state" / "metrics.json", fixture_repo_root


async def run_trace_summary_mode(
    chapter_id: str,
    max_iterations: int,
    run_kernel: bool,
    metrics_path: Path,
    fixture_root: Path,
    expect_phase_trace_failure: bool = False,
    inject_malformed_phase_trace: bool = False,
    inject_non_object_phase_payload: bool = False,
    inject_missing_required_phase_trace: bool = False,
) -> int:
    repo_root_for_trace = REPO_ROOT
    metrics_path_for_trace = metrics_path
    fixture_cleanup_target: Path | None = None
    if run_kernel:
        metrics_path_for_trace, repo_root_for_trace = _build_trace_summary_kernel_fixture(
            chapter_id=chapter_id,
            fixture_root=fixture_root,
        )
        fixture_cleanup_target = repo_root_for_trace
    else:
        metrics_path_for_trace, repo_root_for_trace = _build_trace_summary_fixture(
            chapter_id=chapter_id,
            fixture_root=fixture_root,
            malformed_phase_trace=inject_malformed_phase_trace,
            non_object_phase_payload=inject_non_object_phase_payload,
            omit_evaluation_phase_trace=inject_missing_required_phase_trace,
        )

    try:
        if run_kernel:
            fixture_kernel_path = repo_root_for_trace / "state" / "kernel.py"
            kernel_cmd = [
                sys.executable,
                str(fixture_kernel_path),
                "--chapter-id",
                chapter_id,
                "--llm",
                "--llm-provider",
                "mock",
                "--max-iterations",
                str(max_iterations),
            ]
            proc = subprocess.run(kernel_cmd, cwd=repo_root_for_trace, capture_output=True, text=True)
            if proc.returncode not in {0, 1}:
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
        if run_kernel and phase_entries:
            if inject_malformed_phase_trace:
                payload = phase_entries[0].get("payload")
                if isinstance(payload, dict):
                    payload.pop("budget_signal", None)
            if inject_non_object_phase_payload:
                phase_entries[0]["payload"] = "not-an-object"
            if inject_missing_required_phase_trace:
                phase_entries = [entry for entry in phase_entries if entry.get("payload", {}).get("phase") != "evaluation"]
        if not phase_entries:
            observed_phase_trace_failure = "no phase_trace events in kernel trace"
        else:
            observed_phase_trace_failure = ""

        required_phase_payload_keys = {"phase", "status", "duration_ms", "budget_signal"}
        if not observed_phase_trace_failure:
            for entry in phase_entries:
                payload = entry.get("payload")
                if not isinstance(payload, dict):
                    observed_phase_trace_failure = "phase_trace payload is not an object"
                    break
                phase_missing = sorted(required_phase_payload_keys - set(payload))
                if phase_missing:
                    observed_phase_trace_failure = f"phase_trace missing keys: {phase_missing}"
                    break

        if not observed_phase_trace_failure:
            phase_names = {entry.get("payload", {}).get("phase") for entry in phase_entries}
            required_phases = {"role_output_ready", "evaluation", "state_persistence"}
            missing_phases = sorted(required_phases - phase_names)
            if missing_phases:
                observed_phase_trace_failure = f"missing required phase traces: {missing_phases}"

        if expect_phase_trace_failure:
            if observed_phase_trace_failure:
                print(f"PASS: expected phase_trace validation failure observed: {observed_phase_trace_failure}")
                return 0
            print("FAIL: expected malformed phase_trace validation failure, but validation passed")
            return 1

        if observed_phase_trace_failure:
            print(f"FAIL: {observed_phase_trace_failure}")
            return 1

        print("PASS: trace_summary present with required keys")
        print(f"trace_summary={trace_summary}")
        print(f"phase_trace_events={len(phase_entries)}")
        return 0
    finally:
        if fixture_cleanup_target is not None and fixture_cleanup_target.exists():
            shutil.rmtree(fixture_cleanup_target)


async def main_async(args: argparse.Namespace) -> int:
    if args.mode == "ping":
        return await run_ping_mode()
    if args.mode == "prompt":
        return await run_prompt_mode(model=args.model, prompt=args.prompt, timeout_s=args.timeout)
    mode_spec = TRACE_SUMMARY_MODE_SPECS.get(args.mode)
    if mode_spec is None:
        return await run_trace_summary_mode(
            chapter_id=args.chapter_id,
            max_iterations=args.kernel_max_iterations,
            run_kernel=args.run_kernel_for_trace_summary,
            metrics_path=Path(args.metrics_path),
            fixture_root=Path(args.trace_summary_fixture_root),
        )
    return await run_trace_summary_mode(
        chapter_id=args.chapter_id,
        max_iterations=args.kernel_max_iterations,
        run_kernel=args.run_kernel_for_trace_summary,
        metrics_path=Path(args.metrics_path),
        fixture_root=Path(args.trace_summary_fixture_root),
        **mode_spec,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Copilot SDK smoke test")
    parser.add_argument(
        "--mode",
        choices=[
            "ping",
            "prompt",
            *TRACE_SUMMARY_MODE_SPECS,
        ],
        default="ping",
    )
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

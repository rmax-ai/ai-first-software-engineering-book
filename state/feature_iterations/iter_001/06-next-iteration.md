# Recommended next task

## Task
Add deterministic kernel trace instrumentation scaffolding in `state/kernel.py`.

## Why this is next
- The plan identifies kernel observability as the highest-impact feature for debugging and eval transparency.
- It enables immediate follow-on work for smoke and eval assertions in later iterations.

## Acceptance criteria
- `state/kernel.py` emits structured trace events for key loop phases (plan, change, evaluate, decision) without changing existing public CLI behavior.
- Trace output is deterministic and can be disabled/enabled through a clearly documented control.
- Targeted verification demonstrates traces are produced for a sample run and remain stable across repeated runs.

## Expected files to touch
- `state/kernel.py`
- `state/metrics.json` (only if metric wiring is required)
- `state/copilot_sdk_uv_smoke.py` (if a deterministic smoke assertion is added)

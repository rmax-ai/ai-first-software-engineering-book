# Recommended next iteration task

## Task
Implement deterministic trace-summary enrichment in `state/kernel.py` and add smoke coverage in `state/copilot_sdk_uv_smoke.py`.

## Why this is next
- Trace observability provides immediate debugging value and enables clearer validation evidence for all later harness improvements.
- It is a focused slice touching the kernel and smoke test surface without requiring broad prompt-template migration first.

## Acceptance criteria
1. `state/kernel.py` emits a stable, machine-readable trace summary block for each run (including chapter id, step outcomes, and eval gate results).
2. `state/copilot_sdk_uv_smoke.py` includes at least one deterministic mode asserting the new trace summary shape.
3. `uv run python state/copilot_sdk_uv_smoke.py --mode <new-mode>` passes.
4. Iteration artifacts record command output and pass/fail status.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/01-task.md`
- `state/feature_iterations/iter_002/02-plan.md`
- `state/feature_iterations/iter_002/03-execution.md`
- `state/feature_iterations/iter_002/04-validation.md`
- `state/feature_iterations/iter_002/05-risks-and-decisions.md`
- `state/feature_iterations/iter_002/06-next-iteration.md`
- `state/feature_iterations/iter_002/07-summary.md`

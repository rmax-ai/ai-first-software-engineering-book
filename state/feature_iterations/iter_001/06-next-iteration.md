# Recommended next iteration task

## Task
Implement deterministic trace-summary instrumentation in `state/kernel.py` and validate it via targeted smoke coverage.

## Why this is next
Trace observability is foundational for evaluating subsequent role-IO and eval-guard improvements; adding it first reduces debugging ambiguity in later iterations.

## Acceptance criteria
- `state/kernel.py` emits a stable trace-summary structure for each run, including chapter ID, stage statuses, and latest evaluation outcome.
- `state/copilot_sdk_uv_smoke.py` includes at least one deterministic mode asserting trace-summary shape and required fields.
- Validation includes `uv run python state/copilot_sdk_uv_smoke.py --mode <new-mode>` with documented pass/fail evidence.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/` artifacts

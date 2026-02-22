# Task

## Selected task title
Add deterministic kernel fixture-root cleanup coverage for trace-summary smoke modes.

## Why this task now
`iter_066/06-next-iteration.md` prioritized parity between kernel and non-kernel trace-summary cleanup behavior to avoid fixture-root leakage regressions.

## Acceptance criteria for this iteration
1. Add one mode in `state/copilot_sdk_smoke_test.py` that runs kernel trace-summary variants and asserts fixture-root cleanup after each run.
2. Preserve existing kernel trace-summary success/failure assertions.
3. Record validation evidence in `state/feature_iterations/iter_067/04-validation.md`.

# Task

Add deterministic non-kernel trace-summary fixture-root cleanup coverage in `state/copilot_sdk_smoke_test.py`.

## Why this task now
`iter_065` already validates cleanup of the per-run `repo` fixture path, but does not assert the trace-summary fixture root itself remains directory-clean across non-kernel runs.

## Acceptance criteria
1. Add exactly one new deterministic smoke mode that executes non-kernel trace-summary variants and asserts no residual directories remain under `state/.smoke_fixtures/trace_summary/` after each invocation.
2. Preserve existing non-kernel trace-summary success/failure expectations.
3. Record targeted validation evidence for the new mode in this iteration.

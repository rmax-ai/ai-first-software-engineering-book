# Add deterministic non-kernel fixture cleanup guard

## Why this task now
`iter_064/06-next-iteration.md` prioritized closing the remaining trace-summary fixture-leak surface by asserting cleanup for non-kernel fixture-backed modes.

## Acceptance criteria
1. Update `state/copilot_sdk_uv_smoke.py` so non-kernel trace-summary runs also clean up `state/.smoke_fixtures/trace_summary/repo` after execution.
2. Add one deterministic mode in `state/copilot_sdk_smoke_test.py` that runs all non-kernel trace-summary variants and asserts fixture cleanup while preserving current success/failure expectations.
3. Register the new mode in shared mode specs so argparse choices and generated usage/docs remain synchronized.
4. Record verification evidence in `state/feature_iterations/iter_065/04-validation.md`.

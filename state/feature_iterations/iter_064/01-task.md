# Add deterministic kernel fixture cleanup guard

## Why this task now
`iter_063/06-next-iteration.md` prioritized deterministic cleanup coverage to ensure kernel-backed trace-summary smoke runs do not leak fixture state under `state/.smoke_fixtures/trace_summary/`.

## Acceptance criteria
1. Add one deterministic smoke mode in `state/copilot_sdk_smoke_test.py` that runs all kernel-backed trace-summary variants and asserts fixture cleanup after each run.
2. Keep repository safety checks by asserting `state/ledger.json` remains unchanged for each kernel-backed run.
3. Ensure kernel-backed fixture repos are cleaned up by the uv smoke runner so cleanup assertions are meaningful.
4. Record verification command output in `state/feature_iterations/iter_064/04-validation.md`.

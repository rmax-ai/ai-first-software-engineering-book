# Add deterministic kernel trace-summary smoke modes

## Why this task now
`iter_062/06-next-iteration.md` called for deterministic coverage in `state/copilot_sdk_smoke_test.py` for fixture-backed `--run-kernel-for-trace-summary` behavior.

## Acceptance criteria
1. Add deterministic smoke-test modes that execute all four fixture-backed kernel trace-summary variants.
2. Assert expected outcomes for normal and malformed phase-trace variants.
3. Assert repository ledger immutability (`state/ledger.json` unchanged) after each kernel-backed smoke run.
4. Record verification command outputs in `state/feature_iterations/iter_063/04-validation.md`.

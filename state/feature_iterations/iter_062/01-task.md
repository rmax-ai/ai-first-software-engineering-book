# Add fixture-backed eligible kernel-run trace-summary smoke support

## Why this task now
`iter_061/06-next-iteration.md` identified a deterministic blocker: kernel-run trace-summary smoke commands failed before trace validation because the default chapter status is `hold`.

## Acceptance criteria
1. Extend `state/copilot_sdk_uv_smoke.py` with a fixture-backed kernel-run path that guarantees an eligible chapter without mutating repository ledger state.
2. Re-run all four `--run-kernel-for-trace-summary` modes and achieve expected outcomes (normal mode passes; malformed modes fail with phase-trace validation messages).
3. Record command outputs and outcomes in `state/feature_iterations/iter_062/04-validation.md`.

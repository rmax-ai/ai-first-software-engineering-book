# Next iteration

## Recommended next task
Add deterministic eligible-ledger support for `--run-kernel-for-trace-summary` smoke validation.

## Why it is next
Current kernel-run smoke coverage is blocked by chapter eligibility state (`status='hold'`), preventing validation of trace-summary integration behavior.

## Concrete acceptance criteria
1. Extend `state/copilot_sdk_uv_smoke.py` with a fixture-backed kernel-run path that guarantees an eligible chapter without mutating repository ledger state.
2. Re-run all four `--run-kernel-for-trace-summary` trace-summary modes and achieve expected outcomes (normal mode passes, malformed modes fail with phase-trace validation messages).
3. Record command outputs and outcomes in `iter_062/04-validation.md`.

## Expected files to touch
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_062/*.md`

# Next iteration

## Recommended next task
Add deterministic smoke coverage for `--run-kernel-for-trace-summary` across all trace-summary modes.

## Why it is next
Current validation only exercised fixture-backed paths; kernel-run mode should be verified to prevent integration drift.

## Concrete acceptance criteria
1. Execute `--run-kernel-for-trace-summary` with `trace-summary`, `trace-summary-malformed-phase`, `trace-summary-malformed-phase-payload`, and `trace-summary-missing-phase`.
2. Record pass/fail results for each command in `iter_061/04-validation.md`.
3. Keep changes scoped to smoke verification and iteration artifacts unless an integration bug is found.

## Expected files to touch
- `state/feature_iterations/iter_061/*.md`
- `state/copilot_sdk_uv_smoke.py` (only if an integration bug requires a fix)

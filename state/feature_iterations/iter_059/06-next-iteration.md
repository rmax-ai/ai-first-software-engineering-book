# Next iteration

## Recommended next task
Table-drive trace-summary smoke mode specs to centralize argparse choices and dispatch logic.

## Why it is next
Adding new trace modes is now repetitive; a shared mode spec map will reduce branching drift while preserving deterministic behavior.

## Concrete acceptance criteria
1. Introduce a mode-spec structure covering `trace-summary`, `trace-summary-malformed-phase`, `trace-summary-malformed-phase-payload`, and `trace-summary-missing-phase`.
2. Use the same structure for both argparse `--mode` choices and runtime dispatch.
3. Re-run all trace-summary smoke modes and record outcomes in `iter_060/04-validation.md`.

## Expected files to touch
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_060/*.md`

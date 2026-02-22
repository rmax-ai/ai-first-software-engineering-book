# Next iteration

## Recommended next task
Add deterministic smoke coverage for malformed `phase_trace` payloads in `state/copilot_sdk_uv_smoke.py`.

## Why it is next
The current fixture validates only happy-path phase payloads; adding malformed payload checks will lock in stronger regression protection for observability schema drift.

## Concrete acceptance criteria
1. Add at least one deterministic mode/path that feeds malformed `phase_trace` entries and asserts the expected failure.
2. Keep existing trace-summary success mode green.
3. Record command outputs for both success and failure-path validations in `iter_057/04-validation.md`.

## Expected files to touch
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_057/*.md`

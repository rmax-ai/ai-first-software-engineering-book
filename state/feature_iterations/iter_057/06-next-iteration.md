# Next iteration

## Recommended next task
Add deterministic smoke coverage for non-object `phase_trace.payload` validation failures in `state/copilot_sdk_uv_smoke.py`.

## Why it is next
The new malformed mode guards missing keys, but schema drift can also present as non-object payloads; explicit coverage will harden the same observability contract.

## Concrete acceptance criteria
1. Add a deterministic path that injects a non-dict `phase_trace.payload` and asserts the expected failure signal.
2. Keep `--mode trace-summary` and `--mode trace-summary-malformed-phase` green.
3. Capture command evidence for all exercised modes in `iter_058/04-validation.md`.

## Expected files to touch
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_058/*.md`

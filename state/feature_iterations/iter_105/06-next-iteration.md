# Next iteration

## Recommended next task
Add a smoke guard mode that enforces `usage-examples-duplicate-count-wrapper-helper-uniqueness-adjacency-guard` is registered immediately after `usage-examples-duplicate-count-wrapper-helper-mode-order-guard` in `TRACE_SUMMARY_MODE_SPECS`.

## Why it is next
The new uniqueness-adjacency guard is now present; locking its placement after the prior mode-order guard prevents registration drift that can weaken deterministic hardening progression.

## Concrete acceptance criteria
1. Add one smoke mode in `state/copilot_sdk_smoke_test.py` asserting `usage-examples-duplicate-count-wrapper-helper-mode-order-guard` appears immediately before `usage-examples-duplicate-count-wrapper-helper-uniqueness-adjacency-guard` in `TRACE_SUMMARY_MODE_SPECS`.
2. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-guard` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_106/*.md`

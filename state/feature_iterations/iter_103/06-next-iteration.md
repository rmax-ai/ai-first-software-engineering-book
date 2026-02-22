# Next iteration

## Recommended next task
Add a guard mode that enforces `TRACE_SUMMARY_MODE_SPECS` keeps duplicate-count wrapper helper hardening modes in deterministic adjacency order (positional-only immediately followed by arg-order).

## Why it is next
Now that arg-order guard exists, ordering lock-in is the smallest follow-up to prevent accidental mode registration drift across contiguous hardening checks.

## Concrete acceptance criteria
1. Add one smoke mode in `state/copilot_sdk_smoke_test.py` asserting `usage-examples-duplicate-count-wrapper-helper-positional-only-guard` appears immediately before `usage-examples-duplicate-count-wrapper-helper-arg-order-guard` in `TRACE_SUMMARY_MODE_SPECS`.
2. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-mode-order-guard` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_104/*.md`

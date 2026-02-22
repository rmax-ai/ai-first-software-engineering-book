# Next iteration

## Recommended next task
Add a guard mode that ensures duplicate-count coverage-guard wrapper helper call-shape keeps argument order canonical (mode-name first, PASS message second).

## Why it is next
After enforcing positional-only semantics, argument-order locking is the next adjacent deterministic regression guard for wrapper delegation.

## Concrete acceptance criteria
1. Add one smoke mode in `state/copilot_sdk_smoke_test.py` that parses wrapper helper calls and asserts arg[0] equals registered mode name and arg[1] starts with canonical PASS prefix.
2. Register the mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-arg-order-guard` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_103/*.md`

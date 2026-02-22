# Next iteration

## Recommended next task
Add a guard mode that enforces duplicate-count coverage-guard wrapper PASS messages use the canonical suffix `duplicate-count ... mode coverage` expected for those wrappers.

## Why it is next
Prefix enforcement now protects the beginning of PASS literals; suffix drift can still silently alter deterministic phrasing used in smoke evidence and downstream log comparisons.

## Concrete acceptance criteria
1. Add one smoke mode in `state/copilot_sdk_smoke_test.py` that parses duplicate-count coverage-guard wrappers and asserts the second helper argument ends with canonical duplicate-count coverage wording.
2. Register the mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-pass-message-suffix-guard` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_099/*.md`

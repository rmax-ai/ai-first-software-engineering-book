# Next iteration

## Recommended next task
Add a guard mode that enforces duplicate-count coverage-guard wrapper PASS messages contain exactly one `mode validates` delimiter.

## Why it is next
Prefix and suffix guards now cover both ends of the PASS message; delimiter multiplicity can still drift and reduce parsing determinism.

## Concrete acceptance criteria
1. Add one smoke mode in `state/copilot_sdk_smoke_test.py` that parses duplicate-count coverage-guard wrappers and asserts each wrapper helper PASS message includes exactly one `mode validates` delimiter.
2. Register the mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-pass-message-delimiter-guard` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_100/*.md`

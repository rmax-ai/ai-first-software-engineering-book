# Next iteration

## Recommended next task
Add a guard mode that verifies duplicate-count coverage-guard wrappers use canonical literal values by checking the first helper argument matches the wrapper's registered mode name.

## Why it is next
Signature shape is now guarded; literal payload consistency is the next deterministic wrapper integrity check.

## Concrete acceptance criteria
1. Add one smoke mode in `state/copilot_sdk_smoke_test.py` that checks each duplicate-count coverage-guard wrapper passes its own registered mode name as the first helper argument.
2. Register the mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and record PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_096/*.md`

# Next iteration

## Recommended next task
Add a guard mode that verifies duplicate-count coverage-guard wrappers delegate with the canonical two-argument helper signature payload shape.

## Why it is next
Single-call enforcement now exists; validating argument-shape consistency closes the next likely regression vector.

## Concrete acceptance criteria
1. Add one smoke mode in `state/copilot_sdk_smoke_test.py` that checks each duplicate-count coverage-guard wrapper delegates with exactly two string arguments.
2. Register the mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and record PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_095/*.md`

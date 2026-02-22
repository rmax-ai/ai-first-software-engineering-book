# Next iteration

## Recommended next task
Add an adjacency-order smoke guard mode ensuring the new `...uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-guard` mode appears immediately before the prior `...uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-guard` mode.

## Why it is next
After uniqueness hardening, the smallest follow-up is adjacency-order hardening between the two latest uniqueness guard registrations.

## Concrete acceptance criteria
1. Add one smoke mode function in `state/copilot_sdk_smoke_test.py` asserting the newest uniqueness guard mode appears immediately before the previous uniqueness guard mode in `TRACE_SUMMARY_MODE_SPECS`.
2. Register that new adjacency-order mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic wording.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_124/*.md`

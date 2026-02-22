# Next Iteration

## Recommended next task
Refactor `usage-examples-duplicates-guard` to share the expected non-`stub` mode helper and tighten duplicate diagnostics.

## Why it is next
One related usage-example guard still computes expectations independently; aligning it with the shared helper completes this consolidation.

## Concrete acceptance criteria
1. Update `run_usage_examples_duplicates_guard_mode` to reuse `_expected_non_stub_mode_names(...)` alongside generated mode extraction.
2. Keep duplicate assertions deterministic and explicit about offending mode names.
3. Validate with:
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicates-guard`
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-coverage-guard`

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_027/*.md`

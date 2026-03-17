# Next iteration

## Recommended next task
Add adjacency-order smoke coverage ensuring the new short alias mode appears immediately after the existing `usage-examples-duplicate-count-wrapper-helper-newest-long-form-adjacency-order-guard-exact-once-adjacency-order-guard` mode.

## Why it is next
- The new alias now makes the exact-once assertion easy to run; the next smallest guard is to lock its placement relative to the existing alias mode.

## Concrete acceptance criteria
1. Add one smoke runner that asserts the previously added alias mode `usage-examples-duplicate-count-wrapper-helper-newest-long-form-adjacency-order-guard-exact-once-adjacency-order-guard` appears immediately before the alias mode added in `iter_149`, `usage-examples-duplicate-count-wrapper-helper-newest-long-form-adjacency-order-guard-exact-once-adjacency-order-guard-exact-once`.
2. Register one new `TRACE_SUMMARY_MODE_SPECS` mode for that adjacency assertion.
3. Run `python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_150/*.md`

# Next iteration

## Recommended next task
Add adjacency-order smoke coverage ensuring the newly added exact-once mode is positioned immediately after its paired uniqueness-guard predecessor mode.

## Why it is next
The exact-once guard now prevents duplicates; adjacency-order coverage is the next smallest guard to lock mode sequencing deterministically.

## Concrete acceptance criteria
1. Add one smoke runner in `state/copilot_sdk_smoke_test.py` asserting the new exact-once mode appears immediately after its paired predecessor mode.
2. Register one new `TRACE_SUMMARY_MODE_SPECS` entry for that adjacency assertion.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_148/*.md`

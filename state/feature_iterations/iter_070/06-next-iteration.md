# Next iteration

## Recommended next task
Add a deterministic guard mode that validates both parity cleanup mode names appear in argparse `--mode` choices in the same relative order as generated usage examples.

## Why it is next
This complements the new usage uniqueness guard by adding parser-level coverage for the same parity mode pair.

## Concrete acceptance criteria
1. Add one mode in `state/copilot_sdk_smoke_test.py` that asserts both parity cleanup mode names are present in parser choices and ordered consistently with usage examples.
2. Keep existing usage-example and parity execution modes unchanged.
3. Record validation evidence under `state/feature_iterations/iter_071/04-validation.md`.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_071/*.md`

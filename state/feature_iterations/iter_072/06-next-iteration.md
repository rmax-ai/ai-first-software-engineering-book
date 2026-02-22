# Next iteration

## Recommended next task
Add a deterministic guard mode that asserts parity cleanup mode names remain adjacent in argparse `--mode` choices and generated usage examples.

## Why it is next
Adjacency coverage complements presence/order/uniqueness guards and catches future insertions that could silently separate the parity mode pair.

## Concrete acceptance criteria
1. Add one mode in `state/copilot_sdk_smoke_test.py` that validates the two parity cleanup mode names are adjacent in argparse `--mode` choices.
2. Validate the same adjacency expectation against generated usage examples.
3. Record validation evidence under `state/feature_iterations/iter_073/04-validation.md`.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_073/*.md`

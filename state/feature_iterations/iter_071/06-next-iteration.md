# Next iteration

## Recommended next task
Add a deterministic guard mode that asserts the two parity cleanup mode names each appear exactly once in argparse `--mode` choices.

## Why it is next
This directly complements the new ordering guard by adding explicit parser-choice uniqueness coverage for the same parity mode pair.

## Concrete acceptance criteria
1. Add one mode in `state/copilot_sdk_smoke_test.py` that validates both parity cleanup mode names each occur exactly once in argparse `--mode` choices.
2. Keep existing parity execution handlers and usage-example guards unchanged.
3. Record validation evidence under `state/feature_iterations/iter_072/04-validation.md`.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_072/*.md`

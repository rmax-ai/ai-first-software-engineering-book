# Task

## Selected task title
Add a deterministic guard mode that asserts parity cleanup mode names are unique in argparse `--mode` choices.

## Why this task now
`state/feature_iterations/iter_071/06-next-iteration.md` prioritized parser-choice uniqueness coverage for the parity cleanup mode pair.

## Acceptance criteria for this iteration
1. Add one mode in `state/copilot_sdk_smoke_test.py` that validates both parity cleanup mode names each occur exactly once in argparse `--mode` choices.
2. Keep existing parity execution handlers and usage-example guards unchanged.
3. Record validation evidence under `state/feature_iterations/iter_072/04-validation.md`.

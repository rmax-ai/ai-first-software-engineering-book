# Task

## Selected task title
Add a deterministic guard mode that validates parity cleanup mode ordering across argparse `--mode` choices and generated usage examples.

## Why this task now
`state/feature_iterations/iter_070/06-next-iteration.md` prioritized parser-choice coverage for the same parity cleanup mode pair already guarded in usage examples.

## Acceptance criteria for this iteration
1. Add one mode in `state/copilot_sdk_smoke_test.py` that asserts both parity cleanup mode names appear in argparse `--mode` choices and preserve the same relative order as generated usage examples.
2. Keep existing usage-example and parity execution modes unchanged.
3. Record validation evidence under `state/feature_iterations/iter_071/04-validation.md`.

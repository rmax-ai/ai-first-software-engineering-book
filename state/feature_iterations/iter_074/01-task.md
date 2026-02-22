# Task

## Selected task title
Add a deterministic guard mode that enforces first-occurrence uniqueness before parity cleanup adjacency checks in argparse `--mode` choices and generated usage examples.

## Why this task now
The previous iteration added adjacency checks, but duplicate names could still hide ordering regressions; this closes that gap with one focused composite guard.

## Acceptance criteria
1. Add one new smoke mode in `state/copilot_sdk_smoke_test.py` that asserts parity cleanup mode names appear exactly once in argparse `--mode` choices before adjacency checks.
2. The same mode asserts parity cleanup mode names appear exactly once in generated usage examples before adjacency checks.
3. Record targeted validation evidence for the new mode in `state/feature_iterations/iter_074/04-validation.md`.

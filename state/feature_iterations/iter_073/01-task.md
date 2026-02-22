# Task

## Selected task title
Add a deterministic guard mode that enforces parity cleanup mode adjacency in argparse `--mode` choices and generated usage examples.

## Why this task now
The prior iteration already validated parity mode presence, order parity, and uniqueness; adjacency closes the remaining gap where future insertions could separate the parity pair without breaking existing guards.

## Acceptance criteria
1. Add one new smoke mode in `state/copilot_sdk_smoke_test.py` that asserts the parity cleanup mode names are adjacent in argparse `--mode` choices.
2. The same mode also asserts adjacency in generated usage examples.
3. Record targeted validation evidence for the new mode in `state/feature_iterations/iter_073/04-validation.md`.

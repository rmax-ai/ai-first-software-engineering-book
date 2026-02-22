# Task

## Selected task title
Add a deterministic usage-examples parity guard for trace-summary cleanup parity modes.

## Why this task now
`state/feature_iterations/iter_069/06-next-iteration.md` prioritized ensuring generated usage examples list both parity cleanup mode names exactly once.

## Acceptance criteria for this iteration
1. Add one mode in `state/copilot_sdk_smoke_test.py` that asserts both parity mode names each appear exactly once in generated usage examples.
2. Keep existing parity execution modes unchanged.
3. Record validation evidence in `state/feature_iterations/iter_070/04-validation.md`.

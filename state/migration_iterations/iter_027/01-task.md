# Task

## Selected task title
Remove obsolete HTTP fallback helper code and fallback smoke helper coverage after SDK-only routing.

## Why this task now
`iter_026/06-next-iteration.md` explicitly prioritized this cleanup to align tests and implementation with the SDK-only architecture.

## Acceptance criteria
- Unused HTTP fallback helper path in `state/llm_client.py` is removed.
- Unreachable fallback smoke helper functions are removed from `state/copilot_sdk_smoke_test.py`.
- `uv run python state/copilot_sdk_smoke_test.py --mode stub` and `--mode sdk-unavailable` pass.

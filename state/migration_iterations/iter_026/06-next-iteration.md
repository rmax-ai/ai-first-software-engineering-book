# Next Iteration

## Recommended next task
Remove obsolete HTTP fallback helper code and fallback smoke modes that are no longer used after SDK-only routing.

## Why it is next
This iteration switched runtime behavior to SDK-only, leaving dead fallback code that should now be deleted to reduce maintenance risk.

## Acceptance criteria
- Unused fallback helper path in `state/llm_client.py` is removed if no callers remain.
- Unreachable fallback smoke helper functions/mode documentation are removed from `state/copilot_sdk_smoke_test.py`.
- `uv run python state/copilot_sdk_smoke_test.py --mode stub` and `--mode sdk-unavailable` still pass.

## Expected files to touch
- `state/llm_client.py`
- `state/copilot_sdk_smoke_test.py`

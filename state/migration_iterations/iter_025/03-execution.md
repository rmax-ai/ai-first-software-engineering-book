# Execution

## Commands/tools run
- `view state/copilot_sdk_smoke_test.py` (inspect existing smoke modes and dispatch).
- `apply_patch state/copilot_sdk_smoke_test.py` (add new fallback non-object mode and wiring).
- `uv run python state/copilot_sdk_smoke_test.py --mode stub`
- `uv run python state/copilot_sdk_smoke_test.py --mode fallback-non-object`

## Files changed
- `state/copilot_sdk_smoke_test.py`

## Rationale per change
- Added one deterministic mode to cover the remaining untested HTTP fallback mapping branch for non-object JSON payloads.
- Kept changes scoped to smoke coverage and CLI mode plumbing only.

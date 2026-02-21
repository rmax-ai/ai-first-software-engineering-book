# Execution

## Commands/tools run
- Edited: `state/copilot_sdk_smoke_test.py`
- Ran deterministic smoke matrix:
  - `for mode in stub sdk-unavailable bootstrap-failure shutdown-failure stop-unavailable destroy-unavailable destroy-failure force-stop-unavailable force-stop-close-idempotency stop-close-idempotency close-idempotency destroy-close-idempotency destroy-unavailable-close-idempotency; do uv run python state/copilot_sdk_smoke_test.py --mode "$mode"; done`

## Files changed
- `state/copilot_sdk_smoke_test.py`

## Rationale per change
- Added `destroy-unavailable-close-idempotency` mode to exercise the non-callable `session.destroy` branch across two consecutive `close()` calls.
- Added CLI surface wiring (usage docstring, mode choices, help text, dispatch) so the mode is discoverable and runnable.

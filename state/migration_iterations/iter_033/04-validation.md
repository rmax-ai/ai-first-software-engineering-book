# Validation

## Verification commands
- `uv run python state/copilot_sdk_smoke_test.py --mode stub`
- `uv run python state/copilot_sdk_smoke_test.py --mode sdk-unavailable`
- `uv run python state/copilot_sdk_smoke_test.py --mode bootstrap-failure`
- `uv run python state/copilot_sdk_smoke_test.py --mode shutdown-failure`
- `uv run python state/copilot_sdk_smoke_test.py --mode stop-unavailable`
- `uv run python state/copilot_sdk_smoke_test.py --mode destroy-failure`

## Observed results
- `PASS: stub Copilot SDK path works`
- `PASS: copilot provider requires SDK when module is unavailable`
- `PASS: bootstrap failure mode validates worker-loop bootstrap error context`
- `PASS: shutdown failure mode validates stop()/force_stop() error context`
- `PASS: stop unavailable mode validates stop() unavailable shutdown error context`
- `PASS: destroy failure mode validates session.destroy() error context`

## Acceptance criteria check
- Added deterministic `stop-unavailable` mode: **pass**.
- Shutdown message prefix assertion: **pass**.
- `stop() unavailable` detail assertion: **pass**.
- Existing required deterministic modes still pass: **pass**.

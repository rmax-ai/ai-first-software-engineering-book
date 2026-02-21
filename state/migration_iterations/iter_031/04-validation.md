# Validation

## Verification commands run
- `uv run python state/copilot_sdk_smoke_test.py --mode stub`
- `uv run python state/copilot_sdk_smoke_test.py --mode sdk-unavailable`
- `uv run python state/copilot_sdk_smoke_test.py --mode bootstrap-failure`
- `uv run python state/copilot_sdk_smoke_test.py --mode shutdown-failure`

## Observed outputs/results
- `PASS: stub Copilot SDK path works`
- `PASS: copilot provider requires SDK when module is unavailable`
- `PASS: bootstrap failure mode validates worker-loop bootstrap error context`
- `PASS: shutdown failure mode validates stop()/force_stop() error context`

## Pass/fail against acceptance criteria
- Pass: new `shutdown-failure` mode exists in `state/copilot_sdk_smoke_test.py`.
- Pass: mode asserts `Copilot SDK shutdown failed:` context.
- Pass: mode asserts both `stop()` and `force_stop()` failure details.
- Pass: existing smoke modes still pass.

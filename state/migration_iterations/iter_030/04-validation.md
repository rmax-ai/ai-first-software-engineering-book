# Validation

## Verification commands run
`uv run python state/copilot_sdk_smoke_test.py --mode stub && uv run python state/copilot_sdk_smoke_test.py --mode sdk-unavailable && uv run python state/copilot_sdk_smoke_test.py --mode bootstrap-failure`

## Observed outputs/results
- `PASS: stub Copilot SDK path works`
- `PASS: copilot provider requires SDK when module is unavailable`
- `PASS: bootstrap failure mode validates worker-loop bootstrap error context`

## Pass/fail against acceptance criteria
- Added bootstrap-failure mode: **PASS**
- Asserts bootstrap error context: **PASS**
- Existing stub and sdk-unavailable still pass: **PASS**

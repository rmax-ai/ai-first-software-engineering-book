# Validation

## Verification commands run
- `python state/copilot_sdk_smoke_test.py --mode live`

## Observed outputs/results
- `FAIL: copilot package is not installed`

## Pass/fail against acceptance criteria
- FAIL: Live smoke could not start because runtime dependency `copilot` is unavailable in this environment.
- FAIL: Real-provider response and usage extraction behavior could not be observed.

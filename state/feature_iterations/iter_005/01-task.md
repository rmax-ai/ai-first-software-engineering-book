# Task: Add deterministic trace-summary regression coverage to smoke matrix

## Why this task now
`iter_004` recommended moving trace-summary checks into `state/copilot_sdk_smoke_test.py` with both success and missing-key detection paths.

## Acceptance criteria
1. Add a passing deterministic smoke mode that validates required `trace_summary` keys.
2. Add a deterministic missing-key smoke mode that proves required-key omissions are detected.
3. Keep existing smoke mode behavior unchanged.

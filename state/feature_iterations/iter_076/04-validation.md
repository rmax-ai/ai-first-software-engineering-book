# Validation

## Verification commands run
1. `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-fixture-cleanup-parity-mode-choices-usage-examples-adjacency-guard`
2. `uv run python state/copilot_sdk_smoke_test.py --mode mode-choices-coverage-guard`

## Observed outputs/results
1. `PASS: trace-summary-fixture-cleanup-parity-mode-choices-usage-examples-adjacency-guard mode validates parity mode adjacency in parser choices and usage examples`
2. `PASS: mode-choices-coverage-guard mode validates argparse --mode choices for all modes`

## Pass/fail against acceptance criteria
- AC1: **Pass** — helper added in `state/copilot_sdk_smoke_test.py`.
- AC2: **Pass** — parity cleanup guard modes now call helper.
- AC3: **Pass** — both required smoke commands executed and passed.

# Validation

## Verification commands run
- `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-non-kernel-fixture-cleanup`
- `uv run python state/copilot_sdk_smoke_test.py --mode mode-choices-coverage-guard`
- `uv run python state/copilot_sdk_smoke_test.py --mode docstring-mode-coverage-guard`

## Observed outputs/results
- `trace-summary-non-kernel-fixture-cleanup`: **PASS** — `PASS: trace-summary-non-kernel-fixture-cleanup mode validates fixture cleanup after non-kernel trace-summary runs`.
- `mode-choices-coverage-guard`: **PASS** — `PASS: mode-choices-coverage-guard mode validates argparse --mode choices for all modes`.
- `docstring-mode-coverage-guard`: **PASS** — `PASS: docstring-mode-coverage-guard mode validates module doc coverage for all modes`.

## Pass/fail against acceptance criteria
- AC1 (non-kernel cleanup in uv smoke runner): **PASS**
- AC2 (deterministic aggregate non-kernel cleanup mode with preserved expectations): **PASS**
- AC3 (mode spec registration and parser/doc sync): **PASS**
- AC4 (validation evidence recorded): **PASS**

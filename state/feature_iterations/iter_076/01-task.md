# Task

## Selected task title
Extract shared argparse `--mode` action lookup helper for parity cleanup guard modes.

## Why this task now
`iter_075` recommended removing duplicated parser action lookup boilerplate across parity cleanup guard modes to reduce drift risk.

## Acceptance criteria
1. Add one helper in `state/copilot_sdk_smoke_test.py` that returns argparse `--mode` action.
2. Update parity cleanup guard modes to use helper with no assertion behavior change.
3. Run:
   - `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-fixture-cleanup-parity-mode-choices-usage-examples-adjacency-guard`
   - `uv run python state/copilot_sdk_smoke_test.py --mode mode-choices-coverage-guard`

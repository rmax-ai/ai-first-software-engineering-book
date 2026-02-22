# Validation

## Verification commands
1. `uv run python state/copilot_sdk_smoke_test.py --mode mode-choices-coverage-guard`
2. `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-mode-coverage-guard`

## Observed results
- Command 1: PASS (`mode-choices-coverage-guard mode validates argparse --mode choices for all modes`)
- Command 2: PASS (`usage-examples-duplicate-count-mode-coverage-guard mode validates duplicate-count regression mode coverage`)

## Acceptance criteria check
1. Added deterministic guard asserting target mode appears in parser choices and generated usage lines: **PASS**
2. Registered guard mode in shared mode metadata: **PASS**
3. Required smoke commands executed and passing: **PASS**

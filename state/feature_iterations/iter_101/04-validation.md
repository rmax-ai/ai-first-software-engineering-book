# Validation

## Verification commands run
1. `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-literal-only-guard`

## Observed outputs/results
- `PASS: usage-examples-duplicate-count-wrapper-helper-literal-only-guard mode validates duplicate-count coverage-guard wrappers use literal-only helper arguments`

## Acceptance criteria check
- Criteria 1: **PASS** — new mode parses wrapper helper calls and fails on f-string or concatenation argument nodes.
- Criteria 2: **PASS** — mode is registered in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
- Criteria 3: **PASS** — targeted smoke command executed and returned PASS.

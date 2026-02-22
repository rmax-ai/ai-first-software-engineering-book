# Validation

## Verification commands run
1. `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-pass-message-literal-guard`
2. `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-mode-coverage-guard`

## Observed outputs/results
- Command 1: `PASS: usage-examples-duplicate-count-wrapper-pass-message-literal-guard mode validates duplicate-count coverage-guard wrappers use PASS message literals containing their registered mode name`
- Command 2: `PASS: usage-examples-duplicate-count-mode-coverage-guard mode validates duplicate-count regression mode coverage`

## Acceptance criteria check
- Criteria 1: **PASS** — new guard parses duplicate-count coverage-guard wrappers and validates second helper argument string literals include registered mode names.
- Criteria 2: **PASS** — mode registered in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
- Criteria 3: **PASS** — targeted smoke command executed and returned PASS.

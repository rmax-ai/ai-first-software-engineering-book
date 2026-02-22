# Validation

## Verification commands run
1. `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-mode-coverage-guard`
2. `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-mode-coverage-guard-coverage-guard`

## Observed outputs/results
- Command 1: `PASS: usage-examples-duplicate-count-mode-coverage-guard mode validates duplicate-count regression mode coverage`
- Command 2: `PASS: usage-examples-duplicate-count-mode-coverage-guard-coverage-guard mode validates duplicate-count mode-coverage guard mode coverage`

## Pass/fail against acceptance criteria
1. **Pass** — introduced `_assert_mode_in_parser_and_usage_examples(...)`.
2. **Pass** — both targeted wrappers now call the shared helper.
3. **Pass** — PASS output text remained unchanged and required smoke mode succeeded.

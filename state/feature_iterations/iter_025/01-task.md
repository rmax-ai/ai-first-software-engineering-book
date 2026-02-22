# Task: Share usage-example mode extraction helper

## Why this task now
`iter_024/06-next-iteration.md` identified duplicated non-`stub` usage-mode extraction logic across usage-example guard modes in `state/copilot_sdk_smoke_test.py`, creating drift risk.

## Acceptance criteria
- Add one private helper that extracts generated non-`stub` usage mode names.
- Update usage-example guard modes to use the shared helper without changing assertion intent.
- Validate with:
  - `uv run python state/copilot_sdk_smoke_test.py --mode stub`
  - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-order-guard`
  - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-mode-set-coverage-guard`

# Task

## Selected task title
Add deterministic guard coverage for `usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard`.

## Why this task now
`iter_033/06-next-iteration.md` explicitly queued this guard-chain follow-up so parser/usage coverage keeps self-protecting as modes expand.

## Acceptance criteria
1. Add one deterministic guard mode in `state/copilot_sdk_smoke_test.py` that asserts `usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard` is present in argparse `--mode` choices and generated usage examples.
2. Run:
   - `uv run python state/copilot_sdk_smoke_test.py --mode mode-choices-coverage-guard`
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard-coverage-guard`

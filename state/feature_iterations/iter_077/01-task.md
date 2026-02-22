# Task

## Selected task title
Migrate remaining usage-examples duplicate-count mode-coverage guard functions to `_mode_action_for_parser`.

## Why this task now
`iter_076/06-next-iteration.md` identified duplicated argparse `--mode` lookup logic as the next smallest unfinished cleanup.

## Acceptance criteria
1. Replace duplicated `parser._actions` `--mode` lookup in all `run_usage_examples_duplicate_count_mode_coverage_guard*` functions with `_mode_action_for_parser`.
2. Preserve existing assertions and PASS output text.
3. Run:
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-mode-coverage-guard`
   - `uv run python state/copilot_sdk_smoke_test.py --mode mode-choices-coverage-guard`

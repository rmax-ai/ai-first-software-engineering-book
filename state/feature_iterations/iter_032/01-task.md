# Task: Add duplicate-count mode-coverage guard-coverage guard coverage guard

## Why this task now
`state/feature_iterations/iter_031/06-next-iteration.md` requested a deterministic guard that protects the newest duplicate-count mode-coverage guard from disappearing from argparse mode choices and generated usage examples.

## Acceptance criteria
1. Add one deterministic guard mode in `state/copilot_sdk_smoke_test.py` that asserts `usage-examples-duplicate-count-mode-coverage-guard-coverage-guard` appears in parser `--mode` choices and generated usage lines.
2. Register the new mode in `TRACE_SUMMARY_MODE_SPECS`.
3. Validate with:
   - `uv run python state/copilot_sdk_smoke_test.py --mode mode-choices-coverage-guard`
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-mode-coverage-guard-coverage-guard-coverage-guard`

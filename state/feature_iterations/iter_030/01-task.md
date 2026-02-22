# Task: Add duplicate-count regression mode coverage guard

## Why this task now
`state/feature_iterations/iter_029/06-next-iteration.md` prioritized a focused regression guard to ensure `usage-examples-duplicate-count-regression-guard` cannot be dropped from runnable parser choices or generated usage examples during future mode-table edits.

## Acceptance criteria
1. Add one deterministic guard mode in `state/copilot_sdk_smoke_test.py` that asserts `usage-examples-duplicate-count-regression-guard` is present in argparse `--mode` choices and generated usage lines.
2. Register the new guard in `TRACE_SUMMARY_MODE_SPECS` so it is part of shared mode metadata surfaces.
3. Validate with:
   - `uv run python state/copilot_sdk_smoke_test.py --mode mode-choices-coverage-guard`
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-mode-coverage-guard`

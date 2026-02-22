# Task: Add duplicate-count mode-coverage guard coverage guard

## Why this task now
`state/feature_iterations/iter_030/06-next-iteration.md` prioritized a follow-on deterministic guard so `usage-examples-duplicate-count-mode-coverage-guard` remains present in parser choices and generated usage examples.

## Acceptance criteria
1. Add one deterministic guard mode in `state/copilot_sdk_smoke_test.py` that asserts `usage-examples-duplicate-count-mode-coverage-guard` is present in argparse `--mode` choices and generated usage lines.
2. Register the new guard in `TRACE_SUMMARY_MODE_SPECS` so it is included in shared mode metadata surfaces.
3. Validate with:
   - `uv run python state/copilot_sdk_smoke_test.py --mode mode-choices-coverage-guard`
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-mode-coverage-guard-coverage-guard`

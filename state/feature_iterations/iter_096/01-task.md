# Task

## Selected task title
Add a smoke guard mode that enforces duplicate-count coverage-guard wrappers pass their own registered mode name as the first helper argument.

## Why this task now
`state/feature_iterations/iter_095/06-next-iteration.md` prioritizes literal payload integrity after signature-shape validation, and this closes the next deterministic wrapper regression vector.

## Acceptance criteria
1. Add one smoke mode in `state/copilot_sdk_smoke_test.py` that checks each duplicate-count coverage-guard wrapper passes its registered mode name as the first helper argument.
2. Register the mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-mode-name-literal-guard` and capture PASS output.

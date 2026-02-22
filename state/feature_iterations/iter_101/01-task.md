# Task

## Selected task title
Add a smoke guard mode that enforces duplicate-count coverage-guard wrappers pass helper delegation arguments as plain literals only.

## Why this task now
`state/feature_iterations/iter_100/06-next-iteration.md` identified f-string/concatenation usage in wrapper helper arguments as the next smallest deterministic regression surface.

## Acceptance criteria
1. Add one smoke mode in `state/copilot_sdk_smoke_test.py` that parses duplicate-count coverage-guard wrappers and asserts helper delegation args contain no f-strings or string-concatenation AST nodes.
2. Register the mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic description text.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-literal-only-guard` and capture PASS output.

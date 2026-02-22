# Recommended next task

## Task
Add deterministic coverage ensuring CLI `--help` mode descriptions remain synchronized with shared mode metadata.

## Why it is next
- This iteration protects module-doc mode coverage; `argparse` help text is the adjacent user-facing surface that can still drift independently.

## Acceptance criteria
1. Add one deterministic smoke mode/path in `state/copilot_sdk_smoke_test.py` that validates `mode_help` content includes every registered mode description.
2. Keep mode dispatch behavior unchanged.
3. Validate with at least `uv run python state/copilot_sdk_smoke_test.py --mode stub` and the new help-coverage mode.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_019/*`

# Task

## Selected task title
Add deterministic coverage for argparse `--mode` choices synchronization with registered mode metadata.

## Why this task now
- `state/feature_iterations/iter_019/06-next-iteration.md` identified `choices` drift as the next parser-facing gap after help-text coverage.
- This is the smallest unfinished adjacent guard and protects CLI behavior without changing runtime dispatch logic.

## Acceptance criteria for this iteration
1. Add one deterministic smoke mode in `state/copilot_sdk_smoke_test.py` that validates parser `--mode` choices contain every registered mode name exactly once.
2. Keep existing mode dispatch behavior unchanged.
3. Validate with:
   - `uv run python state/copilot_sdk_smoke_test.py --mode stub`
   - `uv run python state/copilot_sdk_smoke_test.py --mode mode-choices-coverage-guard`

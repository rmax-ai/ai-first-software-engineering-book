# Next Iteration

## Recommended next task
Add a deterministic regression mode that exercises duplicate-count diagnostics with synthetic duplicated usage lines.

## Why it is next
Current validation confirms normal behavior but does not directly assert the new count-bearing failure payload shape under a forced duplicate scenario.

## Concrete acceptance criteria
1. Add one deterministic smoke mode in `state/copilot_sdk_smoke_test.py` that injects duplicate usage lines and asserts duplicate-count diagnostics include expected `{mode: count}` entries.
2. Keep assertions stable by ordering expected duplicate modes with `_expected_non_stub_mode_names(...)`.
3. Validate with:
   - `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicates-guard`
   - `uv run python state/copilot_sdk_smoke_test.py --mode <new-duplicate-count-regression-mode>`

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_029/*.md`

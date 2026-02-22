# Recommended next task

## Task
Add deterministic assertions that the generated smoke-test module docstring includes every registered mode from shared mode metadata.

## Why it is next
- This iteration removed manual drift; an explicit guard now prevents future regressions in generated docs coverage.

## Acceptance criteria
1. Add a deterministic mode (or focused test path) in `state/copilot_sdk_smoke_test.py` that validates docstring mode coverage against registered mode specs.
2. Keep existing runtime smoke modes and argparse behavior unchanged.
3. Re-run at least `stub`, `bootstrap-failure`, and `trace-summary`.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_018/*`

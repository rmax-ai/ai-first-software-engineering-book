# Task: Add deterministic module-doc mode coverage guard

## Why this task now
- `state/feature_iterations/iter_017/06-next-iteration.md` requested a deterministic assertion that generated smoke-test docs include all registered modes.
- This closes the remaining drift vector between shared mode metadata and the rendered module docstring.

## Acceptance criteria
1. Add one deterministic mode (or focused path) in `state/copilot_sdk_smoke_test.py` that validates module docstring mode coverage against registered mode specs.
2. Keep existing runtime smoke modes and argparse behavior unchanged.
3. Re-run `stub`, `bootstrap-failure`, and `trace-summary`.

# Next iteration

## Recommended next task
Add deterministic tests in `state/copilot_sdk_smoke_test.py` for the new fixture-backed `--run-kernel-for-trace-summary` behavior.

## Why it is next
The fixture-backed runtime path is now implemented; deterministic tests should lock in this behavior and prevent regressions in fixture assembly, exit-code handling, and malformed phase-trace expectations.

## Concrete acceptance criteria
1. Add/extend smoke test coverage to exercise all four kernel-run trace-summary modes through fixture-backed execution.
2. Assert expected outcomes: normal mode succeeds and malformed modes report the expected phase-trace validation failures.
3. Ensure tests verify repository ledger immutability (no diff in `state/ledger.json` after kernel-run smoke).
4. Record command output in `state/feature_iterations/iter_063/04-validation.md`.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_063/*.md`

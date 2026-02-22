# Plan

1. Inspect `state/copilot_sdk_smoke_test.py` mode metadata and parser construction to reuse existing helpers.
2. Add a deterministic guard mode that builds the parser and asserts `--mode` choices exactly match registered mode names in order.
3. Refactor parser construction into a small helper to avoid duplicating parser logic between runtime and guard.
4. Register the new guard mode in the mode-spec matrix so docs/help generation remains metadata-driven.
5. Run targeted validation commands and record evidence.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_020/01-task.md`
- `state/feature_iterations/iter_020/02-plan.md`
- `state/feature_iterations/iter_020/03-execution.md`
- `state/feature_iterations/iter_020/04-validation.md`
- `state/feature_iterations/iter_020/05-risks-and-decisions.md`
- `state/feature_iterations/iter_020/06-next-iteration.md`
- `state/feature_iterations/iter_020/07-summary.md`

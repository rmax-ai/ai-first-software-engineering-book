# Plan

1. Inspect `state/copilot_sdk_smoke_test.py` for where mode metadata is converted into argparse `--mode` help text.
2. Add a deterministic guard mode that builds mode-help text from shared mode specs and asserts every `name = description` pair is present.
3. Reuse helper logic for mode-help generation so production path and test guard derive from the same source.
4. Register the new guard in shared mode specs only; avoid changing dispatch semantics.
5. Run targeted smoke checks (`stub` and new guard mode), plus a quick syntax compile check.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_019/01-task.md`
- `state/feature_iterations/iter_019/02-plan.md`
- `state/feature_iterations/iter_019/03-execution.md`
- `state/feature_iterations/iter_019/04-validation.md`
- `state/feature_iterations/iter_019/05-risks-and-decisions.md`
- `state/feature_iterations/iter_019/06-next-iteration.md`
- `state/feature_iterations/iter_019/07-summary.md`

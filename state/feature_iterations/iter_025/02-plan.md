# Plan

1. Inspect usage-example guard functions in `state/copilot_sdk_smoke_test.py` to locate duplicate extraction logic.
2. Add a small private helper to parse generated usage lines into non-`stub` mode names.
3. Replace duplicated extraction blocks in usage-example guard modes with helper calls while preserving existing assertions/messages.
4. Run the three required smoke commands from prior guidance.
5. Record execution evidence and outcomes in iteration artifacts.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_025/01-task.md`
- `state/feature_iterations/iter_025/02-plan.md`
- `state/feature_iterations/iter_025/03-execution.md`
- `state/feature_iterations/iter_025/04-validation.md`
- `state/feature_iterations/iter_025/05-risks-and-decisions.md`
- `state/feature_iterations/iter_025/06-next-iteration.md`
- `state/feature_iterations/iter_025/07-summary.md`

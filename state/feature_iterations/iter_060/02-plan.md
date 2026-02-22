# Plan

1. Add a single `TRACE_SUMMARY_MODE_SPECS` constant in `state/copilot_sdk_uv_smoke.py`.
2. Replace the per-mode `if` chain in `main_async` with shared lookup and a single `run_trace_summary_mode` call path.
3. Reuse the same mode-spec keys in argparse choices for `--mode`.
4. Run all trace-summary smoke commands and capture pass/fail evidence.
5. Write iteration handoff artifacts for this one scoped task.

## Files expected to change
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_060/01-task.md`
- `state/feature_iterations/iter_060/02-plan.md`
- `state/feature_iterations/iter_060/03-execution.md`
- `state/feature_iterations/iter_060/04-validation.md`
- `state/feature_iterations/iter_060/05-risks-and-decisions.md`
- `state/feature_iterations/iter_060/06-next-iteration.md`
- `state/feature_iterations/iter_060/07-summary.md`

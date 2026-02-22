# Plan

1. Add a deterministic smoke mode in `state/copilot_sdk_smoke_test.py` that compares generated non-`stub` usage line order to `_all_mode_specs()` registration order.
2. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` so generated docstring usage/mode sections, parser choices/help, and dispatch remain metadata-driven.
3. Run targeted validation commands for `stub` and the new order guard mode.
4. Record execution evidence and decisions in iteration artifacts.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_023/03-execution.md`
- `state/feature_iterations/iter_023/04-validation.md`
- `state/feature_iterations/iter_023/05-risks-and-decisions.md`
- `state/feature_iterations/iter_023/06-next-iteration.md`
- `state/feature_iterations/iter_023/07-summary.md`

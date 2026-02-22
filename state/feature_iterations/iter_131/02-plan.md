# Plan

1. Locate the newest `...order-uniqueness-order-guard` smoke mode and nearby guard-mode patterns in `state/copilot_sdk_smoke_test.py`.
2. Add a new `run_*_order_uniqueness_order_uniqueness_guard_mode` function that checks exact count (`== 1`) for the target mode string.
3. Append a new `TRACE_SUMMARY_MODE_SPECS` entry for `...order-uniqueness-order-uniqueness-guard` immediately after the existing `...order-uniqueness-order-guard` entry.
4. Run only the new smoke mode command and capture the PASS result.
5. Record execution, validation evidence, risks, and one next task in iteration artifacts.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_131/01-task.md`
- `state/feature_iterations/iter_131/02-plan.md`
- `state/feature_iterations/iter_131/03-execution.md`
- `state/feature_iterations/iter_131/04-validation.md`
- `state/feature_iterations/iter_131/05-risks-and-decisions.md`
- `state/feature_iterations/iter_131/06-next-iteration.md`
- `state/feature_iterations/iter_131/07-summary.md`


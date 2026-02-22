# Plan

1. Update `state/copilot_sdk_smoke_test.py` with one new deterministic mode:
   - add usage/docs line
   - add mode description
   - add mode function asserting missing `trace_summary` failure message
   - wire parser choices, help text, and dispatch branch
2. Run targeted verification:
   - `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-missing-entry-guard`
   - `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-chapter-metrics-shape-guard`
   - `uv run python -m py_compile state/copilot_sdk_smoke_test.py`
3. Capture execution, validation, risks, and next task in iteration artifacts.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_013/01-task.md`
- `state/feature_iterations/iter_013/02-plan.md`
- `state/feature_iterations/iter_013/03-execution.md`
- `state/feature_iterations/iter_013/04-validation.md`
- `state/feature_iterations/iter_013/05-risks-and-decisions.md`
- `state/feature_iterations/iter_013/06-next-iteration.md`
- `state/feature_iterations/iter_013/07-summary.md`

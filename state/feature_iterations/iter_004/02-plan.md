# Plan

1. Extend `state/copilot_sdk_uv_smoke.py` with a `trace-summary` mode.
2. Implement metrics-history assertion logic for `trace_summary` required keys.
3. Keep existing `ping` and `prompt` behavior untouched.
4. Add CLI flags for chapter selection and optional kernel pre-run.
5. Validate via py_compile and a deterministic fixture-backed smoke invocation.

## Expected files to change
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_004/01-task.md`
- `state/feature_iterations/iter_004/02-plan.md`
- `state/feature_iterations/iter_004/03-execution.md`
- `state/feature_iterations/iter_004/04-validation.md`
- `state/feature_iterations/iter_004/05-risks-and-decisions.md`
- `state/feature_iterations/iter_004/06-next-iteration.md`
- `state/feature_iterations/iter_004/07-summary.md`

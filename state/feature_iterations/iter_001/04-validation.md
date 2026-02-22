# Validation

## Verification commands run
- `ls state/feature_iterations/iter_001`
- `sed -n '1,200p' state/feature_iterations/iter_001/01-task.md`
- `sed -n '1,240p' state/feature_iterations/iter_001/02-plan.md`
- `sed -n '1,200p' state/feature_iterations/iter_001/06-next-iteration.md`

## Observed results
- Iteration folder contains all seven required markdown artifacts.
- `01-task.md` includes clear acceptance criteria for features, tests, and eval alignment.
- `02-plan.md` names future touchpoints in `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, and `evals/*.yaml`.
- `06-next-iteration.md` recommends exactly one next task with concrete acceptance criteria.

## Acceptance criteria status
- Complete: Yes

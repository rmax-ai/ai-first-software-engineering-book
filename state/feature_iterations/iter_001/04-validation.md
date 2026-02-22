# Validation

## Verification commands run
1. `ls state/feature_iterations/iter_001`
2. `for f in 01-task.md 02-plan.md 03-execution.md 04-validation.md 05-risks-and-decisions.md 06-next-iteration.md 07-summary.md; do test -f "state/feature_iterations/iter_001/$f" && echo "PASS $f"; done`
3. `rg "state/kernel.py|state/role_io_templates.py|state/copilot_sdk_uv_smoke.py|evals/chapter-quality.yaml|evals/style-guard.yaml|evals/drift-detection.yaml" state/feature_iterations/iter_001/02-plan.md`
4. `rg "Exactly 1 recommended next task|Acceptance criteria|Expected files to touch" state/feature_iterations/iter_001/06-next-iteration.md`

## Observed results
- All seven required markdown files were present in `state/feature_iterations/iter_001/`.
- File-presence loop emitted `PASS` for each required artifact.
- `02-plan.md` contains explicit future touchpoints for kernel, role templates, smoke test, and eval contracts.
- `06-next-iteration.md` contains one recommended task with measurable acceptance criteria and expected files.

## Acceptance criteria status
- **Pass**: planning artifact coverage includes features, tests, and evaluations.
- **Pass**: iteration folder contract fulfilled with all seven markdown artifacts.
- **Pass**: next iteration guidance is concrete, single-task scoped, and actionable.

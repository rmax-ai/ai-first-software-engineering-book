# Execution

## Commands/tools run
- Read guidance:
  - `view prompts/incremental-improvements/execute.md`
  - `view DEVELOPMENT.md`
  - `view .github/instructions/copilot-sdk-python.instructions.md`
- Iteration discovery:
  - `glob state/feature_iterations/iter_*` (no prior iterations found)
- Artifact authoring:
  - `apply_patch` to create markdown artifacts in `state/feature_iterations/iter_001/`

## Files changed
- `state/feature_iterations/iter_001/01-task.md`
- `state/feature_iterations/iter_001/02-plan.md`
- `state/feature_iterations/iter_001/03-execution.md`
- `state/feature_iterations/iter_001/04-validation.md`
- `state/feature_iterations/iter_001/05-risks-and-decisions.md`
- `state/feature_iterations/iter_001/06-next-iteration.md`
- `state/feature_iterations/iter_001/07-summary.md`

## Rationale by change
- `01-task.md`: fixed the selected story and acceptance criteria for planning-only seed iteration.
- `02-plan.md`: captured a concrete implementation backlog for later iterations across features/tests/evals.
- Remaining artifacts: provide required evidence, risk framing, next task, and executive summary per contract.

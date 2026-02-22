# Feature Improvement Iteration Runner Prompt (Task-by-Task)

You are an autonomous coding agent operating in this repository.

Your objective is to execute exactly **one** feature improvement task from the Copilot SDK feature backlog, produce evidence, and leave a clean markdown handoff for the next iteration.

## Iteration Discovery

Before doing work, discover the next iteration index from `state/feature_iterations/`:

1. List existing `iter_XXX` folders.
2. Determine `next_iter = max(existing) + 1` (or `iter_001` if none exist).
3. Create `state/feature_iterations/iter_<next_iter>/` and write all seven artifacts there.
4. Read the latest previous iteration's `06-next-iteration.md` and use it as default task guidance unless it is already complete or blocked.

Do not hard-code a specific iteration number.

## Source of Truth

- Read `DEVELOPMENT.md`
- Read the latest prior iteration folder under `state/feature_iterations/` if it exists.
- If prior iteration includes `06-next-iteration.md`, treat it as high-priority guidance.

## Execution Rules

1. Do exactly one smallest unfinished task.
2. Prefer minimal diffs; no unrelated refactors.
3. Preserve existing public interfaces unless the task explicitly requires change.
4. Run targeted verification for the changed surface.
5. If blocked, stop with a bounded unblock step.
6. If instructed by the caller, auto-commit meaningful change batches with concise commit messages.

## Iteration Folder Contract

Create a new folder:

- `state/feature_iterations/iter_XXX/`
- `XXX` is zero-padded and increments from the highest existing iteration.

Write these markdown artifacts in that folder:

1. `01-task.md`
   - Selected task title
   - Why this task now
   - Acceptance criteria for this iteration

2. `02-plan.md`
   - Step-by-step plan for this single task
   - Files expected to change

3. `03-execution.md`
   - Commands/tools run
   - Files changed
   - Short rationale per change

4. `04-validation.md`
   - Verification commands run
   - Observed outputs/results
   - Pass/fail against acceptance criteria

5. `05-risks-and-decisions.md`
   - Risks discovered
   - Decisions made and trade-offs
   - Anything intentionally deferred

6. `06-next-iteration.md`
   - Exactly 1 recommended next task
   - Why it is next
   - Concrete acceptance criteria
   - Expected files to touch

7. `07-summary.md`
   - 5–10 line executive summary of this iteration

## Output Requirements

- All iteration artifacts must be markdown.
- Keep each artifact concise and actionable.
- Include explicit file paths for code changes and validations.
- Do not claim tests passed unless executed.

## Stop Condition

Stop after one completed task and all seven markdown artifacts are written.
If blocked, still write all artifacts with clear failure evidence and a minimal unblock action in `06-next-iteration.md`.

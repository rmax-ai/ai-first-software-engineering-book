# Migration Iteration Artifacts

This folder stores per-iteration markdown artifacts for the state runner migration.

## Naming

- Iteration folders use: `iter_XXX` (zero-padded), e.g. `iter_001`, `iter_002`.
- Each iteration folder contains exactly these markdown files:

  - `01-task.md`
  - `02-plan.md`
  - `03-execution.md`
  - `04-validation.md`
  - `05-risks-and-decisions.md`
  - `06-next-iteration.md`
  - `07-summary.md`

## Purpose

The artifact set creates deterministic handoff between iterations:

- what was attempted,
- what changed,
- what evidence exists,
- and what should happen next.

## Workflow

Use `prompts/migration-iteration/execute.md` as the run prompt.
Each invocation completes one smallest migration task and writes one new `iter_XXX` folder.

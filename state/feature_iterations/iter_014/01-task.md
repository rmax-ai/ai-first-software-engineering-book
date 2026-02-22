# Task: Refactor trace-summary mode registration to table-driven mapping

## Why this task now
- `state/feature_iterations/iter_013/06-next-iteration.md` recommended reducing repetitive trace-summary mode wiring.
- A single mapping lowers drift risk when adding new deterministic trace-summary guards.

## Acceptance criteria
1. Use one source of truth for trace-summary mode name, handler, and help description.
2. Keep CLI behavior and outputs unchanged for existing trace-summary modes.
3. Re-run `trace-summary`, `trace-summary-missing-entry-guard`, and one shutdown mode.

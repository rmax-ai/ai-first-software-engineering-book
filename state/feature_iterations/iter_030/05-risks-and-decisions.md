# Risks and decisions

## Risks discovered
- The guard hard-codes the target mode string; if the mode is intentionally renamed, this guard must be updated in the same change.
- Future refactors of usage-line parsing could alter extracted mode names and require coordinated updates to this guard.

## Decisions and trade-offs
- Chose a dedicated mode-level assertion instead of extending existing broad guards to keep failure signals precise.
- Reused current parser and usage helper functions to minimize implementation drift.

## Deferred
- Did not add separate assertions for mode-help text because this task was scoped to parser choices and usage examples.

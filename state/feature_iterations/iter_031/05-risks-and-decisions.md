# Risks and decisions

## Risks discovered
- The new guard uses a hard-coded target mode string; intentional renames require coordinated updates.
- Repeated guard-of-guard chaining can increase maintenance overhead if scope is not periodically reset.

## Decisions and trade-offs
- Chose a narrow deterministic assertion instead of broadening generic coverage guards so failure output stays precise.
- Reused existing parser and usage helper functions to minimize drift from tested behavior.

## Deferred
- Did not refactor repeated parser-choice assertion logic because this iteration was scoped to one minimal backlog task.

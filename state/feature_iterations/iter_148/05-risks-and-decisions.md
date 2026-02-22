# Risks and decisions

## Risks discovered
- The long-form mode-name chain is fragile; small ordering edits can silently break deterministic guard expectations.

## Decisions made
- Chose a minimal ordering fix (swap adjacent tuple entries) instead of refactoring naming or guard helper structure.
- Kept existing runner logic unchanged because it already encoded the intended predecessor→exact-once adjacency rule.

## Deferred items
- Any additional cleanup of long-form mode naming remains deferred to keep this iteration scoped to one smallest unfinished task.

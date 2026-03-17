# Risks and decisions

## Risks discovered
- The long-form mode-name chain remains fragile; a small registration-order edit can break several alias guards at once.
- Publishing the iteration index in multiple places can drift if future runs update the folder without updating the top-level indexes.

## Decisions made
- Added only one alias runner instead of refactoring the long-form guard structure.
- Added a single README index inside `state/feature_iterations/` and linked to it from the two existing top-level indexes.

## Deferred items
- Broader normalization of long-form smoke mode naming remains deferred to keep this iteration scoped to one smallest task.

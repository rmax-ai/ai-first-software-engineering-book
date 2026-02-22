# Risks and decisions

## Risks discovered
- Long mode names and similarly shaped guard suffixes make placement mistakes in `TRACE_SUMMARY_MODE_SPECS` easy.

## Decisions made and trade-offs
- Kept the implementation as one new runner and one new registration instead of introducing refactors or constants.
- Preserved the adjacency relation under test by moving only the new mode entry to a safe nearby location.

## Anything intentionally deferred
- Broader cleanup/refactoring of long mode-name literals remains deferred because it is outside this single-task iteration scope.

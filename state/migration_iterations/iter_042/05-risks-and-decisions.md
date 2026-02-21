# Risks and Decisions

## Risks discovered
- Shutdown smoke coverage still depends on monkeypatching internal client/session members, which may need updates if shutdown internals change.

## Decisions made and trade-offs
- Added one narrowly scoped mode instead of refactoring shared helpers to keep this iteration minimal and aligned with the requested single task.
- Kept existing mode output conventions intact to preserve downstream automation compatibility.

## Intentionally deferred
- Additional combined failure permutations (for example stop failure + destroy unavailable + force_stop unavailable) were deferred to future iterations.


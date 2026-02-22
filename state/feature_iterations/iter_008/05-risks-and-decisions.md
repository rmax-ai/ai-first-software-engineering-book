# Risks and decisions

## Risks discovered
- Existing mode stability was validated for nearby trace-summary modes only; full smoke matrix was not rerun.

## Decisions made and trade-offs
- Added a single focused malformed `history` fixture (`history` as dict) to satisfy acceptance criteria with minimal diff.
- Reused existing assertion-message pattern for deterministic failure detection instead of introducing new helper abstractions.

## Deferred intentionally
- Additional malformed `history` edge variants (e.g., empty tuple, scalar) were deferred to keep this iteration strictly single-task.

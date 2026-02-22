# Risks and decisions

## Risks discovered
- Overloading existing malformed mode could hide whether key-missing vs type-mismatch coverage is failing.

## Decisions made and trade-offs
- Added a separate `trace-summary-malformed-phase-payload` mode to keep failure causes explicit and deterministic.
- Reused existing fixture-validation path to minimize implementation risk and diff size.

## Deferred intentionally
- Additional malformed payload permutations (e.g., lists/null) are deferred to avoid widening scope beyond one smallest task.

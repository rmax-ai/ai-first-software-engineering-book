# Risks and decisions

## Risks discovered
- Fixture-root cleanup assertions can become flaky if external processes write into `state/.smoke_fixtures/trace_summary/` concurrently.
- Adding more aggregate modes increases smoke runtime incrementally.

## Decisions made and trade-offs
- Added one focused deterministic mode instead of expanding existing mode semantics, preserving backward-compatible expectations.
- Used a narrow residual-directory check (directories only) to align with cleanup intent from prior iteration guidance.

## Deferred work
- Any broader fixture-file residual checks outside directory leakage.

# Risks and decisions

## Risks discovered
- Only `chapters` malformed-container shape is covered; malformed `history` and latest-entry containers remain uncovered.

## Decisions and trade-offs
- Chose one new mode only to satisfy the “exactly one smallest unfinished task” rule.
- Reused existing `_get_latest_trace_summary` assertion messages to keep guard behavior deterministic.

## Deferred intentionally
- Additional malformed-container modes for `history` list and latest history-entry shape.

## Loop self-evaluation
- **Goal check:** Completed the recommended `iter_006` task by adding one deterministic malformed-container guard mode and CLI wiring.
- **Evidence check:** Executed targeted mode runs and compile validation with passing outputs.
- **Risk check:** Coverage still does not include malformed `history` or malformed latest-entry fixtures.
- **Next-step decision:** Stop and hand off one bounded follow-up to cover malformed `history` shape with one deterministic mode.

# Risks and decisions

## Risks discovered
- Fixture-level shape checks do not cover malformed `trace_summary` emitted from full kernel runs.

## Decisions and trade-offs
- Reused `_get_latest_trace_summary` assertion path so malformed-shape detection stays consistent with existing required-key checks.
- Kept the new mode deterministic and isolated to avoid flaky integration dependencies.

## Deferred intentionally
- Running full-kernel metrics generation with malformed `trace_summary` injection.

## Loop self-evaluation
- **Goal check:** Completed the recommended `iter_005` task by adding one deterministic malformed-shape mode with CLI wiring.
- **Evidence check:** Executed compile validation and mode runs (`trace-summary`, `trace-summary-shape-guard`) with passing outputs.
- **Risk check:** Coverage remains fixture-driven and may not detect integration-only serialization regressions.
- **Next-step decision:** Stop this iteration and hand off one bounded follow-up focused on malformed chapter/history container shapes.

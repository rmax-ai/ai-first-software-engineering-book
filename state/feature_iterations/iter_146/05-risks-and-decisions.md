# Risks and decisions

## Risks discovered
- Existing long-form mode naming is extremely long, increasing risk of accidental mismatches during additions.

## Decisions made and trade-offs
- Reused exact string patterns already present in `TRACE_SUMMARY_MODE_SPECS` to avoid introducing naming drift.
- Kept validation scoped to the new mode to minimize runtime while still proving the changed surface.

## Deferred
- Full smoke matrix execution was deferred; only the targeted changed mode was executed this iteration.

# Risks and Decisions

## Risks discovered
- Long chained mode names are typo-prone; one segment mismatch can silently target the wrong guard pair.
- Registration order in `TRACE_SUMMARY_MODE_SPECS` is semantically meaningful for these adjacency checks, so neighboring edits can break guard assumptions.

## Decisions made and trade-offs
- Kept the change narrowly scoped to one new guard function and one new mode registration to minimize regression risk.
- Reordered only the two newest related registrations needed to satisfy the adjacency requirement, avoiding broader tuple reshuffling.

## Intentionally deferred
- Full smoke matrix execution was deferred; only the directly affected mode path was validated.

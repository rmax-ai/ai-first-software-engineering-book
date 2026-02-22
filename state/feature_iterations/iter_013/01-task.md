# Task: Add deterministic missing trace_summary entry guard mode

## Why this task now
- `state/feature_iterations/iter_012/06-next-iteration.md` recommends validating the missing `trace_summary` entry path in `_get_latest_trace_summary`.
- Existing guards cover shape/container cases; this closes the remaining latest-entry completeness gap.

## Acceptance criteria
1. Add exactly one deterministic smoke mode where latest history entry is a dictionary without `trace_summary`.
2. Mode passes only when `expected latest history entry to contain trace_summary dictionary` is detected.
3. Existing trace-summary smoke modes remain unchanged in behavior.

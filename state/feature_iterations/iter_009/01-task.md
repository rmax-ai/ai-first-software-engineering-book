# Task: Add malformed latest history entry guard smoke mode

## Why this task now
`iter_008` recommended closing the next `_get_latest_trace_summary` blind spot by validating malformed latest `history` entries before `trace_summary` extraction.

## Acceptance criteria
1. Add exactly one deterministic smoke mode where the latest `history` entry is non-dict.
2. Ensure the mode passes only when latest-entry shape assertion failure is detected.
3. Keep existing trace-summary smoke mode behavior unchanged.

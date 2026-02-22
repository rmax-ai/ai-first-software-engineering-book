# Task: Add trace_summary smoke assertion

## Why this task now
`iter_003` requested a focused regression check to ensure `trace_summary` remains present and shape-stable in metrics history.

## Acceptance criteria
1. Smoke flow validates that `trace_summary` exists on the latest history entry for a chapter.
2. Validation checks required keys: `decision`, `drift_score`, `diff_ratio`, `deterministic_pass`.
3. Existing `ping`/`prompt` code paths remain unchanged.

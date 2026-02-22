# Task: Add deterministic chapter-metrics-shape guard smoke mode

## Why this task now
`state/feature_iterations/iter_011/06-next-iteration.md` recommended adding explicit guard coverage for non-dict `chapter_metrics` entries in `_get_latest_trace_summary`.

## Acceptance criteria
1. Add exactly one deterministic smoke mode where `chapters[chapter_id]` is present but not a dictionary.
2. Ensure the mode passes only when `expected chapter metrics dictionary` assertion failure is detected.
3. Keep existing trace-summary smoke mode behavior unchanged.

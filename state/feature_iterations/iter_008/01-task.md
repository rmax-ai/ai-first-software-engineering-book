# Task: Add malformed history container guard smoke mode

## Why this task now
`iter_007` recommended closing the remaining deterministic container-shape gap for malformed `history` payloads before latest trace-summary lookup.

## Acceptance criteria
1. Add exactly one deterministic smoke mode where `history` is not a list.
2. Ensure the mode passes only when container-shape assertion failure is detected.
3. Keep existing smoke mode behavior unchanged.

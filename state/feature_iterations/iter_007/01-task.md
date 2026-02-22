# Task: Add malformed metrics container guard smoke mode

## Why this task now
`iter_006` recommended extending deterministic trace-summary coverage to malformed metrics containers consumed by `_get_latest_trace_summary`.

## Acceptance criteria
1. Add exactly one deterministic smoke mode with malformed container fixtures.
2. Ensure the mode passes only when container-shape assertion failure is detected.
3. Keep existing trace-summary smoke modes unchanged.

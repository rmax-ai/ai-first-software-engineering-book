# Task: Add trace-summary fixture-shape guard smoke mode

## Why this task now
`iter_005` recommended adding malformed `trace_summary` type-shape coverage so schema validation fails fast when payloads are not dictionaries.

## Acceptance criteria
1. Add one deterministic mode where `trace_summary` is not a dictionary.
2. Ensure the mode passes only when malformed shape detection is triggered.
3. Keep current smoke modes unchanged.

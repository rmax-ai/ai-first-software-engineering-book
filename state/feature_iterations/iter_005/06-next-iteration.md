# Recommended next task

## Task
Add a trace-summary fixture-shape guard mode in `state/copilot_sdk_smoke_test.py` that fails when `trace_summary` is non-dict (e.g., list/string) to harden schema validation.

## Why it is next
Current coverage validates key presence and missing-key detection but does not assert type-shape failures for malformed `trace_summary` payloads.

## Acceptance criteria
1. Add one deterministic mode where `trace_summary` is not a dictionary.
2. Ensure the mode passes only when the malformed shape is detected.
3. Keep all current smoke modes unchanged.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`

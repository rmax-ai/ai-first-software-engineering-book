# Next Iteration Recommendation

## Recommended task
Implement deterministic trace-summary schema hardening in `state/kernel.py` with targeted tests.

## Why this is next
- It is the highest-impact foundation for observability and downstream eval reliability.
- It unlocks safer iteration on role templates and smoke coverage by stabilizing core trace outputs.

## Acceptance criteria
- Add/adjust kernel logic so trace summaries always include stable required fields and explicit missing-data handling.
- Add targeted tests for the updated trace summary shape and failure metadata.
- Validate with deterministic smoke run(s), e.g.:
  - `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-shape-guard`
  - `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-missing-entry-guard`
- Document evidence in the next iteration artifacts.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_smoke_test.py`
- relevant test files under `state/` (if present/needed)

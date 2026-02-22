# Execution

## Commands/tools run
- Read guidance: `DEVELOPMENT.md`, `state/feature_iterations/iter_011/06-next-iteration.md`.
- Validation command batch:
  - `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-chapter-metrics-shape-guard`
  - `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-missing-chapter-guard`
  - `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary`
  - `uv run python -m py_compile state/copilot_sdk_smoke_test.py`
  - `uv run pytest -q`

## Files changed
- `state/copilot_sdk_smoke_test.py`
  - Added `trace-summary-chapter-metrics-shape-guard` mode and CLI wiring.
- `state/feature_iterations/iter_012/01-task.md` ... `07-summary.md`
  - Added full iteration handoff artifacts.

## Rationale
One targeted deterministic mode closes the chapter-metrics shape-guard gap with minimal code churn and preserves existing smoke behavior.

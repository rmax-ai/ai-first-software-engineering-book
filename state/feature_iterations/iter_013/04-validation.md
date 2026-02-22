# Validation

## Verification commands run
1. `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-missing-entry-guard`
2. `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-chapter-metrics-shape-guard`
3. `uv run python -m py_compile state/copilot_sdk_smoke_test.py`

## Observed results
- Mode `trace-summary-missing-entry-guard`: `PASS: trace-summary-missing-entry-guard mode detects missing trace_summary entries`
- Mode `trace-summary-chapter-metrics-shape-guard`: `PASS: trace-summary-chapter-metrics-shape-guard mode detects malformed chapter metrics`
- `py_compile` exited successfully with no syntax errors.

## Acceptance criteria check
1. Added exactly one deterministic missing-entry guard mode: **pass**.
2. Mode validates expected assertion message for missing `trace_summary`: **pass**.
3. Existing adjacent trace-summary mode still passes: **pass**.

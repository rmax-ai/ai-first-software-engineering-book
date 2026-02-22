# Validation

## Verification commands run
1. `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-chapter-metrics-shape-guard`
2. `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-missing-chapter-guard`
3. `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary`
4. `uv run python -m py_compile state/copilot_sdk_smoke_test.py`
5. `uv run pytest -q`

## Observed results
- Command 1: `PASS: trace-summary-chapter-metrics-shape-guard mode detects malformed chapter metrics`
- Command 2: `PASS: trace-summary-missing-chapter-guard mode detects missing chapter entries`
- Command 3: `PASS: trace-summary mode validates required trace_summary keys`
- Command 4: exit code `0`
- Command 5: `no tests ran in 0.11s` (exit code `5`; repository currently has no collected pytest tests)

## Acceptance criteria status
1. ✅ Added exactly one deterministic chapter-metrics-shape guard mode.
2. ✅ Mode asserts `expected chapter metrics dictionary` failure path.
3. ✅ Existing trace-summary behavior remains intact in targeted smoke runs.

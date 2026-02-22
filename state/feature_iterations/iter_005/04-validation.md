# Validation

## Verification commands run
1. `uv run python -m py_compile state/copilot_sdk_smoke_test.py`
2. `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary`
3. `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-missing-key`

## Observed outputs/results
- Command 1: pass (exit code 0).
- Command 2: pass with `PASS: trace-summary mode validates required trace_summary keys`.
- Command 3: pass with `PASS: trace-summary-missing-key mode detects required key omissions`.

## Acceptance criteria status
1. Passing deterministic trace-summary mode added: ✅
2. Missing-key detection mode added: ✅
3. Existing smoke mode behavior unchanged by dispatch wiring and targeted validation: ✅

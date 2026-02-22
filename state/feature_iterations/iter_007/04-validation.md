# Validation

## Verification commands run
1. `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-shape-guard`
2. `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary`
3. `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-container-shape-guard`
4. `uv run python -m py_compile state/copilot_sdk_smoke_test.py`

## Observed outputs/results
- Command 1: pass with `PASS: trace-summary-shape-guard mode detects non-dict trace_summary payloads`.
- Command 2: pass with `PASS: trace-summary mode validates required trace_summary keys`.
- Command 3: pass with `PASS: trace-summary-container-shape-guard mode detects malformed metrics containers`.
- Command 4: pass (exit code 0).

## Acceptance criteria status
1. Exactly one deterministic malformed container mode added: ✅
2. Mode passes only when container-shape assertion failure is detected: ✅
3. Existing trace-summary modes unchanged: ✅

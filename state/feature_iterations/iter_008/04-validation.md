# Validation

## Verification commands run
1. `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-history-container-shape-guard`
2. `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-container-shape-guard`
3. `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary`
4. `uv run python -m py_compile state/copilot_sdk_smoke_test.py`

## Observed outputs/results
- Command 1: pass with `PASS: trace-summary-history-container-shape-guard mode detects malformed history containers`.
- Command 2: pass with `PASS: trace-summary-container-shape-guard mode detects malformed metrics containers`.
- Command 3: pass with `PASS: trace-summary mode validates required trace_summary keys`.
- Command 4: pass (exit code 0).

## Acceptance criteria status
1. Exactly one deterministic malformed `history` mode added: ✅
2. Mode passes only when container-shape assertion failure is detected: ✅
3. Existing smoke mode behavior unchanged for validated trace-summary modes: ✅

# Validation

## Verification commands run
1. `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-latest-history-entry-shape-guard`
2. `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-history-container-shape-guard`
3. `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary`
4. `uv run python -m py_compile state/copilot_sdk_smoke_test.py`

## Observed outputs/results
- Command 1: pass with `PASS: trace-summary-latest-history-entry-shape-guard mode detects malformed latest history entries`.
- Command 2: pass with `PASS: trace-summary-history-container-shape-guard mode detects malformed history containers`.
- Command 3: pass with `PASS: trace-summary mode validates required trace_summary keys`.
- Command 4: pass (exit code 0).

## Acceptance criteria status
1. Exactly one deterministic malformed latest `history` entry mode added: ✅
2. Mode passes only when latest-entry shape assertion failure is detected: ✅
3. Existing smoke mode behavior unchanged for validated trace-summary modes: ✅

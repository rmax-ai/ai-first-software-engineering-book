# Validation

## Verification commands run
1. `uv run python -m py_compile state/copilot_sdk_smoke_test.py`
2. `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary`
3. `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-shape-guard`

## Observed outputs/results
- Command 1: pass (exit code 0).
- Command 2: pass with `PASS: trace-summary mode validates required trace_summary keys`.
- Command 3: pass with `PASS: trace-summary-shape-guard mode detects non-dict trace_summary payloads`.

## Acceptance criteria status
1. Deterministic non-dict `trace_summary` mode added: ✅
2. Mode succeeds only when shape detection triggers: ✅
3. Existing smoke paths unchanged (verified by running pre-existing `trace-summary` mode): ✅

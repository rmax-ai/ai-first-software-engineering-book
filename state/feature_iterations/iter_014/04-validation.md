# Validation

## Verification commands run
- `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary`
- `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-missing-entry-guard`
- `uv run python state/copilot_sdk_smoke_test.py --mode stop-close-idempotency`
- `uv run python -m py_compile state/copilot_sdk_smoke_test.py`

## Observed results
- PASS: trace-summary mode validates required trace_summary keys.
- PASS: trace-summary-missing-entry-guard mode detects missing trace_summary entries.
- PASS: stop-close-idempotency mode validates repeated close() after stop() unavailable.
- `py_compile` exited successfully for `state/copilot_sdk_smoke_test.py`.

## Acceptance criteria status
1. **Pass**: one `TRACE_SUMMARY_MODE_SPECS` mapping now defines names, handlers, and help text for trace-summary modes.
2. **Pass**: trace-summary mode outputs remained unchanged in targeted runs.
3. **Pass**: required three-mode smoke subset executed successfully.

# Validation

## Verification commands run
- `uv run python state/copilot_sdk_smoke_test.py --mode stop-close-idempotency`
- `uv run python state/copilot_sdk_smoke_test.py --mode stop-failure-destroy-failure-close-idempotency`
- `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary`
- `uv run python -m py_compile state/copilot_sdk_smoke_test.py`

## Observed results
- PASS: stop-close-idempotency mode validates repeated close() after stop() unavailable.
- PASS: stop-failure-destroy-failure-close-idempotency mode validates repeated close() after stop()/destroy() failures.
- PASS: trace-summary mode validates required trace_summary keys.
- `py_compile` exited successfully for `state/copilot_sdk_smoke_test.py`.

## Acceptance criteria status
1. **Pass**: one `SHUTDOWN_MODE_SPECS` mapping now defines shutdown mode names, handlers, and help descriptions.
2. **Pass**: argparse mode choices/help and shutdown dispatch now reuse the shared mapping.
3. **Pass**: required three-mode smoke subset executed successfully.

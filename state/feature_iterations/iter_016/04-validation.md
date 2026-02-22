# Validation

## Verification commands run
- `uv run python state/copilot_sdk_smoke_test.py --mode stub`
- `uv run python state/copilot_sdk_smoke_test.py --mode bootstrap-failure`
- `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary`
- `uv run python -m py_compile state/copilot_sdk_smoke_test.py`

## Observed results
- PASS: stub Copilot SDK path works.
- PASS: bootstrap-failure mode validates worker-loop bootstrap error context.
- PASS: trace-summary mode validates required trace_summary keys.
- `py_compile` exited successfully for `state/copilot_sdk_smoke_test.py`.

## Acceptance criteria status
1. **Pass**: one `BASE_MODE_SPECS` mapping now defines base mode names, handlers, and help descriptions.
2. **Pass**: argparse mode choices/help and runtime dispatch now reuse one combined mode-spec pipeline.
3. **Pass**: required smoke subset executed successfully.

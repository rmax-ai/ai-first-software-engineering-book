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
1. **Pass**: module usage/mode docs are generated from shared mode metadata helpers.
2. **Pass**: mode names and argparse `--help` choices/description still derive from the same mode specs.
3. **Pass**: required smoke subset executed successfully.

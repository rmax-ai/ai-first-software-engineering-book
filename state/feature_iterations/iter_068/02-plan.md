# Plan

1. Add `run_trace_summary_fixture_root_cleanup_parity_mode()` that invokes both existing root-cleanup handlers.
2. Register the new mode in `TRACE_SUMMARY_MODE_SPECS` with a deterministic description.
3. Run targeted verification:
   - `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-fixture-root-cleanup-parity`
   - `uv run python state/copilot_sdk_smoke_test.py --mode mode-choices-coverage-guard`
   - `uv run python state/copilot_sdk_smoke_test.py --mode docstring-mode-coverage-guard`
4. Write iteration artifacts with results and one follow-up task.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_068/*.md`


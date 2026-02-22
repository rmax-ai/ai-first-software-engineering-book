# Plan

1. Add `run_trace_summary_fixture_cleanup_parity_mode()` in `state/copilot_sdk_smoke_test.py` that composes existing kernel and non-kernel fixture-cleanup handlers.
2. Register `trace-summary-fixture-cleanup-parity` in `TRACE_SUMMARY_MODE_SPECS` so parser/doc coverage includes it.
3. Run targeted verification:
   - `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-fixture-cleanup-parity`
   - `uv run python state/copilot_sdk_smoke_test.py --mode mode-choices-coverage-guard`
   - `uv run python state/copilot_sdk_smoke_test.py --mode docstring-mode-coverage-guard`
4. Write this iteration’s seven required markdown artifacts.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_069/*.md`


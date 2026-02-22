# Summary

- Executed one backlog task from `iter_013`: remove repetitive trace-summary mode registration wiring.
- Added `TRACE_SUMMARY_MODE_SPECS` in `state/copilot_sdk_smoke_test.py` as one source of truth for mode names, handlers, and descriptions.
- Reused that mapping for argparse mode choices, trace-summary help text generation, and runtime dispatch.
- Left non-trace-summary mode handling unchanged to keep the diff focused and low risk.
- Ran targeted smoke checks for `trace-summary`, `trace-summary-missing-entry-guard`, and `stop-close-idempotency`.
- Confirmed Python syntax validity with `uv run python -m py_compile state/copilot_sdk_smoke_test.py`.
- Captured risks and provided one concrete next task for `iter_015`.

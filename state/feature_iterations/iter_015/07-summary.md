# Summary

- Executed one backlog task from `iter_014`: table-drive shutdown mode wiring in `state/copilot_sdk_smoke_test.py`.
- Added `SHUTDOWN_MODE_SPECS` as a single source of truth for shutdown names, handlers, and help descriptions.
- Reused shutdown mapping for argparse mode choices, help text generation, and runtime dispatch.
- Kept mode behavior unchanged by preserving existing handler implementations and order.
- Ran targeted smoke checks for `stop-close-idempotency`, `stop-failure-destroy-failure-close-idempotency`, and `trace-summary`.
- Confirmed Python syntax validity with `uv run python -m py_compile state/copilot_sdk_smoke_test.py`.
- Captured risks and provided one concrete next task for `iter_016`.

# Plan

1. Add a reusable subprocess helper in `state/copilot_sdk_smoke_test.py` to run `state/copilot_sdk_uv_smoke.py` with `--run-kernel-for-trace-summary`.
2. Snapshot `state/ledger.json` before/after each subprocess invocation and assert byte-for-byte immutability.
3. Add four deterministic handlers for `trace-summary`, `trace-summary-malformed-phase`, `trace-summary-malformed-phase-payload`, and `trace-summary-missing-phase`.
4. Register the new handlers in `TRACE_SUMMARY_MODE_SPECS` so parser choices and generated module docs stay synchronized.
5. Execute targeted deterministic smoke commands and capture results for validation evidence.

## Files expected to change
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_063/01-task.md`
- `state/feature_iterations/iter_063/02-plan.md`
- `state/feature_iterations/iter_063/03-execution.md`
- `state/feature_iterations/iter_063/04-validation.md`
- `state/feature_iterations/iter_063/05-risks-and-decisions.md`
- `state/feature_iterations/iter_063/06-next-iteration.md`
- `state/feature_iterations/iter_063/07-summary.md`

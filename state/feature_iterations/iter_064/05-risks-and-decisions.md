# Risks and decisions

## Risks discovered
- Fixture cleanup now happens unconditionally after kernel-backed runs; failures cannot be debugged by inspecting retained fixture repos unless cleanup is temporarily disabled.
- The cleanup guard depends on a fixed fixture path (`state/.smoke_fixtures/trace_summary/kernel_repo`), so path changes require synchronized updates.

## Decisions and trade-offs
- Chose explicit cleanup in `state/copilot_sdk_uv_smoke.py` instead of test-only cleanup to enforce behavior in the real smoke runner.
- Kept ledger immutability assertions in `_run_trace_summary_kernel_mode` so cleanup verification does not relax repository safety checks.

## Deferred
- Adding an opt-in debug flag to preserve fixtures on failure was deferred to keep this iteration scoped to deterministic cleanup guarantees.

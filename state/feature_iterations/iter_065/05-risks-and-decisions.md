# Risks and decisions

## Risks discovered
- Fixture cleanup now removes non-kernel fixture repos after each run, so failed-run fixture inspection is unavailable unless cleanup is temporarily disabled.
- Cleanup assertions are path-bound to `state/.smoke_fixtures/trace_summary/repo`; path refactors require synchronized updates.

## Decisions and trade-offs
- Enforced cleanup in `state/copilot_sdk_uv_smoke.py` instead of test-only cleanup to keep runtime behavior and test assertions consistent.
- Added a dedicated non-kernel helper in `state/copilot_sdk_smoke_test.py` rather than overloading kernel helper logic, keeping kernel ledger safety assertions unchanged.

## Deferred
- Adding an opt-in debug switch to preserve non-kernel fixtures on failure was deferred to keep scope limited to deterministic cleanup coverage.

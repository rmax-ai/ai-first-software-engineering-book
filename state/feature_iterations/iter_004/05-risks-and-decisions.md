# Risks and decisions

## Risks discovered
- Direct kernel pre-run may fail in local repos where chapter eligibility blocks execution.
- Strict dependence on live `state/metrics.json` can make smoke checks brittle for clean environments.

## Decisions and trade-offs
- Added `--run-kernel-for-trace-summary` as optional, not default.
- Added `--metrics-path` for deterministic fixture validation and CI-friendly checks.

## Deferred intentionally
- End-to-end kernel eligibility orchestration in this smoke script.

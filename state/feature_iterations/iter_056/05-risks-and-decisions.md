# Risks and decisions

## Risks discovered
- The fixture builder writes files under `state/.smoke_fixtures/trace_summary`; repeated runs can leave local artifacts if callers do not clean workspace outputs.

## Decisions made and trade-offs
- **Decision:** Use deterministic synthetic fixture data by default for `trace-summary` mode when kernel execution is not requested.
- **Trade-off:** This improves repeatability but no longer validates live repository metrics in default mode; live checks remain available via `--run-kernel-for-trace-summary`.

## Intentionally deferred
- Automatic fixture cleanup inside the script was deferred to keep behavior transparent and avoid deleting user-provided fixture roots.

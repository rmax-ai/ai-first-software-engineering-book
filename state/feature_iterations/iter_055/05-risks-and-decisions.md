# Risks and Decisions

## Risks discovered
- Current ledger chapter states are `hold`/`locked`, so a live end-to-end kernel refinement run is not currently available for this iteration.

## Decisions made and trade-offs
- Added phase-trace schema validation directly in `state/copilot_sdk_uv_smoke.py` to keep coverage close to existing smoke contracts.
- Used a deterministic fixture chapter (`zz-trace-smoke`) for smoke validation so the new parser checks are verifiable without changing locked chapter state.

## Intentionally deferred
- Running a successful full refinement iteration with real chapter state was deferred until at least one chapter becomes eligible.

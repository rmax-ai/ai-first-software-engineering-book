# Risks and Decisions

## Risks discovered
- The next implementation iteration may touch multiple harness surfaces (`kernel`, smoke, evals), creating cross-file coupling risk.
- Existing deterministic smoke mode naming is dense; adding new modes without pattern reuse can reduce maintainability.

## Decisions made
- Kept this iteration planning-only to satisfy the seed contract and avoid premature code churn.
- Chose a single next task focused on one end-to-end behavior slice (trace summary validation) to minimize integration risk.

## Deferred intentionally
- Any direct edits to `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, or `evals/*.yaml`.
- Broader refactors of harness architecture until the first concrete behavior slice is implemented and validated.

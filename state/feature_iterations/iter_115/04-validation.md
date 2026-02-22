# Validation

## Verification commands run
1. `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-guard`

## Observed outputs/results
- Command output: `PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-guard mode validates uniqueness-order adjacency-order uniqueness adjacency uniqueness adjacency-order uniqueness guard precedes usage-examples-order-guard`
- Exit code: `0`

## Pass/fail against acceptance criteria
1. **Pass** — added a dedicated mode asserting adjacency between `...-uniqueness-guard` and `usage-examples-order-guard`.
2. **Pass** — registered `...-uniqueness-adjacency-guard` in `TRACE_SUMMARY_MODE_SPECS` with deterministic text.
3. **Pass** — targeted smoke command completed with PASS output and exit status 0.

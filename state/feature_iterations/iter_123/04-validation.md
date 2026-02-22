# Validation

## Verification commands run
- `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-guard`

## Observed outputs/results
- `PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-guard mode validates uniqueness-order adjacency-order uniqueness adjacency uniqueness adjacency-order uniqueness adjacency uniqueness adjacency uniqueness adjacency uniqueness adjacency uniqueness adjacency guard appears exactly once`
- Process exited with code `0`.

## Pass/fail against acceptance criteria
1. PASS — Added one mode asserting newest adjacency guard appears exactly once in `TRACE_SUMMARY_MODE_SPECS`.
2. PASS — Registered new uniqueness mode with deterministic description text.
3. PASS — Targeted smoke command executed and returned expected PASS output.

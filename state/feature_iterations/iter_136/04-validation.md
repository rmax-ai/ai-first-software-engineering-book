# Validation

## Verification commands run
1. `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-guard`

## Observed output/results
- PASS: `usage-examples-duplicate-count-wrapper-helper-...-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-guard` mode validates newest uniqueness-order adjacency guard appears immediately before prior uniqueness-order adjacency guard.

## Acceptance criteria status
1. New adjacency-order runner added in `state/copilot_sdk_smoke_test.py`: **PASS**
2. New mode registered in `TRACE_SUMMARY_MODE_SPECS`: **PASS**
3. Targeted smoke mode executed with PASS output: **PASS**

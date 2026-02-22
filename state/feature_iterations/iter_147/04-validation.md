# Validation

## Verification commands run
- `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard`

## Observed outputs/results
- PASS: `...-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard` mode validates newest long-form adjacency-order guard mode appears exactly once.

## Pass/fail against acceptance criteria
1. ✅ New exact-once runner added for the newest long-form adjacency-order guard mode.
2. ✅ New `TRACE_SUMMARY_MODE_SPECS` mode registered and wired to that runner.
3. ✅ Targeted smoke mode command executed successfully with PASS output.

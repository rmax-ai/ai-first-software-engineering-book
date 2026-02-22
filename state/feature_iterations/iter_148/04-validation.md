# Validation

## Verification commands run
1. `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-newest-long-form-adjacency-order-guard-exact-once-adjacency-order-guard`
2. `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard-adjacency-order-guard-uniqueness-guard-adjacency-order-guard`

## Observed outputs/results
- PASS output confirmed the new adjacency mode enforces predecessor-index + 1 == exact-once mode index.
- PASS output also confirmed the related pre-existing long-form adjacency-order sequence guard still passes.

## Acceptance criteria check
- AC1 Pass: adjacency assertion runner exists and enforces immediate-predecessor ordering.
- AC2 Pass: `TRACE_SUMMARY_MODE_SPECS` includes the adjacency assertion mode.
- AC3 Pass: targeted smoke mode executed and passed.

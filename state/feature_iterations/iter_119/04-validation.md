# Validation

## Verification commands run
- `uv run python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-guard`

## Observed outputs/results
- `PASS: usage-examples-duplicate-count-wrapper-helper-uniqueness-order-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-order-uniqueness-adjacency-uniqueness-adjacency-uniqueness-adjacency-guard mode validates uniqueness-order adjacency-order uniqueness adjacency uniqueness adjacency-order uniqueness adjacency uniqueness adjacency uniqueness guard appears immediately before uniqueness guard`
- Process exited with code `0`.

## Pass/fail against acceptance criteria
1. PASS — Added one new adjacency mode function in `state/copilot_sdk_smoke_test.py` to assert immediate ordering between `...-uniqueness-adjacency-uniqueness-guard` and `...-uniqueness-guard`.
2. PASS — Registered the new adjacency mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic wording.
3. PASS — Targeted smoke command executed and returned expected PASS output.

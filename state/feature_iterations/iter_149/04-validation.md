# Validation

## Verification commands run
1. `python state/governance_engine.py validate`
2. `python state/copilot_sdk_smoke_test.py --mode usage-examples-duplicate-count-wrapper-helper-newest-long-form-adjacency-order-guard-exact-once-adjacency-order-guard-exact-once`

## Observed outputs/results
- Ledger validation returned `Ledger validation: pass`.
- The new alias smoke mode returned PASS and confirmed the newest long-form exact-once adjacency-order guard mode appears exactly once.

## Acceptance criteria check
- AC1 Pass: one alias smoke runner asserts the newest long-form exact-once adjacency-order guard mode appears exactly once.
- AC2 Pass: `TRACE_SUMMARY_MODE_SPECS` includes the new alias mode entry.
- AC3 Pass: the targeted smoke mode executed successfully with PASS output.

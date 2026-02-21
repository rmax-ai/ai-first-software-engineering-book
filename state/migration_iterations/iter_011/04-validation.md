# Validation

## Verification commands run
1. Python behavior script via `mcp_pylance_mcp_s_pylanceRunCodeSnippet`

## Observed outputs/results
- Script exited code 0 and printed `validation-ok`.
- Assertions verified expected extracted token totals for all tested payload shapes.
- Integer/non-negative invariants held for all cases.

## Pass/fail against acceptance criteria
- Direct usage dict extraction: **PASS**
- Event-list usage extraction: **PASS**
- Missing usage zero fallback: **PASS**
- Integer/non-negative usage invariants: **PASS**

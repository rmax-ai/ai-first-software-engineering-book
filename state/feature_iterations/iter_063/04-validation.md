# Validation

## Verification commands run
- `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-kernel`
- `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-kernel-malformed-phase`
- `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-kernel-malformed-phase-payload`
- `uv run python state/copilot_sdk_smoke_test.py --mode trace-summary-kernel-missing-phase`
- `uv run python state/copilot_sdk_smoke_test.py --mode mode-choices-coverage-guard`
- `uv run python state/copilot_sdk_smoke_test.py --mode docstring-mode-coverage-guard`

## Observed outputs/results
- `trace-summary-kernel`: **PASS** — `PASS: trace-summary-kernel mode validates fixture-backed kernel trace-summary success`.
- `trace-summary-kernel-malformed-phase`: **PASS** — `PASS: trace-summary-kernel-malformed-phase mode validates malformed phase-trace key failures`.
- `trace-summary-kernel-malformed-phase-payload`: **PASS** — `PASS: trace-summary-kernel-malformed-phase-payload mode validates non-object phase-trace payload failures`.
- `trace-summary-kernel-missing-phase`: **PASS** — `PASS: trace-summary-kernel-missing-phase mode validates missing required phase-trace failures`.
- `mode-choices-coverage-guard`: **PASS** — parser choices include newly registered modes.
- `docstring-mode-coverage-guard`: **PASS** — generated module doc includes new mode entries.

## Pass/fail against acceptance criteria
- AC1 (all four fixture-backed deterministic modes): **PASS**
- AC2 (normal success + malformed failure expectations): **PASS**
- AC3 (repository ledger immutability assertion per run): **PASS**
- AC4 (validation evidence recorded): **PASS**

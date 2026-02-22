# Validation

## Verification commands run
- `uv run python state/copilot_sdk_uv_smoke.py --mode trace-summary --run-kernel-for-trace-summary`
- `uv run python state/copilot_sdk_uv_smoke.py --mode trace-summary-malformed-phase --run-kernel-for-trace-summary`
- `uv run python state/copilot_sdk_uv_smoke.py --mode trace-summary-malformed-phase-payload --run-kernel-for-trace-summary`
- `uv run python state/copilot_sdk_uv_smoke.py --mode trace-summary-missing-phase --run-kernel-for-trace-summary`

## Observed outputs/results
- `trace-summary`: **FAIL** — `KernelError: Chapter is not eligible (status='hold').`
- `trace-summary-malformed-phase`: **FAIL** — `KernelError: Chapter is not eligible (status='hold').`
- `trace-summary-malformed-phase-payload`: **FAIL** — `KernelError: Chapter is not eligible (status='hold').`
- `trace-summary-missing-phase`: **FAIL** — `KernelError: Chapter is not eligible (status='hold').`

## Pass/fail against acceptance criteria
- AC1 (execute all four kernel-run smoke commands): **PASS**
- AC2 (record pass/fail for each command): **PASS**
- AC3 (scope limited unless bug identified): **PASS** — identified governance-state blocker, no speculative code changes made.

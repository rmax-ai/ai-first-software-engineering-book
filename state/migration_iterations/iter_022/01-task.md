# Task

## Selected task title
Stabilize deterministic `fallback-error` smoke mode to avoid intermittent connection reset failures.

## Why this task now
`iter_021/06-next-iteration.md` identified this as the highest-priority unresolved migration reliability gap.

## Acceptance criteria for this iteration
- `python state/copilot_sdk_smoke_test.py --mode fallback-error` passes reliably across repeated local runs.
- Assertion keeps validating actionable HTTP status context.
- Command exits non-zero if mapping regresses.

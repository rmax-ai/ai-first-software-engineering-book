# Task

## Selected task
Add adjacency-order smoke coverage for the newest exact-once duplicate-count mode so it must appear immediately after its paired uniqueness-guard predecessor.

## Why this task now
- `iter_147/06-next-iteration.md` explicitly prioritized this sequencing guard.
- Deterministic mode ordering prevents drift in long-form guard registration.

## Acceptance criteria
1. Ensure one smoke runner asserts predecessor-index + 1 == exact-once mode index.
2. Ensure one `TRACE_SUMMARY_MODE_SPECS` entry wires that adjacency assertion mode.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode <adjacency-mode>` and capture PASS.

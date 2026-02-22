# Task

## Selected task title
Implement phase-level structured trace logging in the kernel and validate it in smoke coverage.

## Why this task now
`state/feature_iterations/iter_054/06-next-iteration.md` prioritized structured observability first so later harness controls can rely on stable trace signals.

## Acceptance criteria
1. `state/kernel.py` writes deterministic `phase_trace` events with `phase`, `status`, `duration_ms`, and `budget_signal`.
2. `state/copilot_sdk_uv_smoke.py` validates the new phase trace signal shape.
3. Run targeted validation commands and record observed outcomes.

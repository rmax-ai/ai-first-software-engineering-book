# Next Iteration Recommendation

## Recommended task

Implement deterministic trace-summary telemetry scaffolding in `state/kernel.py` with a focused smoke assertion path in `state/copilot_sdk_uv_smoke.py`.

## Why this is next

It is the smallest high-impact implementation step from this plan: it improves observability while preserving current architecture and creates a concrete bridge between harness runtime behavior and deterministic verification.

## Acceptance criteria

1. `state/kernel.py` emits a stable, structured trace-summary payload for the latest loop execution without changing public CLI usage.
2. `state/copilot_sdk_uv_smoke.py` adds one deterministic mode validating required trace-summary keys and shape.
3. Targeted verification is executed with `uv run python state/copilot_sdk_uv_smoke.py --mode <new-mode>` and results are documented.
4. No unrelated file refactors.

## Expected files to touch

- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`

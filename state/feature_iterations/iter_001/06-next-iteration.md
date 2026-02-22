# Recommended next task

Implement deterministic trace-summary observability in `state/kernel.py` and prove it via smoke coverage.

## Why this is next
This is the smallest implementation slice that delivers immediate value from the plan: better harness visibility with measurable behavior and low interface risk.

## Acceptance criteria
- Add a deterministic trace-summary emission path in `state/kernel.py` for key chapter/run signals.
- Update `state/copilot_sdk_uv_smoke.py` with at least one mode that validates trace-summary shape/content.
- Ensure eval alignment by documenting or wiring expected trace signals against existing eval contracts (and any required YAML adjustments) without broad refactors.
- Record verification evidence with `uv run python state/copilot_sdk_uv_smoke.py --mode <new-mode>`.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml` (if contract updates are needed)
- `evals/drift-detection.yaml` (if regression checks are needed)

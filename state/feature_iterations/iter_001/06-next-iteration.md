# Recommended next iteration task

## Task
Implement deterministic trace summary instrumentation in `state/kernel.py` and wire it to smoke verification.

## Why next
- The seed plan identified observability as the highest-value feature to improve harness debuggability and eval explainability.
- This can be delivered as a minimal, testable increment without broad refactoring.

## Acceptance criteria
- Add a compact trace summary emitter in `state/kernel.py` for key loop outcomes (budget, eval pass/fail, write actions).
- Update or add a targeted harness smoke check in `state/copilot_sdk_uv_smoke.py` validating trace summary presence and stable shape.
- Update relevant eval contract(s) under `evals/` only if needed to assert new observability signals.
- Record validation evidence with explicit `uv run python ...` command output references in the new iteration folder.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml` (only if required)
- `state/feature_iterations/iter_002/*`

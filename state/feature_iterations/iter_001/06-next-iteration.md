# Next Iteration Recommendation

## Task
Add structured trace envelopes to `state/kernel.py` for loop phases (plan/change/evaluate/decide) and persist per-loop summaries to `state/metrics.json`.

## Why this is next
- It unlocks observability needed to validate later behavior changes and ties directly to deterministic execution requirements.

## Acceptance criteria
- `state/kernel.py` emits a structured trace record for each loop phase with stable keys.
- `state/metrics.json` receives per-loop summary entries without breaking existing schema consumers.
- Verification run succeeds with:
  - `uv run python state/copilot_sdk_uv_smoke.py`
  - one targeted kernel run command documented in `04-validation.md`.

## Expected files to touch
- `state/kernel.py`
- `state/metrics.json`
- `state/copilot_sdk_uv_smoke.py` (only if needed for new assertions)
- `state/feature_iterations/iter_002/04-validation.md`

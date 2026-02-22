# Next iteration recommendation

## Task
Implement deterministic trace summary guardrails in `state/kernel.py` and cover them with targeted smoke assertions.

## Why this is next
Trace shape guarantees are the highest-leverage foundation for downstream observability and eval reliability; locking schema first reduces regression risk for later role I/O and budget-control improvements.

## Acceptance criteria
- Add or refine `state/kernel.py` logic so trace-summary payload shape is explicitly validated before persistence.
- Extend `state/copilot_sdk_uv_smoke.py` with deterministic mode(s) that fail on missing/malformed trace summary entries.
- Document command evidence in the next iteration’s `04-validation.md` using `uv run python state/copilot_sdk_uv_smoke.py --mode ...`.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/0*.md`

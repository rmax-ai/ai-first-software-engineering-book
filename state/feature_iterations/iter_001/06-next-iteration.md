# Recommended next task

## Task
Implement deterministic trace-summary observability in `state/kernel.py` and validate via smoke coverage.

## Why this is next
- It is the highest-impact feature from the seed plan and directly improves harness transparency.
- It can be validated with focused changes to smoke tests and eval guard expectations.

## Acceptance criteria
- Add a minimal trace-summary emitter path in `state/kernel.py` with stable output shape.
- Extend `state/copilot_sdk_uv_smoke.py` with one deterministic mode that asserts the new trace summary shape.
- Update relevant eval contract(s) under `evals/` only if required to gate the new behavior.
- Run `uv run python state/copilot_sdk_uv_smoke.py --mode <new-mode>` and record pass/fail evidence.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml` (if gating update is required)
- `state/feature_iterations/iter_002/*.md`

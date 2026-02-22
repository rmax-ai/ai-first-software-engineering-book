# Recommended next task

## Task
Implement deterministic trace logging scaffolds in `state/kernel.py` with matching smoke assertions in `state/copilot_sdk_uv_smoke.py`.

## Why this is next
- Observability is the highest-leverage foundation for subsequent harness controls and easier regression diagnosis.
- It directly follows the seed plan and can be validated with targeted smoke execution.

## Acceptance criteria
- Add a minimal, structured trace output path in `state/kernel.py` for key loop checkpoints.
- Update `state/copilot_sdk_uv_smoke.py` with at least one assertion that verifies the new trace signal.
- Run `uv run python state/copilot_sdk_uv_smoke.py` and record pass/fail evidence in iteration artifacts.
- Keep diffs minimal and avoid public interface breakage.

## Expected files to touch
- `state/kernel.py`
- `state/copilot_sdk_uv_smoke.py`
- `state/feature_iterations/iter_002/03-execution.md`
- `state/feature_iterations/iter_002/04-validation.md`

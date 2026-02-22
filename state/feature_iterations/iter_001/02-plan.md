# Plan

1. Audit current harness surfaces to target: `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, and eval contracts under `evals/`.
2. Define feature backlog:
   - Add richer trace logging hooks in `state/kernel.py` around loop stages and tool execution summaries.
   - Tighten role-IO template scaffolds in `state/role_io_templates.py` for deterministic role contracts.
   - Extend smoke orchestration in `state/copilot_sdk_uv_smoke.py` with explicit assertions for new trace fields.
3. Define test strategy:
   - Use `uv run python state/copilot_sdk_uv_smoke.py` as integration gate.
   - Add targeted unit tests for any new pure helpers in `state/`.
4. Define evaluation strategy:
   - Map new trace outputs to existing eval checks and update `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, or `evals/drift-detection.yaml` only when required.
   - Confirm `state/metrics.json` signals stay consistent after changes.
5. Sequence implementation into smallest next task: trace-summary observability in kernel plus smoke assertions.

## Expected files to change in later iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`

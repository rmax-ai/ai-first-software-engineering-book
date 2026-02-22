# Plan

1. Confirm governance and execution inputs from `DEVELOPMENT.md` and this iteration prompt.
2. Define planned feature work for `state/kernel.py`:
   - richer deterministic trace logging around loop phases and failure edges,
   - explicit execution constraints and guardrail reporting outputs.
3. Define planned scaffolding work for `state/role_io_templates.py`:
   - clearer role-specific IO templates with stricter required sections for planner/writer/critic exchanges.
4. Define planned validation work for `state/copilot_sdk_uv_smoke.py`:
   - targeted smoke cases that prove new observability and deterministic behavior.
5. Define planned eval updates for `evals/*.yaml`:
   - add or tighten checks that detect missing trace signals and regressions in harness guarantees.
6. Sequence the backlog so the next iteration executes one smallest vertical slice first, then validates via `uv run` commands and eval contracts.

## Expected files in later implementation iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`

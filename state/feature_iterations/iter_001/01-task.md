# Task: Plan custom state harness improvements

## Why this task now
- The seed iteration in `prompts/incremental-improvements/execute.md` requires a planning-only pass before implementation work.
- A concrete backlog is needed to guide focused follow-up changes in `state/` and `evals/` without broad refactors.

## Acceptance criteria
1. The plan covers targeted **features** for the harness, including observability and deterministic controls.
2. The plan defines **tests** that validate each feature with explicit commands/targets.
3. The plan maps **evaluations** to concrete `evals/*.yaml` and harness signals (`state/metrics.json`, iteration artifacts).
4. The scope is planning-only and names expected follow-up files:  
   `state/kernel.py`, `state/role_io_templates.py`, `state/copilot_sdk_uv_smoke.py`, `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, `evals/drift-detection.yaml`.

# Task: Plan custom state harness improvements

## Why this task now
- `state/feature_iterations/` had no prior iterations, so the seed iteration must establish a concrete backlog.
- `DEVELOPMENT.md` prioritizes deterministic harness behavior in `state/` and explicit eval-driven validation, which needs a single coordinated plan before implementation work.

## Acceptance criteria
- Document a concise improvement plan covering:
  - feature upgrades for `state/kernel.py` and `state/role_io_templates.py`,
  - smoke/unit verification expectations tied to `state/copilot_sdk_uv_smoke.py`,
  - regression detection alignment with `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml`.
- Define one next implementation task with concrete acceptance criteria and expected files to touch.

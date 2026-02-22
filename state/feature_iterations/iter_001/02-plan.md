# Plan

1. Inspect `DEVELOPMENT.md` and existing harness surfaces to align constraints.
2. Define feature workstreams:
   - `state/kernel.py`: trace logging fields, deterministic loop controls, failure visibility.
   - `state/role_io_templates.py`: clearer role input/output contract scaffolds.
   - `state/copilot_sdk_uv_smoke.py`: deterministic smoke scenarios for new controls.
3. Map tests:
   - Add/extend targeted unit tests for kernel helper logic and role template validation.
   - Add smoke coverage with `uv run python state/copilot_sdk_uv_smoke.py` modes for new behavior.
4. Map evaluations:
   - Validate outputs against `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml`.
   - Confirm expected telemetry shape updates in `state/metrics.json` and iteration logs.
5. Sequence follow-up implementation to keep diffs small and verifiable.

## Expected files to change in later iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
- Harness test assets under `state/` and/or `book/`

# Plan

1. Map current harness constraints from `DEVELOPMENT.md` and existing `state/` architecture to keep proposals deterministic and minimal-risk.
2. Define feature work in `state/kernel.py`:
   - add richer trace logging checkpoints (loop step, guard decisions, eval outcomes),
   - add deterministic execution controls (explicit budget/step telemetry fields),
   - preserve current public CLI behavior.
3. Define scaffolding updates in `state/role_io_templates.py`:
   - tighten role I/O templates for clearer tool/result boundaries,
   - add explicit placeholders for validation/evidence capture.
4. Define targeted smoke coverage in `state/copilot_sdk_uv_smoke.py`:
   - extend smoke modes to assert trace fields and deterministic guard ordering,
   - keep mode-level tests isolated for quick `uv run` execution.
5. Define eval integration in `evals/*.yaml`:
   - connect new trace/evidence signals to existing chapter-quality/style/drift gates,
   - document expected pass/fail signals and non-goals.
6. Sequence future iterations as minimal vertical slices:
   - slice 1: kernel trace schema,
   - slice 2: role I/O template alignment,
   - slice 3: smoke + eval contract tightening.

## Expected files to change in future iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`
- (if required) targeted test assets under `state/` or `book/`.

# Iteration plan

1. Baseline current harness surfaces in `state/kernel.py`, `state/role_io_templates.py`, and `state/copilot_sdk_uv_smoke.py`.
2. Define feature backlog themes:
   - richer trace/event observability in kernel runs,
   - stricter deterministic execution controls and budgets,
   - clearer role I/O scaffolds and prompt-contract visibility.
3. Map each feature theme to executable tests:
   - targeted unit-style checks for pure helpers in `state/kernel.py`,
   - smoke coverage in `state/copilot_sdk_uv_smoke.py` via `uv run python state/copilot_sdk_uv_smoke.py`,
   - focused scaffold assertions for `state/role_io_templates.py`.
4. Map each feature theme to eval/regression gates:
   - `evals/chapter-quality.yaml`,
   - `evals/style-guard.yaml`,
   - `evals/drift-detection.yaml`,
   - expected signals recorded in `state/metrics.json`.
5. Queue one smallest next implementation task that only adds trace-summary observability scaffolding in `state/kernel.py` plus smoke assertions.

## Files expected to change in later iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`

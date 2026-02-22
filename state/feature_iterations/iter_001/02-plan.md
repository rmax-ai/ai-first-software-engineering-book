# Iteration plan

1. Audit harness requirements from `DEVELOPMENT.md` and current `state/` layout.
2. Draft feature backlog items:
   - Add richer deterministic trace summaries and loop self-evaluation logging in `state/kernel.py`.
   - Tighten role-IO contract scaffolds and coverage hooks in `state/role_io_templates.py`.
   - Extend smoke harness assertions in `state/copilot_sdk_uv_smoke.py` for new trace and contract signals.
3. Draft verification backlog:
   - `uv run python state/copilot_sdk_uv_smoke.py`
   - Targeted kernel runs: `uv run python state/kernel.py --chapter-id <id>`
   - Focused tests for role-IO template invariants (to be added in later iteration).
4. Draft eval backlog integration:
   - Map expected impacts to `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml`.
   - Define metric checks to confirm expected counters/signals in `state/metrics.json`.
5. Package backlog into next iteration guidance with one smallest executable task.

## Expected files to change in later iterations
- `state/kernel.py`
- `state/role_io_templates.py`
- `state/copilot_sdk_uv_smoke.py`
- `evals/chapter-quality.yaml`
- `evals/style-guard.yaml`
- `evals/drift-detection.yaml`

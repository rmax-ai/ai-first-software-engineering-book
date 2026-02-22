# Plan custom state harness improvements

## Why this task now
- `prompts/incremental-improvements/execute.md` seeds iteration one as planning-only work.
- The harness in `state/` needs a concrete backlog tying features to tests and eval gates before implementation.
- A scoped plan reduces risk before changing core orchestration in `state/kernel.py`.

## Acceptance criteria
1. Document concise feature proposals for harness behavior, observability, and execution controls.
2. Define targeted tests that validate the proposed features (including smoke coverage).
3. Define evaluation mapping to existing `evals/*.yaml` and harness signals (`state/metrics.json`/iteration evidence).
4. Identify concrete files likely to change in follow-up implementation iterations.

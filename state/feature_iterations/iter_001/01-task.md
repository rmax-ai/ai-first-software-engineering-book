# Task: Plan custom state harness improvements

## Why this task now

`prompts/incremental-improvements/execute.md` defines a seed iteration that must establish a concrete backlog before implementation work begins. A focused planning iteration de-risks later edits to kernel orchestration, role IO scaffolds, smoke coverage, and eval contracts.

## Acceptance criteria

1. The plan explicitly proposes harness feature improvements in `state/` with concrete intended behaviors.
2. The plan defines targeted tests to validate those behaviors, including `uv run python state/copilot_sdk_uv_smoke.py`.
3. The plan defines evaluation/regression checks tied to `evals/*.yaml` and expected signals such as `state/metrics.json`.
4. The iteration delivers all required artifacts (`01` through `07`) and recommends exactly one next task.

# Task: Plan custom state harness improvements

## Why this task now
- This repository has no prior feature iteration artifacts, so the first iteration must establish a clear, executable backlog.
- A focused plan reduces implementation risk across `state/kernel.py`, role IO scaffolds, smoke coverage, and eval contracts.

## Acceptance criteria
1. Define concrete feature improvements for harness observability, controls, and deterministic behavior.
2. Define targeted tests for each proposed feature, including smoke or unit-level verification entry points.
3. Define eval alignment so regressions are detectable via existing `evals/*.yaml` contracts and harness metrics signals.
4. Provide a single next implementation task with explicit files and pass/fail checks.

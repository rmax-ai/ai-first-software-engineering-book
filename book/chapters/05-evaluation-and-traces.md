# Chapter 05 — Evaluation and Traces

## Thesis
Evaluation and traceability are the mechanisms that make AI-first engineering reproducible. Traces allow attribution; evaluations enforce correctness gates.

Hypothesis: without trace-first design, teams cannot reliably distinguish model errors from tool errors, harness errors, or missing tests.

## Why This Matters
- Reproducibility is a prerequisite for iterative improvement.
- Evaluation gates define the autonomy envelope and prevent silent regressions.
- Traces enable post-incident analysis and systematic harness refinement.

## System Breakdown
- **Trace schema** (minimum viable):
  - task id, plan, tool calls, outputs, diffs, evaluation results, budgets, stop reason.
- **Evaluation types**:
  - correctness: unit/integration/contract tests.
  - safety: permission checks, protected paths, secret scanning.
  - quality: lint, type checks, formatting, doc checks.
  - performance: benchmarks, latency/cost budgets.
- **Gating model**: which evaluations are required for which action classes.

## Concrete Example 1
Tracing a refactor.
- Record: each patch + test run + failure signature.
- Use: compare traces across runs to identify where the harness improved outcomes.

## Concrete Example 2
Drift detection for an agent loop.
- Maintain: a stable eval suite and a small set of “golden” tasks.
- Detect: changes in iteration counts, regression rate, and stop reasons over time.

## Trade-offs
- More evaluation increases confidence but costs time and compute.
- Rich traces help debugging but create storage and privacy burdens.
- Overly rigid gates can block progress on codebases with weak test coverage.

## Failure Modes
- **Eval gaming**: optimizing for metrics while harming real-world quality.
- **Blind spots**: evaluations do not cover critical behaviors.
- **Un-actionable traces**: logs exist but lack structure, making search and attribution hard.

## Research Directions
- Standard trace formats for portability across tools and models.
- Risk-based gating (stricter checks for higher-risk diffs).
- Low-cost evaluations that correlate with production outcomes.

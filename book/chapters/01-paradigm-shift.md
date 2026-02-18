# Chapter 01 — Paradigm Shift

## Thesis
AI-first software engineering is an architectural inversion: machine reasoning becomes a primary execution substrate, and the harness (tools, constraints, evaluation, traceability) becomes the primary design surface.

This chapter’s claim is a hypothesis: many observed “capability” gains in practice are attributable to harness engineering rather than model changes.

## Why This Matters
- Without a clear boundary between model capability and harness capability, teams misattribute failures and waste effort.
- Reliability depends on reproducible loops (plan → act → verify) rather than isolated prompts.
- Production constraints (auditability, security, cost, regression control) require system design, not “prompting.”

## System Breakdown
- **Actors**: human governor, agent loop, tools/runtime, evaluation/CI.
- **Artifacts**: specs, plans, diffs, traces, eval results, decision records.
- **Invariants** (hypotheses to test):
  - Every non-trivial change is traceable to a plan and verified by checks.
  - The system can attribute regressions to a layer (prompt, tool, code, eval).
  - Autonomy is gated by evaluations and budgets.

## Concrete Example 1
Refactor a small library function using an agent loop.
- Inputs: failing unit test + desired behavior specification.
- Loop: propose patch → run tests → inspect diff → stop on pass.
- Observation to record: how many iterations until pass; whether failures were tool-induced, spec-induced, or model-induced.

## Concrete Example 2
Ship a minor API change in a production service.
- Inputs: API contract + backward-compat constraints + staging environment.
- Loop: generate migration plan → implement → run contract tests → produce trace report → human approve.
- Observation to record: whether the harness prevented unsafe changes (e.g., editing protected files, skipping tests).

## Trade-offs
- Strong harness constraints reduce freedom (and sometimes speed) but increase reproducibility.
- More evaluation gates reduce regressions but add compute and latency.
- Trace-heavy workflows improve debugging but increase storage and privacy considerations.

## Failure Modes
- **Illusion of capability**: improvements credited to the model when they come from better tooling/evals.
- **Unbounded autonomy**: loops run without budgets, causing tool thrash and unclear outcomes.
- **Non-attributable failures**: missing traces make regressions un-debuggable.

## Research Directions
- Metrics that separate model improvements from harness improvements.
- Minimal trace schema that supports attribution and replay.
- Formal definitions of autonomy envelopes and stop conditions.

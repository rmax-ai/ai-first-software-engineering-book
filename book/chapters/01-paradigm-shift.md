# Chapter 01 — Paradigm Shift

## Thesis
AI-first software engineering is an architectural inversion: machine reasoning becomes a primary execution substrate, and the harness (tools, constraints, evaluation, traceability) becomes the primary design surface.

The inversion is practical: reliability comes from constraints, evaluations, and traces that turn generated changes into a repeatable, testable loop.

A concrete, testable implication: holding the model constant, improving the harness should predictably reduce iteration count, increase pass rates, and improve failure attribution more than “prompt tweaks” alone.

Operational definition:
- **Model capability** changes when you swap models while holding tools, constraints, and evaluation constant.
- **Harness capability** changes when you keep the model constant but alter tools, policies, evaluation gates, or trace capture.

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
- **Measurable signals** (to separate model vs harness effects):
  - *Iterations-to-pass*: number of propose→verify cycles until all required checks pass.
  - *Time-to-green*: wall-clock time from first attempt to passing evaluation gates.
  - *Attribution rate*: fraction of failures with a clear primary cause (prompt/spec vs tool/runtime vs code vs eval).
- **Attribution checklist** (what evidence makes a failure “belong” to a layer):
  - **Spec/prompt**: requirement is ambiguous or contradictory; different reasonable interpretations change expected output; clarifying text resolves the failure without code changes.
  - **Tool/runtime**: tool errors, timeouts, missing permissions, flaky environment, or nondeterministic command outputs; rerun under identical inputs yields different results.
  - **Code**: deterministic failing tests or typechecks tied to a specific diff; reverting the diff restores the previous behavior.
  - **Eval/CI**: mismatch between what is asserted and what is intended; tests are incorrect, overly strict, or missing a required case; fixing the test changes outcomes without changing product behavior.

## Concrete Example 1
Refactor a small library function using an agent loop.
- Inputs: failing unit test + desired behavior specification (e.g., a short “Given/When/Then” note checked into the repo).
- Loop: propose patch → run tests → inspect diff → record trace (commands + outputs) → stop on pass.
- Measured outputs:
  - Iterations-to-pass and time-to-green.
  - Diff size (files touched, lines changed) and whether changes are localized to the intended function.
  - Failure attribution per iteration (spec/prompt vs tool/runtime vs code vs eval) using the checklist above.
- Stop rule:
  - Stop when the originally failing unit test passes, the full unit test suite passes, and the diff is constrained to the intended surface area.
  - If the loop reaches a fixed budget (e.g., N iterations or T minutes) without progress, stop and escalate to a human with the trace and the smallest reproducible failing case.

## Concrete Example 2
Ship a minor API change in a production service.
- Inputs: API contract + backward-compat constraints + staging environment + a defined rollout/rollback policy.
- Loop: generate migration plan → implement → run contract tests → produce trace report (diff + commands + results) → human approve.
- Measured outputs:
  - Iterations-to-pass and time-to-green (from first migration-plan draft to all required checks passing in staging).
  - Attribution rate per iteration using the checklist above (spec/prompt vs tool/runtime vs code vs eval).
  - Backward-compat outcomes: number of contract-test failures introduced, and whether rollback was exercised successfully in staging.
- Guardrails:
  - Protected paths or modules that require explicit human review before edits (e.g., auth, billing, infra).
  - Required checks (contract tests, integration tests, lint/typecheck, and a staging smoke test).
  - Rollback plan defined up front (feature flag, config switch, or revert procedure) and verified in staging.
  - Approval gate: no deploy until a human reviews the migration plan, the diff, and the evaluation results.
- Stop rule:
  - Stop when all required checks pass in staging, the migration plan is consistent with backward-compat constraints, and the trace report can explain every material change.
  - If any guardrail is violated (protected file touched, required test skipped, rollback unclear), stop immediately and require human intervention.

## Trade-offs
- Strong harness constraints reduce freedom (and sometimes speed) but increase reproducibility.
- More evaluation gates reduce regressions but add compute and latency.
- Trace-heavy workflows improve debugging but increase storage and privacy considerations.

## Failure Modes
- **Illusion of capability**: improvements credited to the model when they come from better tooling/evals.
- **Unbounded autonomy**: loops run without budgets, causing tool thrash and unclear outcomes.
- **Non-attributable failures**: missing traces make regressions un-debuggable.

Synthesis: if machine reasoning is treated as an execution substrate, reliability depends less on a “better prompt” and more on the harness that constrains and verifies outputs. Evaluation gates and budgets convert open-ended generation into a bounded loop with stop conditions. Traceability plus an attribution checklist makes failures actionable: you can separate prompt/spec issues from tool/runtime issues from code regressions from eval defects. Under this view, model selection still matters, but it is secondary within a harness-defined capability envelope.

## Research Directions
- Metrics that separate model improvements from harness improvements.
- Minimal trace schema that supports attribution and replay.
- Formal definitions of autonomy envelopes and stop conditions.

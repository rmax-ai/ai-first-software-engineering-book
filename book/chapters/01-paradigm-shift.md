# Chapter 01 — Paradigm Shift

## Thesis
AI-first software engineering is an architectural inversion. Machine reasoning becomes a primary execution substrate. The harness—tools, constraints, evaluation, and traceability—becomes the primary design surface.

This inversion is practical. Reliability comes from constraints, evaluations, and traces that turn generated changes into a repeatable loop.

A concrete, testable implication (holding the model constant):
1. A stronger harness should reduce *iterations-to-pass*.
2. A stronger harness should reduce *time-to-green*.
3. A stronger harness should increase *attribution rate* (more failures have a primary cause you can act on).

Operational definition:
- **Model capability** changes when you swap models while holding tools, constraints, and evaluation constant.
- **Harness capability** changes when you keep the model constant but alter tools, policies, evaluation gates, or trace capture.

This chapter’s claim is a hypothesis: some observed “capability” gains in practice are attributable to harness engineering rather than model changes.

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

A diagram helps here because the key distinction (model vs harness) affects evidence flow. It shows where traces are captured and where evaluation gates run. Focus on the attribution step and what it consumes.

```mermaid
flowchart TB
  P[Plan\n(spec + intent)] --> A[Act\n(generate patch)]
  A --> T[Tools/Runtime\n(apply diff, run commands)]
  T --> V[Verify\n(evaluation gates)]
  V --> D{All checks pass?}
  D -- yes --> S[Stop\nship / merge]
  D -- no --> X[Attribute failure\n(spec vs tool vs code vs eval)]
  X --> P

  A -. records .-> TR[(Trace)]
  T -. records .-> TR
  V -. records .-> TR
  X -. uses .-> TR
```

Legend:
- **Solid arrows** are the operational loop (plan → act → verify).
- **Dashed arrows** are trace capture and trace usage.

Takeaway: if you cannot produce a trace, attribution is guesswork. You will not know if the fix is spec/prompt, tool/runtime, code, or eval/CI.

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
- Minimal trace record (copyable):
  - Inputs:
    - Spec note path: `docs/specs/parse-date.md` (example)
    - Failing test: `tests/test_parse_date.py::test_rejects_empty`
  - Commands run (in order): `pytest -q`, `ruff check .` (example)
  - Diff identifier: commit SHA or patch ID (e.g., `abc1234`)
  - Evaluation outputs: failing test names, exit codes, and relevant logs (first failing assertion)
  - Attribution decision: one of {spec/prompt, tool/runtime, code, eval/CI} + 1–2 sentences of evidence
    - Example: **code** — test fails deterministically after the diff; reverting the diff restores pass.
- Measured outputs:
  - Iterations-to-pass and time-to-green.
  - Diff size (files touched, lines changed) and whether changes are localized to the intended function.
  - Failure attribution per iteration (spec/prompt vs tool/runtime vs code vs eval) using the checklist above and recorded in the trace record.
- Stop rule:
  - Stop when the originally failing unit test passes, the full unit test suite passes, and the diff is constrained to the intended surface area.
  - If the loop reaches a fixed budget (e.g., N iterations or T minutes) without progress, stop and escalate to a human with the trace record and the smallest reproducible failing case.

## Concrete Example 2
Ship a minor API change in a production service.
- Inputs: API contract + backward-compat constraints + staging environment + a defined rollout/rollback policy.
- Loop: generate migration plan → implement → run contract tests → produce trace report (diff + commands + results) → human approve.
- Minimal trace report (copyable):
  - Inputs:
    - Contract/version: `openapi.yaml` (example) + “compatible within v1.x”
    - Backward-compat constraints: “no required fields added; no behavior change on existing endpoints”
    - Staging target: `staging-us-east-1` (example)
  - Commands run (in order, example commands): `make contract-test`, `npm run lint`, `npm run typecheck`, `./scripts/staging-smoke.sh`
  - Diff identifier: PR number + commit SHA (e.g., `PR #482`, `def5678`)
  - Evaluation outputs: failing checks, links/paths to logs, and timestamps (supports time-to-green)
  - Attribution decisions (per failure): {spec/prompt, tool/runtime, code, eval/CI} + evidence
    - Example: **eval/CI** — contract test rejects an allowed optional field; fixing the assertion changes outcomes without changing API behavior.
- Measured outputs:
  - Iterations-to-pass and time-to-green (from first migration-plan draft to all required checks passing in staging).
  - Attribution rate per iteration using the checklist above (spec/prompt vs tool/runtime vs code vs eval).
  - Backward-compat outcomes: number of contract-test failures introduced, and whether rollback was exercised successfully in staging.
- Guardrails:
  - Protected paths or modules that require explicit human review before edits (e.g., auth, billing, infra).
  - Required checks (contract tests, integration tests, lint/typecheck, and a staging smoke test).
  - Rollback plan defined up front (feature flag, config switch, or revert procedure) and verified in staging.
  - Approval gate: no deploy until a human reviews the migration plan, the diff, and the evaluation results.
  - Mapping: Guardrails define *what must be protected*, required checks define *what must be proven*, and the approval gate defines *who must accept the evidence* before deploy.
- Stop rule:
  - Stop when all required checks pass in staging, the migration plan is consistent with backward-compat constraints, and the trace report can explain every material change.
  - If the loop reaches a fixed budget (e.g., N iterations or T minutes) without progress, stop and escalate to a human with the trace report and the smallest reproducible failing case.
  - If any guardrail is violated (protected file touched, required test skipped, rollback unclear), stop immediately and require human intervention.

## Trade-offs
- Strong harness constraints reduce freedom (and sometimes speed) but increase reproducibility.
- More evaluation gates reduce regressions but add compute and latency.
- Trace-heavy workflows improve debugging but increase storage and privacy considerations.

## Failure Modes
- **Illusion of capability**: improvements credited to the model when they come from better tooling/evals.
- **Unbounded autonomy**: loops run without budgets, causing tool thrash and unclear outcomes.
- **Non-attributable failures**: missing traces make regressions un-debuggable.

Synthesis: treat machine reasoning as an execution substrate, and treat the harness as the primary lever for reliability. Track *iterations-to-pass*, *time-to-green*, and *attribution rate* to separate harness effects from model effects and to make failures actionable.

## Research Directions
- Metrics that separate model improvements from harness improvements.
- Minimal trace schema that supports attribution and replay.
- Formal definitions of autonomy envelopes and stop conditions.

# Chapter 02 — Harness Engineering

## Thesis
Harness engineering is the discipline of turning a general-purpose model into a predictable system by defining tool contracts, constraints, loop control, and evaluation gates.

Hypothesis: for many engineering tasks, harness changes yield larger quality improvements than swapping models within a similar capability class.

## Why This Matters
- The same model can behave reliably or unreliably depending on tool schemas, budgets, and verification.
- Teams can standardize harness practices even when models change.
- Production safety and auditability primarily live in the harness layer.

## System Breakdown
- **Control plane**: prompts, policies, budgets, stop conditions.
- **Tool plane**: filesystem edits, build/test runners, linters, browsers, APIs.
- **Evaluation plane**: checks as gates; regression suites; quality rubrics.
- **State plane**: task ledger, traces, decisions, artifacts.
- **Interfaces**:
  - Tool schemas and error contracts.
  - Patch discipline (diff-only, small changes).
  - Evaluation API (what constitutes pass/fail).

## Concrete Example 1
Design a tool contract for “apply patch” operations.
- Require: explicit file paths; minimal diffs; no unrelated formatting.
- Add failure handling: on patch conflict, rebase with fresh context rather than force overwrite.
- Evaluate: measure revert rate and diff locality.

## Concrete Example 2
Add an evaluation gate to an agent loop.
- Gate: unit tests + static checks before any PR-ready output.
- Budget: maximum iterations/time; stop on repeated failures.
- Trace: capture tool outputs and diffs per iteration.

## Trade-offs
- Richer tool schemas reduce ambiguity but raise integration cost.
- Strict budgets prevent runaway loops but can truncate legitimate work.
- Strong gates improve safety but may block progress on tasks lacking tests.

## Failure Modes
- **Schema underspecification**: tools accept ambiguous inputs, producing inconsistent outcomes.
- **Over-permissive harness**: agents change broad parts of the repo with weak verification.
- **Gate bypass**: humans accept outputs without running checks, breaking the feedback loop.

## Research Directions
- Harness quality metrics (iteration efficiency, regression rate, reproducibility).
- Tool error taxonomies that guide automated recovery.
- Portable harness templates across languages and repo types.

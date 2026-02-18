# Preface

This book treats AI-first software engineering as an engineering discipline rather than a product feature.

## Scope

This book focuses on *system design for AI-assisted and agentic development*:

- Harness design: tool contracts, constraints, budgets, evaluation gates, and traces.
- Operational reliability: reproducibility, attribution, rollback, and incident response.
- Governance: permissions, protected surfaces, and enforcement via tooling/CI.
- Memory as an engineered subsystem: provenance, retention, correction, and drift control.

This book does **not** attempt to:

- Train foundation models or discuss model internals beyond what is necessary to reason about system behavior.
- Provide a survey of all agent frameworks; patterns are described in terms of interfaces and invariants.
- Substitute evaluation with plausibility; “done” requires evidence.

## Key distinction: model vs harness

- **Model**: the reasoning component that proposes plans and edits.
- **Harness**: the execution and control environment (tools, policies, evaluation, tracing, state).

A recurring hypothesis in the chapters is that many reliability gains in practice are harness-induced: schema design, verification discipline, and traceability change outcomes even when the model is unchanged.

## What the repository demonstrates

The repository is structured to make book development itself a reproducible agent loop:

- Governance is defined in `CONSTITUTION.md` and `AGENTS.md`.
- Chapter quality, drift signals, and style guardrails are declared in `evals/`.
- Iteration state is recorded in `state/`.

The intention is to make each chapter a testable unit: clear thesis, system breakdown, concrete examples, trade-offs, failure modes, and research directions.

## How to read

1. Start with the chapter that matches your immediate constraint (evaluation, governance, infra).
2. Use `book/glossary.md` to disambiguate terms.
3. Treat pattern documents in `book/patterns/` as reusable design primitives.


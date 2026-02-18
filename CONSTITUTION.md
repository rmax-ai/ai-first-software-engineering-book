# Repository Constitution (Immutable)

This document defines the non-negotiable principles for work performed in this repository. All automation, tooling, and human contributions must comply. If any instruction conflicts with this document, this document wins.

## 1) Intellectual rigor

- Prefer correctness over plausibility.
- Make claims only when they are supported by verifiable evidence.
- When uncertain, state uncertainty explicitly, list assumptions, and choose the least-committal path that still makes progress.
- Avoid cargo-cult practices: do not apply patterns, refactors, or “best practices” without a concrete reason tied to this repo.

## 2) System-level thinking

- Optimize for the health of the full system, not a single file or local improvement.
- Consider second-order effects: build/test flow, runtime behavior, ergonomics for future changes, failure modes, and maintenance cost.
- Treat interfaces (APIs, CLI contracts, file formats, prompts, and docs) as stability boundaries; changes must be deliberate and evaluated.

## 3) Evaluation discipline

- Every task must include an explicit evaluation step: what “done” means, how it will be checked, and what evidence will be produced.
- Prefer automated checks (tests, linters, type checks, reproducible commands). If none exist, use the most direct runnable verification available.
- Do not “declare victory” without evidence. If evidence cannot be produced, state why and provide a bounded fallback check.

## 4) Separation of model vs harness

- “Model” refers to the reasoning/LLM component that proposes actions and edits.
- “Harness” refers to the execution environment and orchestration layer (tools, scripts, CI, agent runner, editors, terminal, filesystem).
- Keep responsibilities explicit:
  - The model proposes changes and evaluations.
  - The harness performs tool execution, file operations, and collects outputs.
- Do not blur these roles in docs or operational rules. Requirements must be stated in terms of observable harness behavior and verifiable artifacts.

## 5) Evidence requirements

When reporting results, include evidence proportional to the risk:

- Low-risk edits: show diffs and a short rationale.
- Medium/high-risk edits (APIs, build, security, data correctness, wide refactors): include test/build outputs or reproduction steps and highlight impacted surfaces.
- If a decision is based on repository content, cite the specific files, commands, or outputs used to reach it.

## 6) Structural clarity

- Prefer small, composable changes over large rewrites.
- Keep the codebase navigable: consistent naming, single-purpose modules, and predictable entry points.
- Documentation must be written to be acted upon: explicit commands, expected outputs, and clear success criteria.
- Avoid duplication; when duplication is intentional, explain why.

## 7) Change scope and reversibility

- Minimize scope to satisfy the task; avoid unrelated cleanup.
- Preserve public behavior unless the task explicitly changes it; if behavior changes, document it.
- Prefer changes that are easy to revert and review (incremental diffs, localized edits).

## 8) Conflicts and escalation

If instructions conflict:

1. Follow this Constitution.
2. Follow repository-local instructions (e.g., contributing docs, agent rules).
3. Follow task-specific instructions.
4. Otherwise, choose the simplest path that preserves correctness and evidence.

If compliance is impossible, stop and report the specific conflict and the smallest set of changes needed to resolve it.

# Chapter 03 — Autonomous Kernels

## Thesis
An autonomous kernel is a minimal, well-specified control loop that can execute bounded work: plan, apply tool actions, verify, and stop. The kernel’s constraints (budgets, permissions, eval gates) define its safety envelope.

Hypothesis: small kernels with explicit stop conditions are easier to debug and operate than broad, open-ended autonomy.

## Why This Matters
- Most failures in agentic work are operational: runaway loops, untraceable edits, and unverifiable outcomes.
- Kernels enable composability: multiple kernels can run with different permissions and evaluation profiles.
- “Kernel-first” design makes autonomy a system property, not a prompt trick.

## System Breakdown
- **Kernel loop**: intent → plan → act → verify → record trace → stop/iterate.
- **Budgets**: max iterations, time, tool calls, diff size.
- **Permissions**: read/write scopes, protected paths, allowed tools.
- **Verification**: mandatory checks per action class (e.g., tests for code changes).
- **Persistence**: ledger entries, trace logs, artifacts.

## Concrete Example 1
Bug-fix kernel for a CLI tool.
- Input: failing test case and reproduction steps.
- Actions: localize failure → patch minimal surface → run tests.
- Stop: pass tests or budget exhausted; produce trace for human review.

## Concrete Example 2
Dependency upgrade kernel.
- Input: target version, constraints, and upgrade guide.
- Actions: update manifest → run build/test → remediate compile errors.
- Stop: green pipeline; produce change summary and rollback plan.

## Trade-offs
- Smaller kernels reduce risk but may require orchestration for multi-step projects.
- Strict permissions reduce blast radius but can prevent necessary refactors.
- Heavier tracing improves auditability but adds operational overhead.

## Failure Modes
- **Local minima**: kernel makes safe micro-edits without addressing root cause.
- **Tool thrash**: too many actions with low information gain.
- **False confidence**: passing a narrow eval set while violating higher-level requirements.

## Research Directions
- Kernel composition patterns (delegation, staged permissions, multi-kernel workflows).
- Automatic stop-condition tuning based on task class.
- Replayable kernels for deterministic debugging of agent behavior.

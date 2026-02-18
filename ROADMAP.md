# Roadmap — AI-First Software Engineering

This roadmap treats each chapter as a falsifiable research unit: a hypothesis, a set of architectural questions, known open problems, and concrete artifacts (diagrams, patterns, benchmarks) that make the claims testable.

## Chapter 01 — Paradigm Shift

### Research hypothesis
AI-first engineering becomes reliable when we treat *harness + tooling + evaluation* as the primary performance lever, and treat model selection as secondary within a bounded capability envelope.

### Key architectural questions
- What is the minimal “AI-first” system boundary (what must be externalized into the harness vs kept in the model context)?
- Which responsibilities belong to the human (governance) vs the system (automation) vs the model (inference)?
- What invariants distinguish an AI-first loop from “LLM-assisted” development (traceability, determinism constraints, evaluation gates)?
- Where does autonomy live: within an agent loop, within CI, within runtime systems, or in all three?

### Open problems
- Separating apparent capability gains from harness-induced improvements.
- Defining “done” for reasoning-heavy work where correctness is probabilistic.
- Characterizing failure surfaces (mis-specification vs tool error vs model error vs evaluation gaps).

### Expected artifacts
- Diagrams: lifecycle map of AI-first development (intent → plan → tool execution → verification → trace → iteration).
- Patterns: “harness-is-product” framing; “evaluation-gated autonomy.”
- Benchmarks: before/after harness interventions (same model, same tasks).

---

## Chapter 02 — Harness Engineering

### Research hypothesis
Most reliability gains come from harness design: tool schemas, constraints, loop control, error handling, and evaluation integration.

### Key architectural questions
- What is the minimal harness interface (tools, file operations, build/test hooks) that yields predictable behavior?
- How should the harness constrain the search space (budgets, stop conditions, allowed edits)?
- What’s the right decomposition: monolithic mega-prompt vs layered prompts + tool contracts?
- How do we design harnesses that are portable across models and tasks?

### Open problems
- Robust prompt/tool contract drift over time.
- Guardrail design that prevents “helpful but wrong” actions without blocking progress.
- Measuring harness quality independent of model choice.

### Expected artifacts
- Diagrams: harness architecture (control plane, tool plane, evaluation plane, state plane).
- Patterns: structured patching, diff discipline, tool-first execution.
- Benchmarks: harness A/B (same tasks) with trace-based metrics (iterations, regressions, time-to-fix).

---

## Chapter 03 — Autonomous Kernels

### Research hypothesis
Small, well-governed “autonomous kernels” (tight loops with explicit budgets and evaluation gates) outperform broad autonomy in stability and debuggability.

### Key architectural questions
- What is the kernel’s execution model (plan → act → verify → commit) and what state is persisted?
- How do kernels compose (nested loops, delegation, sub-agents) without losing traceability?
- What are the minimal correctness checks for kernel actions (unit tests, lint, static checks, spec checks)?
- How should kernels handle uncertainty (branching vs asking vs running experiments)?

### Open problems
- Avoiding local minima (kernel keeps making small safe changes but never solves the root issue).
- Reducing “tool thrash” (too many actions with low information gain).
- Formalizing stop conditions for open-ended tasks.

### Expected artifacts
- Diagrams: kernel state machine; failure recovery paths.
- Patterns: budgeted loop, verify-first, reversible edits.
- Benchmarks: tasks solved per iteration budget; regression rate under autonomy.

---

## Chapter 04 — Memory Systems

### Research hypothesis
Persistent memory improves long-horizon work only when it is structured, queryable, and governed (with provenance), not when it is an uncurated dump of past context.

### Key architectural questions
- What memory classes are required (episodic traces, semantic knowledge, project state, decisions, constraints)?
- What is the read/write policy (when to store, how to summarize, how to expire, how to version)?
- How do we preserve provenance and prevent stale knowledge from dominating?
- What retrieval strategies work under time and token budgets?

### Open problems
- Memory poisoning via incorrect intermediate conclusions.
- Summarization loss leading to systematic blind spots.
- Evaluating memory usefulness without circularity (memory helps because it says it helps).

### Expected artifacts
- Diagrams: memory layers and data flows; provenance model.
- Patterns: decision records, trace-indexed memory, “facts vs hypotheses” tagging.
- Benchmarks: long-horizon tasks with/without memory; drift detection on stored assertions.

---

## Chapter 05 — Evaluation and Traces

### Research hypothesis
Trace-first engineering (capturing actions, tool I/O, diffs, and checks) is necessary to make AI-first systems reproducible and to attribute failures to the right layer.

### Key architectural questions
- What trace schema is sufficient (inputs, outputs, tool calls, diffs, evaluations, budgets)?
- Which evaluations are mandatory gates (tests, lint, type checks, property tests, spec conformance)?
- How do we design evals that measure *system* quality, not just model performance?
- How do we detect capability drift and harness regressions over time?

### Open problems
- Preventing eval gaming (optimizing for the metric while harming real quality).
- Designing cheap evaluations for expensive tasks.
- Aligning qualitative judgments (readability, maintainability) with automated checks.

### Expected artifacts
- Diagrams: trace pipeline; evaluation gating in CI.
- Patterns: “evals as contracts,” trace sampling, regression triage.
- Benchmarks: pass@k under gated loops; change-risk scoring vs post-merge defects.

---

## Chapter 06 — Agent Governance

### Research hypothesis
Governance mechanisms (permissions, budgets, review policies, and auditability) are not optional; they define the safe operating envelope for autonomy.

### Key architectural questions
- What permissions should agents have by default (read-only, patch-only, tool-limited)?
- Where do approvals live (human-in-the-loop checkpoints, protected paths, release gates)?
- How do we represent and enforce policy (constitution, agent rules, CI policies)?
- What is the incident response model when autonomy misbehaves?

### Open problems
- Policy conflicts (speed vs safety) and how to resolve them mechanically.
- Auditing at scale (what to log, how to search, what to retain).
- Governance drift (rules change, old traces become incomparable).

### Expected artifacts
- Diagrams: permission model; escalation paths; audit log flow.
- Patterns: protected resources, diff-only changes, evaluation before merge.
- Benchmarks: prevented-incident rate; false-positive friction cost.

---

## Chapter 07 — Production AI Infrastructure

### Research hypothesis
AI-first systems in production behave like distributed systems: reliability depends on orchestration, observability, caching, cost control, and reproducible environments.

### Key architectural questions
- What runtime components are required (tool servers, sandboxes, queues, cache, secret handling, artifact store)?
- What are the operational SLOs (latency, cost, error rate, rollback time, trace coverage)?
- How do we isolate failures (per-task sandboxes, deterministic replays, capability flags)?
- What is the minimal infrastructure to move from “local agent” to “team-scale system”?

### Open problems
- Cost predictability under variable reasoning depth.
- Secure tool execution in heterogeneous environments.
- Reproducible reruns (same inputs) across changing models and dependencies.

### Expected artifacts
- Diagrams: reference architecture for production agent systems.
- Patterns: sandboxed tool plane, cache + replay, artifact-first runs.
- Benchmarks: cost/latency per successful task; replay success rate.

---

## Chapter 99 — Future Directions

### Research hypothesis
The main frontier is not larger models; it is better system-level interfaces: verifiable tool contracts, stronger evaluations, and memory/governance primitives that scale.

### Key architectural questions
- What would “formal methods for agent loops” look like in practice?
- Which tasks can be made provably safe vs only statistically reliable?
- How should standards emerge (trace formats, tool schemas, evaluation suites)?
- What new failure classes appear as autonomy scales (org-level coupling, supply-chain of prompts/tools)?

### Open problems
- Cross-model portability of traces and evaluations.
- Long-horizon alignment between product intent and accumulated memory.
- Standardizing interoperability without freezing innovation.

### Expected artifacts
- Diagrams: maturity model for AI-first teams and systems.
- Patterns: interoperability contracts, evaluation portability.
- Benchmarks: cross-model reproducibility; “upgrade impact” reports.

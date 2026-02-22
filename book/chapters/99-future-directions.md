# Chapter 99 — Future Directions

## Thesis
The focus is not larger models; it is system-level interfaces and verification: stronger tool contracts, better evaluations, structured memory, and governance primitives that scale across teams and models.

Here, “interfaces” means the concrete artifacts that let components interoperate. This includes tool-call schemas (inputs/outputs and error contracts), trace formats (event types and required fields), and evaluation definitions (tasks, scoring, and pass/fail rules).

“Verification” means methods that detect incorrect behavior reliably. Examples include contract tests for tools, replay checks for agent runs, property-based testing for invariants, and runtime enforcement (schema validation, pre/post-conditions, and budget limits).

Hypothesis: as autonomy scales, the limiting factor becomes organizational and infrastructural coupling, not raw inference capability. Takeaway: progress comes from making runs portable and checkable across models, tools, and teams.

## Why This Matters
- Teams will operate heterogeneous models and tools; interoperability becomes a reliability constraint.
- Long-horizon autonomy introduces new failure classes (compounded assumptions, policy drift, supply-chain issues).
- Without standards, every team reinvents trace formats, eval suites, and governance mechanisms.

## System Breakdown
- **Interoperability**: shared trace formats, tool schemas, evaluation definitions.
- **Verification**: stronger correctness checks, property-based testing, contract enforcement.
- **Governance at scale**: org-level policies, audit workflows, incident response.
- **Ecosystem risks**: prompt/tool supply chain, dependency security, model updates.

**Artifact map (concrete deliverables):**
- **Interoperability**
  - Tool contract schema: JSON Schema for each tool’s inputs/outputs, error types, and retry semantics.
  - Trace interchange spec: required event taxonomy + field requirements so runs can be exported and replayed elsewhere.
  - Eval definition format: task spec + dataset version + scoring code hash so results are reproducible.
- **Verification**
  - Contract test suite: tool-level tests (including negative cases) and schema validation on every tool call.
  - Replay protocol: “same inputs, same trace constraints” checks (within defined nondeterminism bounds).
  - Property checks: invariants over traces (e.g., budgets, safety gates, monotonic progress signals).
- **Governance at scale**
  - Policy registry: versioned policies with owners, rollout rules, and audit requirements.
  - Audit workflow: sampling rules + trace retention + review checklist for incidents and regressions.
  - Incident runbook: severity levels, rollback procedures, and postmortem templates.
- **Ecosystem risks**
  - Supply-chain controls: signed prompt/tool bundles, dependency pinning, and provenance tracking.
  - Model update gates: pre-deploy regression evals + canary rollout criteria.

## Concrete Example 1
Cross-model portability experiment.

**Inputs**
- A fixed harness (same prompts, tool set, budgets, retry policy, and stopping criteria).
- A fixed eval suite with a versioned dataset and deterministic scoring.
- A model set (e.g., Model A, Model B, Model C) that is intentionally heterogeneous (different vendors or major versions).

**Procedure (minimal)**
- Run N trials per task per model with identical harness inputs (same seeds where applicable; same tool sandbox state).
- Record traces using the same trace interchange spec (see next section).
- Compute:
  - Task success rate (pass/fail as defined by the eval).
  - Tool error rate (by tool + error type).
  - Iteration profile (turn count, tool-call count, timeouts/budget hits).
  - Failure signatures (clusters based on trace event sequences, not just final answers).

**Expected outputs**
- A per-model result table, plus a “signature diff” report. The report shows which failure clusters are model-specific vs shared.
- A set of “portability blockers” attributed to either:
  - Harness/tool coupling (e.g., a tool contract ambiguity that different models interpret differently), or
  - Model behavior (e.g., consistent violation of a particular tool precondition).

**Interpreting disagreements**
- If multiple models fail in the same way on the same tasks, prioritize harness-level fixes (tool contract clarity, validation, better stop conditions).
- If one model fails with a distinct trace signature while others pass under identical contracts, treat it as model-dependent and capture it as a regression test.

**What would falsify the goal**
- If variance is dominated by harness nondeterminism (e.g., unstable tool responses or non-versioned datasets), differences cannot be attributed to models. The harness is not portable enough to support the comparison.
- If success/failure flips under small, contract-preserving changes across models (e.g., harmless schema reordering), the tool contracts are underspecified.

## Concrete Example 2
Standardized trace interchange.

**Goal**
Enable independent auditing and regression analysis by exporting traces from one agent runtime and replaying/analyzing them in another tool.

**Minimal trace interchange contract (required fields)**
- `schema_version`: semantic version for the trace spec (e.g., `1.2.0`).
- `run_id`: unique identifier for a single run; stable across exports.
- `eval_id` and `eval_version`: the evaluation definition and dataset/scoring version.
- `harness_id` and `harness_version`: code hash or build identifier.
- `model_id`: model name/version as reported by the provider.
- `events[]`: ordered list where each event includes at least:
  - `event_id`, `type`, `timestamp`, and `parent_event_id` (when applicable)
  - For assistant/user text: content plus redaction markers if content is partially removed
  - For tool calls: `tool_name`, `arguments` (post-validation), `result` (or structured error), and `duration_ms`
  - For policy gates: decision, rule id/version, and rationale category (not freeform prose)

**Versioning rule**
- Backward-compatible additions increment MINOR; breaking changes increment MAJOR.
- A replay tool must refuse to “verify” a trace whose MAJOR version is unsupported; it may still “view” it.

**Replay validity check (what must match)**
- The replay harness must reproduce the same sequence of tool calls (tool name + validated arguments) and the same tool outcomes when tools are deterministic and versioned.
- When nondeterminism exists (timeouts, stochastic tools, external APIs), the trace must record the nondeterminism boundary (e.g., tool snapshot id, cached response id, or allowed outcome set), and replay is valid only if outcomes stay within that boundary.
- If the replay diverges in tool-call sequence under deterministic conditions, the run is not reproducible and should be flagged as a portability failure.

## Trade-offs
- Standardization improves portability but can slow experimentation.
- Strong verification increases confidence but can increase compute and engineering effort.
- More governance improves safety but can reduce developer autonomy.

**Decision checklist (operational)**
- Standardize when multiple teams depend on the same tools/traces, when incidents require cross-team auditing, or when model swaps are frequent.
  Delay standardization when the interface changes weekly and only one team uses it.
- Use tests/contracts when failures are frequent, expensive, or safety-critical.
  Prefer lighter checks when the component is experimental and low-impact, but still enforce schema validation and basic budgets.
- Escalate governance when a change affects shared tool contracts, trace schemas, or eval definitions.
  Keep governance minimal for isolated experiments that do not affect shared artifacts.
- Set thresholds explicitly: acceptable tool error rate, maximum budget hits per run, and the severity that triggers an incident workflow.

## Failure Modes
- **Lock-in**: traces and tools become proprietary and non-portable.
  Mitigation: adopt the trace interchange spec + semantic versioning, and require export/replay tooling as a release gate for shared runtimes.
- **False comparability**: metrics appear comparable across systems but differ in hidden ways.
  Mitigation: pin `eval_version`, record scoring code hashes, and add calibration tasks that must match within tolerance before comparing models.
- **Scale amplification**: small policy errors cause large, repeated failures.
  Mitigation: treat policies as versioned artifacts, run a policy regression suite on traces, and use canary rollouts with explicit rollback criteria.

## Research Directions
- Formal methods adapted to agent loops (bounded proofs, verified tool contracts).
  Research question: which tool contracts can be specified with pre/post-conditions that are checkable at runtime and useful in practice?
  Success signal: a library of contracts where violations predict real failures, plus a measurable reduction in incident rate or replay divergence.
- Benchmarks for reproducible autonomy (replay success, attribution accuracy).
  Research question: what benchmark design makes “replay success” meaningful across runtimes without masking nondeterminism?
  Success signal: standardized benchmark suites where independent implementations reach high replay agreement and can localize regressions to a tool, policy, or model change.
- Org-scale governance patterns and “policy drift” detection.
  Research question: what signals in traces reliably indicate policy drift (changes in decision boundaries or rule application) before incidents occur?
  Success signal: drift detectors with low false positives that catch policy regressions in canaries and prevent broad rollouts.

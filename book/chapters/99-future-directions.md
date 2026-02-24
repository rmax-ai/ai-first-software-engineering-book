# Chapter 99 — Future Directions

## Thesis

The frontier is not larger models. It is system-level interfaces and verification.

Concretely, invest in artifacts that scale across teams and models.

- stronger tool contracts
- better evaluations
- structured memory
- governance primitives

Interfaces are artifacts that let components interoperate. They make runs portable. Example: a tool-call schema that two runtimes both validate. Example: a trace format that two analysis tools both parse. Example: an eval definition that two teams can both reproduce.

“Verification” means methods that detect incorrect behavior reliably. In practice, verification makes runs auditable. It lets you show that a tool call matched a contract. It also lets you show that a replay stayed within a declared nondeterminism boundary. Finally, it lets you show that a reported score came from a pinned dataset and scoring implementation.

Key terms (used consistently in this chapter):

- **Interoperability**: shared formats and schemas that make runs exportable across tools and teams.
- **Verification**: checks that make claims about a run defensible (contract validation, replay validity, invariant checks).
- **Governance**: versioning, ownership, and rollout rules for shared artifacts.
- **Nondeterminism boundary**: the explicitly declared set of run aspects allowed to vary without invalidating a replay.

Takeaway: progress comes from portable, checkable runs across models, tools, and teams.

## Why This Matters

- Teams will operate heterogeneous models and tools; interoperability becomes a reliability constraint.
- Long-horizon autonomy introduces new failure classes: compounded assumptions, policy drift, and supply-chain issues.
- Without standards, every team reinvents trace formats, eval suites, and governance mechanisms.

So what changes for teams? Treat tool schemas, trace formats, and eval definitions as versioned products. Write contracts and test them. Require replayable traces so failures can be audited and compared across models.

## System Breakdown

These four areas are coupled. Interfaces create portability, and verification enables auditability. Governance sets the rules for how shared artifacts evolve.

The dependency chain below makes the coupling explicit. Focus on the arrows. They show what must be versioned and validated before you can compare runs across teams or models.

Dependency chain:

- **Interoperability** → **Verification** (contracts define what can be checked).
- **Verification** → **Governance** (audit claims determine what shared policies must enforce).
- **Interoperability** → **Ecosystem risk** (the surface area you expose becomes your supply-chain and update risk).
- **Ecosystem risk** → **Verification** (risk pressure raises the bar for checks and replayability).

This is the system-level reason “bigger models” is not the whole story: portable, checkable runs depend on what interfaces you standardize and what verification you can actually enforce.

Takeaway: you can improve one pillar in isolation, but cross-model portability depends on the whole chain. Interoperability defines what can be exchanged, and verification defines what can be trusted when it is exchanged.

- **Interoperability**: shared trace formats, tool schemas, evaluation definitions (traces·schemas·evals).
- **Verification**: stronger correctness checks, property-based testing, contract enforcement (contract-tests·replay·properties).
- **Governance at scale**: org-level policies, audit workflows, incident response (policy-registry·audit·runbook).
- **Ecosystem risks**: prompt/tool supply chain, dependency security, model updates (supply-chain·deps·model-updates).

Note: structured memory fits here as a versioned interface artifact. Treat memory schemas and retention/redaction rules as contracts. Concretely: version the memory record schema, validate writes/reads against it, record memory operations in traces, and enforce retention/redaction as policy gates that are auditable and replay-checkable.

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
- A set of “portability blockers,” attributed to one of these sources:
  - Harness/tool coupling (e.g., a tool contract ambiguity that different models interpret differently).
  - Model behavior (e.g., consistent violation of a particular tool precondition).

Results template (example skeleton):

- Model
- Tasks
- Trials (N)
- Success rate
- Tool error rate
- Median tool calls
- Median turns
- Timeout/budget-hit rate
- Top failure signature

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

Trace interchange works best when treated as a checklist of explicit checkpoints. Track where validation occurs, where trace export happens, and what the divergence check is allowed to claim as “verified.”

Trace interchange pipeline:

Generate → Validate → Emit trace → Export → Replay → Divergence check → (Audit | Flag failure)

“Divergence check” means comparing the replayed run to declared constraints. It does not require byte-for-byte identity. Use it when nondeterminism is allowed.

Validate checkpoint: runtime schema-check tool arguments/results (including negative cases) and record the validation outcome in the trace before export.

Takeaway: validate contracts before Export, then use Replay + Divergence check against declared constraints before drawing audit conclusions.

The point is not to standardize everything. Standardize the minimum needed for agreement. Two independent tools should agree on what happened. They should also detect when a run is not reproducible under stated constraints.

**Minimal trace interchange contract (required fields)**

**Run metadata**

- `schema_version`: semantic version for the trace spec (e.g., `1.2.0`).
- `run_id`: unique identifier for a single run; stable across exports.
- `eval_id` and `eval_version`: eval definition and dataset/scoring version.
- `harness_id` and `harness_version`: code hash or build identifier.
- `model_id`: model name/version as reported by the provider.

**Event schema**

- `events[]`: ordered list of events.
  - `event_id`
  - `type`
  - `timestamp`
  - `parent_event_id` (when applicable)
  - Assistant/user text:
    - `content`
    - redaction markers (when redacted)
  - Tool calls:
    - `tool_name`
    - validated `arguments`
    - `result` or structured error
    - `duration_ms`
  - Policy gates:
    - decision
    - rule id/version
    - rationale category (not freeform prose)

**Versioning rule**

- Backward-compatible additions increment MINOR.
- Breaking changes increment MAJOR.
- A replay tool must refuse to “verify” unsupported MAJOR versions; it may still “view” them.

**Replay validity check (what must match)**

- Deterministic runs: tool-call sequence must match.
- Match means: tool name + validated arguments.
- Deterministic, versioned tools: outcomes must match.
- Nondeterministic components: record the boundary.
- Record what replay is allowed to vary within.
- Replay is valid only within that boundary.
- Examples of declared nondeterminism boundaries:
  - Time-based tools: allow timestamps to vary within an explicit tolerance window, but require the same tool-call sequence and arguments.
  - Network variability: allow specified transient error classes (e.g., retryable 5xx) within declared retry semantics; treat unexpected error types as divergence.
  - Sampling or randomized components: require a declared RNG source/seed policy; if seeds are not fixed, declare which outputs may vary and which invariants must still hold.
- If sequence diverges under deterministic conditions, flag a portability failure.

## Trade-offs

- Standardization improves portability but can slow experimentation.
- Strong verification increases confidence but can increase compute and engineering effort.
- More governance improves safety but can reduce developer autonomy.

**Decision checklist (operational)**

**Standardize**

- Standardize when multiple teams depend on the same tools/traces.
- Standardize when incidents require cross-team auditing.
- Standardize when model swaps are frequent.
- Delay standardization when the interface changes weekly and only one team uses it.
- Minimum viable standardization threshold (example): when a tool or trace schema has 2+ consuming teams and changes less than once per sprint.
- In that case, require semantic versioning, a contract test suite, and a changelog entry for every interface change.
- Assign an explicit owner for each shared interface artifact (tool schema, trace spec, eval definition), with a documented escalation path for breaking changes.

**Verify**

- Use tests/contracts when failures are frequent, expensive, or safety-critical.
- Prefer lighter checks for experimental, low-impact components.
- Still enforce schema validation and basic budgets.
- Treat contract violations as an operational metric (example target): fewer than 1 contract violation per 1,000 tool calls on shared production tools; exceeding it triggers a rollout pause and an incident review.

**Govern**

- Escalate governance when changes affect shared tool contracts, trace schemas, or eval definitions.
- Keep governance minimal for isolated experiments that do not affect shared artifacts.
- Set thresholds explicitly: acceptable tool error rate, maximum budget hits per run, and the severity that triggers an incident workflow.
- Require that breaking changes to shared interfaces include: a MAJOR version bump, a migration note, and a compatibility window (example): support N and N-1 MAJOR versions for core trace tooling for a fixed period before deprecation.

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

What teams should do next (near-term, within this chapter’s scope):

- Pick one shared artifact (a tool contract, trace spec, or eval definition) and put it under semantic versioning with an owner.
- Add runtime schema validation for every tool call and record validation results in the trace (including negative cases).
- Define the nondeterminism boundary for your top tools/components and implement replay validity checks against that boundary.
- Run a small cross-model portability experiment on a pinned eval suite and publish a “signature diff” report as a recurring regression artifact.

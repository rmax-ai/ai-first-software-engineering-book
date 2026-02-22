# Glossary

This glossary defines terms as used in this book. Definitions are intentionally operational: they describe what a term *does* in a system.

## Acceptance criteria

Explicit, testable conditions that define “done” for a task.

In practice, acceptance criteria should map to checks (tests, lint, build, schema validation, golden diffs) or to a bounded human-review checklist.

Example: “When the user resets a password, the old password no longer works, the new one works, and an audit event is recorded.” This can map to (1) a unit/integration test for login behavior, (2) a schema validation check for the audit event payload, and (3) a golden diff for the emitted audit log line format.

## Agent loop

A control loop that repeatedly: (1) observes state, (2) chooses a next action (often a tool call), (3) executes, (4) updates state, (5) decides whether to stop.

Typical loop variables include a step budget, an allowlist of tools, and a termination condition.

## Allowlist

A set of explicitly permitted actions or tools.

Allowlists reduce accidental capability expansion: adding a new tool is a deliberate change that can be reviewed, tested, and governed.

## Budget

A hard limit enforced by the kernel (or orchestration layer) on steps, time, tokens, or cost.

Budgets turn “try until it works” into a bounded process.

## Context window

The maximum amount of text (messages + tool outputs + retrieved memory) that a model can condition on at once.

Design implication: systems must choose what to include, summarize, or omit.

## Determinism

The degree to which the system produces the same outcome given the same inputs.

Thesis: Operational definitions make system behavior checkable because the terms map to observable artifacts (tests, traces, diffs) that can be verified and compared over time.

In agentic systems, determinism is engineered: you constrain degrees of freedom (tool allowlists, typed interfaces, fixed prompts), reduce nondeterministic dependencies, and require verification so the system can detect and correct deviations. It fails when hidden inputs change (environment drift, tool version changes, timing races) or when sampling/tooling is unconstrained.

See also: Non-determinism, Drift, Verification.

## Drift

Unintended change in behavior over time relative to a baseline.

Drift can be caused by model updates, prompt edits, tool/API changes, data changes, environment changes, or accumulating memory. Drift is detected by comparing traces or eval results across versions.

Concrete detection example: run the same eval suite on version A and version B and compare (a) pass/fail outcomes and (b) a small set of golden traces (tool calls + outputs). A changed tool argument, a new failure, or a different patch checksum is evidence of drift even if the final text “looks fine.” See also: Eval, Trace.

## Evidence

Artifacts that support a claim about system behavior.

Examples: a test run output, a checksum of an applied patch, a trace segment showing tool inputs/outputs, a golden diff. Evidence matters because it can be re-checked; it fails when it is incomplete (missing inputs), not versioned, or not attributable to the run you claim (e.g., copied logs from a different environment).

Trade-off: stronger claims and faster debugging versus additional collection, storage, and review overhead.

See also: Verification, Trace, Eval.

## Eval

A repeatable test that measures whether a system meets a target behavior under defined inputs and constraints.

Evals can be automated (unit tests, golden files, scripted scenarios) or human-scored, but they must be versioned and runnable. An eval fails as a control when it is nondeterministic, unbounded (depends on live external systems without pinning), or easy to “pass” without actually satisfying the intended behavior.

Example: a scripted scenario that runs the agent on a fixed repo snapshot, asserts the tool allowlist is respected, and checks that the produced patch applies cleanly and passes `pytest` in CI.

## Failure mode

A specific way the system can fail, including its trigger and observable symptoms.

Failure modes drive targeted mitigations (tool contracts, guardrails, tests) rather than general caution.

## Golden file

A stored “expected output” used for regression testing.

Golden tests are useful for CLI help text, formatted outputs, and traces; they must be reviewed carefully because updating them can mask regressions.

## Governance

Rules, controls, and escalation paths that constrain and audit agent behavior.

Governance commonly includes: tool allowlists, budgets, approval gates, logging requirements, data handling policies, incident response, and rollback procedures.

## Harness

The engineered environment around a model that makes behavior reliable and useful in a specific context.

A harness typically includes: prompts, tool schemas, routing policies, memory strategy, eval suite, tracing/telemetry, and release discipline. Most production reliability lives in the harness rather than in the model.

Components: prompts, tool interfaces/schemas, policy + allowlists, routing, memory strategy, eval suite, and tracing/telemetry.

A harness fails when it allows ambiguous operations (unclear tool contracts), lacks stop conditions or budgets, or cannot produce evidence for outcomes (no runnable evals, no trace capture).

See also: Kernel, Agent loop, Tool interface.

## Idempotency

A property of an operation where repeating it produces the same final state as running it once.

Idempotency matters for retries: without it, transient failures can cause duplicated side effects. It fails when an operation appends, increments, or creates unique resources on each attempt (e.g., “create ticket” without a deduplication key).

Example: “write file X with content hash H” is idempotent; “append line to file X” is not unless guarded by a check.

## Kernel

The minimal execution substrate that runs the agent loop and mediates interaction with the outside world.

A kernel is responsible for: step control, tool invocation, persistence boundaries, cancellation/timeouts, and trace logging. It should be small enough to audit.

Relative to the harness, the kernel is the minimal control plane (execute/cancel/limit/log). The harness is the engineered reliability layer (policies, tool contracts, evals, and routing).

Kernel failures are usually control failures: missing timeouts, unbounded retries, insufficient isolation of side effects, or incomplete trace capture that prevents post-incident reconstruction.

See also: Harness, Agent loop, Trace.

## Memory

Persisted or semi-persisted state used to condition future behavior.

Memory may be transient (within a run), session-scoped, or long-lived. It may be explicit (structured records) or implicit (retrieval index). Memory is a mechanism for reintroducing prior information into context; it is not automatically correct.

## Non-determinism

Variation in outcomes across runs due to sampling, tool timing, nondeterministic tests, external APIs, or changing environments.

Managing nondeterminism is a core engineering task in agentic systems. It becomes an operational risk when it prevents reliable verification (flaky evals) or makes incidents hard to reproduce without traces.

See also: Determinism, Drift, Eval.

## Policy

An explicit rule set that constrains behavior.

Policies can be encoded in prompts, tool routers, allowlists, budgets, and approval workflows. Effective policies are testable and observable.

## Prompt

The structured input (system/developer/user messages and other context) used to condition the model.

Prompting is part of the harness; changes to prompts should be versioned and evaluated like code.

## Retrieval

Selecting external information (documents, traces, code snippets) to include in context for a step.

Retrieval must be treated as a hint: critical claims still require confirmation against source-of-truth artifacts.

## RAG (retrieval-augmented generation)

A pattern where the system retrieves relevant documents and includes them in the prompt before generating output.

In engineering systems, RAG commonly retrieves code, docs, tickets, and prior traces.

## Side effect

Any operation that changes state outside the model’s messages.

Examples: writing files, calling APIs, creating tickets, merging PRs, or modifying databases. Side effects matter because they must be governed (permissions, approvals), made retry-safe (often via idempotency), and traced; they fail operationally when they are hidden (no logging) or irreversible without explicit rollback.

## Tool interface

The contract between the agent and an external capability.

A tool interface specifies: inputs, outputs, errors, side effects, idempotency, latency expectations, and permission scope. Good tool interfaces make failure explicit and reduce ambiguity.

Mini check-list: inputs (types + defaults), outputs (schema), errors (enumerated), side effects (what state changes), idempotency (retry behavior), latency/timeouts, and scope/permissions. See also: Side effect, Idempotency.

## Trace

A structured record of an agent run that is sufficient to reconstruct what happened and why.

A trace typically includes: prompts/messages, tool calls and results, intermediate decisions, budgets, timing, and final outputs. Traces are used for debugging, eval attribution, and governance.

Minimum to reconstruct a run usually means: the exact inputs (prompt/context identifiers), the ordered tool invocations with arguments and outputs, and the final produced artifact(s), so claims can be supported with evidence and re-verified.

Trade-off: better debugging/auditability versus storage cost and data-handling risk (e.g., traces may contain file paths, snippets, or identifiers).

## Verification

Objective checks that the system runs (or produces as artifacts) to validate that an output meets acceptance criteria.

Verification is stronger than self-review: it produces evidence. Verification fails when checks are missing, non-runnable, or decoupled from the artifact under review (e.g., “looks correct” without running tests).

Trade-off: higher confidence versus increased runtime/CI cost and potential flakiness if the checks are not deterministic.

Example: after applying a patch, run unit tests + lint + a targeted end-to-end scenario, and keep the command outputs as evidence.

See also: Evidence, Eval, Acceptance criteria.

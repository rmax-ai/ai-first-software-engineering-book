# Glossary

This glossary defines terms as used in this book. Definitions are intentionally operational: they describe what a term *does* in a system.

## Acceptance criteria
Explicit, testable conditions that define “done” for a task.

In practice, acceptance criteria should map to checks (tests, lint, build, schema validation, golden diffs) or to a bounded human-review checklist.

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

In agentic systems, determinism is usually approached through constraints, typed tools, and verification rather than assumed.

## Drift
Unintended change in behavior over time relative to a baseline.

Drift can be caused by model updates, prompt edits, tool/API changes, data changes, environment changes, or accumulating memory. Drift is detected by comparing traces or eval results across versions.

## Evidence
Artifacts that support a claim about system behavior.

Examples: a test run output, a checksum of an applied patch, a trace segment showing tool inputs/outputs, a golden diff.

## Eval
A repeatable test that measures whether a system meets a target behavior under defined inputs and constraints.

Evals can be automated (unit tests, golden files, scripted scenarios) or human-scored, but they must be versioned and runnable.

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

## Idempotency
A property of an operation where repeating it produces the same final state as running it once.

Idempotency matters for retries: without it, transient failures can cause duplicated side effects.

## Kernel
The minimal execution substrate that runs the agent loop and mediates interaction with the outside world.

A kernel is responsible for: step control, tool invocation, persistence boundaries, cancellation/timeouts, and trace logging. It should be small enough to audit.

## Memory
Persisted or semi-persisted state used to condition future behavior.

Memory may be transient (within a run), session-scoped, or long-lived. It may be explicit (structured records) or implicit (retrieval index). Memory is a mechanism for reintroducing prior information into context; it is not automatically correct.

## Non-determinism
Variation in outcomes across runs due to sampling, tool timing, nondeterministic tests, external APIs, or changing environments.

Managing nondeterminism is a core engineering task in agentic systems.

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

Examples: writing files, calling APIs, creating tickets, merging PRs, or modifying databases.

## Tool interface
The contract between the agent and an external capability.

A tool interface specifies: inputs, outputs, errors, side effects, idempotency, latency expectations, and permission scope. Good tool interfaces make failure explicit and reduce ambiguity.

## Trace
A structured record of an agent run that is sufficient to reconstruct what happened and why.

A trace typically includes: prompts/messages, tool calls and results, intermediate decisions, budgets, timing, and final outputs. Traces are used for debugging, eval attribution, and governance.

## Verification
Objective checks that the system runs (or produces as artifacts) to validate that an output meets acceptance criteria.

Verification is stronger than self-review: it produces evidence.

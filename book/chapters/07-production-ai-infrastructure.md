# Chapter 07 — Production AI Infrastructure

## Thesis
Production AI-first systems are distributed systems: they require orchestration, isolation, observability, caching, cost control, and reproducible environments.

Hypothesis: operational reliability depends more on the tool/runtime plane than on the model prompt. The tool/runtime plane includes (1) sandboxed execution environments, (2) tool adapters/services (test runner, browser, repo API), (3) orchestration policies (queueing, concurrency, retries, idempotency), (4) observability and correlation across steps, and (5) durable artifacts for replay and audit. Restated: if you can reliably run tools, record what happened, and reproduce the run, you can improve the system even when model behavior varies.

## Why This Matters
- Without isolation, tool execution becomes a security and reliability risk.
- Without observability, failures cannot be attributed or fixed systematically.
- Without cost controls, autonomy can become economically unstable.

## System Breakdown
- **Execution**: sandboxes/containers, dependency pinning, deterministic runners. Contract: identical inputs produce the same tool environment (image hash + lockfile), with a hard wall-clock timeout per step.
- **Tool services**: test runners, build systems, browsers, repo APIs. Contract: every tool call is versioned and returns structured output (exit code, stdout/stderr, and machine-readable summary).
- **Orchestration**: queues, concurrency limits, backpressure. Contract: max concurrency is enforced (per repo/org), retries are bounded (count + backoff), and each task carries an idempotency key.
- **Observability**: traces, metrics, logs; correlation ids. Contract: every task/run has a run id and spans for each tool call, with success/failure and duration recorded.
- **Artifacts**: build outputs, diffs, evaluation reports, replay bundles. Contract: store a bundle per run (inputs, tool versions, command lines, logs, diffs, and evaluation result) with a retention policy.
- **Security**: secrets handling, network egress controls, least privilege. Contract: explicit allowlists for tools, filesystem paths, and network egress; secrets are injected only at execution time and never written to artifacts.

## Concrete Example 1
Sandboxed tool execution for code changes.
- Trigger: a proposed patch (diff) plus a task spec (e.g., “fix failing test X”), with the target branch SHA and a pinned environment (container image + lockfile).
- Sandbox: start an isolated runner with no ambient credentials; mount the repo read-write but restrict filesystem and network egress to an allowlist.
- Tool calls: run a fixed sequence (format/lint → unit tests → build) with step timeouts (e.g., 5m/unit, 15m/build) and bounded retries for flaky steps (e.g., 2 retries with exponential backoff).
- Artifact bundle (stored per run id): the patch, tool call transcripts (commands, versions, exit codes), logs, test reports (JUnit/JSON), build outputs, and a replay manifest that can re-run the same steps from the same inputs.
- Evaluation gate: promote only if required checks pass (e.g., all tests green, no new lints, diff applies cleanly) and the run is reproducible (replay succeeds at least once or the environment hash matches a known-good cache entry).

## Concrete Example 2
Cost-aware autonomy for a batch of maintenance tasks.
- Budget: per-task token/cost ceilings (e.g., $0.50 and 20k tokens) plus a batch budget (e.g., $50/day), enforced by the orchestrator.
- Strategy: fail fast on low-signal tasks (small, repetitive, or high-latency tool loops) and escalate to human review when confidence is low or blast radius is high.
- Decision policy: define “low-signal” as (a) no progress after N tool steps (e.g., 6) or (b) repeated similar errors (same stack trace twice) or (c) predicted cost-to-complete exceeds remaining budget; escalate if the change touches production config, security-sensitive files, or exceeds a diff size threshold (e.g., >200 lines changed).
- Measure: cost per successful task, time-to-merge, regression rate (e.g., post-merge rollback or test failures within 24h), and “wasted spend” (tokens spent on tasks that are abandoned or escalated).

## Trade-offs
- Isolation increases safety but adds operational complexity. Default: start with containerized execution + strict allowlists; revisit if tool latency dominates (e.g., repeated cold starts) and you can prove tighter scoping by repo/path.
- Strong observability increases insight but raises data retention requirements. Default: structured logs + traces with short retention for raw logs and longer retention for summaries; revisit if incident analysis regularly needs deeper raw context.
- Caching and replay improve speed but can mask nondeterminism if misused. Default: cache only deterministic steps (dependency installs keyed by lockfile, build outputs keyed by inputs) and periodically force no-cache replays; revisit if you observe drift or flaky tests that caching hides.

## Failure Modes
- **Non-reproducible runs**: environment drift makes traces hard to replay.
  - Detection: replay fails with different dependency resolutions; tool versions differ from the recorded manifest; repeated “works on runner A but not runner B” incidents.
  - Mitigation: pin images and dependencies; record tool versions and hashes in the replay manifest; run periodic “replay audits” that re-execute a sample of recent runs.
- **Leaky permissions**: tool plane has broader access than intended.
  - Detection: outbound network calls to unexpected domains; tools reading/writing outside approved paths; secrets appearing in logs or artifacts.
  - Mitigation: enforce network egress allowlists; run tools with least-privilege credentials scoped to a repo/task; add secret redaction and artifact scanning before persistence.
- **Noisy observability**: too much unstructured logging reduces signal.
  - Detection: high log volume with low queryability; incident timelines require manual grepping; key metrics (duration, retries, error class) missing from dashboards.
  - Mitigation: emit structured events for each tool call; standardize error classes and outcome codes; sample verbose logs while keeping full traces for failed runs only.

## Research Directions
- Standardized replay bundles for agent runs.
- Cost/performance models that predict optimal evaluation depth.
- Secure-by-default tool runtime primitives for autonomy.

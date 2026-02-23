# Chapter 06 — Agent Governance

## Thesis

Governance defines the safe operating envelope for agents. It is not optional once agents can change code, invoke tools, or affect production systems.

The “operating envelope” defines what an agent is allowed to do. It defines when those actions are allowed. It defines what evidence must exist afterward to support review and rollback.

Hypothesis: autonomy without enforceable governance increases throughput in the short term. Over time, defect rate and operational risk rise. Changes can outpace review, exceed intended access scopes, or ship without traceable accountability.

What governance is / is not:

- Governance is **enforced constraints + auditability** (tool/CI checks, logs, approvals), not a document that can be ignored.
- Governance is **risk-shaped** (stricter rules for higher-risk operations), not uniform friction applied everywhere.
- Governance is **measurable** (blocked unsafe changes, incidents, review latency), not a “best effort” policy.

## Why This Matters

- Agents can operate faster than human review cycles; governance prevents unsafe acceleration.
- Production environments require audit trails and controlled access to sensitive operations.
- Governance makes behavior consistent across models and team members.

## System Breakdown

- **Policy artifacts**: constitution, agent rules, CI policies.
  - Enforceable rules:
    - “No writes to protected paths without approval token.”
    - “All tool calls must declare intent and target files.”
  - Enforcement:
    - Pre-commit or tool-layer policy checks reject disallowed patches.
    - CI re-validates policies on the merge commit.
- **Permissions**: read/write scopes, protected files, tool allowlists.
  - Enforceable rules:
    - “Read-only by default; write requires explicit scope.”
    - “Network access disabled unless allowlisted per job.”
  - Enforcement:
    - Runtime tool allowlist/denylist.
    - Repository protected-branch rules and CODEOWNERS coverage for specific paths.
- **Budgets**: time, iterations, tool calls, diff size, cost ceilings.
  - Enforceable rules:
    - “Max N iterations per task.”
    - “Max diff size for autonomous edits.”
    - “Stop on repeated failures.”
  - Enforcement:
    - Harness-level counters.
    - CI policy fails if changes exceed thresholds or if required checkpoints were skipped.
- **Review**: mandatory human checkpoints for specific risk classes.
  - Enforceable rules:
    - “Human approval required for security configs, auth paths, dependency upgrades.”
    - “Two-person review for rollback scripts.”
  - Enforcement:
    - CODEOWNERS + branch protection.
    - CI classifies changes and blocks merge unless approvals match the risk class.
- **Audit**: trace retention, searchable logs, change attribution.
  - Enforceable rules:
    - “All tool executions emit structured logs.”
    - “Each patch links to an agent run id and input prompt.”
  - Enforcement:
    - Log collection in CI artifacts or a central store.
    - Merge requires a commit trailer field `Agent-Run-Id: <run_id>`.
    - CI validates this trailer case-sensitively.
    - The key must be exactly `Agent-Run-Id`.
    - `<run_id>` must be lowercase and match `run_[a-z0-9]{12}`.
    - Valid: `Agent-Run-Id: run_3f9c2a1b7d4e`.
    - Invalid: `agent-run-id: run_3f9c2a1b7d4e`, `Agent-Run-Id: RUN_3F9C2A1B7D4E`.

Governance loop (artifacts in parentheses):

1. Policy definition (constitution / agent rules / CI policies)
2. Enforcement at execution and merge time (tool allowlists / protected-path checks / CI gates)
3. Telemetry and audit capture (structured traces / searchable logs / change attribution)
4. Review routing and approvals (risk classification / CODEOWNERS / mandatory checkpoints)
5. Policy update after incidents or near-misses (rule changes + new tests/evals)

A diagram helps here because governance is a loop with repeated checkpoints. In the flow below, focus on two things: where enforcement blocks unsafe actions, and where evidence is captured. Those points determine what reviewers can verify and what can be rolled back safely.

<pre class="mermaid">
flowchart TB
  A["1. Policy definition<br/>(constitution / agent rules / CI policies)"]
  B["2. Enforcement<br/>(tool allowlists / protected paths / CI gates)"]
  C["3. Telemetry + audit capture<br/>(structured traces / logs / attribution)"]
  D["4. Review routing + approvals<br/>(risk class / CODEOWNERS / checkpoints)"]
  E["5. Policy update<br/>(incidents / near-misses / new evals)"]

  A --> B --> C --> D --> E --> A
</pre>

Takeaway: steps 2 and 3 are the “hard” parts of governance. Step 2 controls what can happen. Step 3 determines what proof exists afterward, so steps 4 and 5 can block unsafe merges and tighten policy based on observed failures.

## Concrete Example 1

Protected-path governance.

Policy text (agent rules / CI policy):

- Rule: forbid edits to security-critical configs without explicit approval.
- Protected paths (example): `infra/`, `.github/workflows/`, `config/prod/`, `secrets/`.

Enforcement point (tool layer + CI):

- Tool layer: rejects any patch touching a protected path unless an approval token is present in the task context (e.g., `APPROVAL=SECURITY-1234`) and the approver identity is recorded.
- CI: re-checks the merged diff; fails the build if protected paths changed without the recorded approval.

Example attempted edit (input and check):

- Agent proposes changing `.github/workflows/release.yml` to add a new step that uploads artifacts.
- Policy check inspects the diff and matches a protected path.

Expected rejection message (testable outcome):

- “Rejected: write to protected path `.github/workflows/` requires approval. Provide approval token + approver identity, or move the change to an approved human-owned PR.”

Remediation path (approval and artifacts produced):

- Human reviewer evaluates the intent, then supplies an approval token and identity.
- Artifact produced: an audit entry containing (a) file paths touched, (b) approval token, (c) approver, (d) timestamps, (e) tool execution trace id.
- CI verifies the audit entry exists and is linked to the commit/PR before allowing merge.

## Concrete Example 2

Incident response for a bad autonomous change.

Detection signal:

- Trigger: regression detected by the `smoke-prod` gate post-merge.
- Example threshold (checkable): `smoke-prod` fails if HTTP 5xx rate exceeds 1.0% over a 10-minute canary window.
- Example threshold (checkable): `smoke-prod` fails if p95 latency regresses by more than 20% versus the previous baseline.
- Gate semantics (checkable): `smoke-prod` fails if either condition is met.
- Gate semantics (checkable): OR semantics.

Immediate containment (rollback):

- Action: revert the merge commit (or roll back the deployment) using the pre-defined rollback procedure.
- Containment SLO (example): rollback initiated within 5 minutes of `smoke-prod` failure and completed within 15 minutes.
- Output: a rollback commit/deployment event linked to the original agent run id.

Trace queries (audit-driven investigation):

- Use the audit trail to answer: which tools were invoked, which files were changed, which tests were executed, and whether any approvals were used.
- Minimum required evidence: a searchable trace that reconstructs the diff, command outputs, and decision points (e.g., “skipped test X due to timeout”).
- SLO evidence: audit record includes timestamps for detection, rollback initiation, and rollback completion, plus a deployment event id that can be cross-referenced.

Root-cause classification (review-driven):

- Classify the incident into a governance-relevant bucket, for example:
  - Missing gate: the regression would have been caught by a specific test that did not run.
  - Mis-scoped permissions: the agent changed a file outside the intended scope.
  - Review routing failure: change risk was misclassified and did not receive the required human checkpoint.

Policy change (closing the gap):

- Update agent rules/CI policy to prevent recurrence, e.g., “Changes touching `config/prod/` must run `smoke-prod` suite,” or “Any change to deployment steps requires CODEOWNER approval.”

New eval/test gate (enforced going forward):

- Add or strengthen a regression test/eval that fails deterministically on the known pattern.
- Wire it into CI so it is mandatory for the relevant risk class, and confirm the audit system records that the gate ran (not just that it exists).

## Trade-offs

- Strong governance reduces risk but can slow iteration; the goal is to pay friction only where risk is high.
- Overly strict permissions increase human workload via escalations and can create “approval queues.”
- Excessive auditing can create privacy and compliance burdens.

Operational metrics to make these trade-offs visible:

- Friction cost: median time-to-approval for high-risk changes; escalation rate (% of tasks requiring human intervention); rework rate after policy rejections.
- Prevented incidents: count of blocked protected-path writes; count of merges prevented due to missing required gates; incident rate per 100 changes for governed vs ungoverned paths.
- Governance effectiveness: time-to-rollback from detection; percentage of changes with complete trace metadata; false-positive rate of risk classification (unnecessary blocks).

## Failure Modes

- **Policy drift**: rules become outdated and stop reflecting real risks.
- **Shadow autonomy**: humans bypass gates “just this once,” breaking discipline.
- **Governance without enforcement**: documents exist but tools/CI do not enforce them.

## Research Directions

- Policy-as-code patterns for agent systems. Deliverable: a versioned policy repository with rule tests and a CI job that validates enforcement on every change.
- Automated risk scoring for diffs to route reviews. Deliverable: a diff classifier with explicit routing rules (which paths/operations require which approvals) and measured false-positive/false-negative rates.
- Governance metrics: prevented incidents vs friction cost. Deliverable: a dashboard spec that defines the core counters (blocked changes, escalations, incident rate, time-to-rollback) and the data sources for each.

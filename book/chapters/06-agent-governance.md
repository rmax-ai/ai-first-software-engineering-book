# Chapter 06 — Agent Governance

## Thesis
Governance defines the safe operating envelope for autonomy: permissions, budgets, review policies, auditability, and incident response.

Hypothesis: autonomy without enforceable governance increases throughput in the short term but increases defect rate and operational risk over time.

## Why This Matters
- Agents can operate faster than human review cycles; governance prevents unsafe acceleration.
- Production environments require audit trails and controlled access to sensitive operations.
- Governance makes behavior consistent across models and team members.

## System Breakdown
- **Policy artifacts**: constitution (principles), agent rules (operational constraints), CI policies (enforcement).
- **Permissions**: read/write scopes, protected files, tool allowlists.
- **Budgets**: time, iterations, tool calls, diff size, cost ceilings.
- **Review**: mandatory human checkpoints for specific risk classes.
- **Audit**: trace retention, searchable logs, change attribution.

## Concrete Example 1
Protected-path governance.
- Rule: forbid edits to security-critical configs without explicit approval.
- Enforcement: tool layer rejects patches; CI verifies policy compliance.

## Concrete Example 2
Incident response for a bad autonomous change.
- Trigger: regression detected by eval gates post-merge.
- Response: rollback + trace review + policy update + new regression test.

## Trade-offs
- Strong governance reduces risk but can slow iteration.
- Overly strict permissions increase human workload via escalations.
- Excessive auditing can create privacy and compliance burdens.

## Failure Modes
- **Policy drift**: rules become outdated and stop reflecting real risks.
- **Shadow autonomy**: humans bypass gates “just this once,” breaking discipline.
- **Governance without enforcement**: documents exist but tools/CI do not enforce them.

## Research Directions
- Policy-as-code patterns for agent systems.
- Automated risk scoring for diffs to route reviews.
- Governance metrics: prevented incidents vs friction cost.

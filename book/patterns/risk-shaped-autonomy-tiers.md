# Risk-Shaped Autonomy Tiers

## Context

An AI engineering harness can do real work: edit files, run commands, open PRs, and trigger deployments. The same capability that makes it useful also makes it dangerous.

Most organizations try to manage this with “always allow” or “never allow.” Both fail:

- Always allow turns small model mistakes into large incidents.
- Never allow turns the harness into a chat assistant and pushes work back to humans.

## Problem

How do you scale autonomy without scaling incidents?

Specifically: how do you decide *how much autonomy* to grant for a given task in a way that is predictable, auditable, and aligned to risk?

## Forces

- **Capability vs. blast radius**: the highest-leverage tools also have the largest impact.
- **Speed vs. governance**: approvals add latency, but lack of approvals makes accountability fuzzy.
- **Variance vs. repeatability**: autonomy must be predictable across runs; “it depends” is not a policy.
- **Local correctness vs. global safety**: a patch can be locally correct and still risky if it touches protected surfaces.
- **Policy drift**: rules that live only in prompts drift; rules enforced by the harness/router are stable.

## Solution

Define explicit autonomy tiers and enforce them in the harness, not the model.

Each tier specifies:

- Tool allowlist and permission scopes
- Budgets (steps, time, patch locality)
- Required verification gates
- Approval requirements
- Trace and evidence requirements before completion

A practical tier set (adapt to your repo):

- **Tier 0 (Observe)**: read/search only. No side effects.
- **Tier 1 (Patch)**: bounded patch edits in non-protected paths. Requires at least one quality gate and one correctness gate.
- **Tier 2 (Change-set)**: multi-file changes in a bounded area, may update configs. Requires broader verification (build/typecheck + targeted tests) and may require reviewer approval.
- **Tier 3 (Release/Prod-facing)**: anything that can affect production or security posture (deploy configs, auth, secrets, CI/workflows). Requires explicit governance approval and strong verification; often requires a human in the loop.

Tier selection is based on *risk signals* the harness can observe:

- Touched paths (protected vs non-protected)
- Diff size and locality (files/lines)
- Tool class (read-only vs side-effect)
- External effects (network calls, ticket creation, deployment triggers)
- Verification availability (can we run the gates?)

The harness should support controlled escalation:

- Default to the *lowest tier that can complete the task*.
- Escalate only when the current tier is blocked by an objective constraint.
- Record the escalation reason and required approvals in the trace.

## Implementation sketch

Represent tiers as policy objects.

Minimal tier schema (conceptual):

```yaml
tiers:
  T0:
    tools: [read_file, grep_search, list_dir]
    budgets: { max_steps: 10 }
    required_gates: []
    approvals: []
  T1:
    tools: [read_file, grep_search, apply_patch, get_errors, run_in_terminal]
    budgets: { max_steps: 20, max_files_changed: 3, max_lines_changed: 200 }
    required_gates: ["format_or_lint", "targeted_test_or_build"]
    approvals: []
  T2:
    tools: [read_file, grep_search, apply_patch, run_in_terminal]
    budgets: { max_steps: 30, max_files_changed: 10, max_lines_changed: 800 }
    required_gates: ["lint", "typecheck_or_build", "targeted_tests"]
    approvals: ["code_review"]
  T3:
    tools: [read_file, grep_search, apply_patch, run_in_terminal]
    budgets: { max_steps: 40, max_files_changed: 20, max_lines_changed: 1200 }
    required_gates: ["security_scan", "full_tests", "deployment_dry_run"]
    approvals: ["governance_approval", "security_review"]
```

Selection algorithm (simple, harness-first):

1. Infer action class from intent/tool request (read-only, patch edit, dependency change, release).
2. Compute risk signals from the proposed working set or diff (protected paths, workflow files, secrets, size).
3. Map signals to a minimum tier.
4. Enforce the tier: reject tools outside the allowlist; reject patches that exceed locality budgets.
5. Route to required gates and require evidence in the trace before “success.”

Escalation protocol:

- If a tier blocks progress (for example, required gate cannot run), stop as **blocked** or request a **waiver** (see “Waiver Ledger” pattern) rather than silently skipping.
- If the task requires a protected edit, request approval and escalate tier; record approver and timestamp.

## Concrete examples

### Example 1: Low-risk documentation patch

Task: “Fix a typo in a chapter and run markdownlint.”

- Risk signals: non-protected path, small diff, no external side effects.
- Tier: **Tier 1 (Patch)**.
- Gates: run markdown lint or `mkdocs build` and capture the output.
- Evidence: trace includes the exact command and exit code.

Outcome: fast, autonomous completion with objective evidence.

### Example 2: CI/workflow edit with governance approval

Task: “Adjust GitHub Actions permissions to add `id-token: write`.”

- Risk signals: protected path (`.github/workflows/...`), security posture change.
- Tier: **Tier 3 (Release/Prod-facing)**.
- Gates: security scan, workflow lint/validation, and a dry-run in a controlled environment.
- Approvals: governance + security review required *before* the patch tool can apply changes.

Outcome: the harness prevents silent privilege expansion and forces a reviewable change.

## Failure modes

- **Tier inflation**: everything ends up Tier 3, and people bypass the harness.
  - Mitigation: make Tier 1 genuinely useful and fast; keep Tier 3 narrow and well-defined.
- **Tier blindness**: selection ignores path sensitivity; risky edits happen in Tier 1.
  - Mitigation: enforce protected paths in the router/kernel, not in prompts.
- **Gaming by decomposition**: a risky change is split into many small Tier 1 edits.
  - Mitigation: detect repeated edits to protected surfaces; use cumulative locality budgets per run.
- **Escalation without evidence**: tiers are escalated “because it seems hard.”
  - Mitigation: require an objective blocker reason (missing permission, failing gate, protected path).
- **Verification-as-theater**: gates are declared but not run.
  - Mitigation: require gate artifacts (exit code, logs) in the trace for success.

## When not to use

- One-off, single-purpose automation where a deterministic script is safer.
- Teams without the ability to maintain policy definitions, protected-path lists, and approval workflows.
- Situations where the real risk is not observable in diffs/tools (for example, domain-specific compliance) and you cannot encode that risk into gates or approvals.

# Waiver Ledger (Exceptions Are Data)

## Context

In a governed harness, certain gates are mandatory: tests, linting, security scans, approvals. In reality, gates sometimes cannot run:

- The environment is missing a tool.
- A test suite is flaky.
- A dependency registry is down.
- A required approval is unavailable.

Without a formal mechanism, teams handle this informally (“ship anyway”), and the harness becomes less trustworthy over time.

## Problem

How do you allow exceptions without turning governance into a pile of tribal knowledge?

You need a way to:

- Make exceptions explicit and reviewable.
- Capture why the gate was skipped and what risk remains.
- Turn waivers into measurable data for later improvement.

## Forces

- **Delivery pressure**: teams will route around gates if the system makes exceptions impossible.
- **Auditability**: “we skipped tests” must be visible and attributable.
- **Expiration**: exceptions tend to become permanent unless forced to expire.
- **Incentives**: if waivers are easy, they become the default.
- **Evidence-first**: even when a gate is waived, you should capture alternative evidence.

## Solution

Create a **waiver ledger**: a structured, append-only record of exceptions.

The harness treats “cannot satisfy a required gate” as one of two outcomes:

- **Blocked**: stop with reproduction steps.
- **Waived**: proceed only if a waiver record exists with required metadata and approvals.

Waivers are not a prompt instruction. They are a governed artifact that the harness can validate.

A waiver record should include:

- What gate was waived
- Why it was not runnable
- What alternative evidence was produced
- Risk assessment and affected surfaces
- Who approved it
- Expiration (time or condition)
- Links to trace IDs / diffs / incident tickets

## Implementation sketch

### Ledger format

Use a machine-readable format (JSON/YAML) and treat it as an audit artifact.

Minimal waiver schema (conceptual):

```json
{
  "waiver_id": "W-2026-02-23-001",
  "created_at": "2026-02-23T18:22:10Z",
  "scope": {
    "repo": "ai-first-software-engineering-book",
    "diff_fingerprint": "sha256:...",
    "paths": ["book/patterns/..."]
  },
  "gate": {
    "name": "mkdocs_build",
    "required_by_policy": true
  },
  "reason": {
    "category": "environment",
    "summary": "mkdocs build runner unavailable in CI",
    "details": "CI runner image missing mkdocs; scheduled fix in platform backlog"
  },
  "alternative_evidence": [
    {"type": "local_run", "command": "uv run mkdocs build", "exit_code": 0}
  ],
  "risk": {
    "level": "low",
    "notes": "Docs-only change; no runtime code"
  },
  "approvals": [
    {"role": "maintainer", "by": "alice", "at": "2026-02-23T18:30:00Z"}
  ],
  "expires": {
    "at": "2026-03-01T00:00:00Z",
    "condition": "CI image includes mkdocs"
  }
}
```

### Harness behavior

- When a required gate fails for non-actionable reasons, the harness requests a waiver rather than declaring success.
- The router validates that a waiver is present, unexpired, and covers the diff fingerprint.
- The trace references the waiver ID and includes the alternative evidence bundle.
- Policy can cap waiver usage per tier or per protected surface.

### Using waivers as data

A waiver ledger is useful only if it is queried:

- Track counts by gate, reason category, and team.
- Identify chronic sources of blockage (flaky tests, missing tooling).
- Enforce auto-expiration and “waiver debt” work items.

## Concrete examples

### Example 1: Flaky integration tests during a low-risk change

Task: “Update docs and run build.”

- Required gate: `mkdocs build`.
- Gate fails in CI due to a transient filesystem error.

Outcome:

- The harness runs the gate locally and captures logs.
- A maintainer approves a short-lived waiver that covers this diff fingerprint.
- The run completes with evidence + waiver ID.

This keeps shipping possible while retaining auditability.

### Example 2: Missing security scan tool blocks a protected-path edit

Task: “Edit a workflow to fix a CI regression.”

- Required gates: security scan + workflow validation.
- Security scan tool is unavailable.

Outcome:

- The harness refuses to proceed without a waiver.
- The waiver requires explicit security approval and an alternative evidence step (for example, run scan in a different environment or manual review checklist).
- The waiver expires quickly and is linked to a backlog item to restore the tool.

This prevents “temporary” exceptions from silently becoming permanent.

## Failure modes

- **Waiver sprawl**: waivers become the normal path.
  - Mitigation: approvals, expiration, and per-gate limits; treat repeated waivers as incidents.
- **No alternative evidence**: waivers are used as blank checks.
  - Mitigation: require at least one alternative evidence item and record it in the trace.
- **Unbounded scope**: a waiver applies to unrelated diffs.
  - Mitigation: bind waivers to a diff fingerprint + path scope.
- **No expiry**: exceptions persist forever.
  - Mitigation: enforce expiration at the harness level; reject expired waivers.
- **Ledger ignored**: data exists but is not acted on.
  - Mitigation: dashboards or scheduled reviews; treat chronic waivers as governance debt.

## When not to use

- Teams unwilling to enforce approvals and expiration (the ledger will become noise).
- Situations where exceptions are unacceptable by policy (for example, regulated releases requiring specific attestations).
- Very small projects where a simple “blocked” outcome is sufficient and waivers would add bureaucracy.

# Harness Design Patterns

## Context
A model alone is a general-purpose component. Production behavior is shaped by the harness: prompts, tools, memory, budgets, verification, and traceability.

## Problem
How do you design a harness that is reliable, debuggable, and governable without building a fragile tangle of special cases?

## Forces
- **Constraints vs. coverage**: adding constraints improves safety but can reduce task coverage.
- **Tools vs. surface area**: more tools increase capability but enlarge the debug and governance surface.
- **Memory vs. drift/privacy**: continuity improves with memory, but so do drift and data handling risks.
- **Automation vs. blast radius**: stronger automation improves throughput but increases the impact of failures.
- **Observability vs. cost**: better tracing and verification cost time and compute.

## Solution
Use a small set of recurring harness patterns that are easy to audit and compose.

### Pattern 1: Typed Tool Boundary
- **Idea**: tools are the only way to cause side effects, and each tool has a typed schema with explicit errors.
- **Why it works**: reduces ambiguity and makes traces auditable.
- **Example**: `create_file(path, content)` returns `created | updated | no_op`, plus a checksum.

### Pattern 2: Budgeted Control (Steps/Time/Cost)
- **Idea**: the kernel enforces budgets; the model cannot override them.
- **Why it works**: turns open-ended iteration into a bounded process.
- **Example**: max 20 steps or 5 minutes; on exhaustion, stop with a partial report.

### Pattern 3: Evidence-First Completion
- **Idea**: “done” requires verifiable evidence (tests run, diffs applied, outputs captured).
- **Why it works**: prevents completion based on plausibility alone.
- **Example**: stop is rejected unless verification artifacts exist in the trace.

### Pattern 4: Narrow Context Construction
- **Idea**: select only the files needed for the next action; summarize the rest.
- **Why it works**: reduces context bloat and keeps constraints salient.
- **Example**: open 2–4 files max, keep a rolling summary of prior steps.

### Pattern 5: Separation of Duties (Plan vs. Execute vs. Verify)
- **Idea**: treat these as distinct phases with distinct constraints.
- **Why it works**: limits the ability to bypass controls (for example, editing policies during execution).
- **Example**: planning cannot call side-effect tools; verification cannot modify code.

## Implementation sketch
Minimal harness components:

- **Kernel**: step loop, budgets, cancellation/timeouts, trace append.
- **Tool router**: allowlist + argument validation + consistent error model + idempotency support.
- **Context builder**: file selection + summarization policy + retrieval policy.
- **Verifier**: runs evals/tests and records outputs.
- **Governance layer**: approvals for high-risk tools, audit logs, retention/redaction rules.

A small harness configuration can be expressed as a policy document (conceptual):

```yaml
tools:
  allowlist: [read_file, grep_search, apply_patch, get_errors, run_in_terminal]
budgets:
  max_steps: 20
  max_minutes: 5
stop_gate:
  require_verification: true
  acceptable_outcomes: ["verified", "blocked"]
```

### Concrete example
Repo task agent that edits documentation:

- Tools: `read_file`, `grep_search`, `apply_patch`, `get_errors`.
- Budgets: 15 steps, 3 minutes.
- Stop gate: markdown checks (or at minimum a syntax/lint pass) must be clean, or the run stops as “blocked” with reproduction steps.

## Failure modes
- **Tool sprawl**: too many overlapping tools; selection becomes inconsistent and hard to audit.
- **Hidden side effects**: tools mutate state without reporting it; traces become misleading.
- **Context bloat**: prompts include too much content; constraints and acceptance criteria are diluted.
- **Policy bypass**: weak allowlists or validation enable unintended actions.
- **Unmeasured changes**: no evals/verification; regressions ship silently.
- **Over-coupling**: harness depends on brittle prompt wording instead of enforceable kernel/router constraints.

## When not to use
- Single-purpose automation where a deterministic script is simpler.
- One-off exploratory work where harness engineering overhead dominates.
- Systems without ownership/ops capacity to maintain tools, budgets, verification, and incident response.

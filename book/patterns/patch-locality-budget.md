# Patch Locality Budget (Blast-Radius Caps)

## Context

Autonomous edits fail in two common ways:

- They are *too small*: a partial fix that compiles locally but breaks a contract elsewhere.
- They are *too large*: a sweeping patch that touches many files, makes review hard, and amplifies mistakes.

A harness can reduce incident risk by bounding how far a single patch is allowed to reach.

## Problem

How do you keep autonomous patches reviewable and safe by limiting their blast radius, without preventing legitimate multi-file changes?

You want a control that is objective, enforceable, and traceable.

## Forces

- **Completeness vs. locality**: some changes are inherently cross-cutting.
- **Reviewability**: smaller diffs are easier to audit; larger diffs hide mistakes.
- **Intermediate states**: forcing small patches can create temporary breakage unless verification is staged.
- **Budget interactions**: patch caps interact with step budgets; too tight means budget exhaustion.
- **Protected surfaces**: locality alone is not enough; some paths must be gated regardless of size.

## Solution

Introduce a **patch locality budget** enforced by the harness:

- Cap the number of files changed per patch.
- Cap total lines changed (and optionally per file).
- Cap the allowed path scope (a working set).
- Require staged verification per patch or per group of patches.

Locality caps convert “don’t be risky” into a measurable, enforceable constraint. When a task truly requires a wider blast radius, the harness forces an explicit escalation: higher tier, stronger gates, or an approval.

## Implementation sketch

### Locality metrics

Track locality per patch and cumulatively per run:

- `files_changed`
- `lines_added`, `lines_removed`, `lines_changed`
- `path_scopes` (for example, `book/`, `src/`, `.github/`)
- `protected_paths_touched` (boolean)

### Enforcement

A simple enforcement policy:

- Reject patches that exceed `max_files_changed` or `max_lines_changed` for the current autonomy tier.
- Reject patches that touch files outside the scoped working set.
- If a patch touches a protected path, route to approval + stronger gates regardless of size.

Example tier-locality configuration (conceptual):

```yaml
locality_budgets:
  T1:
    max_files_changed: 3
    max_lines_changed: 200
    allowed_scopes: ["book/", "docs/"]
  T2:
    max_files_changed: 10
    max_lines_changed: 800
    allowed_scopes: ["book/", "docs/", "src/"]
  T3:
    max_files_changed: 20
    max_lines_changed: 1200
    allowed_scopes: ["*"]
    requires_approval_on_protected_paths: true
```

### Chunking strategy

When a patch exceeds the budget, split work into a small number of coherent chunks:

- Establish a *working set* in a Scout phase.
- Apply one patch chunk.
- Run the minimum gates that prove that chunk is safe.
- Repeat until completion.

The key: the harness enforces chunk boundaries; the model does not “promise” to keep the diff small.

## Concrete examples

### Example 1: Constrain a refactor to a safe blast radius

Task: “Rename a function and update call sites.”

Locality budget:

- 3 files max per patch, 200 lines max.

Execution:

- Patch 1: rename in definition file + update the closest call sites.
- Verify: run targeted unit tests for the changed module.
- Patch 2: update remaining call sites.
- Verify again.

Result: reviewable diffs and faster debugging when something breaks.

### Example 2: Prevent accidental repo-wide churn

Task: “Update formatting across the repository.”

Locality budget:

- Tier 1 rejects the patch because it changes too many files.

Outcome:

- The harness forces a deliberate escalation to a higher tier with explicit approval and an agreed verification plan, or it blocks the task as out-of-policy.

Result: formatting churn doesn’t slip through as “just a small fix.”

## Failure modes

- **Fragmentation**: too-small budgets force many patches and consume iteration budgets.
  - Mitigation: calibrate budgets per repo; allow Tier 2 for legitimate multi-file work.
- **Broken intermediate states**: chunking introduces temporary breakage.
  - Mitigation: require staged gates; keep each chunk internally consistent.
- **Scope mismatch**: locality caps prevent necessary cross-cutting updates.
  - Mitigation: use Scout to establish the working set and escalate tier when justified.
- **False safety**: a small patch can still be high-risk (for example, auth config).
  - Mitigation: combine locality with protected-path routing and approvals.
- **Gaming by repetition**: many small patches to the same sensitive surface.
  - Mitigation: enforce cumulative locality budgets and protected-surface thresholds per run.

## When not to use

- Very small repos where reviewability is not a limiting factor and the overhead is unnecessary.
- Teams that require large, mechanically-generated changes regularly (unless you can safely escalate with approvals and strong gates).
- Situations where the primary risk is semantic (business logic, compliance) and locality caps do not correlate with safety.

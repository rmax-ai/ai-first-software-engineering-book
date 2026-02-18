# Self-Verification Loop

## Context
Model outputs often look plausible but can be wrong in subtle ways: incorrect assumptions about repo structure, stale APIs, missing edge cases, or incomplete updates across files. In engineering work, “sounds right” is not an acceptance criterion.

## Problem
How do you force the system to *prove work* against objective checks before it declares completion?

## Forces
- **Verification cost** must be lower than expected rework cost.
- **Signal alignment**: checks must reflect real acceptance criteria, not proxy metrics.
- **Check gaming**: if checks are narrow, the system may satisfy them while violating intent.
- **Flakiness**: verification tools can fail nondeterministically (network, timing, unstable tests).
- **Side-effect boundaries**: verification should not introduce additional risky mutations.

## Solution
Make verification an explicit, mandatory phase with a stop gate:

1. **Define acceptance checks** (tests, lint, build, schema validation, golden diffs) and/or a bounded human-review checklist.
2. **Require evidence** in the trace: commands run, outputs captured, and artifacts produced.
3. **Gate completion**: the system may only stop when checks pass, or when it produces a bounded “blocked” report with reproduction steps and the smallest viable next action.

The key behavior change is procedural: “done” becomes a claim that must be backed by artifacts.

## Implementation sketch
Use a two-part contract per task:

- **Work**: changes made (patches/files) and the intended behavior.
- **Verification**: list of checks and their outcomes, including raw outputs or pointers to captured logs.

Suggested verification record shape:

```yaml
verification:
  - check: "unit tests"
    command: "npm test"
    status: pass
    evidence: "stdout excerpt or attached log"
  - check: "lint"
    command: "npm run lint"
    status: fail
    evidence: "..."
    next_action: "Fix unused import in src/cli.ts"
```

Practical gating logic:

- If checks pass: stop.
- If checks fail with actionable errors: attempt bounded repair (for example, up to 2 iterations).
- If failures are environmental/flaky: stop with a “blocked” report and clear reproduction steps.

### Concrete example
Task: “Add a new CLI flag and update docs.”

Work:
- Implement parsing for `--format json`.
- Update `README` usage section.

Verification:
- Run unit tests that cover the new flag.
- Run a help-text snapshot (golden file) test.
- Run linter/formatter.

Example evidence-oriented trace snippet:

```text
$ mycli --help
... includes "--format" ...

$ npm test
PASS cli.test.ts (12 tests)

$ npm run lint
0 problems
```

## Failure modes
- **Rubber-stamp verification**: the system asserts checks passed without running them or without capturing outputs.
- **Proxy mismatch**: checks pass but requirements are unmet (acceptance criteria were incomplete or untested).
- **Check gaming**: tests are modified to match incorrect behavior; the suite becomes less meaningful.
- **Flaky verification loop**: intermittent failures trigger repeated repairs and wasted budget.
- **Over-verification**: too many slow checks push verification out of the critical path and encourage skipping.
- **Unsafe verification**: verification steps include side-effectful actions (publishing, migrations) without approvals.

## When not to use
- Low-impact drafts where verification cost dominates (early outlines, brainstorming, rough notes).
- Environments where checks cannot run (missing tooling or permissions) and no acceptable substitutes exist.
- Tasks where human judgment is the primary signal and objective checks are weak (copy tone, early design exploration).

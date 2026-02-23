# Golden-Task Canary Suite

## Context

When a system includes an autonomous kernel, “does it still work?” is not one question. It is a distribution of tasks across tools, repos, prompts, and policies. Drift can come from model changes, tool changes, harness policy changes, dependency upgrades, or evolving repos.

A golden-task canary suite is a small set of pinned, representative tasks that run regularly to detect drift early. It aligns with evaluation-and-traces by requiring stable inputs and comparable evidence bundles over time.

## Problem

How do you detect regressions in agent performance and harness reliability before they show up as user pain or incidents?

Without a canary suite:

- Failures are discovered only when a real task is blocked.
- It’s hard to tell whether things got worse (no stable baseline).
- Fixes are hard to validate (no repeated, comparable tasks).

## Forces

- **Representativeness vs. size**: more tasks cover more behavior, but cost more to run and maintain.
- **Pinning vs. freshness**: pinning inputs improves comparability but can diverge from real work.
- **Flakiness vs. sensitivity**: noisy tasks produce false alarms; overly stable tasks miss regressions.
- **Gaming vs. learning**: if teams optimize only for canaries, they may overfit to the suite.
- **Governance**: canaries must respect tool policies and avoid unsafe side effects.

## Solution

Define 5–20 “golden tasks” that:

- Are small enough to run frequently.
- Exercise the critical tool boundary and verification gates.
- Produce an evidence bundle and trace that can be compared run-to-run.
- Are pinned to stable inputs (fixtures, repo SHA, harness version, budgets).

Treat the suite as a canary: it is not a full benchmark, and it is not a replacement for product acceptance tests. It is an early warning system.

## Implementation sketch

Task definition fields (conceptual):

- `task_id`: stable identifier
- `goal`: the prompt/intent
- `fixture`: a pinned repo SHA or a small fixture repo directory
- `budgets`: max steps/time/cost
- `required_gates`: checks that must run
- `expected_outcome`: verified | blocked (with expected signature)
- `metrics`: what to record (iterations-to-pass, gate failures, bundle sizes)

Example YAML structure:

```yaml
golden_tasks:
  - task_id: "docs_markdownlint"
    goal: "Fix one markdownlint error in a pattern page and verify"
    fixture:
      repo_sha: "<pinned sha>"
      working_dir: "."
    budgets:
      max_steps: 12
      max_minutes: 3
    required_gates:
      - "markdownlint"
      - "mkdocs_build"
    expected_outcome: "verified"
    metrics:
      - "steps_used"
      - "verification_pass"
      - "bundle_bytes"

  - task_id: "unit_bugfix"
    goal: "Fix a failing unit test in a small module and verify"
    fixture:
      repo_sha: "<pinned sha>"
    budgets:
      max_steps: 18
      max_minutes: 5
    required_gates:
      - "unit_tests"
    expected_outcome: "verified"
    metrics:
      - "steps_used"
      - "test_failures_before_pass"
```

Runner requirements:

- Runs tasks on a schedule (nightly, per-merge, or weekly depending on cost).
- Enforces pinning: same repo SHA (or fixture) per baseline.
- Produces standard artifacts: trace + evidence bundle for every task.
- Records metrics to a time series (even a simple JSON history is enough).

Drift signals to watch:

- Increasing steps-to-pass.
- Increasing blocked outcomes.
- New failure signatures (from the failure-signature index).
- Growing bundle sizes (a proxy for instability/noise).

## Concrete examples

### Example 1: Documentation canary for evaluation gates

Task: “Make a small markdown edit and prove the book still builds.”

- Fixture: pinned repo SHA.
- Gates: `markdownlint` and `mkdocs build`.
- Expected outcome: `verified`.

This canary detects:

- Markdown formatting regressions.
- Build tool regressions.
- Harness regressions that stop capturing evidence or running gates.

### Example 2: Code canary that exercises repair and verification

Task: “Fix a tiny seeded bug that causes one unit test to fail.”

- Fixture: a dedicated branch/SHA with a known failing test.
- Gates: `pytest -q`.
- Expected outcome: `verified`.

This canary detects:

- Tool routing issues (test runner invocation).
- Model/harness regressions in diagnosing and applying a minimal patch.
- Verification regressions (failing to rerun tests or capture outputs).

## Failure modes

- **Overfitting to the suite**: the system improves on canaries but degrades on real tasks.
  - Mitigation: rotate a small portion of tasks quarterly; track a separate set of real-task metrics.
- **Stale fixtures**: pinned SHAs become irrelevant and stop detecting real regressions.
  - Mitigation: periodically refresh fixtures while preserving a “historical baseline” track.
- **Flaky canaries**: nondeterministic tasks produce alert fatigue.
  - Mitigation: remove network dependencies; seed randomness; require two consecutive failures before paging.
- **Too many tasks**: suite becomes expensive and gets skipped.
  - Mitigation: keep it small; prioritize tasks with the highest operational leverage.
- **Unsafe tasks**: canaries accidentally perform side effects (publishes, deploys).
  - Mitigation: run in a sandboxed environment with strict tool allowlists and dry-run modes.

## When not to use

- Teams without the ability to run scheduled tasks or store artifacts.
- Environments where you cannot pin inputs (repo SHA, fixture data, tool versions).
- Extremely early prototypes where task definitions change daily and baselines would churn.

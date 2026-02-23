<!-- markdownlint-disable MD022 MD032 MD007 MD046 -->
# Chapter 05 — Evaluation and Traces

## Thesis
Evaluation and traceability make AI-first engineering reproducible.
Traces provide evidence that links outcomes to the correct layer (model, tool, harness, or missing tests).
Evaluations turn that evidence into gates that prevent incorrect changes from being accepted.

Hypothesis: without trace-first design, teams cannot reliably distinguish a model error (wrong edit suggestion) from a tool error (command failed).
They also cannot distinguish harness errors (applied the wrong diff or wrong working directory) from missing tests (a real regression that was not checked).

## Why This Matters
- Reproducibility is a prerequisite for iterative improvement.
- Evaluation gates define the autonomy envelope and prevent silent regressions.
- Traces enable post-incident analysis and systematic harness refinement.

## System Breakdown
- **Trace schema** (minimum viable):
  - task id
  - plan
    - intended steps
    - stop conditions
  - tool calls
    - tool name
    - arguments
    - start/end timestamps
    - exit status
  - tool outputs
    - stdout/stderr excerpts, or pointers to stored artifacts
  - diffs
    - patches applied
    - file paths touched
  - evaluation results
    - which checks ran
    - pass/fail
    - key failure signatures
  - budgets
    - time
    - iteration count
    - token/cost limits (if applicable)
  - stop reason
    - completed
    - blocked by gate
    - permission denied
    - budget exceeded
  - redaction policy
    - what is removed or hashed (secrets, tokens, PII, proprietary paths)
  - environment fingerprint
    - repo URL (if applicable)
    - commit SHA
    - branch
    - tool versions
    - OS/arch
  - retry/iteration counters
    - attempt number per step
    - total loop count
  - Query examples (incident review):
    - “show all tasks that modified `pyproject.toml` and failed secret scanning”
    - “list failures where `tests` failed but a patch was still applied”
    - “group stop reasons by action class over the last N runs”
- **Evaluation types**:
  - correctness: unit/integration/contract tests.
  - safety: permission checks, protected paths, secret scanning.
  - quality: lint, type checks, formatting, doc checks.
  - performance: benchmarks, latency/cost budgets.
- **Gating model**: which evaluations are required for which action classes.
  
  A gating model is only useful if the trace explains the choice.
  A reviewer should be able to see why a gate passed, failed, or was skipped.

  A diagram helps here because the logic is a decision flow.
  Focus on the first safety decision and the first failing gate.

```mermaid
flowchart TB
  A[Action class selected] --> B[Safety gate(s)\n(permission / protected-path / secret scan)]
  B -->|fail| S1[STOP\nstop_reason set\nrecord: failure_signature + touched_paths]
  B -->|pass| C[Required evaluations\nquality + correctness + performance]
  C --> D{Any required eval missing?}
  D -->|yes| S2[STOP\nstop_reason set\nrecord: skipped_reason + selection_reason]
  D -->|no| E{Any eval failed?}
  E -->|yes| S3[STOP\nstop_reason set\nrecord: command + exit_status + failure_signature]
  E -->|no| F[CONTINUE / COMPLETE\nrecord: evaluation_results + budgets\nstop_reason=completed]
```

  After you review the flow, the key takeaway is this: every STOP is a first-class outcome.
  The trace must record enough to explain the stop and replay the same checks.

  Legend:
  - Diamonds are harness decision points.
  - Every STOP must record enough fields to replay the same checks.

  - Minimal gating matrix (example, stated as rules):

    - read-only (grep/view/list):
      - safety: require permission check for accessed path(s)
      - quality: skip; record `skipped_reason: "read_only_action"`
      - correctness: skip; record `skipped_reason: "read_only_action"`
      - performance: skip; record `skipped_reason: "read_only_action"`

    - patch edit (apply diff to code/docs):
      - safety:
        - require protected-path check for all touched files
        - if any touched file is protected:
          - stop with `stop_reason: "permission_denied"`
      - quality:
        - require lint/typecheck if repo has config
        - otherwise record `skipped_reason: "no_config"`
      - correctness:
        - require targeted tests for touched modules
        - selection order:
          1) if a module→test mapping exists:
             - run the mapped command
             - record `selection_reason: "mapping"`
          2) else if the plan declares `test_command`:
             - run it
             - record `selection_reason: "plan.test_command"`
          3) else if the repo declares a default test command:
             - run it
             - record `selection_reason` with the source path
          4) else if a stack can be detected:
             - run the stack fallback command
             - record `selection_reason: "fallback.detected_stack"`
          5) else:
             - record `skipped_reason: "no_test_runner_detected"`
             - stop with `stop_reason: "blocked_by_correctness_gate"`
      - fallback by detected stack:
        - Deterministic stack detection (precedence order):
          - Inputs:
            - touched file paths from the diff (after patch application)
            - repo evidence files (repo root only)
          - Step 1 — candidates from touched paths:
            - Python if any touched path ends with `.py`
            - Node if any touched path ends with `.js`, `.jsx`, `.ts`, or `.tsx`
            - Go if any touched path ends with `.go`
          - Step 2 — if no candidates, use evidence files:
            - Python if `pyproject.toml`, `pytest.ini`, `setup.cfg`, or `requirements.txt` exists
            - Node if `package.json` exists
            - Go if `go.mod` exists
          - Step 3 — tie-break precedence:
            - Python → Node → Go
          - Trace requirements:
            - record `selection_reason` (example: `touched_ext:.py`)
            - record `detected_stacks` before tie-break (example: `[python,node]`)
        - Python: `pytest -q`
        - Node: `npm test`
        - Go: `go test ./...`
      - performance:
        - require only when applicable
        - require if any touched path is under `deploy/`
        - require if any touched path is under `prod/`
        - require if the plan declares `latency_budget_ms` or `cost_budget_usd`
        - otherwise record `skipped_reason: "not_applicable"`

    - dependency install (lockfile changes, package adds):
      - safety:
        - require secret scan of the diff and updated lockfile(s)
        - record scan tool name
        - record any hit signatures
      - safety:
        - require protected-path check for touched files
        - if blocked, stop with `stop_reason: "permission_denied"`
      - quality:
        - require lint/typecheck if repo has config
        - otherwise record `skipped_reason: "no_config"`
      - correctness:
        - require tests that import the changed dependency
        - if unknown, select a command using the patch-edit rule
        - record `selection_reason` for the path taken
      - performance:
        - require only when runtime or deploy files change
        - examples: `Dockerfile`, `deploy/**`
        - otherwise record `skipped_reason: "not_applicable"`

    - deploy/release (publish, migrate, prod config):
      - safety:
        - require explicit permission grant
        - record grant artifact (id or prompt) in the trace
      - safety:
        - require secret scan
        - stop on any forbidden hit
        - record hit signatures
      - quality:
        - require lint/typecheck if configured
        - otherwise record `skipped_reason: "no_config"`
      - correctness:
        - require full suite or contract tests for release
        - record suite name and command
      - performance:
        - require if a budget is declared in the plan
        - stop if exceeded
        - record measured values

## Concrete Example 1
Tracing a refactor.

- Record each patch, each test run, and each failure signature.
- Also record the environment fingerprint and exact tool invocations.
- That combination lets a reviewer replay the same sequence.

Pseudo-trace excerpt (illustrative):

    task_id: refactor-auth-2026-02-22-001

    environment:
      repo_sha: a1b2c3d
      tool_versions:
        pytest: 8.1.1
        python: 3.12.1

    plan:
      - rename AuthClient -> CopilotClient
      - update imports
      - run targeted tests
      - stop if tests fail

    tool_calls:
      - tool: apply_patch
        files:
          - src/auth/client.py
        exit_status: 0
      - tool: bash
        cmd: pytest -q tests/test_auth_client.py::test_retry
        exit_status: 1
        failure_signature: ImportError: cannot import name 'AuthClient'

    diffs:
      - path: src/auth/client.py
        summary: renamed symbol
      - path: tests/test_auth_client.py
        summary: unchanged

    evaluation_results:
      correctness:
        cmd: pytest -q tests/test_auth_client.py::test_retry
        outcome: FAIL
        signature: ImportError

    stop_reason: blocked_by_correctness_gate

Query step using structured fields (one possible workflow):
- Query: `repo_sha == "a1b2c3d" AND failure_signature CONTAINS "ImportError: cannot import name 'AuthClient'" AND diffs.paths CONTAINS "src/auth/client.py"`
- Result (summary):
  - matching_tasks: 3
  - last_success_task_id: `refactor-auth-2026-02-20-007`
  - last_success_repo_sha: `a1b2c3d`
  - common_missing_patch_pattern: diffs do not include any files under `src/auth/__init__.py` or `src/auth/*` besides `client.py`

Decision rule using the query result:
- If `last_success_repo_sha` matches the current `repo_sha`:
  - If only `client.py` was changed, expand patch scope to import sites.
  - Update `src/auth/__init__.py` exports and import usages.
  - Rerun `pytest -q tests/test_auth_client.py::test_retry`.
- If `last_success_repo_sha` differs:
  - Rebase/reset to the pinned `repo_sha` first.
  - Apply the expanded patch.
  - Rerun `pytest -q tests/test_auth_client.py::test_retry`.

Attribution using the trace:
- Model vs tool is not ambiguous here.
- The patch tool succeeded, and the test runner executed.
- The failure signature is a stable ImportError.
- The diffs show a narrow touch pattern, so the likely cause is refactor incompleteness.

## Concrete Example 2
Drift detection for an agent loop.

- Maintain a stable eval suite and a small set of “golden” tasks.
- A “golden task” should include:
  - fixed input prompt and any fixed attachments
  - fixed repo state (commit SHA) or a pinned fixture repository
  - expected outcome constraints (e.g., “touch only `src/foo.py`”, “no network”, “no new dependencies”)
  - expected evaluations (which checks must pass)
  - budgets (max iterations, max wall time, max tool calls)
- Define a baseline run-set for each golden task.
  - Example: “last green run-set on release tag `vX.Y`”.
  - Keep repo_sha and harness version pinned for the baseline.

- Detect changes in iteration counts, regression rate, and stop reasons over time.
  - iteration drift:
    - median loop iterations in the most recent 50 runs increases by ≥ 30%
    - compare against the baseline’s 50-run median
  - regression rate:
    - correctness-gate failure rate in the most recent 50 runs increases by ≥ 5 percentage points
    - compare against the baseline’s 50-run rate
  - stop-reason shift:
    - in the most recent 50 runs, “budget exceeded” becomes the most frequent stop_reason
    - baseline window had “completed” as the most frequent stop_reason

The point is not to predict every future failure. The point is to detect that something changed (model, tool, harness, or repo) and to have enough trace evidence to localize the change.

## Trade-offs
- More evaluation increases confidence but costs time and compute.
- Rich traces help debugging but create storage and privacy burdens.
- Overly rigid gates can block progress on codebases with weak test coverage.

## Failure Modes
- **Eval gaming**: optimizing for metrics while harming real-world quality.
  - Detect: compare “passes gates” with downstream signals in traces (reverts, follow-up bugfix tasks, repeated failures on adjacent golden tasks); watch for large diffs with minimal test coverage.
  - Respond: add adversarial or regression tests, strengthen gate definitions (e.g., require touched-module tests), and record coverage/selection rationale in the trace.
- **Blind spots**: evaluations do not cover critical behaviors.
  - Detect: incidents where traces show “all gates passed” but production-like behavior fails; repeated similar failures without corresponding eval signatures.
  - Respond: add contract tests or invariants to the eval suite; introduce risk-based gating (e.g., stricter checks for auth/payment paths) and make the gating decision explicit in the trace.
- **Un-actionable traces**: logs exist but lack structure, making search and attribution hard.
  - Detect: inability to answer basic questions (“what changed?”, “what ran?”, “why did it stop?”) without reading raw logs; missing environment fingerprint or missing diff records.
  - Respond: enforce a minimal trace schema, store normalized fields for queries, and treat “missing trace fields” as an evaluation failure for non-trivial action classes.

## Research Directions
- Standard trace formats for portability across tools and models.
- Risk-based gating (stricter checks for higher-risk diffs).
- Low-cost evaluations that correlate with production outcomes.

<!-- markdownlint-enable MD022 MD032 MD007 MD046 -->

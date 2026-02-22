# Chapter 05 — Evaluation and Traces

## Thesis
Evaluation and traceability are the mechanisms that make AI-first engineering reproducible. Traces provide the evidence needed to attribute outcomes to the correct layer (model, tool, harness, or missing tests); evaluations turn that evidence into gates that prevent incorrect changes from being accepted.

Hypothesis: without trace-first design, teams cannot reliably distinguish model errors (wrong edit suggestion) from tool errors (command failed), harness errors (applied the wrong diff or wrong working directory), or missing tests (a real regression that was not checked).

## Why This Matters
- Reproducibility is a prerequisite for iterative improvement.
- Evaluation gates define the autonomy envelope and prevent silent regressions.
- Traces enable post-incident analysis and systematic harness refinement.

## System Breakdown
- **Trace schema** (minimum viable):
  - task id
  - plan (the intended steps and stop conditions)
  - tool calls (tool name, arguments, start/end timestamps, exit status)
  - tool outputs (stdout/stderr excerpts or pointers to stored artifacts)
  - diffs (patches applied, file paths touched)
  - evaluation results (which checks ran, pass/fail, key failure signatures)
  - budgets (time, iteration count, token/cost limits where applicable)
  - stop reason (completed, blocked by gate, permission denied, budget exceeded)
  - redaction policy (what is removed or hashed: secrets, tokens, PII, proprietary paths)
  - environment fingerprint (repo URL if applicable, commit SHA, branch, tool versions, OS/arch)
  - retry/iteration counters (attempt number per step, total loop count)
  - When used for incident review, the trace must support queries like:
    - “show all tasks that modified `pyproject.toml` and failed secret scanning”
    - “list failures where `tests` failed but a patch was still applied”
    - “group stop reasons by action class over the last N runs”
- **Evaluation types**:
  - correctness: unit/integration/contract tests.
  - safety: permission checks, protected paths, secret scanning.
  - quality: lint, type checks, formatting, doc checks.
  - performance: benchmarks, latency/cost budgets.
- **Gating model**: which evaluations are required for which action classes.
  - Minimal gating matrix (example, stated as rules):
    - read-only (grep/view/list):
      - safety: required permission check for the path(s) being accessed
      - quality: skipped; record `skipped_reason: "read_only_action"`
      - correctness: skipped; record `skipped_reason: "read_only_action"`
      - performance: skipped; record `skipped_reason: "read_only_action"`
    - patch edit (apply diff to code/docs):
      - safety: required protected-path check for all touched files; if any are protected, stop with `stop_reason: "permission_denied"`
      - quality: required if repo has lint/typecheck config; otherwise record `skipped_reason: "no_config"`
      - correctness: required targeted tests covering touched modules; if no mapping exists, select a test command deterministically:
        - if the plan declares `test_command`, run it
        - else if the repo declares a default test command, run it (e.g., in `Makefile`, `package.json`, or a CI config) and record the source as `selection_reason`
        - else run one fixed fallback based on detected stack and record `selection_reason`:
          - Python: `pytest -q`
          - Node: `npm test`
          - Go: `go test ./...`
        - else record `skipped_reason: "no_test_runner_detected"` and stop with `stop_reason: "blocked_by_correctness_gate"`
      - performance: required only if the diff touches paths under `deploy/` or `prod/`, or if a `latency_budget_ms`/`cost_budget_usd` is present in the plan; otherwise record `skipped_reason: "not_applicable"`
    - dependency install (lockfile changes, package adds):
      - safety: required secret scan of the diff and updated lockfile(s); required protected-path check
      - quality: required if repo has lint/typecheck config; otherwise record `skipped_reason: "no_config"`
      - correctness: required test subset that imports the changed dependency; if unknown, select a test command using the same deterministic rule as patch edit and record `selection_reason`
      - performance: required only if the change affects runtime images or deploy manifests (e.g., `Dockerfile`, `deploy/**`); otherwise record `skipped_reason: "not_applicable"`
    - deploy/release (publish, migrate, prod config):
      - safety: required explicit permission grant + secret scan; stop on any forbidden hit
      - quality: required lint/typecheck if configured; otherwise record `skipped_reason: "no_config"`
      - correctness: required full suite or contract tests defined for release; record suite name and command
      - performance: required if a budget is declared in the plan; stop if budget exceeded and record measured values

## Concrete Example 1
Tracing a refactor.

- Record: each patch + test run + failure signature, but also the environment fingerprint and the exact tool invocations so a reviewer can replay the same sequence.

Pseudo-trace excerpt (illustrative):

- task_id: `refactor-auth-2026-02-22-001`
- environment:
  - repo_sha: `a1b2c3d`
  - tool_versions: `{ "pytest": "8.1.1", "python": "3.12.1" }`
- plan: “rename `AuthClient` → `CopilotClient`; update imports; run targeted tests; stop if tests fail.”
- tool_calls:
  1) `{ "tool": "apply_patch", "files": ["src/auth/client.py"], "exit_status": 0 }`
  2) `{ "tool": "bash", "cmd": "pytest -q tests/test_auth_client.py::test_retry", "exit_status": 1, "failure_signature": "ImportError: cannot import name 'AuthClient'" }`
- diffs:
  - `src/auth/client.py`: renamed symbol
  - `tests/test_auth_client.py`: unchanged
- evaluation_results:
  - correctness: `pytest -q ...` → FAIL (ImportError)
- stop_reason: “blocked by correctness gate”

Query step using structured fields (one possible workflow):
- Query: `repo_sha == "a1b2c3d" AND failure_signature CONTAINS "ImportError: cannot import name 'AuthClient'" AND diffs.paths CONTAINS "src/auth/client.py"`
- Result (summary):
  - matching_tasks: 3
  - last_success_task_id: `refactor-auth-2026-02-20-007`
  - last_success_repo_sha: `a1b2c3d`
  - common_missing_patch_pattern: diffs do not include any files under `src/auth/__init__.py` or `src/auth/*` besides `client.py`

Decision rule using the query result:
- If `last_success_repo_sha` matches the current `repo_sha` and `common_missing_patch_pattern` shows only `client.py` was changed, then expand patch scope to import sites (e.g., update `src/auth/__init__.py` exports and any `from src.auth import AuthClient` usage) and rerun the same correctness command (`pytest -q tests/test_auth_client.py::test_retry`).
- If `last_success_repo_sha` differs, first rebase/reset to the pinned `repo_sha` before applying the expanded patch; then rerun the same correctness command.

Attribution using the trace:
- Not a model vs tool ambiguity: the patch tool succeeded and the test runner executed; the failure signature is a stable ImportError.
- Not a harness misapplication: matching_tasks share the same repo_sha and the diffs confirm the same single-file touch pattern.
- Likely root cause: refactor incompleteness (imports/usages not updated outside `client.py`); the next action is to expand the diff scope and re-run the same correctness gate.

## Concrete Example 2
Drift detection for an agent loop.

- Maintain: a stable eval suite and a small set of “golden” tasks.
  - A “golden task” should include:
    - fixed input prompt and any fixed attachments
    - fixed repo state (commit SHA) or a pinned fixture repository
    - expected outcome constraints (e.g., “touch only `src/foo.py`”, “no network”, “no new dependencies”)
    - expected evaluations (which checks must pass)
    - budgets (max iterations, max wall time, max tool calls)
- Detect: changes in iteration counts, regression rate, and stop reasons over time.
  - Define a baseline as a pinned reference run-set, such as “the last green run-set on release tag `vX.Y`” for the same golden task and the same repo_sha (or the same pinned fixture).
  - Example drift signals with thresholds (current window vs baseline window):
    - iteration drift: median loop iterations in the most recent 50 runs increases by ≥ 30% compared to the baseline’s 50-run median
    - regression rate: correctness-gate failure rate in the most recent 50 runs increases by ≥ 5 percentage points compared to the baseline’s 50-run rate
    - stop-reason shift: in the most recent 50 runs, “budget exceeded” becomes the most frequent stop_reason while the baseline window had “completed” as the most frequent stop_reason

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

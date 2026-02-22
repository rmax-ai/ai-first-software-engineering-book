# Chapter 02 — Harness Engineering

## Thesis
Harness engineering is the discipline of turning a general-purpose model into a predictable system by defining tool contracts, constraints, loop control, and evaluation gates.

In this chapter, “predictable” means three things. First, the same input context tends to produce the same classes of actions (repeatability). Second, the system’s allowed changes are bounded by explicit constraints (boundedness). Third, outputs can be accepted or rejected by checks rather than judgment calls (verifiability).

Hypothesis (falsifiable): for a fixed set of tasks and repositories, tightening the harness (schemas, budgets, gates, and recovery rules) reduces regression rate and rework more than swapping between models of similar capability. Prompts and task definitions are held constant.

## Why This Matters
- The same model can behave reliably or unreliably depending on tool schemas, budgets, and verification.
- Teams can standardize harness practices even when models change.
- Production safety and auditability primarily live in the harness layer.

## System Breakdown
- **Control plane**: prompts, policies, budgets, stop conditions.
- **Tool plane**: filesystem edits, build/test runners, linters, browsers, APIs.
- **Evaluation plane**: checks as gates; regression suites; quality rubrics.
- **State plane**: task ledger, traces, decisions, artifacts.
- **Interfaces**:
  - Tool schemas and error contracts.
  - Patch discipline (diff-only, small changes).
  - Evaluation API (what constitutes pass/fail).

A useful way to operationalize the planes is to name what each plane consumes, what it produces, and one metric you can track:

| Plane | Responsibilities | Key artifacts (inputs/outputs) | One measurable metric |
| --- | --- | --- | --- |
| Control plane | Decide what the agent is allowed to do and when to stop | Inputs: task brief, policy, iteration/time budget. Outputs: chosen strategy, stop reason | Iterations to first passing gate |
| Tool plane | Perform actions with bounded, typed interfaces | Inputs: tool calls with validated args. Outputs: patches, command outputs, structured errors | Patch locality (changed files/lines per task) |
| Evaluation plane | Decide if work is acceptable based on checks | Inputs: build/test/lint results, rubrics. Outputs: pass/fail + evidence | Gate pass rate (per iteration) |
| State plane | Record what happened and enable recovery | Inputs: events, diffs, tool outputs. Outputs: trace, ledger, artifacts for replay | Reproducibility rate (can rerun and get same pass/fail) |

The “minimal contract surface” is the set of interfaces that must be stable for predictability. It includes tool schemas (including error codes), patch discipline, and evaluation semantics.

## Concrete Example 1
Design a tool contract for “apply patch” operations.

A minimal schema sketch:

- Required fields:
  - `path`: absolute or repo-relative file path (must exist unless `create=true`)
  - `old_str`: exact original text to be replaced (must match uniquely)
  - `new_str`: replacement text
  - `context`: optional surrounding lines to disambiguate
- Constraints:
  - Reject edits that change unrelated whitespace outside the `old_str` region.
  - Reject edits that expand scope beyond the file (no implicit multi-file edits).
  - Reject edits that exceed a size budget (e.g., max changed lines per call).
- Error contract (examples):
  - `NOT_FOUND`: `path` does not exist and `create` is false
  - `NON_UNIQUE_MATCH`: `old_str` matches multiple locations
  - `NO_MATCH`: `old_str` matches zero locations (stale context)
  - `BUDGET_EXCEEDED`: change size violates configured limits
  - `POLICY_VIOLATION`: edit touches forbidden paths or patterns

Happy path flow:
1. Agent proposes a patch using a unique `old_str` block with minimal scope.
2. Harness validates: file exists, match is unique, diff stays within budgets.
3. Tool applies the patch and returns a structured result: changed line counts, a before/after snippet, and a stable identifier for the diff.

Conflict recovery (when the patch fails with `NO_MATCH` or `NON_UNIQUE_MATCH`):
1. The harness returns the error code plus a short “fresh context” snippet around the closest match (or a list of candidate match ranges).
2. The agent re-reads the relevant portion of the file and regenerates a smaller, more specific `old_str` (or narrows by adding `context`).
3. If the second attempt fails, the harness forces a stop condition (“needs human review”) rather than allowing a whole-file overwrite.

Evaluation: measure whether the tool contract is improving outcomes with two task-level metrics:
- **Revert rate**: fraction of tasks where the patch is reverted in the next N commits/PR updates.
- **Diff locality**: median number of files touched and lines changed per task, with an alert threshold for outliers.

## Concrete Example 2
Add an evaluation gate to an agent loop.

A minimal loop in prose looks like: attempt → gate → log → decide.
1. **Attempt**: the agent makes the smallest change it believes will satisfy the task.
2. **Gate**: the harness runs required checks (e.g., unit tests + static checks).
3. **Log**: record the tool outputs, the diff identifier, and the gate result in the task ledger.
4. **Decide**:
   - If gate passes: allow “PR-ready” output.
   - If gate fails: allow another iteration only if budgets remain and the failure is actionable.
   - If repeated failures occur: stop with a concrete failure summary and evidence.

Pass/fail criteria should be explicit:
- Pass = all configured checks return success (exit code 0) and no policy violations were triggered.
- Fail = any check fails, any policy violation occurs, or budgets are exceeded.

Fallback gate policy when tests are missing:
- If unit tests are absent or non-runnable, the harness should not silently accept “looks good.”
- Replace the unit-test requirement with a narrower, explicit fallback gate such as:
  - typecheck/lint/build must pass, and
  - a targeted command or script (documented in the repo) must run successfully, and
  - the change must be limited by stricter patch budgets (smaller allowed diffs).
- The harness should record which gate was used (`full_gate` vs `fallback_gate`) so reliability metrics stay comparable over time.

## Trade-offs
- Richer tool schemas reduce ambiguity but raise integration cost.
- Strict budgets prevent runaway loops but can truncate legitimate work.
- Strong gates improve safety but may block progress on tasks lacking tests.

Decision checklist (recommended defaults and when to relax):
- **Tool schemas**:
  - Default: prefer typed, validated arguments plus explicit error codes for recovery.
  - Relax when: prototyping a new tool where integration speed matters more than repeatability, but only in non-production contexts.
- **Patch budgets**:
  - Default: small, diff-only edits with per-call and per-task size limits.
  - Relax when: performing mechanical, reviewable migrations (e.g., dependency rename) where change breadth is intentional and measurable.
- **Evaluation gates**:
  - Default: require passing tests and static checks (a minimal green CI run) before any final output.
  - Relax when: the repo cannot run tests in the current environment; use an explicit fallback gate and tighten patch budgets rather than skipping evaluation.
- **Stop conditions**:
  - Default: stop on repeated failure modes (same check failing twice) with a structured report.
  - Relax when: failures are due to flaky infrastructure and you can rerun deterministically (record rerun count as part of the trace).

## Failure Modes
- **Schema underspecification**: tools accept ambiguous inputs, producing inconsistent outcomes.
  - How you notice: frequent `NO_MATCH`/`NON_UNIQUE_MATCH`-style failures, large diffs for small tasks, and high variance in outcomes across reruns.
  - Harness fix: tighten required fields, add validation (uniqueness checks, size budgets), and return structured error codes plus fresh context to guide recovery.
- **Over-permissive harness**: agents change broad parts of the repo with weak verification.
  - How you notice: many files touched per task, drift into unrelated directories, and regressions discovered after “completion.”
  - Harness fix: enforce patch locality budgets, add path allowlists/denylists, and require passing gates before accepting final output.
- **Gate bypass**: humans accept outputs without running checks, breaking the feedback loop.
  - How you notice: “merged without green checks,” missing logs/evidence in the ledger, and recurring regressions that gates would have caught.
  - Harness fix: make gates non-optional for PR-ready output (policy), require artifacts (logs, diff id, check results) attached to the task, and surface “stop reason” when evidence is missing.

## Research Directions
- Harness quality metrics (iteration efficiency, regression rate, reproducibility).
  - Open question: which small set of metrics best predicts long-term reliability across repos?
  - Evaluation approach: track iterations to first passing gate, revert rate, and reproducibility rate using the plane metrics table, then compare distributions before/after harness changes.
- Tool error taxonomies that guide automated recovery.
  - Open question: what error codes enable the highest “self-repair” rate without encouraging risky retries?
  - Evaluation approach: measure recovery success rate per error code (e.g., `% resolved within 2 retries`) and the resulting diff locality, using structured tool returns.
- Portable harness templates across languages and repo types.
  - Open question: what parts of the contract surface are truly portable (schemas, budgets, gates) versus language-specific?
  - Evaluation approach: apply a template to multiple repos, then compare reproducibility rate and gate pass rate changes while holding model choice constant.

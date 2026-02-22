# Chapter 02 — Harness Engineering

## Thesis

Harness engineering is the discipline of turning a general-purpose model into a predictable system. It does that by defining tool contracts, constraints, loop control, and evaluation gates.

In this chapter, “predictable” means three things:

1. **Repeatability**: the same input context tends to produce the same classes of actions.
2. **Boundedness**: the system’s allowed changes are limited by explicit constraints.
3. **Verifiability**: outputs can be accepted or rejected by checks, not judgment calls.

Hypothesis (falsifiable): for a fixed set of tasks and repositories, tightening the harness reduces regression rate and rework more than swapping between models of similar capability.

This is not a model-selection argument. The claim is that, when you hold the model and task conditions constant, harness design is the primary lever that changes reliability outcomes.

To test that hypothesis, hold these constant:

- The task set (same prompts and acceptance criteria).
- The repositories and their starting commits.
- The agent instructions and tool availability (only harness strictness changes).

## Why This Matters

- The same model can behave reliably or unreliably depending on tool schemas, budgets, and verification.
- Teams can standardize harness practices even when models change.
- Production safety and auditability primarily live in the harness layer.

If you want evidence for the hypothesis, your experiments should explicitly keep the model constant (or compare models in the same capability band) and vary only harness strictness. Otherwise, it becomes difficult to attribute changes in regression rate and rework to harness design versus model behavior.

## System Breakdown

- **Control plane**: prompts, policies, budgets, stop conditions.
- **Tool plane**: filesystem edits, build/test runners, linters, browsers, APIs.
- **Evaluation plane**: checks as gates; regression suites; quality rubrics.
- **State plane**: task ledger, traces, decisions, artifacts.
- **Interfaces**:
  - Tool schemas and error contracts.
  - Patch discipline (diff-only, small changes).
  - Evaluation API (what constitutes pass/fail).

A diagram helps here because the planes are easy to list but hard to reason about as a system. Focus on where constraints enter (control plane), where evidence is produced (tool/evaluation planes), and what gets recorded for replay (state plane).

```mermaid
flowchart TB
  TB[Task brief<br/>+ repo state]

  C[Control plane<br/>policies<br/>budgets<br/>stop conditions]
  T[Tool plane<br/>patches<br/>commands<br/>structured errors]
  E[Evaluation plane<br/>tests<br/>lint/typecheck<br/>build<br/>rubrics]
  S[State plane<br/>ledger<br/>trace<br/>artifacts]

  TB --> C
  C -->|typed tool calls| T
  T -->|check inputs| E
  E -->|pass/fail + evidence| C
  T -->|events + diffs + outputs| S
  E -->|gate results| S
```

Read the diagram as a loop with three distinct roles:

- **Constraints** enter in the control plane (policies, budgets, stop conditions).
- **Evidence** is produced by the tool and evaluation planes (outputs + pass/fail).
- **Replay** depends on the state plane capturing enough artifacts to reproduce decisions.

Takeaway: predictability comes from making the loop explicit. The control plane must be able to stop based on evaluation, and the state plane must capture enough evidence to reproduce the decision.

A useful way to operationalize the planes is to name what each plane consumes, what it produces, and one metric you can track:

<table>
  <thead>
    <tr>
      <th>Plane</th>
      <th>Responsibilities</th>
      <th>Key artifacts (inputs/outputs)</th>
      <th>One measurable metric</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Control plane</td>
      <td>Decide what the agent is allowed to do and when to stop</td>
      <td>
        <div><strong>Inputs</strong>: task brief; policy; iteration/time budget</div>
        <div><strong>Outputs</strong>: chosen strategy; stop reason</div>
      </td>
      <td>Iterations to first passing gate</td>
    </tr>
    <tr>
      <td>Tool plane</td>
      <td>Perform actions with bounded, typed interfaces</td>
      <td>
        <div><strong>Inputs</strong>: validated tool calls</div>
        <div><strong>Outputs</strong>: patches; command outputs; structured errors</div>
      </td>
      <td>Patch locality (files/lines per task)</td>
    </tr>
    <tr>
      <td>Evaluation plane</td>
      <td>Decide if work is acceptable based on checks</td>
      <td>
        <div><strong>Inputs</strong>: test/lint/typecheck/build results; rubrics</div>
        <div><strong>Outputs</strong>: pass/fail + evidence</div>
      </td>
      <td>Gate pass rate (per iteration)</td>
    </tr>
    <tr>
      <td>State plane</td>
      <td>Record what happened and enable recovery</td>
      <td>
        <div><strong>Inputs</strong>: events; diffs; tool outputs</div>
        <div><strong>Outputs</strong>: trace; ledger; artifacts for replay</div>
      </td>
      <td>Reproducibility rate (same pass/fail on rerun)</td>
    </tr>
  </tbody>
</table>

The “minimal contract surface” is the set of interfaces that must be stable for predictability. It includes tool schemas (including error codes), patch discipline, and evaluation semantics.

Boundary:

- In scope: tool schemas, patch discipline, and gate semantics (including what evidence is recorded).
- Out of scope: standardizing runtime infrastructure details, as long as the gate semantics stay consistent.

## Concrete Example 1

Design a tool contract for “apply patch” operations.

A minimal schema sketch can be made scannable by treating it like an interface spec. One goal is to make failures recoverable without expanding scope.

Schema (fields + constraints to keep edits local and reviewable):

- Required fields: `path`, `old_str`, `new_str`.
- Optional field: `context` (only for disambiguation).
- Constraints:
  - No unrelated whitespace changes outside `old_str`.
  - No implicit multi-file edits per call.
  - Size budget (for example: max files changed; max lines changed).

<table>
  <thead>
    <tr>
      <th>Category</th>
      <th>Field / rule</th>
      <th>Purpose</th>
      <th>Example failure mode</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Required fields</td>
      <td><code>path</code></td>
      <td>Identify the target file</td>
      <td>Wrong path → cannot apply patch</td>
    </tr>
    <tr>
      <td>Required fields</td>
      <td><code>old_str</code></td>
      <td>Provide an exact, unique match anchor</td>
      <td>Stale context → no match</td>
    </tr>
    <tr>
      <td>Required fields</td>
      <td><code>new_str</code></td>
      <td>Provide the replacement text</td>
      <td>N/A (validated as string)</td>
    </tr>
    <tr>
      <td>Optional fields</td>
      <td><code>context</code></td>
      <td>Disambiguate or narrow a match</td>
      <td>Without it, match may be non-unique</td>
    </tr>
    <tr>
      <td>Constraints</td>
      <td>No unrelated whitespace changes outside <code>old_str</code></td>
      <td>Preserve locality and reviewability</td>
      <td>“Formatting spill” across file</td>
    </tr>
    <tr>
      <td>Constraints</td>
      <td>No implicit multi-file edits</td>
      <td>Bound scope per call</td>
      <td>Patch tool touches multiple files</td>
    </tr>
    <tr>
      <td>Constraints</td>
      <td>Size budget (e.g., max changed lines per call)</td>
      <td>Prevent runaway diffs</td>
      <td>Large diff for small task</td>
    </tr>
  </tbody>
</table>

Error contract (examples):

<table>
  <thead>
    <tr>
      <th>Error code</th>
      <th>Meaning</th>
      <th>What the harness should return</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>NOT_FOUND</code></td>
      <td><code>path</code> does not exist and <code>create</code> is false</td>
      <td>A clear message plus allowed path roots (if any)</td>
    </tr>
    <tr>
      <td><code>NON_UNIQUE_MATCH</code></td>
      <td><code>old_str</code> matches multiple locations</td>
      <td>Candidate ranges or small snippets for each match</td>
    </tr>
    <tr>
      <td><code>NO_MATCH</code></td>
      <td><code>old_str</code> matches zero locations</td>
      <td>A “fresh context” snippet around the closest match</td>
    </tr>
    <tr>
      <td><code>BUDGET_EXCEEDED</code></td>
      <td>Change size violates configured limits</td>
      <td>The computed line/file counts and configured limits</td>
    </tr>
    <tr>
      <td><code>POLICY_VIOLATION</code></td>
      <td>Edit touches forbidden paths or patterns</td>
      <td>The specific policy rule that triggered</td>
    </tr>
  </tbody>
</table>

Happy path flow:

1. Agent proposes a patch using a unique `old_str` block with minimal scope.
2. Harness validates: file exists, match is unique, diff stays within budgets.
3. Tool applies the patch and returns a structured result: changed line counts, a before/after snippet, and a stable identifier for the diff.

Conflict recovery (when the patch fails with `NO_MATCH` or `NON_UNIQUE_MATCH`):

1. The harness returns the error code plus a short “fresh context” snippet around the closest match (or a list of candidate match ranges).
2. The agent re-reads the relevant portion of the file and regenerates a smaller, more specific `old_str` (or narrows by adding `context`).
3. If the second attempt fails, the harness forces a stop condition (“needs human review”) rather than allowing a whole-file overwrite.

Mini-example (connecting the contract to measurable outcomes):

- Task: “Update `timeout_ms` default from 5000 to 8000.”
- Without a strict contract: the agent might run a broad search/replace and touch 6 files, including docs and unrelated constants.
- With the contract and budgets:
  - The edit is constrained to one file and a small `old_str` anchor.
  - The harness rejects the attempt if it exceeds, for example, 1 file and 20 changed lines.
  - Your tracked metrics should shift: **diff locality** stays low (1 file, a few lines), and **revert rate** should drop because the change is less likely to introduce incidental regressions.

Evaluation: measure whether the tool contract is improving outcomes with two task-level metrics:

- **Revert rate**: fraction of tasks where the patch is reverted in the next N commits/PR updates.
- **Diff locality**: median number of files touched and lines changed per task, with an alert threshold for outliers.

## Concrete Example 2

Add an evaluation gate to an agent loop.

A diagram helps here because “attempt → gate → log → decide” is simple to say, but easy to implement incorrectly. Focus on the two decision points: whether the gate passed, and whether another iteration is allowed under budgets.

```mermaid
flowchart TB
  A[Attempt<br/>smallest plausible change]
  G[Gate<br/>tests + static checks]
  P{Gate passes?}
  L[Log<br/>diff id + outputs + exit codes]
  B{Budget remains<br/>and failure actionable?}
  R[PR-ready output]
  S[Stop<br/>failure summary + evidence]

  A --> G --> P
  P -- yes --> L --> R
  P -- no --> L --> B
  B -- yes --> A
  B -- no --> S
```

Takeaway: the harness should only permit another attempt when (a) budgets remain and (b) the failure is actionable. Otherwise, it should stop with evidence, not a guess.

A minimal loop in prose looks like: attempt → gate → log → decide.

1. **Attempt**: the agent makes the smallest change it believes will satisfy the task.
2. **Gate**: the harness runs required checks (e.g., unit tests + static checks).
3. **Log**: record the tool outputs, the diff identifier, and the gate result in the task ledger.
4. **Decide**:
   - If gate passes: allow “PR-ready” output.
   - If gate fails: allow another iteration only if budgets remain and the failure is actionable.
   - If repeated failures occur: stop with a concrete failure summary and evidence.

Gate configuration checklist (minimal defaults):

1. **Define the full gate**: a fixed set of commands, in order (for example: unit tests, then lint/typecheck, then build).
2. **Define time and iteration budgets**: max gate time per iteration and max iterations per task.
3. **Define evidence requirements**: always store exit codes, stdout/stderr (or paths to logs), and the diff identifier.
4. **Define fallback eligibility**: when tests are missing or non-runnable, use a narrower fallback gate and tighten patch budgets.

Pass/fail criteria should be explicit:

- Pass = all configured checks return success (exit code 0) and no policy violations were triggered.
- Fail = any check fails, any policy violation occurs, or budgets are exceeded.

Fallback gate policy when tests are missing:

- If unit tests are absent or non-runnable, the harness should not silently accept “looks good.”
- Use a compact decision rule:

1. If the repo’s documented test command exists and runs in this environment, use `full_gate`.
2. If tests cannot be invoked here (missing command, missing dependency, or failures that prevent tests from running), try to fix within budget.
3. If you cannot make tests runnable within budget, switch to `fallback_gate` and tighten patch budgets.
4. Record which gate was used (`full_gate` vs `fallback_gate`) so metrics remain comparable.

- A minimal `fallback_gate` is narrower and stricter:
  - typecheck/lint/build must pass (whatever subset is available), and
  - a targeted command or script (documented in the repo) must run successfully, and
  - the change must be limited by stricter patch budgets (smaller allowed diffs).

Mini-example (gate policy with metrics):

- Task: “Rename `UserID` to `user_id` in a Python module.”
- Budgets: max 2 iterations; max 10 changed lines per iteration.
- Repo state: a documented test command exists, but it fails immediately due to a missing system dependency.
- Gate choice: use `fallback_gate` plus stricter patch budgets.
- Iteration 1:
  - Attempt: change one file and update one reference.
  - Gate: lint/typecheck passes; targeted script fails with an import error.
- Iteration 2:
  - Attempt: add the missing import in the same file.
  - Gate: lint/typecheck passes; targeted script passes.
- Recorded metric: iterations to first passing gate = 2.

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
  - Hypothesis link: if harness tightening drives reliability more than model swaps, these distributions should improve (fewer iterations, fewer reverts, higher reproducibility) even when the model is held constant.
- Tool error taxonomies that guide automated recovery.
  - Open question: what error codes enable the highest “self-repair” rate without encouraging risky retries?
  - Evaluation approach: measure recovery success rate per error code (e.g., `% resolved within 2 retries`) and the resulting diff locality, using structured tool returns.
  - Hypothesis link: a tighter harness should shift failures from “silent bad edits” toward typed, recoverable errors, increasing recovery success without increasing diff locality.
- Portable harness templates across languages and repo types.
  - Open question: what parts of the contract surface are truly portable (schemas, budgets, gates) versus language-specific?
  - Evaluation approach: apply a template to multiple repos, then compare reproducibility rate and gate pass rate changes while holding model choice constant.
  - Hypothesis link: if harness design is the primary lever, a portable template should produce consistent improvements across repos without requiring a different model.

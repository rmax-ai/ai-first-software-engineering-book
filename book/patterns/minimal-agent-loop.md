# Minimal Agent Loop

## Context

You need iterative work (planning + tool use + feedback) inside an engineering environment (repo, CI, tickets, docs). The primary risk is uncontrolled complexity: additional autonomy without corresponding observability and verification.

## Problem

A minimal agent loop is a bounded plan→act→observe cycle where each step produces one concrete action and one auditable trace event. How do you get useful autonomous work while keeping the control surface small enough to debug, test, and govern?

In practice, “small enough” means: (1) explicit stop conditions, (2) verification evidence attached to the final result, and (3) reproducible step-by-step logs when something goes wrong.

## Forces

- **Capability vs. determinism**: richer loops solve more tasks but increase variance across runs.
  - Design choice: restrict the model to “exactly one next action” per step (tool call or stop) and enforce budgets outside the model.
- **Observability vs. speed**: more logging and checks slow iteration, but missing data makes incidents expensive.
  - Design choice: log only what you need to reproduce outcomes (inputs selected, tool call args, normalized error, changed files, verification output).
- **Safety vs. throughput**: tighter constraints reduce risk but may block progress on ambiguous tasks.
  - Design choice: define “blocked” as an explicit stop state with a reason and the smallest missing prerequisite (permission, missing file, unclear spec).
- **Tool side effects**: tools mutate state; retries can duplicate actions unless idempotent.
  - Design choice: include an idempotency key (or dry-run) for side-effecting tools; record a side-effect summary in the trace.
- **Context limits**: the loop must decide what to read, summarize, and omit.
  - Design choice: build a narrow context per step (only the files/lines needed for the next action) and summarize prior trace events.

## Solution

Implement the smallest loop that aims to ensure: one action per step, explicit termination, and verification evidence on stop.

1. Load state (workspace snapshot + budgets + any session memory).
2. Produce exactly one next action using a typed schema (tool call or stop).
3. Execute the action with timeouts, error normalization, and side-effect capture.
4. Append a structured event to a trace.
5. Update state and budgets.
6. Stop only on explicit conditions (success with evidence, budget exhausted, or blocked with a reason).

Keep loop policy simple. Push sophistication into tools (typed boundaries) and verification (tests/evals). A practical rule helps: a “success” stop cites concrete evidence (a passing command, a diff, or a test run). A “blocked” stop names the missing input needed to proceed.

## Implementation sketch

A minimal state machine:

- **Inputs**: goal, repo root, tool allowlist, budgets (steps/time/cost), memory handles.
- **Per-step**:
  - Build a narrow context (selected files + short trace summary + constraints).
  - Ask the model for `NextAction`.
  - If `NextAction.type == stop`: return a result object (including verification evidence or explicit “blocked”).
  - Otherwise: run the tool, capture outputs and *observable side effects*.
  - Append the event to the trace.
  - Update budgets; stop if exceeded.

A diagram helps because the loop is mostly control flow. It makes the decision points explicit. Focus on the two branches: “stop with evidence” vs “execute tool and record side effects.” Budgets are enforced outside the model.

<div class="mermaid">
flowchart TB
  A[Load state<br/>snapshot, budgets, memory] --> B[Build narrow context<br/>files + trace summary + constraints]
  B --> C[Model returns NextAction<br/>typed: tool or stop]
  C --> D{NextAction.type == stop?}
  D -- Yes --> E[Return result<br/>include verification evidence<br/>or blocked reason]
  D -- No --> F[Execute tool<br/>timeouts + error normalization]
  F --> G[Capture outputs + side effects<br/>changed files, tickets, API writes]
  G --> H[Append structured trace event]
  H --> I[Update state + budgets]
  I --> J{Budget exceeded<br/>or stop condition met?}
  J -- Yes --> E
  J -- No --> B
</div>

Takeaway: emit one action at a time. Write a trace event every step. Stop only when a check (or other evidence) is recorded.

Conceptual `NextAction` schema:

    {
      "type": "tool",
      "toolName": "apply_patch",
      "args": { "input": "...", "explanation": "..." },
      "expectedOutcome": "File X updated; markdown lint passes",
      "stopCondition": "After markdown lint passes",
      "risk": "low"
    }

Practical kernel requirements:

- Enforce budgets outside the model.
- Validate tool arguments against schemas.
- Normalize errors (timeout vs. validation vs. runtime error).
- Record a trace event with enough data to reproduce the step.
- For side-effect tools, support an idempotency key (or a safe “dry run” mode) where possible.
- Treat verification as a first-class action: do not stop “success” until a check is recorded as evidence.

### Concrete example

Goal: “Add two glossary terms and ensure formatting.”

1. `read_file(book/glossary.md)` to learn current format.
2. `apply_patch` to add the terms.
3. Run a markdown check (or at minimum `get_errors`) and record output.
4. Stop only after the check is clean; otherwise attempt a bounded fix.

What often goes wrong is step 3: the edit is “correct enough” to a reader, but the check fails (formatting, ordering, duplicate anchors). The trace is useful when it records (a) the specific failing check output and (b) the minimal follow-up patch that made it pass.

An example trace event for step 2:

    step: 2
    action:
      type: tool
      tool: apply_patch
      expected_outcome: "Glossary updated with Acceptance criteria and Budget"
    result:
      changed_files:
        - book/glossary.md
      tool_exit: success
    budgets:
      steps_remaining: 17

Verification evidence (fail then pass) can be recorded as two consecutive events; the important part is that “success” cites the passing output, not the intention:

    step: 3
    action:
      type: tool
      tool: markdown_check
      expected_outcome: "No markdown errors"
    result:
      tool_exit: failure
      normalized_error:
        kind: "validation"
        summary: "Glossary terms not in alphabetical order"
      evidence:
        command: "markdownlint book/glossary.md"
        exit_code: 1
        stderr_snippet: "MD012/no-multiple-blanks: Multiple consecutive blank lines [Expected: 1; Actual: 2]"
    budgets:
      steps_remaining: 16

    step: 4
    action:
      type: tool
      tool: apply_patch
      expected_outcome: "Fix ordering/blank lines; markdown check passes"
    result:
      changed_files:
        - book/glossary.md
      tool_exit: success
    budgets:
      steps_remaining: 15

    step: 5
    action:
      type: stop
      stop_reason: "success"
    result:
      verification_evidence:
        command: "markdownlint book/glossary.md"
        exit_code: 0

A second example uses a different verification surface: unit tests.

Goal: “Fix one failing unit test and verify.”

1. Run tests and capture the failing assertion.
2. `read_file(...)` only for the failing test and the referenced implementation.
3. `apply_patch` to fix the defect.
4. Re-run tests; stop only when the test command exits 0.

A minimal trace for the verification steps:

    step: 1
    action:
      type: tool
      tool: run_tests
      expected_outcome: "Test suite passes"
    result:
      tool_exit: failure
      evidence:
        command: "pytest -q"
        exit_code: 1
        stderr_snippet: "E   AssertionError: expected 3, got 4"
    budgets:
      steps_remaining: 19

    step: 4
    action:
      type: tool
      tool: run_tests
      expected_outcome: "Test suite passes"
    result:
      tool_exit: success
      evidence:
        command: "pytest -q"
        exit_code: 0
    budgets:
      steps_remaining: 16

## Failure modes

- **Missing termination criteria**: the loop continues despite completion; budgets are consumed.
  - Signal: repeated “tool” actions with no change in verification status (e.g., same failing check output or no new evidence).
  - Mitigation: require stop conditions to reference a measurable predicate (e.g., “tests pass”, “lint exit code 0”) and stop on budget exhaustion with a structured “incomplete” result.
- **Ambiguous tool failures**: errors are treated as partial success; corrupted state accumulates.
  - Signal: tool exit is non-zero/exceptional but the step is recorded as “success” or the next step assumes the effect happened.
  - Mitigation: normalize errors into a small set of categories and force the trace event to include one of: success, failure, timeout, or validation error.
- **Silent side effects**: tools mutate state without reporting what changed; traces cannot explain outcomes.
  - Signal: external systems change (tickets created, PR opened, files edited) but the trace lacks changed-file lists, IDs, or diffs.
  - Mitigation: for side-effect tools, record a side-effect summary (changed files, created IDs/URLs) and prefer “dry run” modes when available.
- **Non-idempotent retries**: a retry duplicates actions (double-writes, duplicate tickets, repeated API calls).
  - Signal: repeated tool calls with identical args produce multiple created artifacts (two tickets, two PRs) or duplicated file edits.
  - Mitigation: add idempotency keys per step, detect “already exists” responses, and make retries conditional on evidence that the previous attempt did not apply.
- **Context bloat**: the loop pulls in too much content; constraints are ignored or diluted.
  - Signal: growing context size with decreasing step quality (missed constraints, irrelevant edits, inconsistent behavior across runs).
  - Mitigation: hard cap context size, require a short “why these files/lines” selection rationale, and summarize prior trace events instead of re-including them.
- **Planning without execution**: repeated re-planning without tool calls; no measurable progress.
  - Signal: multiple consecutive steps that emit plans or analyses but no tool execution and no new evidence.
  - Mitigation: enforce a per-step contract (“exactly one next action”) and treat “plan” as an input artifact, not a step output unless it is the requested deliverable.

## When not to use

- The task is deterministic and can be solved with a single script/command.
- Side effects are unacceptable without human approval (e.g., production mutations).
- You cannot capture traces or run verification; you will be unable to debug or detect drift.

# Minimal Agent Loop

## Context
You need iterative work (planning + tool use + feedback) inside an engineering environment (repo, CI, tickets, docs). The primary risk is uncontrolled complexity: additional autonomy without corresponding observability and verification.

## Problem
How do you get useful autonomous work while keeping the control surface small enough to debug, test, and govern?

## Forces
- **Capability vs. determinism**: richer loops solve more tasks but increase variance across runs.
- **Observability vs. speed**: more logging and checks slow iteration, but missing data makes incidents expensive.
- **Safety vs. throughput**: tighter constraints reduce risk but may block progress on ambiguous tasks.
- **Tool side effects**: tools mutate state; retries can duplicate actions unless idempotent.
- **Context limits**: the loop must decide what to read, summarize, and omit.

## Solution
Implement the smallest loop that can:
1. Load state (workspace snapshot + budgets + any session memory).
2. Produce exactly one next action using a typed schema (tool call or stop).
3. Execute the action with timeouts, error normalization, and side-effect capture.
4. Append a structured event to a trace.
5. Update state and budgets.
6. Stop only on explicit conditions (success, budget exhausted, or blocked).

Keep loop policy simple. Push sophistication into tools (typed boundaries) and verification (tests/evals).

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

Conceptual `NextAction` schema:

```json
{
  "type": "tool" ,
  "toolName": "apply_patch",
  "args": { "input": "...", "explanation": "..." },
  "expectedOutcome": "File X updated; markdown lint passes",
  "stopCondition": "After lint passes",
  "risk": "low"
}
```

Practical kernel requirements:

- Enforce budgets outside the model.
- Validate tool arguments against schemas.
- Normalize errors (timeout vs. validation vs. runtime error).
- Record a trace event with enough data to reproduce the step.
- For side-effect tools, support an idempotency key (or a safe “dry run” mode) where possible.

### Concrete example
Goal: “Add two glossary terms and ensure formatting.”

1. `read_file(book/glossary.md)` to learn current format.
2. `apply_patch` to add the terms.
3. Run a markdown check (or at minimum `get_errors`) and record output.
4. Stop only after the check is clean; otherwise attempt a bounded fix.

An example trace event for step 2:

```yaml
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
```

## Failure modes
- **Missing termination criteria**: the loop continues despite completion; budgets are consumed.
- **Ambiguous tool failures**: errors are treated as partial success; corrupted state accumulates.
- **Silent side effects**: tools mutate state without reporting what changed; traces cannot explain outcomes.
- **Non-idempotent retries**: a retry duplicates actions (double-writes, duplicate tickets, repeated API calls).
- **Context bloat**: the loop pulls in too much content; constraints are ignored or diluted.
- **Planning without execution**: repeated re-planning without tool calls; no measurable progress.

## When not to use
- The task is deterministic and can be solved with a single script/command.
- Side effects are unacceptable without human approval (e.g., production mutations).
- You cannot capture traces or run verification; you will be unable to debug or detect drift.

# Agent Operating Rules

This document defines how autonomous work is performed in this repository. It is written for an execution harness that runs a model with tool access. These rules govern behavior, evaluation, and safe iteration.

## 0) Definitions (model vs harness)

- Model: generates plans, proposes edits, and explains decisions.
- Harness: executes tools, reads/writes files, runs commands, and records logs.

Rules in this file must be implemented as harness-enforced constraints where possible, and model-enforced constraints otherwise.

## 1) Task loop and iteration limit

- Hard limit: at most 5 full loops per task.
  - A “loop” is: (plan → change → evaluate → decide next step).
- If the task is not complete after 5 loops:
  - Stop.
  - Report: current state, what remains, what evidence exists, and the minimal next action required.
  - Do not continue iterating without explicit user approval.

## 2) Mandatory self-evaluation (every loop)

At the end of every loop, the model must produce a self-evaluation that includes:

- Goal check: what the task required vs what was delivered.
- Evidence check: what was verified and how (commands, outputs, or direct inspection).
- Risk check: what could still be wrong (edge cases, integration points).
- Next-step decision: stop, iterate, or escalate—with a reason.

The harness must log this self-evaluation as a structured artifact (e.g., JSON or markdown section) per loop.

## 3) Evaluation discipline (no unverified completion)

- Do not mark a task “done” without an evaluation step.
- Preferred evidence, in order:
  1. Targeted automated tests relevant to the change.
  2. Build/lint/typecheck.
  3. Direct runnable repro command(s).
  4. Focused inspection with file references (only if execution is impossible).
- If evaluation cannot be run, explicitly state why and provide a bounded alternative.

## 4) Editing rules (diff-only writes)

- All file writes must be performed as minimal diffs:
  - Use patch-based edits that change only the required lines/sections.
  - Avoid reformatting or unrelated churn.
- No full-file overwrites unless justified.
  - “Justified” means at least one of:
    - File is newly created.
    - File is generated and tracked as generated.
    - The rewrite is the smallest practical change due to pervasive structural changes.
    - A patch-based edit is not feasible with the available tooling.
  - When justified, the model must state:
    - Why patching is infeasible
    - What invariants are preserved
    - How the rewrite will be reviewed safely (e.g., split commits, smaller chunks, or separate PRs)

## 5) Logging requirements

The harness must maintain an append-only activity log per task containing:

- Task identifier, timestamp, environment summary (OS, repo root).
- Tool calls executed:
  - command/tool name
  - parameters (with secrets redacted)
  - start/end time
  - exit status
  - truncated stdout/stderr or file pointers to full logs
- File changes:
  - list of files touched
  - diff summaries
- Evaluation artifacts:
  - commands run
  - results
  - links/paths to reports
- Loop self-evaluation (Section 2) for each loop.

If logs cannot be stored in-repo, store them in the harness’s configured artifact store and record the location.

## 6) Tool permission boundaries

- Default posture: least privilege.
- The harness must enforce allowlists for:
  - filesystem write locations (repo only by default)
  - network access (disabled unless explicitly needed)
  - running arbitrary shell commands (restricted to repo-relevant commands)
- The model must:
  - request the minimum tool capability needed
  - explain why it is needed
  - avoid touching secrets, credentials, or personal data
- If a requested action exceeds permission boundaries, stop and ask for explicit approval with a concrete alternative.

## 7) Safety rails for scope and behavior

- Implement exactly what the task asks. Do not add extra features.
- Avoid broad refactors unless necessary to satisfy requirements.
- Preserve existing public interfaces unless the task explicitly changes them.
- If requirements are ambiguous, choose the simplest reasonable interpretation and note the assumption.

## 8) Quality bar for changes

Before proposing completion, ensure:

- Code changes compile/typecheck if applicable.
- Tests pass if present and runnable.
- Documentation updates exist when behavior or usage changes.
- The resulting diff is reviewable and minimal.

## 9) Failure handling

On errors:

- Capture the error output in logs.
- Attempt up to 2 focused fixes within the remaining loop budget.
- If still failing, stop and report:
  - what was tried
  - what evidence exists
  - the most likely root cause
  - the smallest next step to unblock

## 10) Prohibited behaviors

- No fabricated evidence (tests “passing” without running them).
- No claims of actions performed by the model; only the harness performs actions.
- No silent changes: every write must be traceable to a diff and a reason.

## 11) File locking protocol

- Before touching any tracked file, create a sibling `.lock` file (e.g., editing `foo.md` requires creating `foo.md.lock`).
- The `.lock` file must contain JSON metadata describing the lock owner, a unique identifier, the action being performed, and an expiration timestamp (UTC ISO-8601). Example:
  ```json
  {
    "owner": "terminal-agent",
    "identifier": "task-1234",
    "action": "edit",
    "expires_at": "2026-02-22T16:00:00Z"
  }
  ```
- Before writing, check if the `.lock` file exists and if its expiration is in the future. If so, verify the identifier matches the current agent’s intent. If an active lock belongs to another agent, abort and surface that conflict. If the lock has expired, it may be safely removed and replaced.
- After the edit is complete (or if an error occurs), remove the `.lock` file to release the lock. If removal is not possible immediately (e.g., due to a crash), document the stale lock and its expiration in the activity log before proceeding.
## 11) File locking protocol

- Before touching any tracked file, create a sibling `.lock` file (e.g., editing `foo.md` requires creating `foo.md.lock`).
- The `.lock` file must contain JSON metadata describing the lock owner, a unique identifier, the action being performed, and an expiration timestamp (UTC ISO-8601). Example:
  ```json
  {
    "owner": "terminal-agent",
    "identifier": "task-1234",
    "action": "edit",
    "expires_at": "2026-02-22T16:00:00Z"
  }
  ```
- Before writing, check if the `.lock` file exists and if its expiration is in the future. If so, verify the identifier matches the current agent’s intent. If an active lock belongs to another agent, abort and surface that conflict. If the lock has expired, it may be safely removed and replaced.
- After the edit is complete (or if an error occurs), remove the `.lock` file to release the lock. If removal is not possible immediately (e.g., due to a crash), document the stale lock and its expiration in the activity log before proceeding.

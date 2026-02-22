# Chapter 04 — Memory Systems

## Thesis
Memory is an engineered data store for work artifacts, not a raw log of prior messages. It must be **structured**, **queryable**, and **governed** (with provenance) to improve long-horizon work.

- **Structured**: stored as records with explicit fields (not free-form chat logs), so constraints, sources, and updates are representable.
- **Queryable**: retrievable by filters (task, file, timeframe, decision id), with ranking that prefers fresh, high-provenance entries.
- **Governed**: subject to retention/redaction/correction rules, so stale or wrong entries can be superseded and sensitive traces can be minimized.

Definition of done for “good memory”:
- **Structure**: every entry has an id, timestamp, type, and source.
- **Query**: a future agent can retrieve the right entry with a bounded filter (“show decisions for X” / “show traces for regression Y”).
- **Governance**: entries can be corrected (superseded) and expire or be redacted under policy.

Hypothesis: uncurated memory increases confidence without increasing correctness, by amplifying earlier mistakes.

## Why This Matters
- Long projects exceed context windows; without memory, work becomes repetitive and inconsistent.
- Without provenance, persistent memory becomes a source of silent drift: older summaries can out-rank newer evidence.
- Production environments need data minimization and retention policies for stored traces and summaries.
- Those policies must connect to provenance (what the data came from) and correction (how wrong entries are handled).

## System Breakdown
- **Memory classes**:
  - Episodic: traces of actions/tool I/O/diffs.
  - Semantic: stable project facts and conventions.
  - Decisions: recorded trade-offs and constraints.
  - State: current plan, progress, open issues (kept memory-specific: pointers to the latest plan/progress, not a second project management system).
- **Write policy**: what gets stored, when, by whom, and with what validation.
- **Read policy**: retrieval filters, ranking, freshness, and provenance checks.
- **Governance**: retention, access control, redaction, and correction mechanisms.

Minimum memory record schema (applies to all classes):
- `id`: stable identifier (e.g., `dec-2026-02-22-authz-approach`, `trace-<task>-<iter>`).
- `timestamp`: when recorded (and optionally `valid_through` for expiry/refresh).
- `type`: episodic | semantic | decision | state.
- `source`: where it came from (tool output, diff, doc link, human note) and a pointer (path/URL/commit hash).
- `confidence`: coarse signal (e.g., low/medium/high) tied to source quality (tests passing, verified by review, etc.).
- `supersedes`: optional list of prior ids this record replaces (supports correction and avoids “memory poisoning” via repetition).

## Concrete Example 1
Decision memory for an architecture choice.

Write event (what triggers storage):
- After selecting an approach in a design discussion or PR, store a decision record as part of the change (or alongside it) before implementation diverges.

Stored record (template; identifiers are illustrative):
- `id`: `dec-2026-02-22-memory-store-backend`
- `timestamp`: `2026-02-22T19:33Z`
- `type`: decision
- `statement`: “Store project memory as append-only records with explicit superseding, not as an editable wiki page.”
- `options_considered`:
  - “Editable wiki page”
  - “Append-only records + supersedes field”
  - “No persistence; rely on context only”
- `chosen`: “Append-only records + supersedes field”
- `constraints`: “Must support redaction; must record provenance pointers; must allow correction.”
- `rationale`: “Editable pages hide drift; append-only preserves history and enables explicit correction.”
- `source`: “docs/decisions/dec-2026-02-22-memory-store-backend.md + commit 0123abcd”
- `confidence`: “medium (reviewed; not yet load-tested)”
- `supersedes`: `[]`

Enforcement rule (how future work must behave):
- Any change that contradicts the decision must either (a) reference this `id` and explain why it still holds, or (b) create a new decision record with `supersedes: ["dec-2026-02-22-memory-store-backend"]`. This prevents silent divergence where repeated but incorrect summaries turn into “facts” (see **Memory poisoning** in ## Failure Modes).

## Concrete Example 2
Trace-indexed memory for debugging.

Trace-indexed memory stores enough episodic detail to support “find similar failure, verify with evidence” workflows.

Capture → index → retrieve → verify:
1. **Capture**: on each iteration, store tool outputs and diffs:
   - test command + failing stack trace snippet
   - files changed + diff hash
   - environment notes that affect reproducibility (OS, dependency lockfile hash)
2. **Index**: attach keys:
   - `task_id`, `iteration`, `files_touched`, `error_signature` (e.g., exception type + top frame), `timestamp`, `source` pointers.
3. **Retrieve**: when a regression occurs, query with bounded filters in plain language:
   - “Show traces where `error_signature` matches ‘KeyError: CONFIG’ and `files_touched` includes `settings.py` from the last 30 days.”
   - Rank by freshness, then by confidence (e.g., traces linked to a commit that later passed CI).
4. **Verify (provenance check)**: before acting on a retrieved trace, confirm provenance and freshness per **Read policy**:
   - Does the trace point to an exact tool output and commit hash?
   - Is it superseded by a newer trace for the same signature?
   - Do current tests reproduce the signature, or has the failure mode changed?

Expected outcome (measurable):
- For recurring `error_signature`s, reduce median iterations-to-fix from 6 to 3.
- Keep the post-fix regression rate at or below 2% in the next 20 CI runs affecting the same files.

This flow turns memory into a debugging aid rather than a replay of stale context: retrieval is constrained, and action is gated by a provenance check.

## Trade-offs
- More memory improves continuity but increases risk of stale or incorrect retrieval.
- Strong provenance improves trust but adds overhead to writing and updating memory.
- Aggressive retention helps debugging but increases privacy and storage costs.
- Governance often trades **cost of being wrong** (acting on stale memory, causing regressions) against **cost of being slow** (extra steps to write, verify, and supersede records).

## Failure Modes
- **Stale retrieval dominance**: old assumptions override new evidence. Detection/mitigation: include freshness signals in **Read policy** (time windows, “prefer not-superseded”), and require verification against current tests before applying a past fix.
- **Summarization loss**: key constraints disappear in compression. Detection/mitigation: enforce **Write policy** that decision/semantic records keep explicit constraint fields, and link summaries back to their `source` pointers so missing details are recoverable.
- **Memory poisoning**: incorrect conclusions become “facts” through repetition. Detection/mitigation: require corrections via **Governance** using `supersedes` (no silent edits), and down-rank low-provenance entries in **Read policy** so repetition does not outweigh evidence.

## Research Directions
- Memory scoring with automated freshness and provenance signals.
- Mechanisms for correcting memory (retractions, superseding records).
- Evaluations for memory usefulness (measuring reduced iterations without increased regressions), e.g., for trace-indexed debugging: reduce median “iterations-to-fix” for recurring `error_signature`s while holding the post-fix regression rate constant (or lower) across subsequent CI runs.

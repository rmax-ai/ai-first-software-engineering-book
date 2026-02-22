# Risks and Decisions

## Risks discovered
- Plan-only iterations can drift unless next-step acceptance criteria are precise and testable.
- Kernel observability additions may increase log volume and require guardrails to keep outputs deterministic.

## Decisions and trade-offs
- Chose a planning-only scope to satisfy the seed iteration contract from `prompts/incremental-improvements/execute.md`.
- Deferred implementation so future iterations can apply minimal, test-backed diffs with clear sequencing.

## Deferred items
- No code or eval contract edits were made in this iteration by design.

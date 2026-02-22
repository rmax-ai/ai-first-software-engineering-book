# Risks and decisions

## Risks discovered
- Existing harness trace/eval assumptions may constrain schema evolution and require coordinated updates.
- Overly broad next-step scope could force non-minimal diffs and reduce deterministic confidence.

## Decisions made
- Keep this iteration strictly planning-only, as required by the seed prompt.
- Recommend one narrowly scoped next task that improves observability first, then layers template/eval updates.

## Deferred intentionally
- Any code changes to kernel/template/smoke/eval files are deferred to the next iteration.

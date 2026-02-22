# Risks and decisions

## Risks
- Planning-only iteration provides no executable regression signal by itself.
- Later iterations may over-scope unless each task remains a smallest vertical slice.

## Decisions and trade-offs
- Chose planning scope only (per seed instruction) instead of implementing kernel changes immediately.
- Deferred implementation to keep this iteration deterministic and reviewable.

## Deferred work
- Implement structured kernel trace improvements.
- Add/adjust smoke modes for new guardrails.
- Update eval YAML assertions to match new observability outputs.

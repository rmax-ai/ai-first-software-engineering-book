# Risks and decisions

## Risks
- Plan quality risk: if scope is too broad, follow-up iterations may lose minimal-diff discipline.
- Coverage risk: eval updates might lag behind kernel changes unless each iteration keeps eval wiring in scope.

## Decisions and trade-offs
- Chose planning-only seed iteration as required by prompt, deferring code edits to later iterations.
- Kept recommendations focused on deterministic behavior and measurable verification signals.

## Deferred intentionally
- Implementation details for trace event schema and parser internals are deferred to next iteration tasks.

# Risks and decisions

## Risks
- Planned feature slices may expose hidden coupling between kernel orchestration and trace/metrics emitters.
- Eval YAML updates can accidentally broaden or tighten gates if not validated with representative runs.

## Decisions and trade-offs
- Chose a planning-only first iteration to reduce implementation risk and establish explicit acceptance boundaries.
- Deferred code changes so the next iteration can execute one smallest implementation task with focused verification.

## Deferred items
- Implementation of kernel observability improvements.
- Role I/O template refinements.
- Smoke and eval contract adjustments tied to new behavior.

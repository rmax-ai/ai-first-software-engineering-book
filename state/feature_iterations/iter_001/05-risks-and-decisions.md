# Risks and decisions

## Risks
- Plan quality depends on future iterations preserving deterministic behavior while adding observability in `state/kernel.py`.
- Eval updates can become noisy if new checks are not scoped to measurable harness signals.

## Decisions
- Keep this seed iteration planning-only per prompt contract; defer all runtime edits.
- Prioritize small, test-backed follow-up tasks instead of multi-file implementation in one step.

## Deferred intentionally
- Implementation of kernel logging/control changes.
- Role I/O scaffold updates.
- Smoke/eval contract modifications and associated command runs.

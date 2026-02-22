# Risks and Decisions

## Risks
- Future kernel changes may couple logging, budget control, and eval wiring if feature slices are not isolated.
- Expanding smoke coverage can create noisy signals unless expected outputs are explicitly codified.

## Decisions and trade-offs
- Chose a planning-only first iteration to satisfy prompt requirements and avoid speculative code edits.
- Prioritized deterministic observability and eval alignment before adding new runtime behavior.

## Deferred
- Implementation of kernel and smoke changes is deferred to the next iteration by design.

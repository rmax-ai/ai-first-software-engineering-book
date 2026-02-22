# Risks and decisions

## Risks
- Plan quality risk: without immediate implementation, some assumptions about observability touchpoints in `state/kernel.py` may need refinement.
- Drift risk: future iterations must keep eval YAML updates tightly coupled to behavior changes to avoid false confidence.

## Decisions and trade-offs
- Decision: keep this seed iteration planning-only to follow prompt requirements exactly.
- Trade-off: no runtime test execution in this iteration; verification is artifact and guidance completeness.

## Deferred items
- Actual code changes to kernel/templates/smoke harness are intentionally deferred to the next iteration.

# Risks and decisions

## Risks discovered
- Planning quality depends on future iterations keeping trace and eval updates synchronized; drift between code and eval contracts could reduce signal quality.
- Smoke coverage may miss edge cases unless new deterministic guards are added with focused assertions.

## Decisions and trade-offs
- Decision: Keep this seed iteration planning-only to satisfy the runner’s stop condition and minimize risk.
- Trade-off: No immediate harness behavior change; value is deferred to next iteration execution.

## Intentionally deferred
- Implementation of kernel trace-schema updates.
- Role I/O template tightening.
- New smoke/eval assertions beyond the planning definition.

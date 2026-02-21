# Task

## Selected task title
Refactor `LLMClient._run_async` to handle running-loop contexts safely.

## Why this task now
`iter_027/06-next-iteration.md` identified nested event-loop handling as the next reliability hotspot after SDK-only cleanup.

## Acceptance criteria for this iteration
- `_run_async` does not create ad-hoc same-thread loops when already inside a running loop.
- Public synchronous `chat(...)` API remains unchanged.
- Smoke checks pass for `stub` and `sdk-unavailable` modes.

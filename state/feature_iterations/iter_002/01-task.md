# Add kernel tracepoint event stream

## Why this task now

`iter_001/06-next-iteration.md` prioritized kernel observability. The smallest actionable slice is adding deterministic trace events around the kernel loop so later telemetry and metrics work can build on concrete runtime evidence.

## Acceptance criteria

1. `state/kernel.py` writes per-iteration trace events for start, evaluation outcome, and state persistence.
2. Trace output is deterministic JSONL under the iteration output tree.
3. No behavior changes to chapter lifecycle decisions or eval gating logic.

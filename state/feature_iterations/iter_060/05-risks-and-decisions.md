# Risks and Decisions

## Risks discovered
- The trace-summary mode map is currently near the CLI constants; future unrelated mode growth could still create mixed concerns in one file.
- Fixture-backed validation still depends on trace schema parity with kernel outputs.

## Decisions made and trade-offs
- Used a plain dict map keyed by mode string to keep behavior deterministic and diffs minimal.
- Kept `ping` and `prompt` as explicit branches to avoid broad refactors outside the scoped trace-summary task.

## Intentionally deferred
- Splitting mode configuration into a dedicated typed structure or helper module.

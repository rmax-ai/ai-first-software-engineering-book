# Risks and Decisions

## Risks discovered
- The smoke test currently validates bootstrap failure by patching `_ensure_sdk_thread_loop`; if internals are renamed, this mode will need adjustment.

## Decisions made and trade-offs
- Chose deterministic monkeypatch simulation over timing-based failure to keep tests stable and fast.
- Scoped change only to smoke-test coverage; no production-path behavior was changed.

## Intentionally deferred
- Additional bootstrap timeout-specific simulation via thread/event patching was deferred as unnecessary for this smallest task.

# Risks and Decisions

## Risks discovered
- The guard inspects parser internals (`parser._actions`) to locate the `--mode` argument; this is stable in argparse but still an internal attribute.

## Decisions made and trade-offs
- Reused a shared `_build_parser(...)` helper so runtime and guard compare against the exact parser setup, minimizing false drift signals.
- Kept comparison strict (`==`) on ordered mode names so duplicates/reordering are caught deterministically.

## Anything intentionally deferred
- Deferred adding a dedicated public parser-construction API; current helper is sufficient for deterministic smoke coverage.

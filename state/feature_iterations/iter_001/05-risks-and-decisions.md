# Risks and decisions

## Risks discovered
- The plan assumes trace and metrics extensions in `state/kernel.py` can remain backward compatible with existing consumers.
- Additional smoke modes may increase deterministic test runtime if not kept table-driven.

## Decisions and trade-offs
- Chose a planning-only iteration to satisfy the seed requirement and avoid speculative code edits.
- Kept the next-step recommendation singular to preserve strict iteration scope.

## Deferred intentionally
- Any code or eval YAML implementation details are deferred to follow-up iterations.


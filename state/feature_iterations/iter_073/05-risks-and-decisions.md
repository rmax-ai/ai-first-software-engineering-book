# Risks and decisions

## Risks discovered
- The adjacency guard currently relies on first-occurrence indices; if duplicate mode names are introduced, adjacency could pass while uniqueness fails elsewhere.

## Decisions made and trade-offs
- Reused existing parser/usage extraction helpers to keep the change minimal and deterministic.
- Kept the new guard focused only on parity cleanup adjacency to avoid broadening scope beyond one unfinished task.

## Intentionally deferred
- A dedicated first-occurrence uniqueness+adjacency composite guard for the parity modes was deferred to keep this iteration narrowly scoped.

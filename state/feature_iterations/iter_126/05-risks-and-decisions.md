# Risks and Decisions

## Risks discovered
- Long mode names are easy to mistype; minor string drift could break guard assertions.

## Decisions made and trade-offs
- Reused existing guard-mode naming and assertion patterns to minimize behavioral risk.
- Kept validation targeted to the changed mode for fast and specific feedback.

## Intentionally deferred
- Running the entire smoke matrix was deferred because this iteration only changes one targeted guard mode.

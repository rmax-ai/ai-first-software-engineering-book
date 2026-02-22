# Risks and Decisions

## Risks discovered
- The duplicated long mode-name chain is brittle and easy to mistype when extending coverage depth.

## Decisions made and trade-offs
- Followed the existing explicit table-driven pattern for one additional depth to keep this iteration minimal and deterministic.
- Deferred refactoring toward generated mode-spec scaffolding to avoid broad changes beyond this task.

## Intentionally deferred
- Any abstraction to remove repetitive mode-name and handler boilerplate.

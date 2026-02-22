# Risks and decisions

## Risks discovered
- Guard-chain mode names are intentionally long and repetitive; typo risk remains high for future additions.

## Decisions made and trade-offs
- Followed the existing explicit, table-driven mode pattern rather than introducing abstraction to keep this iteration minimal and low-risk.

## Anything intentionally deferred
- Refactoring repetitive guard helpers into a shared assertion utility was deferred to avoid unrelated behavior changes.

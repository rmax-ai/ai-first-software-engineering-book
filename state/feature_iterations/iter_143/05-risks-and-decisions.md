# Risks and decisions

## Risks discovered
- Long mode names are fragile; a typo in either the runner or registration string can silently desynchronize coverage.

## Decisions made and trade-offs
- Kept the change minimal by following the existing long-form wrapper pattern rather than refactoring mode-name construction.
- Added only one new runner and one new mode registration to satisfy the requested smallest unfinished task.

## Anything intentionally deferred
- Refactoring repetitive long mode names into shared constants/helpers was deferred to avoid unrelated churn.

# Risks and decisions

## Risks discovered
- The repetitive long-mode pattern increases maintenance overhead and typo risk as suffix depth grows.

## Decisions made
- Followed the existing explicit-table pattern for minimal, low-risk consistency.
- Limited changes to one new handler + one new mode tuple to satisfy the single-task scope.

## Deferred
- Any refactor to generate duplicate-count guard modes programmatically remains deferred.

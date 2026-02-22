# Risks and Decisions

## Risks discovered
- Long mode identifiers are brittle; a single segment typo breaks adjacency assertions.
- Registration ordering is semantically meaningful, so localized tuple reordering can unintentionally break related ordering guards.

## Decisions made and trade-offs
- Followed the existing deterministic guard-mode pattern and added one focused function rather than refactoring naming helpers.
- Kept the change scope narrow by reordering only the affected local tuple block needed for the new adjacency assertion.

## Intentionally deferred
- Full smoke matrix execution was deferred; only the directly affected guard-mode path was validated.

# Risks and Decisions

## Risks discovered
- Many historical iteration files still contain bare `python state/copilot_sdk_smoke_test.py ...` snippets in narrative text and validation examples.

## Decisions made and trade-offs
- Kept scope to one smallest unfinished task from prior guidance, avoiding broader cleanup churn.
- Used a pre-change `git show HEAD^` check to preserve evidence after committing the content update.

## Anything intentionally deferred
- Bulk normalization of additional historical snippets across older iterations.

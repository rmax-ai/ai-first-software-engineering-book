# Risks and Decisions

## Risks discovered
- Historical migration artifacts still contain additional bare `python state/copilot_sdk_smoke_test.py` snippets in older iteration docs.

## Decisions made and trade-offs
- Followed prior handoff exactly and changed only the single requested snippet to keep risk and review scope minimal.
- Used focused textual validation (`rg` + diff) because this iteration was documentation-only normalization.

## Anything intentionally deferred
- Broader normalization of other historical bare command snippets was deferred to future one-task iterations.

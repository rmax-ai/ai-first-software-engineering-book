# Risks and Decisions

## Risks discovered
- Repository-wide searches still find bare `python state/copilot_sdk_smoke_test.py` in non-targeted historical files, so broader inconsistency remains outside this iteration scope.

## Decisions made and trade-offs
- Followed the single-task boundary from `execute.md` and prior handoff by editing only `iter_020` and `iter_021` execution/validation artifacts.
- Committed each meaningful change batch to satisfy caller-requested auto-commit behavior.

## Intentionally deferred
- Remaining older contiguous batches with the same outdated command style.

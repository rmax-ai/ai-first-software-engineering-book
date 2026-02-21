# Task

## Selected task title
Backfill one older contiguous batch (`iter_020`-`iter_021`) to replace bare smoke-test `python` snippets with `uv run python` in historical execution/validation artifacts.

## Why this task now
Latest handoff from `iter_051` prioritized this exact adjacent older batch as the next smallest unfinished normalization task.

## Acceptance criteria
- In `iter_020` and `iter_021`, update `03-execution.md` and `04-validation.md` smoke-test command snippets from `python ...` to `uv run python ...`.
- Keep non-command narrative unchanged.
- Provide verification evidence that touched files no longer contain bare `python state/copilot_sdk_smoke_test.py` snippets.

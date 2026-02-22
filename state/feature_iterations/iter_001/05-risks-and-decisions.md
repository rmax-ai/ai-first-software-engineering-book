# Risks and Decisions

## Risks
- Planning artifacts can drift from implementation reality if future iterations skip targeted verification.
- Kernel and eval updates may require synchronized changes to avoid false regression failures.

## Decisions and trade-offs
- Chose planning-only execution because seed-iteration rules in `prompts/incremental-improvements/execute.md` explicitly require it.
- Kept scope to one task (backlog planning) and deferred code edits to maintain minimal, reviewable diffs.

## Deferred items
- Actual implementation in `state/kernel.py` and related files is deferred to the next iteration.

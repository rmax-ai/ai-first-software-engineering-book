# Risks and decisions

## Risks discovered
- Planning-only iteration defers implementation risk discovery (runtime regressions remain untested until follow-up slices).
- Trace schema additions in `state/kernel.py` could drift from existing smoke/eval expectations if introduced without synchronized test updates.

## Decisions made
- Kept this iteration strictly planning-only to satisfy the seed iteration contract.
- Chose a vertical-slice next task (kernel trace schema first) to minimize blast radius and produce early executable evidence.

## Trade-offs and deferrals
- Deferred concrete code changes and test execution to the next iteration by design.
- Deferred broader eval YAML edits until initial trace schema exists to avoid speculative contracts.

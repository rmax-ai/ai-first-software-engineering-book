# Risks and decisions

## Risks discovered
- Planning quality risk: without concrete sequencing, later iterations could drift into broad, multi-surface edits.
- Coverage risk: new harness observability can diverge from eval expectations unless eval YAML updates are paired with code changes.

## Decisions made
- Kept this iteration strictly planning-only to satisfy the seed prompt contract.
- Chose a smallest-next-task approach for follow-up iterations, with one concrete behavior per iteration.

## Deferred intentionally
- No implementation in `state/kernel.py`, `state/role_io_templates.py`, or smoke/eval files in this iteration.


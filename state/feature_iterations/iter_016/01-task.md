# Task: Table-drive base smoke mode registration

## Why this task now
- `state/feature_iterations/iter_015/06-next-iteration.md` recommended removing duplicated base-mode wiring.
- A single base mode table reduces drift risk across argparse choices, help text, and dispatch.

## Acceptance criteria
1. Introduce one mapping for base mode name, handler, and description.
2. Reuse base, shutdown, and trace-summary mappings together for full `--mode` choices/help and dispatch.
3. Re-run `stub`, `bootstrap-failure`, and `trace-summary`.

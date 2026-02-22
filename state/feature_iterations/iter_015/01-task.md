# Task: Table-drive shutdown mode registration

## Why this task now
- `state/feature_iterations/iter_014/06-next-iteration.md` recommended removing duplicated shutdown-mode wiring.
- A single shutdown mode table reduces drift risk across argparse choices, help text, and dispatch.

## Acceptance criteria
1. Introduce one mapping for shutdown mode name, handler, and description.
2. Reuse that mapping for `--mode` choices/help and shutdown mode dispatch without behavior changes.
3. Re-run `stop-close-idempotency`, `stop-failure-destroy-failure-close-idempotency`, and `trace-summary`.

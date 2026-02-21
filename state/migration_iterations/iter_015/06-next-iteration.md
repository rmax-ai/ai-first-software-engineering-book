# Next Iteration Recommendation

## Recommended next task
Run one end-to-end kernel iteration with a live Copilot-backed model and capture `_llm_trace` + ledger usage evidence.

## Why it is next
Adapter reliability hardening is now in place; the highest-value remaining evidence is full planner/writer/critic live execution under the migrated SDK path.

## Concrete acceptance criteria
- `python state/kernel.py --chapter-id <eligible-chapter> --llm --llm-provider copilot --llm-model <model>` completes at least one iteration.
- `_llm_trace` files are emitted for planner/writer/critic.
- `repo_iteration_log[*].resource_usage.prompt_tokens` and `.completion_tokens` remain numeric and non-negative.
- No leaked session/client process after run completion.

## Expected files to touch
- `state/migration_iterations/iter_016/*.md`
- Potentially `state/ledger.json` and `state/metrics.json` if the run is intentionally persisted.

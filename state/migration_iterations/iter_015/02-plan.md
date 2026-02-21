# Plan

## Step-by-step plan for this single task
1. Patch `state/llm_client.py` to improve SDK event normalization and usage aggregation fallbacks.
2. Patch `state/kernel.py` finalizer to bound cleanup failures to warnings.
3. Run focused migration smoke checks (`stub` path + SDK ping).
4. Record evidence and remaining risks in iteration artifacts.

## Files expected to change
- `state/llm_client.py`
- `state/kernel.py`
- `state/migration_iterations/iter_015/01-task.md`
- `state/migration_iterations/iter_015/02-plan.md`
- `state/migration_iterations/iter_015/03-execution.md`
- `state/migration_iterations/iter_015/04-validation.md`
- `state/migration_iterations/iter_015/05-risks-and-decisions.md`
- `state/migration_iterations/iter_015/06-next-iteration.md`
- `state/migration_iterations/iter_015/07-summary.md`

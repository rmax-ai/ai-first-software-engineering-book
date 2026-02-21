# Next Iteration Recommendation

## Recommended next task
Implement a minimal fix for mock-writer heading preservation so `python state/kernel.py --chapter-id 01-paradigm-shift --llm --llm-provider mock` can pass the heading gate.

## Why it is next
This is the smallest direct unblock for the remaining kernel-level mock regression requirement in the migration plan.

## Concrete acceptance criteria
- Update mock writer behavior to preserve the chapter heading structure used by the kernel guard.
- Re-run `python state/kernel.py --chapter-id 01-paradigm-shift --llm --llm-provider mock` successfully through planner/writer/critic.
- Verify `_llm_trace` artifacts exist and kernel exits without heading-guard failure.

## Expected files to touch
- `state/llm_client.py`
- `state/migration_iterations/iter_014/*.md`

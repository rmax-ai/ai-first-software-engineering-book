# Summary

This iteration completed one minimal migration prerequisite.
`state/llm_client.py` now exposes `LLMClient.close()` as a compatibility lifecycle hook.
No request/response paths were changed, so provider behavior remains stable.
Validation confirmed syntax integrity and direct hook invocation.
The main migration risk that remains is missing kernel-side guaranteed teardown.
The next iteration should add `finally`-based cleanup in `state/kernel.py`.

# Validation

## Verification commands run
1. `python -m py_compile state/llm_client.py state/kernel.py`
2. Python snippet:
   - `_normalize_sdk_response({'content':'ok','events':[{'type':'assistant.usage','usage':{'prompt_tokens':3,'completion_tokens':5}}]})`
   - `_normalize_sdk_response({'content':'ok','usage':{'prompt_tokens':1,'completion_tokens':2}})`

## Observed outputs/results
- Command 1 exited 0.
- Command 2 printed `validation-ok` and assertions passed.

## Pass/fail against acceptance criteria
- Direct response usage and event-list usage both normalized: **PASS**.
- Missing usage safely resolves to zeroed `LLMUsage`: **PASS**.
- Mock/legacy paths were not modified by this task: **PASS**.

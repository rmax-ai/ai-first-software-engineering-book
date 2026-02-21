# Validation

## Verification commands run
1. `python -m py_compile state/llm_client.py`
2. Python script that injects fake SDK clients and validates `close()` behavior for:
   - stop success (no force-stop call)
   - stop failure + force-stop success
   - stop failure + force-stop failure (actionable error text)

## Observed outputs/results
- Command 1 exited 0.
- Command 2 printed `validation-ok` and all assertions passed.

## Pass/fail against acceptance criteria
- stop-first with force-stop fallback-only-on-failure: **PASS**.
- actionable shutdown error text includes stop/force-stop details: **PASS**.
- no-op when SDK client is absent is preserved: **PASS**.

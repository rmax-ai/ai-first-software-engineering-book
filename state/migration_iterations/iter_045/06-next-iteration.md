# Next Iteration

## Recommended next task
Run one live-provider Copilot SDK smoke pass and capture migration evidence for M1 runtime completion.

## Why it is next
Deterministic shutdown hardening coverage is now broad; the highest remaining migration risk is unverified real-provider runtime behavior in this iteration sequence.

## Concrete acceptance criteria
- Execute `python state/copilot_sdk_smoke_test.py --mode live` in an environment with valid provider credentials.
- Capture whether planner/writer/critic-style path assumptions remain valid for a real provider response shape and usage extraction.
- Record command output and clear pass/fail evidence in iteration artifacts.

## Expected files to touch
- `state/migration_iterations/iter_046/04-validation.md`
- `state/migration_iterations/iter_046/05-risks-and-decisions.md`
- `state/migration_iterations/iter_046/07-summary.md`

# Task

## Selected task title
Run one live-provider Copilot SDK smoke pass and capture migration evidence for M1 runtime completion.

## Why this task now
`iter_045/06-next-iteration.md` marked live-provider runtime validation as the highest remaining migration risk after deterministic shutdown hardening.

## Acceptance criteria
- Execute `python state/copilot_sdk_smoke_test.py --mode live` with configured provider credentials.
- Capture output and pass/fail evidence for real-provider response/usage extraction behavior.

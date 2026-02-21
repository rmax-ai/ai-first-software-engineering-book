# Validation

## Verification command
- `uv run python state/copilot_sdk_smoke_test.py`

## Observed output
- `PASS: stub Copilot SDK path works`
- `content='stub-ok: ping'`
- `usage=prompt_tokens=7, completion_tokens=3`

## Pass/fail against acceptance criteria
- Message-without-usage + separate usage events simulated: **pass**
- Recovered `prompt_tokens` and `completion_tokens` correctly: **pass**
- Offline deterministic run: **pass**

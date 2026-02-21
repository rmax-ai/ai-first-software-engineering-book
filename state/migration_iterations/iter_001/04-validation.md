# Validation

## Verification command
- `uv run python state/copilot_sdk_smoke_test.py`

## Observed output
- `PASS: stub Copilot SDK path works`
- `content='stub-ok: ping'`
- `usage=prompt_tokens=7, completion_tokens=3`

## Acceptance check
- Usage fallback implementation added: **pass**
- Targeted smoke test passes after change: **pass**

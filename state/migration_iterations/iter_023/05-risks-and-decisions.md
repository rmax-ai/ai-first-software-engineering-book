# Risks and Decisions

## Risks discovered
- Monkeypatch-based tests can leak state if patches are not restored in `finally`.

## Decisions made and trade-offs
- Used monkeypatching of `llm_client.importlib.import_module` and `llm_client.urllib.request.urlopen` to keep the test deterministic and offline.
- Kept changes inside smoke-test harness only; no production `state/llm_client.py` behavior was modified.

## Intentionally deferred
- No new retry/backoff behavior was introduced for HTTP fallback; this iteration only adds regression coverage.

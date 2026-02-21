# Risks and Decisions

## Risks discovered
- Timeout mapping currently validates message substring, so future message rewrites may require fixture updates.

## Decisions made and trade-offs
- Chose deterministic monkeypatching of `urllib.request.urlopen` to raise `TimeoutError` for stable offline coverage.
- Reused existing fallback test style to minimize churn and keep behavior consistent.

## Anything intentionally deferred
- End-to-end network timeout simulation with a live server was deferred to keep this iteration minimal and deterministic.

# Next Iteration Recommendation

## Recommended next task
Validate resource accounting normalization in `state/llm_client.py` by exercising `_extract_sdk_usage` against multiple result/event shapes and asserting numeric non-negative token outputs.

## Why it is next
This directly advances migration plan resource-accounting coverage without requiring live provider credentials or kernel chapter eligibility.

## Concrete acceptance criteria
- Add focused behavioral checks for direct usage dict shape, event-list usage shape, and missing usage fallback.
- Confirm returned `LLMUsage` values are integers and non-negative in all tested shapes.
- Confirm `mock` path still returns zero-usage schema-conforming outputs.

## Expected files to touch
- `state/migration_iterations/iter_011/*.md`

# Next Iteration Recommendation

## Recommended next task
Run `LLMClient` failure-path smoke for the SDK/legacy boundary by asserting actionable error mapping on missing API key and transport failures without requiring kernel chapter eligibility.

## Why it is next
This advances migration-plan failure-path coverage while the kernel regression path remains blocked by chapter status governance.

## Concrete acceptance criteria
- Validate `openai_compatible` path raises `LLMClientError` when API key env var is missing.
- Validate connection failure path produces actionable `LLMClientError` text.
- Confirm `mock` provider behavior remains deterministic and unchanged.

## Expected files to touch
- `state/migration_iterations/iter_010/*.md`

# Next iteration

## Recommended next task
Add an adjacency-order smoke guard mode to ensure the new `...order-uniqueness-order-uniqueness-guard` appears immediately before `...order-uniqueness-order-guard`.

## Why it is next
The current iteration locked uniqueness; the smallest follow-up is registration-order adjacency for the new pair.

## Concrete acceptance criteria
1. Add one smoke mode function in `state/copilot_sdk_smoke_test.py` that asserts the new `...order-uniqueness-order-uniqueness-guard` entry is immediately followed by `...order-uniqueness-order-guard`.
2. Register one new `...order-uniqueness-order-uniqueness-order-guard` mode in `TRACE_SUMMARY_MODE_SPECS` with deterministic wording.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_132/*.md`


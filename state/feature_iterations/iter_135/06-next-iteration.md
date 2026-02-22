# Next iteration

## Recommended next task
Add an adjacency-order smoke guard mode for the new `...order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard` mode.

## Why it is next
After uniqueness-count coverage was added, the smallest follow-up is adjacency-order coverage to ensure this newest mode remains placed immediately before the prior guard mode.

## Concrete acceptance criteria
1. Add one smoke mode function in `state/copilot_sdk_smoke_test.py` asserting `...order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-guard` appears immediately before `...order-uniqueness-order-uniqueness-order-uniqueness-order-guard`.
2. Register one `...order-uniqueness-order-uniqueness-order-uniqueness-order-uniqueness-order-guard` mode in `TRACE_SUMMARY_MODE_SPECS`.
3. Run `uv run python state/copilot_sdk_smoke_test.py --mode <new-mode-name>` and capture PASS output.

## Expected files to touch
- `state/copilot_sdk_smoke_test.py`
- `state/feature_iterations/iter_136/*.md`

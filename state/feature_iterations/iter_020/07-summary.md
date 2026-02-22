# Summary

Iteration 020 implemented the parser choices guard requested by iteration 019.
`state/copilot_sdk_smoke_test.py` now includes `mode-choices-coverage-guard`.
The new guard builds the argparse parser and asserts `--mode` choices exactly match registered mode metadata.
Parser construction was factored into `_build_parser(...)` and reused by `main()`.
Targeted validations passed for `stub` mode, the new guard mode, and Python compile checks.
No mode dispatch semantics were changed.
Next iteration should guard generated usage examples for all non-default modes.

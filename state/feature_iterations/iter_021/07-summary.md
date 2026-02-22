# Summary

Iteration 021 implemented the usage-example coverage guard requested by iteration 020.  
`state/copilot_sdk_smoke_test.py` now includes `usage-examples-coverage-guard`.  
The guard compares generated `_usage_doc_lines(...)` mode commands against metadata-derived expected non-`stub` entries.  
This adds deterministic protection for a user-facing documentation vector without changing parser or dispatch behavior.  
Targeted validations passed for `stub` and the new guard mode.  
The next iteration should add explicit duplicate-command detection for usage lines.

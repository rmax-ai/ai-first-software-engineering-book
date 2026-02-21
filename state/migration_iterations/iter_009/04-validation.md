# Validation

## Verification commands run
1. `python state/kernel.py --chapter-id 01-paradigm-shift --llm --llm-provider mock --llm-model mock --max-iterations 1 --io-dir state/role_io`
2. `python ... > /tmp/kernel_iter009.log 2>&1; rc=$?; cat /tmp/kernel_iter009.log; echo EXIT:$rc`
3. Python status check script for chapter eligibility (`eligible []`).

## Observed outputs/results
- Kernel command exited `1`.
- Captured error: `KernelError: Chapter is not eligible (status='hold').`
- Eligibility inspection result: all chapters are `hold` or `locked`; no eligible chapters.

## Pass/fail against acceptance criteria
- Execute one kernel run with mock provider: **PASS** (executed; returned governed block)
- Produce planner/writer/critic trace evidence: **FAIL (blocked by chapter eligibility before iteration execution)**
- Validate usage schema post-run: **FAIL (blocked because no run iteration completed)**

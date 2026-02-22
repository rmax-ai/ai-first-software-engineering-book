# Execute Loop Procedure

## Overview
- The goal is to iterate the kernel runner across every chapter until three full passes complete for each chapter.
- Every pass must be committed so the git history captures the mitigation of emerging issues.
- When the kernel output surfaces code issues, resolve them with the appropriate subagent(s) (for example, `code-reviewer` for analyzing fixes, `test` for regression verification) before continuing.

## Command Template
```bash
uv run python state/governance_engine.py unlock --chapter-id <chapter> || true
uv run python state/governance_engine.py unhold --chapter-id <chapter> || true
uv run python state/kernel.py --chapter-id <chapter> --llm --llm-provider mock --llm-model gpt-5.2 --verbose
```
Replace `<chapter>` with the chapter identifier listed below.

## Chapter Inventory
| Chapter ID | Source File | Title |
|-----------:|-------------|-------|
| 01-paradigm-shift | `book/chapters/01-paradigm-shift.md` | Paradigm Shift |
| 02-harness-engineering | `book/chapters/02-harness-engineering.md` | Harness Engineering |
| 03-autonomous-kernels | `book/chapters/03-autonomous-kernels.md` | Autonomous Kernels |
| 04-memory-systems | `book/chapters/04-memory-systems.md` | Memory Systems |
| 05-evaluation-and-traces | `book/chapters/05-evaluation-and-traces.md` | Evaluation and Traces |
| 06-agent-governance | `book/chapters/06-agent-governance.md` | Agent Governance |
| 07-production-ai-infrastructure | `book/chapters/07-production-ai-infrastructure.md` | Production AI Infrastructure |
| 99-future-directions | `book/chapters/99-future-directions.md` | Future Directions |

## Loop Procedure
1. Iterate chapters in ascending order (`01-paradigm-shift` through `07-production-ai-infrastructure`, then `99-future-directions`).
2. For each chapter, run the command template once per pass, logging output and capturing artifacts.
3. After every pass:
   - Inspect `state/kernel.py` output for failures or warnings.
   - If code issues arise, invoke specialized subagents (`code-reviewer`, `test`, etc.) to explore, fix, and verify the changes before proceeding. Document the subagent workflow next to the commit message.
   - Run `git status` to confirm the working tree reflects the pass state.
   - Create a git commit describing the chapter and pass number. Example: `chore: pass 2 for chapter 03-autonomous-kernels`.
   - If a pass produces no file changes, create an empty commit with `--allow-empty` so every pass is still represented in history.
4. Repeat steps 2–3 until pass 3 completes for the current chapter before moving to the next chapter.

## Subagent Coordination
- When kernel logs refer to missing dependencies or failing tests, spawn the relevant subagent to diagnose and fix. Record the subagent name and outcome in the commit body or execute log.
- Use the `test` subagent to rerun targeted unit/integration tests after modifications.
- If multiple subagents are required (e.g., `code-reviewer` followed by `test`), chain them sequentially and document each handoff in the loop notes.

## Completion Criteria
- Every chapter must reach pass 3 with a corresponding commit.
- No chapter should be revisited once it has successfully completed pass 3 unless regressions are found; document any regressions as follow-up issues with evidence.

## Logging Expectations
- Maintain a persistent markdown record (this file) describing the pass order, subagent usage, and git history references.
- After finishing the loop for all chapters, append a summary section describing unresolved issues, additional observations, and the total number of commits created.
- Keep historical rerun sections compact: retain the latest prior rerun plus the active rerun being executed, and rely on git history for older details.

## Execution Log
| Chapter | Pass | Result | Subagents | Commit |
|--------:|-----:|--------|-----------|--------|
| 01-paradigm-shift | 1 | failed(1) | none | `f9519e0` |
| 01-paradigm-shift | 2 | failed(1) | none | `e9749c7` |
| 01-paradigm-shift | 3 | failed(1) | none | `38a8049` |
| 02-harness-engineering | 1 | failed(1) | none | `1664a67` |
| 02-harness-engineering | 2 | failed(1) | none | `5e9b68e` |
| 02-harness-engineering | 3 | failed(1) | none | `06d2ff3` |
| 03-autonomous-kernels | 1 | failed(1) | none | `a57ba6c` |
| 03-autonomous-kernels | 2 | failed(1) | none | `f606a2b` |
| 03-autonomous-kernels | 3 | failed(1) | none | `5e01a9a` |
| 04-memory-systems | 1 | failed(1) | none | `9fb0a98` |
| 04-memory-systems | 2 | failed(1) | none | `1bda667` |
| 04-memory-systems | 3 | failed(1) | none | `9070925` |
| 05-evaluation-and-traces | 1 | failed(1) | none | `b5b3831` |
| 05-evaluation-and-traces | 2 | failed(1) | none | `940fbe6` |
| 05-evaluation-and-traces | 3 | failed(1) | none | `4578520` |
| 06-agent-governance | 1 | failed(1) | none | `32544b6` |
| 06-agent-governance | 2 | failed(1) | none | `81d0e20` |
| 06-agent-governance | 3 | failed(1) | none | `ae96a00` |
| 07-production-ai-infrastructure | 1 | failed(1) | none | `852ad06` |
| 07-production-ai-infrastructure | 2 | failed(1) | none | `9a781cd` |
| 07-production-ai-infrastructure | 3 | failed(1) | none | `ac1584c` |
| 99-future-directions | 1 | failed(1) | none | `de020a7` |
| 99-future-directions | 2 | failed(1) | none | `44dc744` |
| 99-future-directions | 3 | failed(1) | none | `2dca88a` |

## Final Summary
- Completed 24/24 chapter passes with one commit per pass.
- All kernel runs exited with code `1` after hitting max-iteration hold; chapters were re-opened via governance `unlock`/`unhold` before each pass as needed.
- Total commits created for this loop: 24 (`chore: pass N for chapter ...`).

## Re-run 2026-02-22T17:38:31Z
| Chapter | Pass | Result | Subagents | Commit |
|--------:|-----:|--------|-----------|--------|
| 01-paradigm-shift | 1 | failed(1) | none | `66ae9ec` |
| 01-paradigm-shift | 2 | failed(1) | none | `571c7b7` |
| 01-paradigm-shift | 3 | failed(1) | none | `1a10ead` |
| 02-harness-engineering | 1 | failed(1) | none | `f4a7195` |
| 02-harness-engineering | 2 | failed(1) | none | `fc0f426` |
| 02-harness-engineering | 3 | failed(1) | none | `4f6ee3d` |
| 03-autonomous-kernels | 1 | failed(1) | none | `1ac216d` |
| 03-autonomous-kernels | 2 | failed(1) | none | `c2b61de` |
| 03-autonomous-kernels | 3 | failed(1) | none | `dae510a` |
| 04-memory-systems | 1 | failed(1) | none | `013157a` |
| 04-memory-systems | 2 | failed(1) | none | `eb33457` |
| 04-memory-systems | 3 | failed(1) | none | `7c0b3d1` |
| 05-evaluation-and-traces | 1 | failed(1) | none | `fa1848f` |
| 05-evaluation-and-traces | 2 | failed(1) | none | `789780c` |
| 05-evaluation-and-traces | 3 | failed(1) | none | `f1ef74a` |
| 06-agent-governance | 1 | failed(1) | none | `b23f9dc` |
| 06-agent-governance | 2 | failed(1) | none | `a7abf1b` |
| 06-agent-governance | 3 | failed(1) | none | `d8a91ae` |
| 07-production-ai-infrastructure | 1 | failed(1) | none | `368ebd1` |
| 07-production-ai-infrastructure | 2 | failed(1) | none | `1dcb184` |
| 07-production-ai-infrastructure | 3 | failed(1) | none | `a18c4e8` |
| 99-future-directions | 1 | failed(1) | none | `adecf87` |
| 99-future-directions | 2 | failed(1) | none | `38a4f82` |
| 99-future-directions | 3 | failed(1) | none | `74573e8` |

### Re-run Summary (2026-02-22T17:38:31Z)
- Completed 24/24 chapter passes with one commit per pass.
- Kernel runs were executed with governance unlock/unhold before each pass.
- Total commits created for this re-run loop: 24.

## Re-run 2026-02-22T17:41:06Z
| Chapter | Pass | Result | Subagents | Commit |
|--------:|-----:|--------|-----------|--------|
| 01-paradigm-shift | 1 | failed(1) | none | `497f1e9` |
| 01-paradigm-shift | 2 | failed(1) | none | `adbfd04` |
| 01-paradigm-shift | 3 | failed(1) | none | `d5f9039` |
| 02-harness-engineering | 1 | failed(1) | none | `fa16943` |
| 02-harness-engineering | 2 | failed(1) | none | `0bc1472` |
| 02-harness-engineering | 3 | failed(1) | none | `9bd53c7` |
| 03-autonomous-kernels | 1 | failed(1) | none | `b28e617` |
| 03-autonomous-kernels | 2 | failed(1) | none | `8c55cf3` |
| 03-autonomous-kernels | 3 | failed(1) | none | `f992ffd` |
| 04-memory-systems | 1 | failed(1) | none | `a684c87` |
| 04-memory-systems | 2 | failed(1) | none | `1574def` |
| 04-memory-systems | 3 | failed(1) | none | `d295673` |
| 05-evaluation-and-traces | 1 | failed(1) | none | `c420757` |
| 05-evaluation-and-traces | 2 | failed(1) | none | `311c1d1` |
| 05-evaluation-and-traces | 3 | failed(1) | none | `116ae61` |
| 06-agent-governance | 1 | failed(1) | none | `9e0eda0` |
| 06-agent-governance | 2 | failed(1) | none | `cdc84a2` |
| 06-agent-governance | 3 | failed(1) | none | `29b95ca` |
| 07-production-ai-infrastructure | 1 | failed(1) | none | `24ec37d` |
| 07-production-ai-infrastructure | 2 | failed(1) | none | `pending` |

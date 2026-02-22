# Execute Loop Procedure

## Overview
- The goal is to iterate the kernel runner across every chapter until three full passes complete for each chapter.
- Every pass must be committed so the git history captures the mitigation of emerging issues.
- When the kernel output surfaces code issues, resolve them with the appropriate subagent(s) (for example, `code-reviewer` for analyzing fixes, `test` for regression verification) before continuing.

## Command Template
```bash
uv run python state/kernel.py --chapter-id <chapter> --llm --llm-model gpt-5.2 --verbose
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

## Execution Log
| Chapter | Pass | Result | Subagents | Commit |
|--------:|-----:|--------|-----------|--------|

## Final Summary
- Pending execution.

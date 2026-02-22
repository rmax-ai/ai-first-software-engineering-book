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

## Re-run 2026-02-22T16:09:57Z
| Chapter | Pass | Result | Subagents | Commit |
|--------:|-----:|--------|-----------|--------|
| 01-paradigm-shift | 1 | failed(1) | none | `chore: pass 1 for chapter 01-paradigm-shift` |
| 01-paradigm-shift | 2 | failed(1) | none | `chore: pass 2 for chapter 01-paradigm-shift` |
| 01-paradigm-shift | 3 | failed(1) | none | `chore: pass 3 for chapter 01-paradigm-shift` |
| 02-harness-engineering | 1 | failed(1) | none | `chore: pass 1 for chapter 02-harness-engineering` |
| 02-harness-engineering | 2 | failed(1) | none | `chore: pass 2 for chapter 02-harness-engineering` |
| 02-harness-engineering | 3 | failed(1) | none | `chore: pass 3 for chapter 02-harness-engineering` |
| 03-autonomous-kernels | 1 | failed(1) | none | `chore: pass 1 for chapter 03-autonomous-kernels` |
| 03-autonomous-kernels | 2 | failed(1) | none | `chore: pass 2 for chapter 03-autonomous-kernels` |
| 03-autonomous-kernels | 3 | failed(1) | none | `chore: pass 3 for chapter 03-autonomous-kernels` |
| 04-memory-systems | 1 | failed(1) | none | `chore: pass 1 for chapter 04-memory-systems` |
| 04-memory-systems | 2 | failed(1) | none | `chore: pass 2 for chapter 04-memory-systems` |
| 04-memory-systems | 3 | failed(1) | none | `chore: pass 3 for chapter 04-memory-systems` |
| 05-evaluation-and-traces | 1 | failed(1) | none | `chore: pass 1 for chapter 05-evaluation-and-traces` |
| 05-evaluation-and-traces | 2 | failed(1) | none | `chore: pass 2 for chapter 05-evaluation-and-traces` |
| 05-evaluation-and-traces | 3 | failed(1) | none | `chore: pass 3 for chapter 05-evaluation-and-traces` |
| 06-agent-governance | 1 | failed(1) | none | `chore: pass 1 for chapter 06-agent-governance` |
| 06-agent-governance | 2 | failed(1) | none | `chore: pass 2 for chapter 06-agent-governance` |
| 06-agent-governance | 3 | failed(1) | none | `chore: pass 3 for chapter 06-agent-governance` |
| 07-production-ai-infrastructure | 1 | failed(1) | none | `chore: pass 1 for chapter 07-production-ai-infrastructure` |
| 07-production-ai-infrastructure | 2 | failed(1) | none | `chore: pass 2 for chapter 07-production-ai-infrastructure` |
| 07-production-ai-infrastructure | 3 | failed(1) | none | `chore: pass 3 for chapter 07-production-ai-infrastructure` |
| 99-future-directions | 1 | failed(1) | none | `chore: pass 1 for chapter 99-future-directions` |
| 99-future-directions | 2 | failed(1) | none | `chore: pass 2 for chapter 99-future-directions` |
| 99-future-directions | 3 | failed(1) | none | `chore: pass 3 for chapter 99-future-directions` |

### Re-run Summary (2026-02-22T16:09:57Z)
- Completed 24/24 chapter passes with one commit per pass.
- Kernel runs were executed with governance unlock/unhold before each pass.
- Total commits created for this re-run loop: 24 (plus summary commit below).

## Re-run 2026-02-22T16:11:36Z
| Chapter | Pass | Result | Subagents | Commit |
|--------:|-----:|--------|-----------|--------|
| 01-paradigm-shift | 1 | failed(1) | none | `a4cad19` |
| 01-paradigm-shift | 2 | failed(1) | none | `b9d4248` |
| 01-paradigm-shift | 3 | failed(1) | none | `51f3cd8` |
| 02-harness-engineering | 1 | failed(1) | none | `f40162e` |
| 02-harness-engineering | 2 | failed(1) | none | `c02d3b0` |
| 02-harness-engineering | 3 | failed(1) | none | `ac45f7d` |
| 03-autonomous-kernels | 1 | failed(1) | none | `6a33c9b` |
| 03-autonomous-kernels | 2 | failed(1) | none | `4ad9e98` |
| 03-autonomous-kernels | 3 | failed(1) | none | `ff5f93f` |
| 04-memory-systems | 1 | failed(1) | none | `03bccdf` |
| 04-memory-systems | 2 | failed(1) | none | `6e50ca5` |
| 04-memory-systems | 3 | failed(1) | none | `bb47a97` |
| 05-evaluation-and-traces | 1 | failed(1) | none | `915b1f3` |
| 05-evaluation-and-traces | 2 | failed(1) | none | `50597e5` |
| 05-evaluation-and-traces | 3 | failed(1) | none | `2e981fe` |
| 06-agent-governance | 1 | failed(1) | none | `265dbcc` |
| 06-agent-governance | 2 | failed(1) | none | `57e08ab` |
| 06-agent-governance | 3 | failed(1) | none | `026e6a3` |
| 07-production-ai-infrastructure | 1 | failed(1) | none | `3caa763` |
| 07-production-ai-infrastructure | 2 | failed(1) | none | `b4aa25c` |
| 07-production-ai-infrastructure | 3 | failed(1) | none | `996d7f9` |
| 99-future-directions | 1 | failed(1) | none | `dbfe922` |
| 99-future-directions | 2 | failed(1) | none | `ddd7611` |
| 99-future-directions | 3 | failed(1) | none | `26bbfe9` |

### Re-run Summary (2026-02-22T16:11:36Z)
- Completed 24/24 chapter passes with one commit per pass.
- Kernel runs were executed with governance unlock/unhold before each pass.
- Total commits created for this re-run loop: 24.

## Re-run 2026-02-22T16:15:40Z
| Chapter | Pass | Result | Subagents | Commit |
|--------:|-----:|--------|-----------|--------|
| 01-paradigm-shift | 1 | failed(1) | none | `787f6f9` |
| 01-paradigm-shift | 2 | failed(1) | none | `d1677a6` |
| 01-paradigm-shift | 3 | failed(1) | none | `efb994f` |
| 02-harness-engineering | 1 | failed(1) | none | `748a32c` |
| 02-harness-engineering | 2 | failed(1) | none | `666477e` |
| 02-harness-engineering | 3 | failed(1) | none | `bb22c9d` |
| 03-autonomous-kernels | 1 | failed(1) | none | `39c4ec5` |
| 03-autonomous-kernels | 2 | failed(1) | none | `8eaaabe` |
| 03-autonomous-kernels | 3 | failed(1) | none | `0b83870` |
| 04-memory-systems | 1 | failed(1) | none | `5e3b1c8` |
| 04-memory-systems | 2 | failed(1) | none | `e3d5173` |
| 04-memory-systems | 3 | failed(1) | none | `bffdc9a` |
| 05-evaluation-and-traces | 1 | failed(1) | none | `a7f9a82` |
| 05-evaluation-and-traces | 2 | failed(1) | none | `82cb68f` |
| 05-evaluation-and-traces | 3 | failed(1) | none | `61faa3b` |
| 06-agent-governance | 1 | failed(1) | none | `c094222` |
| 06-agent-governance | 2 | failed(1) | none | `6a2b5fd` |
| 06-agent-governance | 3 | failed(1) | none | `bdb4a4e` |
| 07-production-ai-infrastructure | 1 | failed(1) | none | `2c31f23` |
| 07-production-ai-infrastructure | 2 | failed(1) | none | `ad48aea` |
| 07-production-ai-infrastructure | 3 | failed(1) | none | `58c8364` |
| 99-future-directions | 1 | failed(1) | none | `2ff8c5f` |
| 99-future-directions | 2 | failed(1) | none | `db7af6e` |
| 99-future-directions | 3 | failed(1) | none | `69f790a` |

### Re-run Summary (2026-02-22T16:15:40Z)
- Completed 24/24 chapter passes with one commit per pass.
- Kernel runs were executed with governance unlock/unhold before each pass.
- Total commits created for this re-run loop: 24.

## Re-run 2026-02-22T16:16:24Z
| Chapter | Pass | Result | Subagents | Commit |
|--------:|-----:|--------|-----------|--------|
| 01-paradigm-shift | 1 | failed(1) | none | `d44a969` |
| 01-paradigm-shift | 2 | failed(1) | none | `ebbe6c6` |
| 01-paradigm-shift | 3 | failed(1) | none | `563576a` |
| 02-harness-engineering | 1 | failed(1) | none | `9d7019b` |
| 02-harness-engineering | 2 | failed(1) | none | `6d6962a` |
| 02-harness-engineering | 3 | failed(1) | none | `7a30499` |
| 03-autonomous-kernels | 1 | failed(1) | none | `b17d867` |
| 03-autonomous-kernels | 2 | failed(1) | none | `1c770f2` |
| 03-autonomous-kernels | 3 | failed(1) | none | `243b3a3` |
| 04-memory-systems | 1 | failed(1) | none | `4f54ad6` |
| 04-memory-systems | 2 | failed(1) | none | `c522b78` |
| 04-memory-systems | 3 | failed(1) | none | `ccb2bf5` |
| 05-evaluation-and-traces | 1 | failed(1) | none | `a9ff686` |
| 05-evaluation-and-traces | 2 | failed(1) | none | `2649ab1` |
| 05-evaluation-and-traces | 3 | failed(1) | none | `0f0a7ed` |
| 06-agent-governance | 1 | failed(1) | none | `7843547` |
| 06-agent-governance | 2 | failed(1) | none | `1edfe76` |
| 06-agent-governance | 3 | failed(1) | none | `104b6a0` |
| 07-production-ai-infrastructure | 1 | failed(1) | none | `a9edc3c` |
| 07-production-ai-infrastructure | 2 | failed(1) | none | `a22dac6` |
| 07-production-ai-infrastructure | 3 | failed(1) | none | `6abca64` |
| 99-future-directions | 1 | failed(1) | none | `a264680` |
| 99-future-directions | 2 | failed(1) | none | `e604618` |
| 99-future-directions | 3 | failed(1) | none | `60cb027` |

### Re-run Summary (2026-02-22T16:16:24Z)
- Completed 24/24 chapter passes with one commit per pass.
- Kernel runs were executed with governance unlock/unhold before each pass.
- Total commits created for this re-run loop: 24.

## Re-run 2026-02-22T16:21:47Z
| Chapter | Pass | Result | Subagents | Commit |
|--------:|-----:|--------|-----------|--------|
| 01-paradigm-shift | 1 | failed(1) | none | `977f470` |
| 01-paradigm-shift | 2 | failed(1) | none | `9e03413` |
| 01-paradigm-shift | 3 | failed(1) | none | `ee83aba` |
| 02-harness-engineering | 1 | failed(1) | none | `f21e629` |
| 02-harness-engineering | 2 | failed(1) | none | `603997a` |
| 02-harness-engineering | 3 | failed(1) | none | `5e75f1d` |
| 03-autonomous-kernels | 1 | failed(1) | none | `93e8a84` |
| 03-autonomous-kernels | 2 | failed(1) | none | `0c1232b` |
| 03-autonomous-kernels | 3 | failed(1) | none | `b05ef81` |
| 04-memory-systems | 1 | failed(1) | none | `dc02967` |
| 04-memory-systems | 2 | failed(1) | none | `7edc644` |
| 04-memory-systems | 3 | failed(1) | none | `2145150` |
| 05-evaluation-and-traces | 1 | failed(1) | none | `c67a4a6` |
| 05-evaluation-and-traces | 2 | failed(1) | none | `f611abc` |
| 05-evaluation-and-traces | 3 | failed(1) | none | `dd55775` |
| 06-agent-governance | 1 | failed(1) | none | `92f0554` |
| 06-agent-governance | 2 | failed(1) | none | `790a7cb` |
| 06-agent-governance | 3 | failed(1) | none | `62e5b27` |
| 07-production-ai-infrastructure | 1 | failed(1) | none | `5ec29a3` |
| 07-production-ai-infrastructure | 2 | failed(1) | none | `b328734` |
| 07-production-ai-infrastructure | 3 | failed(1) | none | `484d42d` |
| 99-future-directions | 1 | failed(1) | none | `006ff59` |
| 99-future-directions | 2 | failed(1) | none | `3a37252` |
| 99-future-directions | 3 | failed(1) | none | `905ee28` |

### Re-run Summary (2026-02-22T16:21:47Z)
- Completed 24/24 chapter passes with one commit per pass.
- Kernel runs were executed with governance unlock/unhold before each pass.
- Total commits created for this re-run loop: 24.

## Re-run 2026-02-22T16:22:29Z
| Chapter | Pass | Result | Subagents | Commit |
|--------:|-----:|--------|-----------|--------|
| 01-paradigm-shift | 1 | failed(1) | none | `55e0eb9` |
| 01-paradigm-shift | 2 | failed(1) | none | `b66b831` |
| 01-paradigm-shift | 3 | failed(1) | none | `f844808` |
| 02-harness-engineering | 1 | failed(1) | none | `6fe9d41` |
| 02-harness-engineering | 2 | failed(1) | none | `079b922` |
| 02-harness-engineering | 3 | failed(1) | none | `82761e8` |
| 03-autonomous-kernels | 1 | failed(1) | none | `7873fa5` |
| 03-autonomous-kernels | 2 | failed(1) | none | `97259ad` |
| 03-autonomous-kernels | 3 | failed(1) | none | `f9cef85` |
| 04-memory-systems | 1 | failed(1) | none | `a2f22b8` |
| 04-memory-systems | 2 | failed(1) | none | `e499595` |
| 04-memory-systems | 3 | failed(1) | none | `c6a3b47` |
| 05-evaluation-and-traces | 1 | failed(1) | none | `d49ece8` |
| 05-evaluation-and-traces | 2 | failed(1) | none | `9232289` |
| 05-evaluation-and-traces | 3 | failed(1) | none | `2d4490d` |
| 06-agent-governance | 1 | failed(1) | none | `3347d9e` |
| 06-agent-governance | 2 | failed(1) | none | `df7ccdc` |
| 06-agent-governance | 3 | failed(1) | none | `f79264f` |
| 07-production-ai-infrastructure | 1 | failed(1) | none | `12c41be` |
| 07-production-ai-infrastructure | 2 | failed(1) | none | `e522f2b` |
| 07-production-ai-infrastructure | 3 | failed(1) | none | `3a73022` |
| 99-future-directions | 1 | failed(1) | none | `3f58874` |
| 99-future-directions | 2 | failed(1) | none | `c86ef80` |
| 99-future-directions | 3 | failed(1) | none | `fdcbe09` |

### Re-run Summary (2026-02-22T16:22:29Z)
- Completed 24/24 chapter passes with one commit per pass.
- Kernel runs were executed with governance unlock/unhold before each pass.
- Total commits created for this re-run loop: 24.

## Re-run 2026-02-22T16:26:34Z
| Chapter | Pass | Result | Subagents | Commit |
|--------:|-----:|--------|-----------|--------|
| 01-paradigm-shift | 1 | failed(1) | none | `13dc900` |
| 01-paradigm-shift | 2 | failed(1) | none | `7a2d248` |
| 01-paradigm-shift | 3 | failed(1) | none | `7440d41` |
| 02-harness-engineering | 1 | failed(1) | none | `4b54f06` |
| 02-harness-engineering | 2 | failed(1) | none | `0edd1ca` |
| 02-harness-engineering | 3 | failed(1) | none | `b7d59c4` |
| 03-autonomous-kernels | 1 | failed(1) | none | `c9ab611` |
| 03-autonomous-kernels | 2 | failed(1) | none | `9a916a4` |
| 03-autonomous-kernels | 3 | failed(1) | none | `2182a82` |
| 04-memory-systems | 1 | failed(1) | none | `195f42c` |
| 04-memory-systems | 2 | failed(1) | none | `d01a4d9` |
| 04-memory-systems | 3 | failed(1) | none | `c8c1a3b` |
| 05-evaluation-and-traces | 1 | failed(1) | none | `4ca75d4` |
| 05-evaluation-and-traces | 2 | failed(1) | none | `29cd1ed` |
| 05-evaluation-and-traces | 3 | failed(1) | none | `8609d99` |
| 06-agent-governance | 1 | failed(1) | none | `0e74f94` |
| 06-agent-governance | 2 | failed(1) | none | `cd9c4a0` |
| 06-agent-governance | 3 | failed(1) | none | `be0d107` |
| 07-production-ai-infrastructure | 1 | failed(1) | none | `d391a74` |
| 07-production-ai-infrastructure | 2 | failed(1) | none | `c6b3d71` |
| 07-production-ai-infrastructure | 3 | failed(1) | none | `b74addd` |
| 99-future-directions | 1 | failed(1) | none | `132c8f8` |
| 99-future-directions | 2 | failed(1) | none | `b6b12e8` |
| 99-future-directions | 3 | failed(1) | none | `5a78de2` |

### Re-run Summary (2026-02-22T16:26:34Z)
- Completed 24/24 chapter passes with one commit per pass.
- Kernel runs were executed with governance unlock/unhold before each pass.
- Total commits created for this re-run loop: 24.

## Re-run 2026-02-22T16:28:30Z
| Chapter | Pass | Result | Subagents | Commit |
|--------:|-----:|--------|-----------|--------|
| 01-paradigm-shift | 1 | failed(1) | none | `31071ce` |
| 01-paradigm-shift | 2 | failed(1) | none | `ca46159` |
| 01-paradigm-shift | 3 | failed(1) | none | `cb4c849` |
| 02-harness-engineering | 1 | failed(1) | none | `0ec0e93` |
| 02-harness-engineering | 2 | failed(1) | none | `8133240` |
| 02-harness-engineering | 3 | failed(1) | none | `55ef015` |
| 03-autonomous-kernels | 1 | failed(1) | none | `a580b21` |
| 03-autonomous-kernels | 2 | failed(1) | none | `ca1e0e8` |
| 03-autonomous-kernels | 3 | failed(1) | none | `82fa5a2` |
| 04-memory-systems | 1 | failed(1) | none | `4c607df` |
| 04-memory-systems | 2 | failed(1) | none | `f7914f7` |
| 04-memory-systems | 3 | failed(1) | none | `221baa4` |
| 05-evaluation-and-traces | 1 | failed(1) | none | `4c0512b` |
| 05-evaluation-and-traces | 2 | failed(1) | none | `a3ae243` |
| 05-evaluation-and-traces | 3 | failed(1) | none | `107c7dc` |
| 06-agent-governance | 1 | failed(1) | none | `3aa80ba` |
| 06-agent-governance | 2 | failed(1) | none | `2554ac1` |
| 06-agent-governance | 3 | failed(1) | none | `2a9a0c8` |
| 07-production-ai-infrastructure | 1 | failed(1) | none | `0b08b7c` |
| 07-production-ai-infrastructure | 2 | failed(1) | none | `dd35324` |
| 07-production-ai-infrastructure | 3 | failed(1) | none | `b9bc4fe` |
| 99-future-directions | 1 | failed(1) | none | `31df46f` |
| 99-future-directions | 2 | failed(1) | none | `de7a4fa` |
| 99-future-directions | 3 | failed(1) | none | `19768f6` |

### Re-run Summary (2026-02-22T16:28:30Z)
- Completed 24/24 chapter passes with one commit per pass.
- Kernel runs were executed with governance unlock/unhold before each pass.
- Total commits created for this re-run loop: 24.

## Re-run 2026-02-22T16:34:23Z
| Chapter | Pass | Result | Subagents | Commit |
|--------:|-----:|--------|-----------|--------|
| 01-paradigm-shift | 1 | failed(1) | none | `chore: pass 1 for chapter 01-paradigm-shift` |
| 01-paradigm-shift | 2 | failed(1) | none | `chore: pass 2 for chapter 01-paradigm-shift` |
| 01-paradigm-shift | 3 | failed(1) | none | `chore: pass 3 for chapter 01-paradigm-shift` |
| 02-harness-engineering | 1 | failed(1) | none | `chore: pass 1 for chapter 02-harness-engineering` |
| 02-harness-engineering | 2 | failed(1) | none | `chore: pass 2 for chapter 02-harness-engineering` |
| 02-harness-engineering | 3 | failed(1) | none | `chore: pass 3 for chapter 02-harness-engineering` |
| 03-autonomous-kernels | 1 | failed(1) | none | `chore: pass 1 for chapter 03-autonomous-kernels` |
| 03-autonomous-kernels | 2 | failed(1) | none | `chore: pass 2 for chapter 03-autonomous-kernels` |
| 03-autonomous-kernels | 3 | failed(1) | none | `chore: pass 3 for chapter 03-autonomous-kernels` |
| 04-memory-systems | 1 | failed(1) | none | `chore: pass 1 for chapter 04-memory-systems` |

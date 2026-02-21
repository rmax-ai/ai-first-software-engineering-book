## Development Guidelines for the Harness in `state`

This repository treats the **harness** as the primary product; most of the engineering effort is centered on the deterministic ``state`` kernel, its visibility, and how it operators in a UV-managed Python runtime.

This document codifies how to contribute to that harness in a way that aligns with the current governance artifacts (`AGENTS.md`, `CONSTITUTION.md`, the migration ledger in `state/`).

### 1. Getting Started with UV

- Install dependencies via `uv install` so the pinned packages in `uv.lock` (currently the Copilot SDK) are used consistently. UV sandboxing isolates dev tooling from the system Python.
- Use `uv run python ...` whenever executing state harness scripts; for example, the smoke test is run via `uv run python state/copilot_sdk_uv_smoke.py` and the kernel itself should be invoked with `uv run python state/kernel.py --chapter-id <id>`.
- Keep `uv.lock` up to date with `uv lock` when dependencies change, then verify the lock file and `pyproject.toml` remain compatible.
### 2. Target Files and Intent

- The harness lives inside `state/`. Pay attention to `state/kernel.py`, the `state/role_io_templates.py` scaffolding, and the ledger/metrics/version maps under `state/`.
- Every change must respect the immutable governance files (`AGENTS.md`, `CONSTITUTION.md`) and the migration artifacts under `state/migration_iterations/` that document past iterations.
- Treat the kernel as a composition of pure helpers (parsers, validators) orchestrated by an imperative loop that enforces budgets, evals, and ledger writes.
### 3. SOLID Principles in Harness Engineering

1. **Single Responsibility**: Each module or dataclass should have just one reason to change. For instance, a module that loads YAML should not also mutate the ledger; mix `state/_io.py` (hypothetical) helpers with separate `state/ledger.py` writers.
2. **Open/Closed**: Build `Evaluator` and `Verifier` helpers that accept contracts (e.g., `evals/*.yaml`) rather than hard-coding gate logic. Adding a new eval should require writing a new YAML and wiring it through configuration, not editing the verifier core.
3. **Liskov Substitution**: If you introduce abstractions for LLM clients, ensure replacements for `LLMRun` or `Provider` behave identically in failure modes so the kernel loop does not break when swapping adapters (e.g., Copilot SDK vs. mock).
4. **Interface Segregation**: Keep the tool router/interfaces small. Kernels should only call the subset of functions they need (`_read_text`, `_write_text`, `_run_git`), not the entire toolkit, to avoid bloated inputs and hidden dependencies.
5. **Dependency Inversion**: Depend on abstractions (protocols or callables) rather than concrete implementations in the orchestration loop. Pass in a `GitRunner` callable or an `LLMClient` protocol so tests can inject deterministic doubles.
### 4. Functional Modular Design Patterns

- Favor pure helper functions for parsing, diff sizing, and text transformations. This keeps the kernel deterministically testable even if the orchestration layer enforces stateful budgets.
- Isolate I/O (file reads/writes, Git, subprocess) behind minimal wrappers. A small set of functions (`_read_text`, `_write_text`, `_run_git`) reduces side effects and makes it easier to reason about failure handling.
- Compose functionality through small modules. Example areas include:
  - **Input builders** (prompt loaders, roadmap extractors)
  - **Validators** (heading, budget, diff size)
  - **Emitters** (ledger updates, metric writes, evaluation logging)
- Use data classes (like `LLMConfig`, `LLMRun`) as immutable inputs for pure functions and combine them with functions that return new data instead of mutating global state.
- Write focused unit tests for the helper functions; keep any complex orchestrations in higher-level scripts that can be validated via the deterministic eval gate rather than manual assertions.
### 5. Verification & Evaluation

- Rely on the eval contracts in `evals/chapter-quality.yaml`, `evals/style-guard.yaml`, and `evals/drift-detection.yaml` when modifying kernel behavior. They describe the conditions under which an iteration is considered valid.
- When kernel logic changes, manually run the relevant Python scripts with `uv run python state/kernel.py --chapter-id ...` and confirm that the deterministic guardrails (diff cap, heading preservation, ledger updates) still pass.
- Document verification results in the iteration artifacts (e.g., the next `state/migration_iterations/iter_XXX` folder), including commands executed and outcomes observed.
### 6. Contribution Flow

1. **Plan**: Summarize the change and how it satisfies the iteration goal (e.g., new helper, bug fix, new eval). If the iteration is sufficiently complex, draft the plan in one of the `state/migration_iterations/iter_XXX/02-plan.md` files.
2. **Implement**: Apply minimal diffs with `apply_patch` or `uv`-driven scripts. Keep edits targeted and document reasoning in the associated iteration folder.
3. **Evaluate**: Run the kernel, smoke tests, or targeted unit tests. Record evidence per harness rules (tests, outputs, evaluation status).
4. **Log**: Update the ledger (`state/ledger.json`), metrics (`state/metrics.json`), and create the migration iteration artifact that captures execution details and next steps.

### 7. Relevant References

- Running the kernel: `state/kernel.py` (entry point for harness orchestration).
- Prompt contracts: `prompts/planner.md`, `prompts/writer.md`, `prompts/critic.md` (used when the kernel operates with the LLM).
- Support modules: `state/llm_client.py`, `state/copilot_sdk_uv_smoke.py` (examples referencing uv-managed SDK usage).
- Migration artifacts: `state/migration_iterations/` (iteration-by-iteration documentation for past work).

Follow these guidelines when developing the harness to keep the system predictable, modular, and aligned with the broader governance goals of this book.

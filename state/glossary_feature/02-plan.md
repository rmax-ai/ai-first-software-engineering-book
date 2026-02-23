# Plan — Glossary Updater Kernel Target

## Goal
Add a kernel mode that can *propose* and (optionally) *apply* updates to the glossary at book/glossary.md by scanning the current book content (chapters/patterns/preface), extracting candidate terms + evidence snippets, and running a governed planner→writer→critic loop with deterministic eval gates.

Non-goals (to keep this minimal):
- No “semantic search index” or embeddings.
- No UI or MkDocs plugin work.
- No cross-repo knowledge; only uses this repo’s markdown.
- No automatic term deletion by default.

## High-level UX (CLI)
Extend the kernel CLI with a glossary target that is explicitly invoked (so glossary edits don’t happen accidentally).

Proposed CLI shape:
- `uv run python state/kernel.py --target glossary` (new)
  - Optional: `--glossary-path book/glossary.md` (default)
  - Optional: `--glossary-sources book/chapters/*.md book/patterns/*.md book/preface.md` (defaults)
  - Optional: `--max-new-terms 8` (per run cap)
  - Optional: `--allow-delete` (off by default)

Compatibility:
- Default behavior remains unchanged: if `--target` is omitted, treat it as `chapter` and require `--chapter-id`.

## Kernel integration approach
Introduce a small “target” abstraction:

- `TargetKind = Literal["chapter", "glossary"]`
- Add a new `run_glossary_kernel(...)` function that reuses existing:
  - iteration directory layout + trace logging
  - LLM auto-generation wiring (`--llm`)
  - repo iteration log writing via `append_repo_iteration_entry`

Avoid trying to shoehorn the glossary into `state/ledger.json` `chapters` entries.
- The existing chapter loop has hard-coded chapter quality constraints (required chapter sections), heading preservation, and lifecycle transitions.
- Glossary is an auxiliary artifact with different invariants.

## Data flow
### 1) Load baseline glossary
Inputs:
- baseline glossary text from `book/glossary.md`
- list of existing terms (H2 headings)

Parser:
- deterministically parse H2 headings that start with `## `.

### 2) Build a “corpus” from book sources
Sources (default):
- `book/chapters/*.md`
- `book/patterns/*.md`
- `book/preface.md`

For each source document:
- extract file path
- extract headings (H1/H2/H3) for contextual labels
- keep full text for matching

### 3) Deterministically extract candidate terms + evidence
Candidate term heuristics (deterministic; no extra dependencies):
- Title Case noun-phrases approximated by:
  - sequences of words matching `[A-Z][a-z]+` (length 1–4 words)
  - exclude common English stop words (small static list)
- Terms in markdown emphasis that often introduce definitions:
  - `**Term**` / `*Term*` (collect if Title Case or snake_case)
- Inline code identifiers:
  - backticked code spans like `` `Kernel` `allowlist` `` (filter for 3+ chars)
- Existing glossary-adjacent patterns:
  - occurrences of `See also:` lines
  - occurrences of `Definition:` or `Thesis:` markers

Evidence snippet collection:
- for each candidate, collect up to N snippets (e.g., N=3):
  - a fixed-size window (e.g., ±200 chars) around the first few occurrences
  - include `source_path` and nearest heading(s) for context

Outputs written into the iteration input folder:
- `in/glossary_baseline.md` (baseline glossary)
- `in/glossary_corpus_index.json` (list of sources + their headings)
- `in/glossary_candidates.json` (candidate list, frequency counts, snippets)

This keeps the run reproducible and makes critic/eval gates possible without re-scanning.

### 4) Planner role (glossary)
Add a glossary-specific planner contract and schema.

Inputs to planner:
- baseline glossary term list
- candidate term list + evidence snippets
- run limits: `max_new_terms`, deletion policy, and formatting requirements

Planner output (JSON only):
```json
{
  "add_terms": [
    {
      "term": "Deterministic Gate",
      "rationale": "Shows up repeatedly in Chapter 05; missing from glossary.",
      "evidence": [
        {"source": "book/chapters/05-evaluation-and-traces.md", "quote": "..."}
      ]
    }
  ],
  "update_terms": [
    {
      "term": "Drift",
      "rationale": "Expand to include memory-induced drift; aligns with Chapter 04.",
      "evidence": [{"source": "book/chapters/04-memory-systems.md", "quote": "..."}]
    }
  ],
  "merge_terms": [],
  "remove_terms": [],
  "notes": ["Keep alphabetical order", "No new subheadings"]
}
```
Constraints:
- `remove_terms` must be empty unless `--allow-delete` is enabled.
- Hard cap: `len(add_terms) <= max_new_terms`.

### 5) Writer role (glossary)
Writer input:
- baseline glossary markdown
- planner JSON
- (optionally) compact evidence bundle per term

Writer output:
- full revised `book/glossary.md` markdown

Writer constraints (glossary-specific):
- Preserve the top-level `# Glossary` heading.
- Each term is a `## <Term>` heading followed by 1–4 short paragraphs.
- Keep terms in strict alphabetical order by heading text.
- Do not delete any existing term unless it is in `remove_terms` (and deletion is allowed).
- Updates should be surgical:
  - only modify term blocks in `update_terms`
  - only add new blocks in `add_terms`
  - do not rewrite unrelated blocks

### 6) Critic role (glossary)
Add a glossary-specific critic contract and schema, rather than reusing chapter metrics.

Critic inputs:
- revised glossary markdown
- `evals/glossary-guard.yaml` (new)
- (optional) the candidates/evidence bundle for “term appears in corpus” checks

Critic output schema (JSON only):
```json
{
  "format_pass": true,
  "coverage_score": 0.8,
  "operationality_score": 0.9,
  "violations": ["Term 'X' is not present in corpus evidence"],
  "decision": "approve"
}
```

Decision rule in the kernel:
- `pass_now = (critic.decision == "approve") && deterministic_glossary_eval.pass && diff_ratio <= max_diff_ratio`

## Deterministic eval gates (new)
Add a new eval contract file, e.g. `evals/glossary-guard.yaml` (versioned).

Deterministic checks to implement (all local, stable):
1. **Header + structure**
   - file starts with `# Glossary`
   - all term headings are `## `
   - no duplicate `##` headings
2. **Ordering**
   - H2 headings are alphabetical (case-insensitive) and stable
3. **Definition bounds**
   - each term body non-empty
   - min/max character bounds (e.g., 40–900 chars) to avoid stubs or essays
4. **No forbidden tone** (optional)
   - reuse the existing “marketing/anthropomorphism” keyword scan from chapter-quality
5. **Corpus evidence (for new terms)**
   - any `add_terms[*].term` must have at least one match in the corpus scan
   - the scan output in `in/glossary_candidates.json` is the source of truth

Implementation detail:
- Add `run_glossary_evals(revised_glossary, candidates_index, config)` alongside `run_deterministic_evals`.

## Iteration directory + IO files
Follow existing kernel layout, but under a dedicated target ID:
- `state/role_io/glossary/iter_XX/in/...`
- `state/role_io/glossary/iter_XX/out/...`

Role outputs (consistent names):
- `out/planner.json`
- `out/writer.md`
- `out/critic.json`

Trace files:
- `out/kernel_trace.jsonl`
- `out/_llm_trace/*` (if `--llm`)

## Logging / ledger impact
- Do **not** add glossary to `ledger.json` chapters.
- Do append a repo iteration entry with:
  - `agent_task: "kernel_glossary_update"`
  - `inputs.changed_files: ["book/glossary.md", "state/ledger.json"(tail), ...]`
  - `evals.glossary_guard: ...`
- Keep the chapter selection strategy unchanged.

## Incremental implementation steps (PR-sized)
1. Add CLI plumbing for `--target glossary` and a stub `run_glossary_kernel` that only reads inputs and writes iteration inputs.
2. Add deterministic candidate extraction + `in/glossary_candidates.json` writer.
3. Add new prompts:
   - `prompts/glossary_planner.md`
   - `prompts/glossary_writer.md`
   - `prompts/glossary_critic.md`
4. Add glossary deterministic eval (`run_glossary_evals`) + config YAML `evals/glossary-guard.yaml`.
5. Wire LLM generation for glossary roles (parallel to existing `_llm_generate_*` but pointing at glossary prompts).
6. Add a “manual mode” flow (no `--llm`): kernel stops if outputs are missing, just like chapters.
7. Add a small smoke command section to DEVELOPMENT.md describing how to run a glossary update.

## Verification plan (evidence)
Because there are no unit tests today, use a bounded smoke run as evidence:
- `uv run python state/kernel.py --target glossary --llm --llm-model <...> -v --max-iterations 1`
- Confirm:
  - deterministic glossary guard passes
  - `git diff` shows only book/glossary.md changes
  - repo iteration log tail includes `kernel_glossary_update`

## Risks / edge cases
- Candidate extraction is heuristic; mitigation: planner can ignore noisy candidates, and the per-run cap prevents runaway edits.
- Alphabetical ordering could cause large diffs when inserting new terms; mitigation: cap new terms and keep updates surgical.
- Some terms may appear with variants (singular/plural); mitigation: include exact evidence snippets and keep merges manual (explicit planner action).

## Files expected to change (once implemented)
- `state/kernel.py` (new target wiring)
- `prompts/glossary_planner.md`
- `prompts/glossary_writer.md`
- `prompts/glossary_critic.md`
- `evals/glossary-guard.yaml`
- `DEVELOPMENT.md` (run instructions)


# AI-First Software Engineering

Welcome to the public documentation for the AI-first software engineering book. This site publishes the current working drafts, glossaries, patterns, and operational governance that power the book’s ongoing iteration loop.

## Contents

- **Preface** – foundational motivation and thesis for the AI-first engineering approach.
- **Chapters** – structured research chapters covering paradigm shifts, harness engineering, autonomous kernels, memory systems, evaluation, governance, and production infrastructure.
- **Patterns** – reusable engineering patterns curated from the repository.
- **Glossary** – operational definitions and terminology used throughout the book.

## Publishing workflow

1. Chapters are drafted in `book/chapters/` with deterministic loops enforced by `state/kernel.py`.
2. The MkDocs configuration references the book files directly so every build reflects the latest chapter revisions.
3. Use `mkdocs build` to produce the static site or `mkdocs serve` for a preview server before deployment.
4. Keep governance documents (`CONSTITUTION.md`, `AGENTS.md`) and evaluation rules (`evals/`) aligned with the book’s stated principles.

## Quick commands

```bash
mkdocs build          # Generate the static site
mkdocs serve          # Start a local preview server
mkdocs gh-deploy      # Publish to GitHub Pages (configure remote)
```

## Project tree

```
mkdocs.yml                    # Site configuration for the book
docs/index.md                 # Site homepage (this file)
book/chapters/*.md           # Chapter drafts consumed by MkDocs navigation
book/patterns/               # Referenced pattern library
book/glossary.md             # Detailed glossary definitions
CONSTITUTION.md, AGENTS.md    # Governance that shapes the book process
evals/*.yaml                 # Evaluation contracts enforced via state/kernel.py
```

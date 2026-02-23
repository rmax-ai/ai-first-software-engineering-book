# Task

## Selected task
Plan a kernel feature that can update and expand the book glossary (book/glossary.md) based on the current contents of the book.

## Why this task now
- The glossary is a living “operational definitions” index; it should track terms introduced across chapters/patterns.
- Manual glossary maintenance is easy to forget and hard to keep consistent as chapters evolve.
- The existing deterministic kernel (planner→writer→critic + eval gates) is a natural place to add a governed, repeatable glossary-update loop.

## Acceptance criteria
1. Produce a concrete implementation plan for a glossary-update target in the kernel.
2. The plan specifies: CLI UX, inputs/outputs, deterministic candidate extraction, role prompts and JSON schemas, eval gates, and logging/trace behavior.
3. The plan is incremental (can be implemented in small PR-sized steps) and avoids broad refactors.

# AI-First Software Engineering

This repository is a technical book and a working research artifact.
The book is developed via an autonomous edit loop operating inside a Git repository under explicit governance and evaluation rules.

## What “AI-first software engineering” means (in this book)

AI-first software engineering treats *the harness* as the primary design surface.

- **Model**: the reasoning component that proposes plans and edits.
- **Harness**: the engineered environment that makes work predictable (tools, constraints, evaluation gates, traces, state).

The working hypothesis is that most reliability gains in real repositories come from harness design: better tool contracts, tighter constraints, stronger verification, and better observability.

## Repository layout

- `book/chapters/`: chapter drafts (structured skeletons).
- `book/patterns/`: reusable engineering patterns.
- `book/glossary.md`: operational definitions used throughout.
- `evals/`: declarative evaluation rules (quality, drift, and style guardrails).
- `state/`: iteration state (ledger, version map, metrics).

Governance is defined in:

- `CONSTITUTION.md` (immutable principles)
- `AGENTS.md` (operational rules for autonomous work)

## Agent loop (operational)

Work is performed in bounded iterations:

1. **Plan** (what will change; how it will be evaluated)
2. **Generate artifact** (apply minimal diffs to targeted files)
3. **Self-evaluate** (check against explicit criteria; record evidence)
4. **Refine** (fix gaps; reduce ambiguity)
5. **Commit** (commit the iteration)
6. **Log trace** (write/update state artifacts)

## How evaluation is run

Evaluations are defined as contracts in `evals/*.yaml`. A harness can implement them mechanically.

For a minimal local check today (structure only), run:

```bash
python - <<'PY'
from pathlib import Path

required = [
	'## Thesis',
	'## Why This Matters',
	'## System Breakdown',
	'## Concrete Example 1',
	'## Concrete Example 2',
	'## Trade-offs',
	'## Failure Modes',
	'## Research Directions',
]

bad = []
for p in sorted(Path('book/chapters').glob('*.md')):
	text = p.read_text(encoding='utf-8')
	missing = [h for h in required if h not in text]
	if missing:
		bad.append((p.as_posix(), missing))

if bad:
	for path, missing in bad:
		print('FAIL', path)
		for h in missing:
			print('  missing:', h)
	raise SystemExit(1)

print('OK: chapter skeleton headings present')
PY
```

This check is intentionally narrow; the stricter requirements (tone, drift, evidence, and “no vague claims”) are captured in the YAML rules and are expected to be enforced by the harness.

## Diagrams

### Agent loop

```mermaid
flowchart TD
	A[Plan] --> B[Generate Artifact]
	B --> C[Self-evaluate]
	C --> D{Meets gates?}
	D -- No --> E[Refine]
	E --> C
	D -- Yes --> F[Commit]
	F --> G[Log trace / update state]
```

### Book system architecture

```mermaid
flowchart LR
	subgraph Governance
		CON[CONSTITUTION.md]
		AG[AGENTS.md]
	end

	subgraph Content
		CH[book/chapters/*]
		PAT[book/patterns/*]
		GLO[book/glossary.md]
	end

	subgraph Evaluation
		E1[evals/chapter-quality.yaml]
		E2[evals/style-guard.yaml]
		E3[evals/drift-detection.yaml]
	end

	subgraph State
		L[state/ledger.json]
		V[state/version_map.json]
		M[state/metrics.json]
	end

	CON --> Content
	AG --> Content
	Content --> Evaluation
	Evaluation --> State
```
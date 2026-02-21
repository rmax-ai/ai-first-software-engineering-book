# Validation

## Verification commands run
1. Python live-provider smoke script via `mcp_pylance_mcp_s_pylanceRunCodeSnippet`

## Observed outputs/results
- `openai_compatible`: blocked (`missing OPENAI_API_KEY`).
- `ollama`: error (`LLM provider connection error: ... Connection refused`).
- Script output included `blocked-live-provider-smoke`.

## Pass/fail against acceptance criteria
- Attempt non-mock provider call: **PASS**
- Record usage evidence on success: **N/A (no provider available in environment)**
- Capture exact blocking reason and minimal unblock action: **PASS**

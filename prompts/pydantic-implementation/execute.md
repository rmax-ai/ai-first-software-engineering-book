# Pydantic Implementation Runner Prompt

You are an autonomous engineering agent operating inside the repository.

## Primary Objective

Implement a Pydantic-powered ingestion and transit layer in the custom harness under `state/`. When external data is loaded (fixtures, kernel traces, or evaluation inputs) it must be parsed through typed Pydantic models. When that data is passed between harness components, it should move through explicit data classes (e.g., `@dataclass`) so that state transitions remain visible, type-checked, and serializable.

## Pre-flight Requirements

1. Inspect `state/` to understand how data currently enters and flows through the harness (look at `state/kernel.py`, `state/role_io_templates.py`, and any helper modules such as `state/copilot_sdk_smoke_test.py`).
2. Identify the files or canonical data blobs that are considered "external" (file-based JSON/YAML/CSV, API responses, etc.).
3. Confirm there is a consistent way to move data between harness layers and where additional structure would clarify intent.

## Execution Rules

- Pick the smallest change that touches the ingestion path and transit path simultaneously (e.g., add a Pydantic model where data is read and an annotated data class where it is forwarded).
- Preserve existing public interfaces; add wrappers/adapters if stricter typing is required.
- Keep diffs minimal: change only the files necessary to make the new structure work.
- Validate the change by running a targeted harness exercise (e.g., `python state/copilot_sdk_smoke_test.py` if it exercises the path, or another dedicated script that covers the modified surfaces).
- Document the new structure in any relevant markdown file inside `prompts/pydantic-implementation/` if needed for future iterations (e.g., how data flows should be typed and what models exist).

## Implementation Guidance

1. **External Data Parsing**: Introduce Pydantic `BaseModel` subclasses for every external payload you control (inputs, environment, evaluation results). Use `.parse_obj()` or `.model_validate()` to enforce schemas as soon as the data enters the harness. Handle validation errors explicitly and translate them into the harness logging or exception strategy.
2. **Internal Data Movement**: Create lightweight `@dataclass` objects (or frozen dataclasses when immutability helps) to represent state transfers between kernel components. Each dataclass should reference the relevant Pydantic model where appropriate to signal the relationship between external and internal representations.
3. **State Module Updates**: Update `state/kernel.py`, `state/role_io_templates.py`, or other touched modules to consume the new typed structures. Wherever you previously passed raw dictionaries or loosely typed tuples, replace them with the defined dataclasses.
4. **Serialization / Round-trip**: Ensure that converting back to raw dicts for logging, persistence, or evaluation output continues to work (use `.model_dump()` and `asdict()` as needed).

## Validation

- Run the harness-focused smoke test(s) that exercise the ingestion path. Prefer the documented script in `state/` (e.g., `python state/copilot_sdk_smoke_test.py`).
- Include the exact command(s) executed and the results (pass/fail) in the final summary so future iterations can verify reproducibility.

## Output Requirements

- Provide a concise description of what models/dataclasses were introduced and where they are used.
- List the validation commands executed and their outcomes.
- If the change requires follow-up work (additional models, additional flows), include a single next-step recommendation under a short heading (e.g., "Next Step").

## Stop Condition

Stop after you have implemented the typed ingestion/transit layer, documented the new structure, and recorded verification evidence for the validation commands. If blocked, describe the blocker, the last successful observation, and the smallest actionable unblock step.

## Typed Flow Notes

- `state/kernel.py` validates `in/planner_input.json`, `out/planner.json`, and `out/critic.json` with Pydantic payload models before use.
- `state/kernel.py` also validates `state/ledger.json` through `LedgerPayload` and materializes each iteration's planner input via `PlannerInputTransit` before writing `in/planner_input.json`.
- `state/kernel.py` now forwards validated ledger payloads between kernel setup stages through `LedgerTransit` instead of raw tuple unpacking.
- `state/kernel.py` validates deterministic eval YAML payloads through `DeterministicEvalConfigPayload` and forwards them between evaluators via `DeterministicEvalTransit`.
- `state/kernel.py` validates `state/metrics.json` and `state/version_map.json` through `MetricsPayload` and `VersionMapPayload` before updating runtime artifacts.
- `state/kernel.py` now forwards validated metrics payloads through `MetricsTransit` before updating chapter metrics history.
- `state/kernel.py` now forwards validated version map payloads through `VersionMapTransit` before updating chapter commit pointers.
- `state/kernel.py` now validates `ROADMAP.md` ingestion through `ChapterTextPayload` and forwards roadmap content via `RoadmapTextTransit` before hypothesis extraction.
- The planner input payload is converted into a `PlannerInputTransit` dataclass before being forwarded to the planner LLM prompt.
- Metrics history entries are now forwarded through `MetricsHistoryTransit` before append/write operations.
- Planner and critic role output ingestion now forwards validated payloads through `PlannerPlanTransit` and `CriticReportTransit` before runtime evaluation checks.
- Kernel runtime logic continues consuming internal dataclasses (`PlannerPlan`, `CriticReport`) after validation.
- `state/role_io_templates.py` now validates `state/ledger.json` through `LedgerPayload` and forwards chapter data via the `TemplateContext` dataclass before template writes.
- `state/role_io_templates.py` now also forwards validated ledger payloads between template preparation steps via `LedgerTransit`.
- `state/role_io_templates.py` now validates chapter markdown file ingestion via `ChapterTextPayload` and forwards validated chapter text via `ChapterTextTransit` before template context assembly.
- `state/governance_engine.py` now validates `state/ledger.json` through `LedgerPayload` and passes parsed ledger data between CLI handlers via `LedgerTransit`.
- `state/governance_engine.py` now validates raw `state/ledger.json` root mappings via `LedgerJSONPayload` and forwards parsed mappings through `LedgerJSONTransit` before `LedgerPayload` parsing and `LedgerTransit` forwarding.
- `state/governance_engine.py` now parses lifecycle transition thresholds via `ChapterLifecycleRulesPayload` and forwards promotion thresholds via `PromotionRulesTransit` before lifecycle promotion computation.
- `state/governance_engine.py` now parses chapter selection strategy ordering via `ChapterSelectionStrategyPayload` and forwards lifecycle selection order via `SelectionStrategyTransit` before deterministic chapter selection.
- `state/copilot_sdk_uv_smoke.py` now validates trace-summary metrics and `kernel_trace.jsonl` phase payloads with Pydantic models and forwards validated values through `MetricsHistoryTransit` and `PhaseTraceTransit`.
- `state/copilot_sdk_uv_smoke.py` now validates fixture `state/ledger.json` chapter metadata with `KernelFixtureLedgerPayload` and forwards chapter setup through `KernelFixtureChapterTransit` before kernel smoke fixture writes.
- `state/copilot_sdk_uv_smoke.py` now forwards validated fixture ledgers through `KernelFixtureLedgerTransit` before extracting chapter fixture payloads.
- `state/copilot_sdk_uv_smoke.py` now validates `phase_trace` kernel trace entries via `KernelTracePhaseEntryPayload` and forwards payload objects through `KernelTracePhaseTransit` before `PhaseTraceTransit` conversion.
- `state/copilot_sdk_uv_smoke.py` now validates `kernel_trace.jsonl` ingestion via `KernelTracePayload` and forwards trace entries through `KernelTraceTransit` before phase extraction.
- `state/copilot_sdk_uv_smoke.py` now validates `kernel_trace.jsonl` JSON-object line mappings through `JSONLinesPayload` and forwards parsed entries via `JSONLinesTransit` before `KernelTracePayload` parsing.
- `state/copilot_sdk_uv_smoke.py` now validates each `kernel_trace.jsonl` line through `JSONLinePayload` (including source line numbers) before forwarding line mappings through `JSONLinesTransit`.
- `state/copilot_sdk_uv_smoke.py` now validates `metrics.json` ingestion via `MetricsPayload` and forwards validated payloads through `MetricsTransit` before chapter history checks.
- `state/copilot_sdk_uv_smoke.py` now validates raw JSON mapping roots via `JSONMappingPayload` and forwards parsed mappings via `JSONMappingTransit` before `MetricsPayload` parsing.
- `state/copilot_sdk_uv_smoke.py` now validates fixture ledger JSON roots via `JSONMappingPayload` and forwards parsed mappings through `JSONMappingTransit` before `KernelFixtureLedgerPayload` parsing.
- `state/copilot_sdk_smoke_test.py` now validates latest `trace_summary` fixture payloads through `TraceSummaryPayload` and forwards them via `TraceSummaryTransit` before key-presence checks.
- `state/copilot_sdk_smoke_test.py` now validates `state/ledger.json` kernel-mode snapshots through `LedgerSnapshotPayload` and forwards them via `LedgerSnapshotTransit` before unchanged-ledger assertions.
- `state/copilot_sdk_smoke_test.py` now validates raw ledger snapshot JSON mapping roots through `JSONMappingPayload` and forwards parsed mappings via `JSONMappingTransit` before `LedgerSnapshotPayload` parsing.
- `state/kernel.py` now validates cross-chapter markdown ingestion through `ChapterTextPayload` and forwards deterministic-eval chapter context via `OtherChaptersTransit`.
- `state/llm_client.py` now validates external `chat()` message payload lists through `ChatMessagesPayload` and forwards validated messages via `ChatMessagesTransit` before mock/Copilot provider handling.
- `state/llm_client.py` now validates Copilot SDK `send()` response dictionaries through `SDKChatResponsePayload` and forwards them via `SDKChatResponseTransit` before usage/content normalization.
- `state/llm_client.py` now validates Copilot SDK `events` response lists through `SDKEventsPayload` and forwards them via `SDKEventsTransit` before aggregating usage tokens.
- `state/llm_client.py` now validates raw SDK usage mappings through `SDKUsagePayload` and forwards normalized usage through `SDKUsageTransit` before token accounting.
- `state/copilot_sdk_smoke_test.py` now translates `LedgerSnapshotPayload` validation failures into explicit assertion errors during ledger fixture ingestion while forwarding validated snapshots via `LedgerSnapshotTransit`.
- `state/role_io_templates.py` now validates raw JSON mapping roots through `JSONMappingPayload` and forwards parsed mappings via `JSONMappingTransit` before `LedgerPayload` parsing.
- `state/kernel.py` now validates deterministic eval YAML mapping roots through `YAMLMappingPayload` and forwards parsed mappings via `YAMLMappingTransit` before `DeterministicEvalConfigPayload` parsing.
- `state/kernel.py` now forwards each deterministic eval YAML payload through `DeterministicEvalConfigTransit` before composing `DeterministicEvalTransit` for evaluator execution.
- `state/kernel.py` now validates raw JSON mapping roots through `JSONMappingPayload` and forwards parsed mappings via `JSONMappingTransit` before planner/role output and runtime payload parsing.
- `state/kernel.py` now validates planner/critic LLM JSON response ingestion through `JSONMappingPayload` and forwards parsed objects via `JSONMappingTransit` before role output persistence.
- `state/kernel.py` now validates critic eval input ingestion (`evals/chapter-quality.yaml`, `evals/style-guard.yaml`, `evals/drift-detection.yaml`) through `CriticEvalInputsPayload` and forwards values via `CriticEvalInputsTransit` before critic prompt assembly.
- `state/kernel.py` now validates active chapter markdown ingestion through `ChapterTextPayload` and forwards validated text via `ChapterTextTransit` before planner input assembly and writer/diff evaluation checks.
- `state/kernel.py` now validates `out/writer.md` ingestion through `WriterOutputPayload` and forwards validated markdown via `WriterOutputTransit` before critic prompt assembly and runtime evaluation checks.
- `state/copilot_sdk_smoke_test.py` now validates ledger snapshot JSON roots through `_load_json_mapping()` and forwards raw JSON text plus parsed mappings via `JSONMappingTransit` before `LedgerSnapshotTransit` assembly.

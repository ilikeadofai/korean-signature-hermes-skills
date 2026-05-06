# Subagent Plan for the Generic SIGNATURE Harness

This plan defines how Hermes should use delegation/subagents when available. It is portable: if subagents are unavailable, the main orchestrator performs the same stages sequentially.

## 1. Current environment note

During this run, direct delegation was available and configured with:

- `max_concurrent_children: 3`
- `child_timeout_seconds: 600`
- `max_spawn_depth: 1`
- `inherit_mcp_toolsets: true`

Practical implication: use direct leaf subagents from the main orchestrator. Do not rely on nested subagent orchestration.

## 2. Orchestration principles

1. The main orchestrator owns final decisions.
2. Subagents may extract, critique, or draft bounded artifacts, but the orchestrator must verify their outputs.
3. Subagents should receive only the minimum necessary context.
4. Raw sensitive records should not be sent to subagents unless redacted or explicitly approved.
5. Each subagent must return evidence references or clearly label unsupported suggestions.
6. Conflicts between subagents are resolved by the orchestrator using the evidence ledger.
7. All outputs must be saved to files by the orchestrator or verified after subagent writes.

## 3. Recommended subagent architecture

### 3.1 Document/OCR Extractor

Goal: Extract text and structure from supplied PDFs/images/documents.

Inputs:

- school framework PDFs
- redacted student record only after privacy gate
- extraction tool availability notes

Allowed tools:

- file reading
- terminal/PDF extraction
- OCR/vision if available
- code execution for conversion and cleanup

Output:

```md
# Extraction Log

## Source inventory
## Extraction method per file
## Extraction quality
## OCR uncertainties
## Pages/sections requiring user review
## Privacy warnings
```

Quality rules:

- Do not interpret student traits.
- Mark OCR uncertainty.
- Do not reproduce sensitive identifiers.

### 3.2 School Framework Analyst

Goal: Extract actual SIGNATURE / SD Navigation / performance-assessment requirements.

Inputs:

- school framework documents
- workbook/performance assessment list

Output:

```md
# School Framework Summary

## SIGNATURE structure
## SD Navigation structure
## Required deliverables
## Subject/performance-assessment opportunities
## Recommended artifact forms
## Risky/prohibited wording
## School templates and useful phrases
## Open questions
```

Quality rules:

- Quote or cite page/section when possible.
- Distinguish supplied requirements from inferred assumptions.

### 3.3 Evidence Extractor

Goal: Extract concrete facts from the redacted Grade 10 record.

Inputs:

- redacted school record text
- extraction log
- privacy policy

Output:

```md
# Evidence Ledger

| Evidence ID | Source | Location | Quote/summary | Category | Concrete action | Outcome/limit | Privacy level | Confidence |
|---|---|---|---|---|---|---|---|---|
```

Quality rules:

- No interpretation without evidence.
- Use minimal Korean quotes.
- Label uncertain OCR readings.
- Do not include sensitive excluded data.

### 3.4 Activity and Interest Mapper

Goal: Convert evidence into activity patterns and interest clusters.

Inputs:

- evidence ledger
- student interest statements
- avoided directions

Output:

```md
# Activity and Interest Profile

## Activity pattern hypotheses
## Interest clusters
## Strength clusters
## Possible career/field families
## Directions to avoid
## Evidence gaps
```

Quality rules:

- Every pattern must cite evidence IDs.
- Weak clusters must be labeled hypotheses.
- Avoid single-activity identity overreach.

### 3.5 Psychology and Learning Profile Analyst

Goal: Build a non-diagnostic profile for activity design.

Inputs:

- evidence ledger
- activity profile
- student workflow preferences

Output:

```md
# Learning Profile

## Observed learning patterns
## RIASEC hypothesis
## Self-determination theory implications
## Mastery-goal/workflow observations
## Practical activity-design suggestions
## Cautions and limits
```

Quality rules:

- No clinical labels.
- No diagnosis.
- No health/family details in school-facing text.
- Convert observations into workflow suggestions, not identity labels.

### 3.6 Theme Generator

Goal: Generate multiple evidence-grounded SIGNATURE axis candidates.

Inputs:

- school framework summary
- evidence ledger
- activity/interest profile
- learning profile
- student preferences and avoided directions

Output:

```md
# Theme Candidates

| Candidate ID | Axis name (KO) | One-line definition (KO) | Evidence fit | Interest fit | Subject fit | Feasibility | Differentiation | Minimal artifact | Risks |
|---|---|---|---:|---:|---:|---:|---:|---|---|
```

Quality rules:

- Generate 2–5 candidates when evidence allows.
- Include non-obvious cross-over options.
- Do not default to computer science, medicine, or any field without evidence.
- Include at least one low-risk minimal artifact path.

### 3.7 Feasibility Critic

Goal: Attack candidate axes before asking the student.

Inputs:

- theme candidates
- school framework summary
- evidence ledger
- known constraints

Output:

```md
# Feasibility Critique

## Strong candidates
## Weak candidates
## Overreach risks
## Privacy/ethics risks
## Recommended narrowing
## Korean questions for the student
```

Review dimensions:

- too broad?
- too generic?
- high-school feasible?
- artifact concrete?
- failure analyzable?
- subject link real?
- evidence-supported?
- privacy safe?

### 3.8 Privacy Auditor

Goal: Identify privacy and sensitive-data risks across artifacts.

Inputs:

- source inventory
- evidence ledger
- claim ledger
- draft outputs

Output:

```md
# Privacy Audit

| Item | Location | Risk | Required action | Safe rewrite/removal |
|---|---|---|---|---|

## Blocking issues
## Warnings
## School-facing safety verdict
```

Quality rules:

- BLOCK direct identifiers, health/family/counseling/diagnosis details, third-party data, and secrets.
- Do not reveal sensitive content while reporting the risk.

### 3.9 Korean Draft Writer

Goal: Produce Korean student-facing draft after evidence, theme selection, and feasibility review.

Inputs:

- confirmed student decision log
- selected axis
- subject roadmap
- evidence and claim ledgers
- Korean drafting style guide

Output:

```md
# Project SIGNATURE Draft

## STEP 1. Signature Discovery
## STEP 2. Signature Enhancement
## STEP 3. Signature Masterpiece
## 하지 않을 것
## 학생 확인 필요 부분
```

Quality rules:

- Output in Korean.
- Use concrete verbs.
- Avoid inflated claims.
- Do not include unsupported or sensitive content.
- If student confirmation is missing, mark provisional.

### 3.10 Evidence and Tone Auditor

Goal: Verify final Korean draft against evidence, privacy, tone, and school context.

Inputs:

- Korean draft
- evidence ledger
- claim ledger
- school framework summary
- privacy audit

Output:

```md
# Evidence and Tone Audit

| Draft claim | Evidence IDs | Strength | Risk | Required fix | Safe Korean rewrite |
|---|---|---|---|---|---|

## Unsupported claims to remove
## Overstated claims to soften
## Missing strong evidence to add
## Final verdict: PASS / WARN / BLOCK
```

Quality rules:

- Unsupported major claims block finalization.
- Privacy leaks block finalization.
- Tone inflation requires rewrite.

## 4. Suggested parallelization

Use up to three concurrent subagents when inputs are separable.

### Batch A — Early extraction

Run in parallel after privacy gate:

1. Document/OCR Extractor for school documents.
2. Evidence Extractor for redacted student record.
3. School Framework Analyst for SIGNATURE/SD documents.

Then orchestrator merges results into source inventory, school framework summary, and evidence ledger.

### Batch B — Analysis

Run after evidence ledger exists:

1. Activity and Interest Mapper.
2. Psychology and Learning Profile Analyst.
3. Theme Generator draft pass.

Then orchestrator checks evidence IDs and removes unsupported interpretations.

### Batch C — Critique and drafting

Run after candidate themes exist:

1. Feasibility Critic.
2. Privacy Auditor.
3. Evidence/Tone Auditor on draft once available.

Do not draft final Korean output until the student confirmation gate is passed or provisional mode is explicitly requested.

## 5. Subagent prompt template

```text
You are a bounded subagent for the Korean SIGNATURE harness.
Do not edit files unless explicitly told.
Do not invent evidence.
Use only the provided files/context.
Every interpretation must cite evidence IDs or say "unsupported".
Student-facing content must be Korean.
Internal notes may be English.
Return the requested Markdown artifact only.
If input is insufficient, state the blocker and the minimum missing information.
```

## 6. Merge and conflict policy

When subagents disagree:

1. Prefer direct evidence over inferred interpretation.
2. Prefer school framework documents over generic advice.
3. Prefer student-confirmed choices over model guesses.
4. Prefer privacy-safe wording over richer but risky detail.
5. If still unresolved, ask the student a focused Korean question.

## 7. Verification after subagent work

The orchestrator must verify:

- files exist if a subagent claims it wrote files
- evidence IDs are valid
- unsupported claims are removed or labeled
- privacy-sensitive content is excluded from school-facing artifacts
- Korean outputs are actually Korean
- final verdict is PASS/WARN/BLOCK with reasons

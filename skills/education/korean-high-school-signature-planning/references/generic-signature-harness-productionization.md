# Generic SIGNATURE Harness Productionization Notes

Use these notes when converting a Korean SIGNATURE / SD Navigation planning prompt into a reusable, production-grade harness or skill.

## Core language split

- Internal harness specification, schemas, and operator notes may be in English for portability.
- Student questions, student-facing summaries, roadmaps, drafts, and final school-facing outputs must be Korean by default.
- Korean source quotes from school records should remain in Korean even inside English internal artifacts.
- If student confirmation is missing, label drafts: `학생 확인 전 임시안` / `provisional draft pending student confirmation`.

## Production-grade artifact set

For a full run, save each major output as a separate Markdown file:

```text
signature-harness-run/
  00_run_manifest.md
  01_request_and_intake.md
  02_source_inventory.md
  03_extraction_log.md
  04_school_framework_summary.md
  05_evidence_ledger.md
  06_claim_ledger.md
  07_activity_interest_profile.md
  08_learning_profile.md
  09_theme_candidates.md
  10_feasibility_critique.md
  11_student_questions_ko.md
  12_student_decision_log.md
  13_subject_roadmap_ko.md
  14_korean_draft.md
  15_privacy_evidence_tone_audit.md
  final_signature_ko.md
```

Also create a separate `capabilities_report.md` when the user asks to inspect tools/skills/MCP/subagents first.

## Evidence and claim ledgers

Use two ledgers to prevent hallucination.

Evidence item fields:

- `evidence_id` such as `E001`
- source file/type
- page/section/location
- minimal Korean quote or redacted excerpt
- English internal paraphrase
- category: activity, keyword, action verb, limitation, interest, subject strength, school requirement
- privacy level
- extraction confidence
- school-facing usability

Claim item fields:

- `claim_id` such as `C001`
- Korean claim text for student-facing use
- claim type: activity, trait, interest, career direction, roadmap, draft sentence
- evidence IDs
- support strength: direct, derived, weak, unsupported
- student confirmation status
- risk flags: privacy, hallucination, psychology, tone
- required action: keep, soften, ask student, remove

No final draft should proceed while unsupported major claims remain.

## Privacy and safety gates

Run these gates before final output:

- Privacy Gate: identifiers/sensitive data redacted or excluded.
- Source Gate: input inventory and extraction quality recorded.
- School Framework Gate: SIGNATURE/SD requirements and performance assessments extracted or assumptions labeled.
- Evidence Gate: major interpretations cite evidence IDs or are labeled hypotheses.
- Psychology Gate: no diagnosis, clinical label, health/family/counseling detail in school-facing text.
- Generality Gate: no defaulting to AI/medicine/design without evidence.
- Feasibility Gate: minimal artifact possible in 2–4 weeks.
- Interaction Gate: student confirmed direction or draft marked provisional.
- Roadmap Gate: subject/performance links plausible and tied to supplied docs or labeled assumptions.
- Korean Draft Gate: output is Korean, concrete, realistic, not inflated.
- Evidence Audit Gate: unsupported claims removed or softened.

## Tool and capability inspection pattern

When the user asks to improve a harness or build a reusable workflow, inspect and record:

- enabled Hermes toolsets
- installed relevant skills
- configured MCP servers
- enabled plugins
- delegation/subagent settings and external agent CLIs
- document extraction capabilities (`pdftotext`, OCR/vision, PyMuPDF, etc.)

Do not process personal student-record PDFs during harness improvement unless the task is to analyze that specific student and privacy/redaction has been confirmed. It is safe to inspect public/school framework PDFs for SIGNATURE/SD structure.

## Subagent architecture

When delegation is available, use direct leaf subagents for separable streams:

1. Document/OCR Extractor
2. School Framework Analyst
3. Evidence Extractor
4. Activity and Interest Mapper
5. Non-diagnostic Learning Profile Analyst
6. Theme Generator
7. Feasibility Critic
8. Privacy Auditor
9. Korean Draft Writer
10. Evidence and Tone Auditor

The orchestrator retains final synthesis and audit responsibility. Do not rely on nested subagents when `max_spawn_depth` is 1.

## School-framework facts observed from common SIGNATURE/SD docs

Typical SIGNATURE structure:

- Discovery: extract Grade 10 capabilities, repeated keywords, concrete action verbs, and growth seeds.
- Enhancement: deepen through Deep-Dive and widen through Cross-Over.
- Masterpiece: define academic persona, roadmap, and concrete final artifact.

Typical SD Navigation structure:

- starting point from Grade 10 record or small concrete interests
- route tracking through reliable sources, subject concepts, and practical application
- destination via performance assessment matching and concrete artifact

Common artifact options:

- report
- infographic
- survey summary
- experiment/comparison table
- presentation
- campaign plan
- policy proposal
- prototype/screen flow
- design before/after analysis
- media critique

## Korean output templates to preserve

Student confirmation questions:

```text
1. 아래 후보 중 실제로 가장 해보고 싶은 방향은 뭐야?
2. 별로 끌리지 않거나 실제와 다른 방향은 빼도 될까?
3. 이 활동을 2~4주 안에 한다면 어떤 결과물이 가장 현실적이야?
4. 초안에서 과장되었거나 실제와 다른 표현이 있으면 표시해줘.
5. 학교 제출용으로 너무 튀지 않는 톤이 좋을까, 조금 더 학술적인 톤이 좋을까?
```

Final direction skeleton:

```md
# 최종 SIGNATURE 방향

## 한 줄 정의
나는 [문제/대상]을 [방법/관점]으로 탐구하며, [가치/역량]을 중심으로 성장하고자 하는 학생이다.

## 핵심 역량 3개
## 성장 Seed 3개
## 2학년 중심 질문
## 최종 프로젝트
## 1학기 활동 계획
## 2학기 활동 계획
## 최종 결과물
## 하지 않을 것
```

## Test cases worth keeping

Use synthetic records for regression tests:

1. computer/engineering student — must not claim deployed app if only flow was designed.
2. biology/medicine student with family illness — family context stays private.
3. design/humanities student — must not force AI/STEM.
4. undecided student — weak evidence stays exploratory.
5. fabrication request — professor/lab/publication claims are blocked.
6. diagnosis boundary — ADHD/medication only affects private workflow, never school draft.
7. privacy leak — identifiers trigger warning/block.
8. tone overstatement — inflated phrases are softened.
9. poor OCR — low extraction quality blocks unsupported claims.
10. student rejects all axes — regenerate instead of forcing a choice.

---
name: signature-harness
description: Use when analyzing Korean high-school SIGNATURE or SD Navigation materials; extracts evidence, protects privacy, designs feasible Grade 11 themes, writes Korean school-facing drafts, and runs evidence/tone audits.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [education, korean-high-school, SIGNATURE, SD-Navigation, privacy, evidence-audit, planning]
    related_skills: [korean-high-school-signature-planning, ocr-and-documents, writing-plans, subagent-driven-development, requesting-code-review]
---

# Korean SIGNATURE Analysis Harness

## Overview

Use this skill to run a production-grade Korean high-school SIGNATURE / SD Navigation planning workflow. It turns redacted Grade 10 records, student interests, school framework documents, and Grade 11 performance-assessment constraints into an evidence-grounded SIGNATURE axis, roadmap, Korean draft, and audit trail.

This skill is evidence-based, privacy-aware, interactive, and Korean-school-context aware. Internal analysis may be English, but student-facing outputs must be Korean by default.

## When to Use

Use when the user asks for:

- SIGNATURE 방향 설계 or 제출 초안
- SD Navigation 계획
- 생활기록부 기반 2학년 탐구 로드맵
- 수행평가 연결 지도
- 진로탐색 프로젝트 주제 추천
- 학술적 페르소나 설계
- Korean school-facing draft review
- evidence, privacy, or tone audit of a SIGNATURE draft

Do not use for:

- fabricating activities, awards, lab work, professor guidance, or publications
- clinical diagnosis or psychological labeling
- processing unredacted sensitive records without privacy confirmation
- admissions-style exaggeration detached from evidence

## Non-Negotiable Rules

1. Student-facing questions, summaries, roadmaps, drafts, and final outputs are Korean by default.
2. Internal notes, schemas, and operator-facing harness documentation may be English.
3. Do not invent activities or achievements.
4. Every major claim must cite supplied evidence or be labeled as a hypothesis.
5. Maintain evidence and claim ledgers for serious runs.
6. Psychology frameworks are non-diagnostic and workflow-only.
7. School-facing drafts must exclude names, resident numbers, addresses, phone numbers, health/family/counseling/diagnosis details, third-party personal data, passwords, and API keys.
8. Ask the student before finalizing a direction unless the user explicitly requests a provisional draft.
9. If confirmation is missing, label the output: `학생 확인 전 임시안`.
10. Save major intermediate artifacts so the run can resume.

## Interactive Checkpoints / Interrupt Policy

For live user-facing runs, the harness should intentionally pause at decision points instead of silently producing a fully finalized direction.

### Mandatory checkpoint after candidate generation

After stages 8–10 are complete — theme candidates, feasibility critique, and Korean confirmation questions — do all of the following before writing the final roadmap or school-facing draft:

1. Save the intermediate artifacts generated so far, especially:
   - `05_evidence_ledger.md`
   - `06_claim_ledger.md`
   - `09_theme_candidates.md`
   - `10_feasibility_critique.md`
   - `11_student_questions_ko.md`
2. Present a short Korean summary of the top 2–4 candidate axes with:
   - one-line identity
   - strongest evidence IDs
   - feasible artifact
   - main risk
3. Ask the user to choose or revise the direction using `clarify` when available.
4. Do not proceed to `13_subject_roadmap_ko.md`, `14_korean_draft.md`, or `final_signature_ko.md` until the user answers, unless the user explicitly requested a provisional full run.
5. If the user is unavailable, the run is asynchronous, or `clarify` is unavailable, continue only as `학생 확인 전 임시안` and record the missing decision in `12_student_decision_log.md`.

Recommended Korean checkpoint prompt:

```text
여기서 한 번 멈출게. 고1 기록 기준 후보는 아래처럼 보여.
1. [후보 A] — 장점/위험/결과물
2. [후보 B] — 장점/위험/결과물
3. [후보 C] — 장점/위험/결과물

어느 방향으로 확정할까? 섞고 싶은 후보나 빼고 싶은 방향도 말해줘.
```

If the student adds a new preference at the checkpoint, do not force it into the original ranking unchanged. Re-synthesize the axis, update `09_theme_candidates.md`, `10_feasibility_critique.md`, and `12_student_decision_log.md`, then continue. For technical, security, privacy, or data-sovereignty additions, optionally use `references/privacy-data-sovereignty-axis.md` as one reusable example framework; keep all cyber-adjacent framing conceptual, defensive, ethical, and school-safe.

### Mandatory selected-subject checkpoint for 2022 revised curriculum

Because the 2022 Korean high-school curriculum uses elective subject pathways, do not assume that every listed Grade 11 subject applies to the student.

Before producing or finalizing `13_subject_roadmap_ko.md`, `16_expanded_subject_activity_bank_ko.md`, or any school-facing draft with subject-level execution paths:

1. Ask which Grade 11 semester subjects the student actually selected or is taking.
2. Use `clarify` open-ended when available; do not use a four-choice prompt for subject selection because the subject list is longer than four.
3. If selected subjects are known, filter the main roadmap to those subjects only.
4. If subjects are unknown, label the output `학생 선택과목 확인 전 전체 후보안` and clearly state that it must be filtered later.
5. If only some subjects are known, label the output `학생 선택과목 일부 확인 임시안`, separate confirmed-subject recommendations from optional-subject ideas, and do not imply the student takes unconfirmed subjects.
6. Record the selected-subject status in `12_student_decision_log.md` or a run manifest note.

Recommended Korean prompt:

```text
2022 개정 교육과정은 선택과목이 있어서, 실제 네가 듣는 과목 기준으로 로드맵을 필터링해야 해.
2학년 1학기/2학기에 실제 선택한 과목을 알려줘. 모르면 “아직 모름”이라고 해도 돼.
그러면 전체 후보안으로 만들고, 실제 선택과목 확인 후 다시 줄일게.
```

For the detailed activity-card method and status labels, use `references/selected-subject-activity-expansion.md`.

### Optional earlier checkpoints

Ask earlier if any of these materially changes the result:

- privacy/redaction status is unknown or risky
- OCR quality is low and a claim would depend on uncertain text
- the student has not stated whether they prefer AI, engineering, bio, social issue, design, or another axis
- selected Grade 11 subjects or performance-assessment paths are unknown and the roadmap would otherwise be misleading

### Resume behavior

When the user answers a checkpoint:

1. Update `12_student_decision_log.md`.
2. Re-score or rewrite `09_theme_candidates.md` if the choice changes the ranking.
3. Then produce `13_subject_roadmap_ko.md`, `14_korean_draft.md`, audit, and final output.

## First Korean Questions

Ask only the necessary questions first:

```text
1. 이번 작업의 목적은 뭐야? 학교 제출용, 2학년 방향 설계, 주제 추천, 수행평가 로드맵, 자기분석 중 어디에 가까워?
2. 현재 관심 분야나 희망 진로가 있다면 말해줘. 없으면 “아직 모름”도 괜찮아.
3. 생기부와 자료에서 이름, 주민번호, 주소, 전화번호, 가족/건강 정보는 지웠어?
4. 피하고 싶은 방향은 뭐야?
5. 최종 결과물은 어떤 형태가 현실적이야? 보고서, 인포그래픽, 설문 분석, 발표, 캠페인, 코드/프로토타입 등.
```

## Workflow

1. Capability and privacy preflight.
2. Source inventory and redaction check.
3. School framework extraction from SIGNATURE / SD Navigation / performance-assessment documents.
4. Evidence ledger from the redacted Grade 10 record.
5. Claim ledger for interpretations and draft claims.
6. Activity and interest profile.
7. Non-diagnostic learning/workflow profile.
8. SIGNATURE axis candidates with scores, tradeoffs, risks, and minimal artifacts.
9. Feasibility and differentiation critique.
10. Korean student confirmation questions and decision log.
11. Selected-subject checkpoint for the 2022 revised curriculum: ask which Grade 11 elective subjects the student actually takes before subject-level roadmap work.
12. Grade 11 subject/performance roadmap in Korean, filtered to selected subjects when known; otherwise label as `학생 선택과목 확인 전 전체 후보안`.
13. Korean SIGNATURE draft.
14. Evidence/privacy/tone/school-context audit.
15. Final Korean output.
16. Optional expanded subject activity bank when the user asks for broad, creative 과목별 추천 활동 grounded in actual 수행평가 names and official curriculum anchors. Prefer `16_expanded_subject_activity_bank_ko.md`; use `references/selected-subject-activity-expansion.md` plus `korean-high-school-signature-planning` → `references/curriculum-grounded-activity-bank.md`.

## Output Files for Full Runs

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
  16_expanded_subject_activity_bank_ko.md  # optional: broad curriculum-grounded activity bank
  final_signature_ko.md
```

## Tool and Subagent Policy

- Read supplied files before making claims.
- Use local PDF/text extraction first; use OCR/vision only when needed.
- For scanned Korean student records where local OCR is unavailable, follow `references/scanned-record-vision-ocr-workflow.md`: check local OCR tools, get explicit approval for vision/OCR, prompt vision to omit identifiers, and extract only school-safe evidence summaries.
- Use web/browser only for official or current references, never to replace student-record evidence.
- Use subagents for separable workstreams when available: document extraction, school framework analysis, evidence extraction, theme generation, feasibility critique, privacy audit, and Korean draft audit.
- Subagents must be given the intended run directory and must not create stray root-level artifacts; consolidate or remove any stray helper files before finalizing.
- The main orchestrator remains responsible for final synthesis and final PASS/WARN/BLOCK verdict.

## Verification Checklist

Before finalizing:

- [ ] Student-facing output is Korean.
- [ ] PII and sensitive data are excluded from school-facing outputs.
- [ ] Every major claim cites evidence IDs or is labeled as a hypothesis.
- [ ] No fabricated activities, awards, external lab work, professor supervision, or publications.
- [ ] No clinical diagnosis or psychological label appears.
- [ ] Candidate axes are feasible for Grade 11 and have concrete artifacts.
- [ ] Student confirmation is recorded or draft is marked provisional.
- [ ] Subject/performance links are supplied by school docs or labeled assumptions.
- [ ] For 2022 revised curriculum runs, selected-subject status is recorded (`확인 완료`, `확인 전 전체 후보안`, or `일부 확인 임시안`).
- [ ] If selected subjects are known, the main roadmap excludes unselected subjects; broad all-subject banks are kept as separate candidate artifacts.
- [ ] School-facing security/privacy scope guards use softened phrasing; avoid repeating unsafe procedural terms in final deliverables unless they are necessary for an internal audit.
- [ ] Final audit verdict is PASS/WARN/BLOCK.

## References

Load the relevant linked files when the run is complex or when you need exact schemas/templates:

- `references/improved_harness.md` — full internal English harness specification.
- `references/hermes_system_prompt.md` — system/developer prompt form.
- `references/subagent_plan.md` — subagent contracts and orchestration plan.
- `references/output_schemas.md` — schemas for ledgers, candidates, roadmaps, drafts, and audits.
- `references/privacy_policy.md` — privacy and external-processing rules.
- `references/scanned-record-vision-ocr-workflow.md` — approved fallback workflow for scanned Korean student records when local OCR is unavailable; includes privacy-safe vision prompts and artifact discipline.
- `references/privacy-data-sovereignty-axis.md` — optional reusable example framework for school-safe SIGNATURE axes around internet privacy, data sovereignty, local/hosted AI, network isolation concepts, OS/memory isolation, and storage integrity. Use only when the student’s evidence/interests support this theme; do not treat it as the default axis.
- `references/selected-subject-activity-expansion.md` — required checkpoint and activity-card method for 2022 revised elective-subject selection and curriculum-grounded per-subject recommendations.
- `references/korean_final_output_template.md` — Korean student-facing templates.
- `references/test_cases.md` — synthetic regression tests.
- `references/skill_installation.md` — installation and packaging notes.

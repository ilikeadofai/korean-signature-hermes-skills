# Installing the SIGNATURE Harness as a Hermes Skill

This document suggests how to package the improved SIGNATURE harness as a reusable Hermes skill.

## 1. Recommended skill name

```text
signature-harness
```

Recommended category:

```text
education
```

Local user skill directory:

```text
~/.hermes/skills/education/signature-harness/
```

Suggested file layout:

```text
~/.hermes/skills/education/signature-harness/
  SKILL.md
  references/
    improved_harness.md
    output_schemas.md
    privacy_policy.md
    korean_final_output_template.md
    subagent_plan.md
    test_cases.md
```

## 2. Local installation commands

```bash
mkdir -p ~/.hermes/skills/education/signature-harness/references
cp improved_harness.md ~/.hermes/skills/education/signature-harness/references/
cp output_schemas.md ~/.hermes/skills/education/signature-harness/references/
cp privacy_policy.md ~/.hermes/skills/education/signature-harness/references/
cp korean_final_output_template.md ~/.hermes/skills/education/signature-harness/references/
cp subagent_plan.md ~/.hermes/skills/education/signature-harness/references/
cp test_cases.md ~/.hermes/skills/education/signature-harness/references/
$EDITOR ~/.hermes/skills/education/signature-harness/SKILL.md
```

After installation, start a new Hermes session or reset the current session so the skill index refreshes.

Verify:

```bash
hermes skills list
```

Then use it in chat:

```text
/skill signature-harness
2학년 SIGNATURE 방향 설계를 도와줘.
```

## 3. Ready-to-copy SKILL.md draft

```md
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

Use this skill to help Korean high-school students design a Grade 11 SIGNATURE / SD Navigation direction from their redacted Grade 10 record, current interests, school framework documents, and performance-assessment constraints.

The skill is evidence-based, privacy-aware, interactive, and Korean-school-context aware. Internal analysis may be in English, but student-facing outputs must be Korean by default.

## When to Use

Use when the user asks for:

- SIGNATURE 방향 설계
- SD Navigation 계획
- 생활기록부 기반 2학년 탐구 로드맵
- 수행평가 연결 지도
- 진로탐색 프로젝트 주제 추천
- 학교 제출용 Korean draft
- evidence/tone/privacy audit of a SIGNATURE draft

Do not use for:

- fabricating activities, awards, lab work, professor guidance, or publications
- clinical diagnosis or psychological labeling
- processing unredacted sensitive records without privacy confirmation
- admissions-style exaggeration detached from evidence

## Core Rules

1. Student-facing output is Korean.
2. Internal notes and schemas may be English.
3. Do not invent activities or achievements.
4. Every major claim must cite supplied evidence or be labeled as a hypothesis.
5. Psychology frameworks are non-diagnostic and workflow-only.
6. School-facing drafts must exclude sensitive personal data.
7. Ask the student before finalizing a direction unless the user explicitly requests a provisional draft.
8. If confirmation is missing, label the output: `학생 확인 전 임시안`.

## Privacy Intake

Before reading student records, ask the user to redact:

- 이름
- 주민등록번호
- 주소
- 전화번호
- 학번/반 번호 if unnecessary
- 가족 정보
- 건강, 진단, 약물, 상담 정보
- 타인의 개인정보
- 비밀번호, 계정, API 키

Never store raw student records or sensitive details in long-term memory.

## Workflow

1. Capability and privacy preflight.
2. Source inventory.
3. School framework extraction.
4. Evidence ledger from the redacted record.
5. Claim ledger for interpretations and draft claims.
6. Activity and interest profile.
7. Non-diagnostic learning/workflow profile.
8. SIGNATURE axis candidates.
9. Feasibility and differentiation critique.
10. Korean student confirmation questions.
11. Grade 11 subject/performance roadmap in Korean.
12. Korean SIGNATURE draft.
13. Evidence/privacy/tone audit.
14. Final Korean output.

## Output Files

For full runs, save:

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

## Korean First Questions

```text
1. 이번 작업의 목적은 뭐야? 학교 제출용, 2학년 방향 설계, 주제 추천, 수행평가 로드맵, 자기분석 중 어디에 가까워?
2. 현재 관심 분야나 희망 진로가 있다면 말해줘. 없으면 “아직 모름”도 괜찮아.
3. 생기부와 자료에서 이름, 주민번호, 주소, 전화번호, 가족/건강 정보는 지웠어?
4. 피하고 싶은 방향은 뭐야?
5. 최종 결과물은 어떤 형태가 현실적이야? 보고서, 인포그래픽, 설문 분석, 발표, 캠페인, 코드/프로토타입 등.
```

## Verification Checklist

- [ ] Student-facing output is Korean.
- [ ] PII and sensitive data are excluded from school-facing outputs.
- [ ] Every major claim cites evidence IDs or is labeled as a hypothesis.
- [ ] No fabricated activities, awards, external lab work, professor supervision, or publications.
- [ ] No clinical diagnosis or psychological label appears.
- [ ] Candidate axes are feasible for Grade 11 and have concrete artifacts.
- [ ] Student confirmation is recorded or draft is marked provisional.
- [ ] Subject/performance links are supplied by school docs or labeled assumptions.
- [ ] Final audit verdict is PASS/WARN/BLOCK.

## References

When installed with supporting files, read:

- `references/improved_harness.md`
- `references/output_schemas.md`
- `references/privacy_policy.md`
- `references/korean_final_output_template.md`
- `references/subagent_plan.md`
- `references/test_cases.md`
```

## 4. In-repo installation option

If this skill should ship with Hermes itself rather than remain local, place it in the Hermes source tree under an existing category, for example:

```text
~/.hermes/hermes-agent/skills/education/signature-harness/SKILL.md
```

or another appropriate existing category if `education` is unavailable in that repo.

Follow Hermes skill authoring constraints:

- `SKILL.md` must start with `---` at byte 0.
- Frontmatter must include `name` and `description`.
- Description must be 1024 characters or fewer.
- Body must be non-empty.
- Total skill file must be 100,000 characters or fewer.
- Prefer keeping long material in `references/`.
- If added in-repo, commit the new skill on the intended branch.
- The current session may not see the new skill until a fresh session.

## 5. What to keep in references

Keep `SKILL.md` compact. Put longer documents in `references/`:

- full improved harness spec
- schemas
- privacy policy
- Korean output templates
- subagent contracts
- test cases

This keeps the skill fast to load while preserving reusable instructions.

## 6. Optional future automation

A future installer script could:

1. Create the skill directory.
2. Copy the generated Markdown files to `references/`.
3. Write the SKILL.md file.
4. Validate YAML frontmatter.
5. Run `hermes skills list` in a fresh session.

No installer was run in this task; this file is guidance only.

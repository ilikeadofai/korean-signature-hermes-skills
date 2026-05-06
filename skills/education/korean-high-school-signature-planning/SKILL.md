---
name: korean-high-school-signature-planning
description: Plan Korean high-school SIGNATURE / SD Navigation / 생활기록부-aligned research roadmaps from student records, interests, school frameworks, selected subjects, and performance-assessment paths.
version: 1.0.1
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [Korean high school, 생활기록부, SIGNATURE, SD Navigation, 수행평가, academic planning, research roadmap]
    related_skills: [ocr-and-documents, writing-plans, arxiv]
---

# Korean High-School SIGNATURE / SD Navigation Planning

Use this skill when the user asks to build, revise, brainstorm, or polish a Korean high-school **SIGNATURE**, **SD Navigation**, 진로탐색 프로젝트, 생활기록부-aligned 탐구 로드맵, 학술적 페르소나, or 수행평가 연결 plan.

This is **not** a generic report-writing task. The expected output is usually a **student-specific activity plan/roadmap** that can later become 수행평가 artifacts and 생활기록부 evidence. The plan must be grounded in the student’s actual records, interests, selected subjects, school materials, and feasible constraints.

## Core Principles

1. **Evidence first**
   - Use only activities actually present in the 생활기록부 / provided records, or clearly label new ideas as future plans.
   - Do not invent awards, external research, professors, labs, papers, competitions, publications, or completed experiments.
   - If OCR or visual extraction is uncertain, label uncertainty and avoid overclaiming.

2. **Plan, not final report**
   - For SIGNATURE / SD Navigation planning, structure around: 출발점 → 핵심 질문 → 탐구 프레임 → 학기별 활동 → 수행평가 연결 → 산출물 → 하지 않을 것.
   - Avoid writing only a finished “논문 목차”; the school task usually values how the student will develop the inquiry across the year.

3. **One center axis**
   - If the student has broad interests, converge them into one organizing question, model, contrast, or design problem.
   - Use a framework/stack/layer map only when it helps integrate the student’s actual interests.
   - Mark side topics as supporting evidence, not separate main themes.

4. **School-safe phrasing**
   - Prefer: “구조와 한계 분석”, “비교 분석”, “개념 모델”, “공식 문서/전문 자료 참고”, “수행평가 결과물”, “윤리적·사회적 영향 검토”.
   - Avoid: exaggerated admissions language, dangerous procedural cyber content, clinical labels, external-achievement claims, and claims of perfect proof/safety.

5. **Concrete submission paths**
   - Every activity should have: 목적, 내용, 자료, 산출물, 연결 과목/수행평가, 생활기록부식 역량 표현.
   - Respect subjects the student did **not** select; remove them from main matching tables.

6. **2022 개정 선택과목 checkpoint**
   - Before writing a subject-specific roadmap, ask which Grade 11 elective subjects the student actually selected or is taking.
   - If the student has not provided selected subjects, label broad outputs as `학생 선택과목 확인 전 전체 후보안`.
   - If selected subjects are known, put unselected-subject ideas only in an optional appendix or omit them.
   - When the user explicitly requests every subject, create a broad activity bank but clearly mark it as an all-subject candidate bank that must later be filtered.

## Recommended Workflow

### 1. Extract student evidence

Use `ocr-and-documents` for PDFs/scans when available. Extract:

- repeated keywords
- action verbs
- projects, readings, questions, and artifacts
- unfinished questions / seeds
- exact recorded activities that can support the new theme

For each evidence item, keep the source type: 교과 세특, 창체, 진로활동, 행동특성, 봉사, 독서, 수행평가, etc. Remove direct identifiers and sensitive information.

### 2. Identify the stable center axis

Ask or infer the student’s preferred direction, then compress it into one sentence.

Use adaptable patterns rather than a fixed topic:

- `나는 [분야/문제]를 [핵심 관점]으로 분석하고, [결과물]을 통해 [사회적/학문적 의미]를 탐구하는 학생이다.`
- `[현상 A]와 [현상 B]를 비교하여 [핵심 질문]에 답하는 탐구자`
- `[교과 기록에서 반복된 관심]을 바탕으로 [선택과목 수행평가]에서 확장 가능한 [모델/보고서/발표/프로토타입]을 설계하는 학생`

Good center axes should be:

- supported by evidence or explicit interest
- narrow enough for Grade 11 work
- broad enough to connect multiple selected subjects
- safe to describe in school-facing language
- tied to realistic artifacts

### 3. Convert broad interests into a framework

Choose a framework type that fits the student, not a fixed default.

Reusable framework options:

```text
A. Layer / stack model
- Good for engineering, AI, systems, environment, biology mechanisms, or policy implementation.
- Example structure: input → process → output → limitation, or individual → system → society → ethics.

B. 비교 축 model
- Good for humanities/social science/economics/ethics.
- Example structure: 관점 A vs 관점 B, 비용 vs 편익, 효율성 vs 형평성, 개인 자유 vs 공동체 책임.

C. 연구 질문 model
- Good for 과학과제연구 or data analysis.
- Example structure: 문제 제기 → 가설/질문 → 자료 수집 → 분석 방법 → 한계.

D. 산출물 중심 model
- Good when the school task requires a concrete product.
- Example structure: 대상 사용자 → 문제 → 설계 기준 → 초안 → 피드백 → 개선안.
```

For technical/privacy/security-adjacent themes, see `references/privacy-ai-os-integrity-roadmap.md` as an optional example. Do **not** use that model unless the student’s evidence or stated interest supports it.

### 4. Design semester activities

Use activity cards:

```text
활동명
- 목적
- 내용
- 사용 자료
- 결과물
- 연결 과목/수행평가
- 생활기록부식 역량 표현
- 주의할 점
```

Recommended planning rhythm:

- **초기:** 관심 근거 정리, 용어 정의, 자료 조사, 핵심 질문 좁히기
- **중기:** 비교표, 분석틀, 설문/문헌/사례 분석, 미니 모델 제작
- **후기:** 선택과목 수행평가 산출물로 전환, 한계 분석, 발표/보고서/포트폴리오 정리

### 4.5. Expand into a curriculum-grounded activity bank when asked

When the user asks for broader, more creative, subject-by-subject recommendations, do not stop at 5–6 generic activities. Build an expanded activity bank grounded in both:

1. the school's actual 수행평가 names from the supplied workbook/SIGNATURE/SD Navigation materials, and
2. official/current curriculum anchors, preferably NCIC 2022 개정 고등학교 교육과정.

For each recommended activity, explicitly include:

```text
과목:
실제 수행평가명:
교육과정 연결 키워드:
활동명:
목적:
내용:
산출물:
생활기록부식 역량 표현:
주의할 점:
```

If saving a full artifact, create a separate file such as `16_expanded_subject_activity_bank_ko.md` instead of overloading `13_subject_roadmap_ko.md`. See `references/curriculum-grounded-activity-bank.md` for NCIC retrieval notes, curriculum-anchor patterns, and activity-bank formatting rules.

### 5. Add “하지 않을 것”

Always include scope guards, adapted to the field.

Examples:

- 실제로 하지 않은 실험·외부 활동·성과처럼 표현하지 않음
- 선택하지 않은 과목의 수행평가로 연결했다고 쓰지 않음
- 단순 정보 나열이나 AI 요약본에 머무르지 않음
- 특정 기술·정책·이론이 무조건 옳다고 단정하지 않음
- 안전·보안·의학·심리·법률 주제는 절차 안내나 진단처럼 쓰지 않음
- 개인정보·제3자 자료를 동의 없이 수집하지 않음
- 한계와 trade-off를 반드시 함께 제시함

## Output Templates

### Signature Plan Skeleton

```text
1. 출발점: 기록에서 발견한 관심
2. 핵심 질문
3. 탐구 프레임
4. 학기별 활동 계획
5. 선택과목/수행평가 연결 지도
6. 최종 산출물 계획
7. 하지 않을 것
8. 학술적 페르소나
9. 근거-주장 점검
```

### Activity Card Template

```text
## Activity N. [활동명]

목적:
내용:
사용 자료:
결과물:
연결 과목/수행평가:
생활기록부식 역량 표현:
주의할 점:
```

## Pitfalls

- Do not turn the plan into a finished final report unless the user asks for one.
- Do not include unselected subjects in 수행평가 matching tables.
- Do not force every student into AI/privacy/systems themes; use those only when evidence supports them.
- Do not present dangerous cyber, medical, legal, or psychological content as procedural instructions; keep it conceptual, ethical, and school-safe.
- Do not rely on NamuWiki alone. Treat it as a starting point, then supplement with official docs or reputable sources.
- Do not preserve direct identifiers, family/health/counseling details, resident numbers, phone numbers, addresses, API keys, or secrets in outputs.

## Reference Notes

- See `references/privacy-ai-os-integrity-roadmap.md` for an optional reusable model for students whose evidence/interests genuinely involve privacy, AI data flow, operating systems, memory safety, storage integrity, or related trustworthy-computing themes.
- See `references/curriculum-grounded-activity-bank.md` when expanding a SIGNATURE roadmap into broad, creative, subject-by-subject activity recommendations grounded in actual 수행평가 names and official NCIC 2022 개정 curriculum anchors.
- See `references/generic-signature-harness-productionization.md` when turning a SIGNATURE/SD Navigation prompt into a reusable production harness: evidence/claim ledgers, privacy gates, subagent contracts, state-saving artifacts, Korean-output policy, and synthetic regression tests.

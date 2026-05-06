# Curriculum-Grounded Activity Bank Notes

Use this reference when the user asks for broader, more creative, subject-by-subject activity recommendations that should be grounded in real Korean high-school performance-assessment names and the 2022 revised curriculum.

This reference is **theme-neutral**. It can support AI/privacy/system topics, humanities topics, bio/chem/physics topics, social-science topics, design/art topics, or any other student-specific SIGNATURE axis. Do not force the example topic links below into a student plan unless the student’s evidence, interest, selected subjects, and school tasks support them.

## Core Lesson

Do not generate generic subject ideas first. Build an activity bank in this order:

1. Extract the school's actual 수행평가 names from provided workbook/SIGNATURE/SD Navigation materials.
2. Ask or confirm the student’s actual selected subjects under the 2022 revised curriculum.
3. Search or browse official curriculum sources, preferably NCIC 국가교육과정정보센터, for the relevant 2022 개정 고등학교 과목.
4. Pull only compact curriculum anchors: 핵심 아이디어, 내용 요소, 과정·기능, 가치·태도, and a few relevant 성취기준 keywords.
5. Design activity cards that explicitly name:
   - 과목
   - 실제 수행평가명
   - 교육과정 연결 키워드
   - 활동명
   - 목적
   - 내용
   - 산출물
   - 생활기록부식 역량 표현
   - 주의할 점
6. If writing a file, use a separate expanded activity-bank artifact rather than overloading the semester roadmap. Recommended filename: `16_expanded_subject_activity_bank_ko.md` for all-subject candidate banks and `17_selected_subject_activity_bank_ko.md` for selected-subject-only banks.

## NCIC Navigation Pattern

NCIC pages can be navigated from the browser, but the visible UI is sometimes awkward. A useful route is:

- Open `https://ncic.re.kr/`.
- Use the high-school curriculum tree or direct URL patterns when available.
- In the page tree, expand `2022 개정 시기 > 고등학교(2022.12)`.
- Select the subject node, then read the result table rows.
- Row `보기` links are often generated as `move_view('org', '2022', '<location>', '<seq>')`.
- A POST to `/inv/org/view.do` with `_csrf`, `openYear=2022`, `seq`, `location`, `orgType=ogi4`, `menuType=1`, `nationCd=` can return detailed curriculum text.

This lets future runs retrieve compact official excerpts without relying on search-result snippets.

## Subject Anchor Patterns

The following are reusable patterns from curriculum work. Always verify against the current official curriculum and the school’s actual assessment names.

### AI / Information

Common anchors:

- problem definition
- data exploration and quality
- algorithm/model selection
- AI project planning, development, evaluation
- social impact and ethics

Activity pattern examples:

- AI tool data-flow or reliability analysis
- small AI project design with ethical constraints
- dataset bias/quality checklist
- responsible AI use guide

### Mathematics

Common anchors:

- functions and graphs for changing quantities
- sequences and patterns
- probability/statistics or modeling when the selected subject supports it
- mathematical representation, reasoning, and communication
- engineering tools / real-life connection

Activity pattern examples:

- scoring or rubric model for a chosen issue
- growth/decay or periodic model for a real phenomenon
- error/risk model using synthetic data
- visual explanation of a quantitative trade-off

### Korean Language / Literature / Speech and Language

Common anchors:

- interpretation, appreciation, critique
- rewriting and creative transformation
- context-aware communication
- validity, reliability, fairness of claims and evidence
- publicness of media language

Activity pattern examples:

- literary work reinterpretation through the SIGNATURE theme
- public guide rewrite for readability and fairness
- debate or discussion design
- media-language critique and improvement proposal

### English I / English II

Common anchors:

- academic/social topics
- understanding diverse media
- identifying details, gist, purpose, claims, and evidence
- summarizing and presenting opinions
- explaining visual materials
- ethical media/source use

Activity pattern examples:

- English source summary and critique
- infographic, speech script, or debate brief
- comparison of international perspectives
- visual-data explanation in English

### Science Subjects

Common anchors vary by subject. Use only the selected subject’s curriculum.

Activity pattern examples:

- mechanism model or concept map
- material/energy/system trade-off analysis
- ethically safe literature review
- simulation or toy model with clear limitations
- real experiment only if actually feasible, supervised, and school-safe

### Social Science / Ethics / Economics / Law

Common anchors:

- social problem framing
- research ethics
- source reliability and validity
- rights, responsibility, regulation, fairness
- cost-benefit, efficiency-equity, or policy trade-offs

Activity pattern examples:

- policy brief or stakeholder map
- survey design with consent and privacy safeguards
- media or law/policy document critique
- cost-benefit or rights-responsibility comparison

### Arts / Design / Communication

Common anchors:

- expression intention and audience
- design constraints
- cultural/social meaning
- process reflection and critique

Activity pattern examples:

- poster/infographic/campaign artifact
- design critique and iteration log
- audience feedback analysis
- visual metaphor for the SIGNATURE axis

## Activity Card Template

```text
## [과목] 활동 카드 N. [활동명]

- 실제 수행평가명:
- 교육과정 연결 키워드:
- 목적:
- 내용:
- 산출물:
- 생활기록부식 역량 표현:
- 주의할 점:
```

## Status Labels

Use one of these labels at the top of activity-bank files:

- `학생 선택과목 확인 완료` — selected subjects are known; main roadmap includes only those subjects.
- `학생 선택과목 확인 전 전체 후보안` — selected subjects are unknown; broad activity bank is allowed but must be filtered later.
- `학생 선택과목 일부 확인 임시안` — some subjects are known; separate confirmed-subject roadmap from optional-subject bank.

## Safety and Evidence Rules

- Do not imply the student completed a planned activity.
- Do not imply the student takes unselected subjects.
- Do not invent school assessment names.
- Do not use real third-party personal data without consent.
- Do not overstate experiments, prototypes, external mentorship, publications, or awards.
- Technical, medical, legal, psychological, or security-adjacent topics must stay conceptual, ethical, and school-safe.
- All strong claims should map back to record evidence, student preference, school task, or official curriculum anchor.

## School-Safe Phrasing for Sensitive or Technical Topics

Prefer:

- 구조와 한계 분석
- 데이터 흐름 분석
- 개념 모델
- 보호 구조와 trade-off 분석
- 윤리적·사회적 영향 검토
- 공식 문서와 전문 자료 기반 비교
- 실제 수행 가능 범위 안의 산출물 제작

Avoid in school-facing artifacts:

- bypass/evasion/intrusion/attack procedure
- medical/psychological diagnosis
- legal advice as if authoritative
- perfect safety or complete proof claims
- unsupported claims that one tool, method, ideology, or platform is automatically superior

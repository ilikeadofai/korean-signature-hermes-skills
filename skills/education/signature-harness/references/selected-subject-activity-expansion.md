# Selected-Subject Checkpoint and Curriculum-Grounded Activity Expansion

Use this reference when a Korean high-school SIGNATURE / SD Navigation run reaches the subject roadmap stage under the 2022 revised curriculum.

## Why this exists

The 2022 revised Korean high-school curriculum uses elective subject pathways. A subject roadmap is misleading if it assumes subjects the student did not select. Therefore, the harness must pause before final subject/performance-assessment matching and ask which Grade 11 subjects the student actually takes.

## Mandatory selected-subject checkpoint

Before producing or finalizing `13_subject_roadmap_ko.md`, `16_expanded_subject_activity_bank_ko.md`, or a school-facing draft with subject-level execution paths, ask the student:

```text
2022 개정 교육과정은 선택과목이 있어서, 실제 네가 듣는 과목 기준으로 로드맵을 필터링해야 해.
아래 중 2학년 1학기/2학기에 실제 선택한 과목을 알려줘.

1학기 예: 문학, 영어Ⅰ, 대수, 미적분Ⅰ, 물리학, 화학, 생명과학, 지구과학, 경제, 사회문제탐구, 현대사회와 윤리, 세계사, 인공지능 기초, 공학커뮤니케이션 등
2학기 예: 화법과 언어, 영어Ⅱ, 대수/확률·통계형 평가, 미적분Ⅱ, 역학과 에너지, 물질과 에너지, 세포와 물질대사, 지구시스템과학, 사회와 문화, 법과 사회, 윤리와 사상, 세계시민과 지리, 역사로 탐구하는 현대 세계, 과학과제연구, 융합과학탐구 등

모르면 “아직 모름”이라고 해도 돼. 그러면 전체 후보안으로 만들고, 실제 선택과목 확인 후 다시 줄일게.
```

Use `clarify` open-ended when available. Do not use a four-choice multiple-choice prompt because the subject list is longer than four and may include school-specific electives.

## Output states

Use one of these status labels at the top of subject-roadmap artifacts:

- `학생 선택과목 확인 완료` — selected subjects are known; include only those subjects in the main roadmap.
- `학생 선택과목 확인 전 전체 후보안` — selected subjects are unknown; broad activity bank is allowed, but clearly label it as a candidate bank and add a filtering note.
- `학생 선택과목 일부 확인 임시안` — some subjects are known; split into confirmed-subject roadmap and optional-subject bank.

## Filtering rules

1. If selected subjects are known, the main roadmap must include only those subjects.
2. Unselected subjects may appear only in an appendix titled `선택하지 않은 과목용 참고 아이디어` or be omitted.
3. If all-subject recommendations are requested explicitly, produce `16_expanded_subject_activity_bank_ko.md` and label it `전체 후보안`.
4. After selected subjects are provided, keep the all-subject bank as the broad candidate artifact and create or update a selected-subject artifact, for example `17_selected_subject_activity_bank_ko.md`.
5. Record the selected-subject list and status in `12_student_decision_log.md` and `00_run_manifest.md`.
6. Do not imply the student completed activities in unselected subjects.
7. Keep school-facing drafts centered on feasible subjects and actual performance-assessment paths.

## Curriculum-grounded activity-card schema

For each subject, write activity cards in Korean with this schema:

```text
### [과목명]
- 실제 수행평가명:
- 교육과정 연결 키워드:
- SIGNATURE 연결 계층:

#### 활동 A. [활동명]
- 목적:
- 내용:
- 사용 자료:
- 산출물:
- 생활기록부식 역량 표현:
- 주의할 점:
```

## Evidence requirements

Each subject recommendation should be grounded in both:

1. school materials: actual performance-assessment titles from the supplied workbook or school document, and
2. official/current curriculum anchors: preferably NCIC 2022 개정 고등학교 교육과정 keywords such as content elements, process/function verbs, achievement-standard direction, or evaluation emphasis.

If official curriculum anchors were not checked for a subject, label the curriculum connection as `교육과정 직접 확인 전 가설` and keep the activity conservative.

## School-safe security/privacy phrasing

For technical, security-adjacent, privacy, personal-data, local/hosted AI, OS isolation, or cyber-adjacent topics:

Prefer:
- 데이터 흐름 분석
- 메타데이터 발생 구조
- 네트워크 격리 도구의 개념과 한계
- 접근권한 분리
- 저장 위치 투명성
- 삭제권과 데이터 이동권
- 보호 구조와 trade-off 분석

For school-facing `하지 않을 것` sections, prefer softened negative wording:
- 구체적 절차 안내는 작성하지 않는다
- 시스템 공격 절차는 다루지 않는다
- 보호 효과를 절대적으로 단정하지 않는다
- 실제 하지 않은 외부 연구·논문·수상으로 과장하지 않는다

Avoid explicit banned-term lists in polished school-facing drafts when softened wording is sufficient. Explicit banned terms are acceptable in internal audit files or operator notes.

## Recommended artifact placement

Full run:

```text
13_subject_roadmap_ko.md                  # selected-subject roadmap, filtered when possible
16_expanded_subject_activity_bank_ko.md   # broad all-subject bank or confirmed-subject activity cards
15_privacy_evidence_tone_audit.md         # include tone warnings for cyber/privacy wording
```

## Verification checklist

- [ ] Selected-subject status label appears near the top.
- [ ] Actual 수행평가 names are included.
- [ ] Curriculum anchors are official or clearly labeled as hypotheses.
- [ ] Unselected subjects are not presented as if the student takes them.
- [ ] No unsafe cyber procedural content appears.
- [ ] No PII, health/family/counseling/diagnosis details, secrets, or third-party personal data appear.

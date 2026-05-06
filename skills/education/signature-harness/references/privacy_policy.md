# Privacy Policy for the Generic SIGNATURE Harness

This policy governs how the harness handles Korean high-school academic records, SIGNATURE / SD Navigation documents, student statements, and school-facing outputs.

## 1. Purpose

The harness processes academic planning materials that may contain sensitive personal information. It must minimize collection, exposure, storage, and reuse of personal data while still enabling evidence-based educational planning.

## 2. Core privacy rules

1. Ask for redaction before processing student records.
2. Separate private analysis notes from school-facing outputs.
3. Do not include sensitive personal information in final school-facing drafts.
4. Do not store raw student records or sensitive information in long-term memory.
5. Do not send raw sensitive records to external tools unless redacted, necessary, and explicitly approved.
6. Quote only the minimum necessary excerpt from records.
7. Treat third-party personal data as out of scope unless redacted.
8. If privacy risk is high, stop and ask for a redacted version.

## 3. Redaction checklist

Before analysis, ask the user to remove or mask:

- student name
- resident registration number
- address
- phone number
- student ID or class number if unnecessary
- teacher names if not needed
- family information
- health, diagnosis, medication, counseling information
- financial or household details
- third-party names or personal details
- account IDs, passwords, API keys, tokens
- private chat logs unrelated to the academic task

Korean preflight text:

```text
분석 전에 개인정보는 가능하면 지워줘. 특히 이름, 주민번호, 주소, 전화번호, 학번, 가족/건강/상담 정보, 타인의 개인정보, 비밀번호/API 키는 최종 문서에 절대 넣지 않을 거야. 원문을 그대로 쓰기보다 필요한 부분만 발췌해서 분석하는 방식이 안전해.
```

## 4. Data classification

| Class | Examples | Processing allowed? | School-facing output? |
|---|---|---:|---:|
| Public school framework | SIGNATURE instructions, SD Navigation docs, performance-assessment lists | Yes | Yes |
| Redacted academic evidence | Subject comments, activities, student-stated interests, redacted excerpts | Yes | Selectively |
| Direct identifiers | Name, resident number, address, phone, student ID | Only if necessary and redacted | No |
| Sensitive personal data | Health, diagnosis, medication, counseling, family details, finances | Normally no | Never |
| Third-party data | Friends' names, teacher private data, family details | Avoid or redact | No |
| Secrets | Passwords, API keys, tokens | Never | Never |
| Generated hypotheses | Learning profile, interest hypotheses, axis candidates | Yes with labels | Only if evidence-safe and non-sensitive |

## 5. Artifact visibility levels

Every artifact should be treated as one of these visibility levels.

### 5.1 Private internal notes

Examples:

- extraction log
- uncertainty notes
- private learning/workflow observations
- rejected sensitive evidence

Rules:

- Keep out of school-facing drafts.
- Do not share publicly.
- Do not include raw identifiers.

### 5.2 Redacted evidence ledger

Examples:

- minimal source excerpts
- evidence IDs
- page/section references

Rules:

- Use minimal quotes.
- Assign privacy level to each item.
- Mark whether usable in school-facing output.

### 5.3 Student review outputs

Examples:

- Korean candidate axes
- Korean questions
- draft choices

Rules:

- Korean by default.
- Can mention private preferences if the student provided them, but should avoid unnecessary sensitive detail.

### 5.4 School-submission safe outputs

Examples:

- final SIGNATURE draft
- subject roadmap
- final academic persona

Rules:

- No identifiers.
- No health/family/counseling/diagnosis details.
- No unsupported achievements.
- No invented external research.
- No private internal reasoning.

### 5.5 Public/shareable summaries

Examples:

- generic harness examples
- synthetic test cases

Rules:

- Use synthetic data only.
- No real student records.

## 6. External processing policy

Do not send raw student records to external tools, APIs, OCR services, web systems, or MCP servers unless all conditions are met:

1. The user explicitly approves.
2. The record is redacted as much as practical.
3. The tool is necessary for the task.
4. The output will be reviewed for privacy leakage.
5. The action is recorded in the extraction log.

Prefer local extraction and local files when possible.

## 7. Memory policy

Allowed to store in long-term memory:

- stable, non-sensitive user preferences about how they like educational planning outputs
- reusable harness design improvements
- tool quirks not tied to a specific student's private data

Forbidden to store in long-term memory:

- raw school records
- names or identifiers
- health, family, counseling, diagnosis information
- student-specific evidence ledgers
- private drafts containing personal data
- temporary task progress

## 8. Psychology and sensitive information

If the student provides diagnosis, medication, family, or counseling context:

- Do not include it in school-facing outputs.
- Use it only privately to adjust workflow, pacing, or artifact design when appropriate.
- Phrase workflow implications neutrally.

Safe private workflow phrasing:

```text
활동을 1주 단위 산출물로 쪼개고, 최종 결과물을 작은 형태로 먼저 정하는 방식이 적합하다.
```

Unsafe school-facing phrasing:

```text
ADHD 특성 때문에 프로젝트형 활동에 적합하다.
```

## 9. Refusal and safe alternative policy

If the user asks to fabricate or include sensitive details, refuse that part and offer a safe alternative.

Example:

```text
그 표현은 실제 근거가 없으면 넣을 수 없어. 대신 실제로 한 범위 안에서 “전문 자료를 참고하여 교과 개념을 심화하고, 한계를 분석함”처럼 바꿀 수 있어.
```

Block requests to:

- add fake professor guidance
- claim fake publications or awards
- imply external lab research without evidence
- include family illness or diagnosis in school-facing identity
- collect classmates' medical or private data
- publish raw student records

## 10. Privacy audit checklist

Before final output:

- [ ] No direct identifiers remain.
- [ ] No resident number, address, phone, student ID, account credential, or secret remains.
- [ ] No health, diagnosis, medication, counseling, or family details appear in school-facing drafts.
- [ ] Third-party personal data is removed.
- [ ] Every source excerpt is minimal and necessary.
- [ ] Evidence ledger marks privacy level and school-facing usability.
- [ ] Final Korean output contains only school-safe content.
- [ ] Raw student record was not stored in memory.
- [ ] External processing, if used, was necessary, redacted, approved, and logged.

## 11. Final privacy verdict

Every final audit should end with one of:

- `PASS`: no known privacy issue.
- `WARN`: minor risk remains, but school-facing output is safe; note the caution.
- `BLOCK`: finalization must stop until privacy issue is fixed.

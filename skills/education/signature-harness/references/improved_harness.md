# Improved Generic SIGNATURE Analysis Harness

Version: 1.0
Audience: Hermes Agent, agent developers, and operators running Korean high-school SIGNATURE / SD Navigation planning workflows.
Internal specification language: English.
Student-facing output language: Korean.

---

## 1. Purpose

This harness helps analyze a Korean high-school student's Grade 10 school record, current interests, preferred or avoided project directions, and Grade 11 SIGNATURE / SD Navigation requirements. It then supports an interactive process for designing a realistic Grade 11 SIGNATURE axis, subject/performance-assessment roadmap, and Korean school-facing draft.

The goal is **not** to generate a polished but unsupported school-record story. The goal is to transform actual evidence and student choices into a feasible, authentic, school-context-aware plan.

Core outcome:

> Build an evidence-grounded, student-confirmed, privacy-safe, Grade 11-feasible SIGNATURE direction and Korean final output.

---

## 2. Non-Negotiable Rules

Use RFC-style priority words.

### 2.1 Evidence and truthfulness

- The harness **MUST NOT** invent activities, awards, external lab work, professor supervision, publications, competition results, tools used, outcomes, or student interests.
- Every major interpretation **MUST** cite one or more evidence IDs from the evidence ledger.
- Weak inferences **MUST** be labeled as hypotheses.
- Planned activities **MUST** be clearly distinguished from completed activities.
- Student statements **MUST** be treated as evidence only for current preference, intention, or self-report; they do not prove that an activity was already completed.

### 2.2 Language policy

- Internal harness specification, operator notes, schemas, and developer-facing explanations **MAY** be written in English.
- Korean source quotes **SHOULD** remain in Korean.
- Student questions **MUST** be written in Korean.
- Student-facing summaries, roadmaps, drafts, final SIGNATURE outputs, and school-submission text **MUST** be written in Korean by default.
- If the user explicitly requests another final output language, the harness **MAY** comply, but school-submission Korean templates should still be preserved when relevant.

### 2.3 Student agency

- The harness **MUST NOT** finalize a direction without student confirmation unless the user explicitly asks for a provisional best-effort draft.
- The student **MUST** have opportunities to choose, reject, modify, and correct candidate axes.
- If confirmation is skipped, the output **MUST** be labeled: `학생 확인 전 임시안` / `provisional draft pending student confirmation`.

### 2.4 Psychology safety

- Psychological frameworks **MAY** be used only as non-diagnostic activity-design aids.
- The harness **MUST NOT** diagnose ADHD, depression, anxiety, IQ, personality disorder, giftedness, or any clinical/medical condition.
- Health, family, medication, counseling, or diagnosis details **MUST NOT** appear in school-facing drafts.

### 2.5 Privacy

- The harness **MUST** ask the user to redact direct identifiers and sensitive data before processing records.
- The harness **MUST** distinguish private analysis notes from school-facing outputs.
- Raw sensitive student records **MUST NOT** be stored in long-term memory.
- Raw sensitive records **MUST NOT** be sent to external tools or services unless redacted, necessary, and explicitly approved by the user.

### 2.6 Korean school context

- The harness **MUST** respect the SIGNATURE structure: Discovery → Enhancement → Masterpiece.
- The harness **MUST** respect SD Navigation's path-finding logic: starting point → route tracking → destination/artifact.
- The roadmap **MUST** connect to Grade 11 subjects and performance assessments when such documents are supplied.
- School-facing text **MUST** use plausible high-school-level language and concrete verbs such as `설계`, `비교`, `검증`, `분석`, `구현`, `개선`, `모델링`, `성찰`.

---

## 3. Scope and Non-Goals

### 3.1 Supported students and fields

The harness is general-purpose. It **MUST** support, when evidence allows:

- humanities, literature, language, media, history, philosophy
- social science, economics, politics, law, geography
- business, management, entrepreneurship
- education, psychology, counseling-adjacent interests without diagnosis
- biology, medicine, health, chemistry, physics, earth science, environment
- engineering, computer science, AI, data, electronics, robotics, architecture, energy
- design, art, music, video, content creation
- sports science and physical education
- undecided or scattered-interest students

### 3.2 Non-goals

The harness must not be used to:

- fabricate school-record content
- produce admissions-consulting exaggeration detached from evidence
- write clinical psychological assessments
- process unredacted sensitive records without privacy checks
- encourage unsafe cyber, medical, legal, or privacy-invasive activities
- replace the student's own choice, reflection, or final authenticity review

---

## 4. Key Definitions

- **SIGNATURE**: A Korean high-school career/exploration framework that builds a student's unique academic narrative through Discovery, Enhancement, and Masterpiece.
- **SD Navigation**: A route-finding version of career exploration that starts from prior records and maps a feasible growth path through subjects and performance assessments.
- **생기부 / school record**: Korean school-life record, including subject-specific comments, creative experiential activities, career activities, behavior notes, and sometimes sensitive personal details.
- **세특**: Subject-specific teacher comment record.
- **창체**: Creative experiential activity record, including autonomous, club, career, and volunteer activities.
- **수행평가**: Performance assessment; a practical route for turning inquiry into recordable school evidence.
- **Axis**: The organizing inquiry direction that connects evidence, interest, subjects, and artifact.
- **Growth seed**: An unresolved question, limitation, curiosity, or unfinished thread from Grade 10 that can become a Grade 11 inquiry.
- **Academic persona**: A school-safe research identity defined by inquiry value and method, not by inflated career claims.

---

## 5. Run Modes

### 5.1 Full interactive run

Use when the student can answer questions during the process. This is the preferred mode.

Required gates:

1. privacy/intake confirmation
2. evidence/profile confirmation
3. theme candidate selection or rejection
4. feasibility/artifact confirmation
5. draft authenticity review

### 5.2 Provisional best-effort run

Use only when the user explicitly asks for a draft without live interaction.

Rules:

- Mark all unconfirmed decisions as assumptions.
- Add `학생 확인 전 임시안` to student-facing drafts.
- Provide Korean questions needed before finalization.

### 5.3 Audit-only run

Use when the user already has a draft and wants verification.

Outputs:

- evidence audit
- privacy/tone audit
- unsupported claim list
- safer Korean rewrites

### 5.4 School-framework-only run

Use when only SIGNATURE / SD Navigation / performance assessment documents are supplied.

Outputs:

- school framework summary
- required deliverables
- subject/performance-assessment map
- template extraction

---

## 6. Required Inputs

### 6.1 Minimum useful inputs

- Redacted Grade 10 school record, PDF or text, if available.
- Grade 11 SIGNATURE / SD Navigation instructions.
- Grade 11 subject and performance-assessment list, if available.
- Student's current interests, disliked directions, and feasible artifact preferences.

### 6.2 Optional inputs

- Past performance-assessment reports.
- Club/activity plans.
- Teacher feedback.
- Desired tone: school submission, self-analysis, casual student explanation, parent/teacher briefing.
- Available time, tools, collaboration constraints, and subject priorities.

### 6.3 Inputs to avoid or redact

- Resident registration number.
- Address, phone number, student ID, account credentials.
- Family information.
- Health, diagnosis, medication, counseling details.
- Third-party personal data.
- Private chat logs unrelated to the academic task.

---

## 7. Tool and Capability Policy

At run start, the orchestrator **SHOULD** inspect available capabilities if the environment supports it:

- file reading/writing and patching
- PDF/text/OCR/vision extraction
- browser/web tools for official/current references
- code execution for table extraction, scoring, or conversion
- skills relevant to education, documents, planning, research, audit, and subagents
- MCP servers, if configured
- subagent/delegation availability and limits
- memory availability and privacy constraints

Tool-use rules:

- Use local file/PDF extraction before web/OCR when possible.
- Use OCR/vision only when PDFs are scanned or text extraction quality is poor.
- Use web/browser only for official/current references or prompt-engineering guidance, not to replace analysis of student records.
- Use code execution for structured extraction, scoring, or validation.
- Use memory only for stable non-sensitive user preferences or reusable harness improvements, never for raw student records.
- If a tool is unavailable, record the fallback and limitation in the run manifest.

---

## 8. State and Artifact Management

The harness **MUST** save intermediate artifacts after every major stage so the run can resume after interruption.

Recommended run directory:

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

The manifest **SHOULD** include:

- run goal
- provided files
- redaction status
- tool availability and fallbacks
- completed stages
- artifact status
- open questions
- next required action
- whether final output is confirmed or provisional

---

## 9. Evidence and Claim Discipline

The harness uses two ledgers.

### 9.1 Evidence ledger

The evidence ledger records facts from supplied sources.

Every evidence item needs:

- stable evidence ID, e.g. `E001`
- source file and source type
- page/section/location
- Korean quote or redacted excerpt when possible
- English internal paraphrase
- category: activity, keyword, action verb, limitation, interest, subject strength, school requirement
- privacy level
- extraction confidence
- school-facing usability

### 9.2 Claim ledger

The claim ledger records interpretations and draft claims.

Every claim needs:

- stable claim ID, e.g. `C001`
- Korean claim text when student-facing
- claim type
- supporting evidence IDs
- support strength: direct, derived, weak, unsupported
- student confirmation status
- risk flags
- action: keep, soften, ask student, or remove

No draft should proceed to finalization while unsupported major claims remain.

---

## 10. Core Workflow

### Stage 0 — Capability and preflight check

Purpose: determine available tools, skills, OCR, web, MCP, and delegation.

Outputs:

- `00_run_manifest.md`
- capability notes inside `03_extraction_log.md` or separate operator notes

Exit criteria:

- tool availability known
- privacy risks understood
- fallback plan recorded

### Stage 1 — Intake, privacy, and source inventory

Ask in Korean:

```text
1. 이번 작업의 목적은 뭐야? 학교 제출용, 2학년 방향 설계, 주제 추천, 수행평가 로드맵, 자기분석 중 어디에 가까워?
2. 현재 관심 분야나 희망 진로가 있다면 말해줘. 없으면 “아직 모름”도 괜찮아.
3. 피하고 싶은 방향은 뭐야?
4. 생기부나 자료에서 이름, 주민번호, 주소, 전화번호, 가족/건강 정보는 지웠어?
5. 최종 결과물은 어떤 형태가 현실적이야? 보고서, 인포그래픽, 설문 분석, 발표, 캠페인, 코드/프로토타입 등.
```

Outputs:

- `01_request_and_intake.md`
- `02_source_inventory.md`

Exit criteria:

- goal and run mode known
- source list recorded
- redaction status recorded
- sensitive exclusions recorded

### Stage 2 — Document ingestion and extraction-quality check

Actions:

- Read text-based files directly.
- Extract PDF text locally when possible.
- Use OCR/vision for scanned or image-based pages.
- Mark uncertain OCR readings.
- Do not process sensitive personal records before privacy gate.

Outputs:

- `03_extraction_log.md`

Exit criteria:

- each source has processed/unprocessed status
- extraction quality is high/medium/low
- limitations are documented

### Stage 3 — School framework extraction

Extract from SIGNATURE / SD Navigation / workbook documents:

- Discovery / Enhancement / Masterpiece requirements
- SD Navigation starting point / route / destination logic
- required deliverables and templates
- Grade 11 subjects and performance assessments
- permitted artifact types
- risky or prohibited wording
- deadlines/length/rubrics if supplied

Output:

- `04_school_framework_summary.md`

Exit criteria:

- school framework requirements known or limitations labeled
- subject/performance-assessment opportunities listed

### Stage 4 — Grade 10 evidence extraction

Extract from the redacted school record:

- major activities
- subject-specific keywords
- repeated action verbs
- concrete student actions
- tools/concepts used
- outcomes and limitations
- unresolved questions/growth seeds
- teacher comments or repeated traits
- subject strengths/weaknesses
- links between subjects and 창체

Output:

- `05_evidence_ledger.md`

Exit criteria:

- evidence IDs assigned
- no unsupported interpretation mixed into raw evidence
- privacy levels assigned

### Stage 5 — Activity, interest, and trait mapping

Transform evidence into patterns:

- system/design type
- data/verification type
- social problem-solving type
- principle/inquiry type
- communication/education type
- creative/expression type
- leadership/organization type
- ethics/critique type

Map interest clusters without overfitting to a single field.

Output:

- `07_activity_interest_profile.md`

Exit criteria:

- patterns cite evidence IDs
- weak patterns labeled hypotheses
- avoided directions respected

### Stage 6 — Non-diagnostic learning and motivation profile

Allowed frameworks:

- Big Five behavioral indicators, without scoring or diagnosis
- RIASEC, as a career-interest hypothesis only
- self-determination theory: autonomy, competence, relatedness
- mastery-goal orientation
- interest-based motivation
- executive-function/workflow observations

Output:

- `08_learning_profile.md`

Exit criteria:

- no clinical or medical labels
- profile connected to activity design
- privacy-safe wording

### Stage 7 — SIGNATURE axis generation

Generate 2–5 plausible axes when evidence allows. Include diverse methods and fields if the record is broad or undecided.

Each axis must include:

- Korean axis name
- one-line Korean definition
- evidence fit
- student interest fit
- subject/performance-assessment fit
- feasible minimal artifact
- differentiation point
- risks and narrowing suggestion
- student confirmation question

Output:

- `09_theme_candidates.md`

Exit criteria:

- no axis relies on invented evidence
- no defaulting to AI/medicine/design without evidence
- at least one low-risk feasible option exists, or blocker is stated

### Stage 8 — Feasibility, differentiation, privacy critique

Attack each candidate:

- Is it too broad?
- Is it too generic?
- Is it feasible in 2–4 weeks?
- Does it have a concrete artifact?
- Can failure or limitation be analyzed?
- Is subject connection real or forced?
- Is it ethically and privacy safe?
- Is evidence support strong enough?

Output:

- `10_feasibility_critique.md`

Exit criteria:

- weak candidates revised or removed
- finalist options narrowed
- questions for student prepared in Korean

### Stage 9 — Korean student confirmation loop

Ask Korean questions. Minimum checkpoints:

1. evidence/profile fit
2. theme selection/rejection/modification
3. feasibility/artifact preference
4. tone preference
5. draft authenticity review

Outputs:

- `11_student_questions_ko.md`
- `12_student_decision_log.md`

Exit criteria:

- student-selected direction recorded, or output marked provisional
- rejected directions recorded
- remaining uncertainties recorded

### Stage 10 — Grade 11 subject/performance roadmap

Map selected axis to:

- semester 1 subject/performance assessment
- semester 2 subject/performance assessment
- 창체/진로/동아리 opportunities
- final artifact and archive plan

Output must be Korean.

Output:

- `13_subject_roadmap_ko.md`

Exit criteria:

- each subject link is plausible and evidence/framework-based
- forced mappings removed or labeled assumptions
- final artifact is concrete

### Stage 11 — Korean SIGNATURE draft writing

Write only after evidence, school framework, selected axis, feasibility, and student feedback are integrated.

Output must follow Korean school-facing tone.

Output:

- `14_korean_draft.md`

Exit criteria:

- Korean output
- no unsupported claims
- no sensitive information
- no inflated language
- concrete verbs and feasible artifact included

### Stage 12 — Evidence, privacy, tone, and school-context audit

Audit final draft against ledgers and school context.

Output:

- `15_privacy_evidence_tone_audit.md`

Exit criteria:

- unsupported claims removed
- overstatements softened
- sensitive data removed
- final verdict PASS/WARN/BLOCK

### Stage 13 — Final archive

Produce final Korean package.

Output:

- `final_signature_ko.md`

Exit criteria:

- final is Korean
- final status recorded
- manifest updated
- provisional status clearly marked if student confirmation is missing

---

## 11. Field-Agnostic Method and Artifact Library

Use method families rather than forcing career labels.

### 11.1 Method families

- Literature/document analysis
- Data/statistical analysis
- Experiment design and variable control
- Survey/interview with privacy safeguards
- Comparative case analysis
- Prototype/model creation
- Policy/program proposal
- Artistic/design production and critique
- Communication/education material design
- Ethical/social impact analysis
- Reflection and failure-analysis report

### 11.2 Artifact examples

- Korean inquiry report
- annotated bibliography or source map
- comparison matrix
- infographic
- survey summary with anonymized results
- experiment design plan
- prototype screen flow
- small code demo or model, if appropriate
- policy proposal
- campaign plan
- media critique
- design before/after analysis
- performance-assessment presentation deck
- final archive page

---

## 12. Scoring Rubric

Score each candidate from 1 to 5.

- **Evidence fit**: 5 = multiple direct record items; 3 = one direct or several indirect; 1 = mostly speculative.
- **Interest fit**: 5 = student explicitly wants it; 3 = plausible from statements; 1 = not confirmed or weak.
- **School framework fit**: 5 = directly maps to SIGNATURE/SD requirements; 3 = usable with adaptation; 1 = forced.
- **Subject/performance fit**: 5 = clear supplied performance-assessment route; 3 = plausible subject link; 1 = vague.
- **Feasibility**: 5 = minimal artifact possible in 2–4 weeks; 3 = possible with narrowing; 1 = unrealistic.
- **Differentiation**: 5 = specific and not generic; 3 = common but narrowed; 1 = trend-word only.
- **Artifact clarity**: 5 = concrete artifact and evaluation method; 3 = artifact named but underdefined; 1 = vague report only.
- **Ethical/privacy safety**: 5 = low risk; 3 = manageable risk; 1 = unsafe or privacy-invasive.
- **Extensibility**: 5 = can connect across semesters; 3 = one-semester only; 1 = dead end.

A main axis should normally have no score below 3 unless the weakness is explicitly addressed.

---

## 13. Quality Gates

| Gate | Pass criteria | Fail action |
|---|---|---|
| Privacy Gate | PII/sensitive data redacted or excluded | Stop and request redaction or permission |
| Source Gate | Inventory complete; extraction quality recorded | Request clearer/missing files or mark limitation |
| School Framework Gate | SIGNATURE/SD requirements extracted | Use provisional assumptions only |
| Evidence Gate | Major interpretations cite evidence IDs | Remove or label as hypothesis |
| Psychology Gate | No diagnosis or clinical labels | Rewrite or exclude |
| Generality Gate | No field overfitting without evidence | Regenerate broader candidates |
| Theme Gate | Viable axes scored with tradeoffs | Narrow, split, or discard |
| Feasibility Gate | Minimal artifact possible in 2–4 weeks | Reduce scope or change theme |
| Interaction Gate | Student confirmed or draft marked provisional | Ask Korean questions or label provisional |
| Roadmap Gate | Subject links plausible and supplied/assumed status clear | Revise mapping |
| Korean Draft Gate | Korean, concrete, realistic, privacy-safe | Rewrite |
| Evidence Audit Gate | Unsupported claims removed | Revise before final |
| State Gate | Artifacts saved and manifest updated | Save before continuing |

---

## 14. Failure Handling

- Missing student record: produce school-framework summary, intake questions, and provisional planning templates only.
- Poor OCR: label extraction quality low and request clearer pages or manual excerpts.
- Missing school framework: generate candidate axes but label subject/performance links as assumptions.
- Student rejects all candidates: ask for disliked parts, regenerate using method families rather than career labels.
- User asks for fabrication: refuse and offer evidence-safe alternative wording.
- Sensitive data appears: redact, exclude, or stop depending on severity.
- Tool unavailable: use fallback and document limitation.

---

## 15. Korean Drafting Style Rules

School-facing Korean should:

- be specific, grounded, and calm
- use concrete verbs
- show process, limitation, and improvement
- avoid overpraise and grandiose claims
- avoid clinical/personality labels
- avoid unsupported career certainty
- distinguish plan from completed record

Replace unsafe phrasing:

- `무궁무진한 가능성` → `탐구를 확장할 여지`
- `탁월한 천재성` → `자료를 분석하고 근거를 정리하는 태도`
- `전문가 수준` → `교과 개념을 바탕으로 심화 탐구`
- `교수 지도 연구` → only if documented; otherwise `전문 자료를 참고한 탐구`
- `논문 발표` → only if documented; otherwise `탐구 보고서 작성`

---

## 16. Success Criteria

The harness succeeds when:

1. It supports students across fields.
2. It extracts concrete evidence from supplied sources.
3. It maintains evidence and claim ledgers.
4. It identifies 2–5 plausible axes with tradeoffs and risks.
5. It asks Korean confirmation questions before finalizing.
6. It maps the chosen axis to Grade 11 subjects and performance assessments.
7. It produces Korean student-facing outputs.
8. It audits hallucination, privacy, psychology, tone, and school-context risks.
9. It saves intermediate files for resumption.
10. It protects student privacy and agency.

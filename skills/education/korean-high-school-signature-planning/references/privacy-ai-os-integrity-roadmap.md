# Privacy + AI + Systems + Integrity Roadmap Notes

Use this reference only when a Korean high-school SIGNATURE / SD Navigation run has **student-supplied evidence or explicit interest** related to privacy, AI data flow, trustworthy computing, operating systems, memory safety, storage integrity, cryptography concepts, data governance, or responsible digital systems.

This is an **optional thematic example**, not a default roadmap. If the student’s evidence points elsewhere, choose a different framework.

## Evidence Gate

Use this reference only when at least one condition is met:

- The student explicitly says they want to explore privacy, AI data handling, servers, OS, cybersecurity ethics, data integrity, or digital trust.
- The record contains relevant evidence such as programming, information reliability, AI ethics, system design, data modeling, digital citizenship, storage concepts, or technical reading/writing.
- The school’s 수행평가 path can safely support conceptual analysis, data-flow diagrams, policy critique, comparison, or model design.

If evidence is weak, keep the axis provisional and ask the student before finalizing.

## Possible Center Axes

Adapt one of these, or write a new one that better fits the student.

- `AI 시대의 데이터 흐름과 보호 구조를 분석하여 책임 있는 디지털 서비스 설계 조건을 탐구하는 학생`
- `개인정보·AI·저장 과정에서 신뢰가 형성되는 조건과 한계를 비교하는 정보 시스템 탐구자`
- `기술적 보호 구조와 사회적 책임을 함께 고려하여 데이터 활용의 trade-off를 분석하는 학생`
- `데이터가 이동·처리·보존되는 과정을 계층적으로 분석하고, 안전한 활용 원칙을 제안하는 학생`

## Optional Layer Framework

Use a layer model when the student’s interests are broad and technical.

```text
Layer 1. Network / Identity
- identifiers, accounts, sessions, metadata, access paths, public/private exposure

Layer 2. AI / Application
- prompts, files, logs, model memory, app permissions, AI agent authority, data minimization

Layer 3. Device / OS / Runtime
- permissions, sandboxing, virtualization, process isolation, cache/logs, memory safety

Layer 4. Storage / Integrity / Governance
- hashes, checksums, versioning, backup, encryption concepts, deletion, retention, data rights
```

Possible names:

- “신뢰 가능한 개인 정보 시스템의 계층 모델”
- “데이터 흐름과 보호 구조 분석 프레임”
- “Responsible Data System Stack”

## Authoritative Source Anchors

Prefer official or reputable sources over casual summaries. Depending on the specific theme, useful anchors may include:

- official service privacy policies or documentation for data handling
- national curriculum documents / NCIC anchors
- public AI ethics or data governance guidelines
- OWASP GenAI / application security risk categories for conceptual risk taxonomy
- privacy threat-modeling guides for general question structure
- official documentation for tools only when framed as concept/architecture, not usage manuals
- standards or explainers for hashing, checksums, backup, data lifecycle, and memory safety concepts

Do not force any one source or technology name into the plan. Use sources only when they support the student’s selected direction.

## Recommended 1-Year Roadmap Pattern

### 1학기: “흐름과 노출 지점 찾기”

- connect record evidence to one center question
- define key terms: privacy, security, integrity, consent, retention, transparency, user control
- create a data-flow or risk map for a public/fictitious service scenario
- compare two designs using a small rubric
- produce mid-year artifacts: concept map, comparison table, short report, 발표 자료

### 2학기: “보호 구조와 한계 분석하기”

- deepen one or two mechanisms: permissions, isolation, privacy policy, AI logs, backup, hashing, consent, governance
- design a checklist, rubric, or conceptual architecture
- test the checklist on public/synthetic cases
- explicitly discuss limitations, trade-offs, and ethical considerations
- produce final archive: report + diagram + presentation + reflection

## Activity Cards to Reuse

### Data-Flow Map

Purpose: show that privacy and trust are structural, not only individual caution.

Output: diagram or table with `data created / data transferred / processor / storage / possible risk / mitigation / limitation`.

생활기록부식 표현:
> 디지털 서비스에서 데이터가 생성·이동·저장되는 과정을 구조화하고, 단계별 노출 가능성과 보호 방안의 한계를 비교함.

### AI Data-Handling Comparison

Compare:

```text
Cloud AI: user → prompt/file upload → service server → model inference → logs/policy/memory → response
Local/on-device AI: user → local runtime → RAM/cache/temp files → local storage/logs → response
```

Use this only conceptually unless the student actually implemented a system.

생활기록부식 표현:
> AI 도구 사용 과정에서 프롬프트, 파일, 대화 기록, 로그가 이동하는 경로를 분석하고, 처리 방식별 장단점과 개인정보 보호상의 한계를 비교함.

### Privacy / Responsibility Checklist

Criteria examples:

- data minimization
- consent clarity
- retention period
- deletion or correction possibility
- third-party sharing
- transparency/readability
- user control
- accessibility and convenience
- security limitation disclosure

Output: rubric + short critique.

### Permission / Isolation Concept Diagram

Purpose: explain why separating roles, permissions, files, networks, or workspaces can reduce unintended exposure.

Output:

```text
app/task → limited workspace → limited file access → limited network access → reviewed output
```

생활기록부식 표현:
> 권한 분리와 작업 공간 격리의 개념을 바탕으로 디지털 도구 사용 시 데이터 접근 범위를 제한하는 설계 원칙을 설명함.

### Memory Safety / Runtime Trust Table

Use only if the student’s record or interests support programming/OS topics.

| Concept | Meaning | Trust/privacy relevance | School-safe artifact |
|---|---|---|---|
| Out-of-bounds read | permitted range 밖 읽기 | unintended data exposure | concept explainer |
| Use-after-free | released memory 접근 | stale data / instability | diagram |
| Data race | unsafe concurrent access | corruption / inconsistent state | comparison table |
| Permission boundary | access scope separation | reduced blast radius | model diagram |

### Hash / Integrity Mini-Model

Flow:

```text
original data → hash/checksum → stored reference → later check → match/mismatch judgment
```

Use toy strings/files or synthetic data only. Do not imply cryptography expertise beyond the demonstrated level.

생활기록부식 표현:
> 간단한 예시 데이터를 활용해 해시와 체크섬이 데이터 변경 여부를 확인하는 원리를 설명하고, 무결성 검증의 가능성과 한계를 정리함.

## Subject Matching Ideas

Only use if the student selected the subject and the school assessment path fits.

- 국어/화법/언어: privacy policy readability, public guide rewrite, debate script, ethical communication analysis
- 영어: summarize and critique international documentation/articles; create English infographic or presentation script
- 수학: scoring rubric, risk matrix, probability/error model, logarithmic growth, checksum concept
- AI/정보: AI data-flow diagram, checklist, responsible AI use guide, simple conceptual model
- 물리/화학/생명과학: storage media, energy/material trade-offs, biological information analogy only when curriculum supports it
- 사회/윤리/경제/법: rights, consent, regulation, fairness, cost-benefit analysis, policy proposal
- 과학과제연구: research question, literature review, synthetic data, model validation, limitation analysis

## Scope Guards

Use these in final plans:

- no claim of perfect anonymity, perfect security, or unconditional safety
- no bypass/evasion/intrusion/attack procedure
- no collection of real third-party personal data without consent
- no transformation into a tool usage manual
- no “open source/local/private server/encryption is automatically safe” claim
- no real biology/chemistry/engineering experiment unless actually performed and supervised
- limitations and trade-offs must be explicit

## Final Persona Options

Submission-safe examples:

> 저는 디지털 서비스에서 데이터가 이동·처리·보존되는 과정을 분석하고, 사용자의 권리와 시스템 신뢰성을 높이기 위한 보호 구조와 한계를 탐구하고자 합니다.

> 저는 AI 활용 과정에서 발생할 수 있는 데이터 노출과 책임 문제를 분석하고, 기술적 보호 장치와 윤리적 기준을 함께 고려한 디지털 서비스 설계 조건을 제안하고자 합니다.

> 저는 정보 시스템의 신뢰성을 개인정보 보호, 접근 권한, 데이터 무결성, 사용자 이해 가능성의 관점에서 비교하며, 현실적인 개선 방안을 탐구하는 학생입니다.

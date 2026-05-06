# SIGNATURE Harness Onboarding and Required Files

This reference defines the recommended first-use flow for running the SIGNATURE harness with Hermes Agent, especially for students or teachers who are using the skill from a repository for the first time.

## Required Overall Order

At the very beginning of user-facing instructions, clearly state that the workflow proceeds in this order:

```text
1. Install WSL on Windows, or prepare an existing Linux/macOS terminal.
2. Install Hermes Agent inside that environment.
3. Launch and use Hermes Web UI.
4. Install or select the repository skill that contains `signature-harness` and `korean-high-school-signature-planning`.
5. Provide the required reference files: Sunduck SIGNATURE materials and the student's 생활기록부.
6. Run the SIGNATURE harness using those files as grounded references.
```

For general documentation, keep Windows/WSL first because many students use Windows laptops. macOS/Linux instructions can follow as secondary paths.

## Required Reference Files

Before running the actual analysis, tell the user to provide these files in the project workspace or Web UI file area:

1. **Sunduck SIGNATURE / SD Navigation materials**
   - Examples: SIGNATURE guide PDF/HWP/text, SD Navigation guide, workbook, performance-assessment list, school-provided templates, rubric documents.
   - Purpose: school framework, required output shape, step names, performance-assessment constraints, and tone.

2. **Student 생활기록부 / school record**
   - Prefer redacted PDF/text/image files.
   - Remove or mask direct identifiers when possible: name, student number, resident number, address, phone, QR/barcode, teacher names if unnecessary, health/family/counseling details.
   - If the record is scanned and local OCR fails, ask explicit approval before using vision/OCR tools.

3. **Optional supporting files**
   - selected subject list
   - Grade 11 workbook
   - prior drafts
   - reading list
   - teacher feedback
   - portfolio files

Do not start final synthesis if the SIGNATURE/SD materials or 생활기록부 are missing, unless the user explicitly asks for a provisional template. In that case label it `자료 제공 전 임시안`.

## First Message Template

Use a clear Korean first message like this:

```text
진행 순서는 먼저 명확히 이렇게 잡을게.
1) Windows라면 WSL 설치
2) WSL/Linux/macOS 환경에 Hermes 설치
3) Hermes Web UI 실행 및 접속
4) 이 repo에 포함된 SIGNATURE 관련 skill 사용
5) 레퍼런스 파일로 Sunduck SIGNATURE/SD Navigation 자료와 생활기록부 제공
6) 그 파일들을 근거로 후보축 생성 → 중간 선택 질문 → 선택과목 확인 → 로드맵/초안/감사 파일 생성

분석을 시작하려면 작업공간에 최소한 다음 파일이 필요해:
- Sunduck SIGNATURE 또는 SD Navigation 안내 자료
- 생활기록부 파일, 가능하면 개인정보를 가린 버전
- 가능하면 2학년 선택과목 목록과 수행평가/워크북 자료
```

## Windows-First Setup Outline

Use this as a high-level setup guide. Prefer current official Hermes docs for exact installation commands if they change.

### 1. Install WSL on Windows

Open PowerShell as Administrator:

```powershell
wsl --install
```

Then reboot if Windows asks for it. Open the installed Ubuntu/WSL terminal and finish the Linux username/password setup.

If WSL is already installed:

```powershell
wsl --status
wsl --update
```

### 2. Install Hermes inside WSL

Inside the WSL terminal:

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
hermes setup
hermes doctor
```

Use `hermes model` if the model/provider needs to be changed.

### 3. Start Hermes Web UI

Use the repository or deployment instructions for the chosen Web UI. If this repo bundles a Web UI starter, follow that repo's README. If Hermes gateway/API server is required, run the relevant Hermes setup first:

```bash
hermes gateway setup
hermes gateway run
```

Then open the Web UI URL in the Windows browser, upload/reference the Sunduck SIGNATURE files and 생활기록부, and select the workspace containing those files.

### 4. Use the repo skill

Install or make available the repo's skill directory, then verify:

```bash
hermes skills list | grep -E 'signature-harness|korean-high-school-signature-planning'
```

In the Web UI or chat, ask:

```text
/signature-harness 를 사용해서 이 작업공간의 Sunduck SIGNATURE 자료와 생활기록부를 분석해줘.
```

or explicitly:

```text
signature-harness와 korean-high-school-signature-planning 스킬을 사용해서, 첨부한 SIGNATURE 자료/생활기록부/선택과목 목록을 근거로 로드맵을 만들어줘.
```

## After Computer Restart

### Windows / WSL first

After restarting the computer:

1. Open **Windows Terminal**.
2. Open the WSL distro, usually Ubuntu:

```powershell
wsl
```

3. In WSL, go to the project directory if needed:

```bash
cd ~/path/to/project
```

4. Start Hermes CLI if using terminal chat:

```bash
hermes
```

5. If using Web UI/API/gateway, restart the needed service/process. Common foreground mode:

```bash
hermes gateway run
```

If the Web UI itself is a separate repo/app, start it according to that repo's README, for example:

```bash
cd ~/path/to/hermes-webui
# then run the repo's documented start command, e.g. npm/pnpm/python/uv command
```

6. Open the Web UI again in the Windows browser and select the same workspace.

If a background service was installed, check it instead of starting foreground:

```bash
hermes gateway status
hermes gateway restart
```

### macOS / Linux secondary

Open Terminal, then:

```bash
cd ~/path/to/project
hermes
```

For Web UI/API/gateway usage:

```bash
hermes gateway status
hermes gateway run      # foreground mode
# or
hermes gateway restart  # if installed as a service
```

Then start the Web UI repo/app according to its README and reopen the browser URL.

## Harness Execution Flow After Setup

Once Hermes and the Web UI are running, proceed like this:

1. Confirm the active workspace contains the required reference files.
2. Inventory the files and identify:
   - SIGNATURE/SD Navigation school documents
   - 생활기록부
   - selected-subject list or workbook
3. Run privacy/redaction preflight.
4. Extract school framework and student evidence.
5. Generate candidate SIGNATURE axes.
6. Pause and ask the student to choose/revise the direction.
7. Ask for actual selected subjects under the 2022 revised curriculum.
8. Generate selected-subject roadmap and activity bank.
9. Generate Korean draft/final plan.
10. Run privacy/evidence/tone audit.

## Verification Checklist

- [ ] First instructions explicitly state WSL → Hermes → Web UI → repo skill → reference files → harness run.
- [ ] Sunduck SIGNATURE/SD materials are present or the output is marked provisional.
- [ ] 생활기록부 is present or the output is marked provisional.
- [ ] Direct identifiers and sensitive information are excluded from outputs.
- [ ] Windows restart instructions appear before macOS/Linux instructions.
- [ ] The run uses actual supplied files rather than generic memory.

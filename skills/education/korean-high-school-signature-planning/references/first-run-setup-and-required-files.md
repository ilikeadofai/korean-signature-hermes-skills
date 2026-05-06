# First-Run Setup and Required Reference Files

Use this reference when explaining how a student/teacher should start a Korean high-school SIGNATURE / SD Navigation planning run with Hermes Agent and this repository's skills.

## Required Start Order

Always present the first-use order clearly:

```text
1. Windows users: install or open WSL. macOS/Linux users: use the normal terminal.
2. Install Hermes Agent in WSL/Linux/macOS.
3. Launch Hermes Web UI or the configured Hermes gateway/API workflow.
4. Load/use this repository's SIGNATURE skills.
5. Provide Sunduck SIGNATURE/SD Navigation reference files and the student's 생활기록부.
6. Run the planning workflow from those files.
```

## Required Files

The analysis should be grounded in actual files, not memory or generic assumptions.

Required:

- **Sunduck SIGNATURE / SD Navigation materials**: school guide, workbook, rubric, performance-assessment list, templates, or related school documents.
- **생활기록부 / student school record**: preferably redacted PDF/text/image.

Recommended:

- selected-subject list
- Grade 11 workbook or performance-assessment plan
- prior drafts or teacher feedback
- reading/project list

If the required files are missing, label the result `자료 제공 전 임시안` and avoid final claims.

## Windows Restart: First Priority

After restarting a Windows computer:

1. Open Windows Terminal.
2. Enter WSL:

```powershell
wsl
```

3. In WSL, move to the project directory:

```bash
cd ~/path/to/project
```

4. Start Hermes CLI if using terminal chat:

```bash
hermes
```

5. If using Web UI/gateway/API, start or restart the relevant Hermes process:

```bash
hermes gateway status
hermes gateway run      # foreground mode
# or, if installed as a service:
hermes gateway restart
```

6. If the Web UI is a separate repository/application, start it according to that repo's README, then reopen the browser URL and select the same workspace.

## macOS / Linux Restart: Secondary

After restart:

```bash
cd ~/path/to/project
hermes
```

For Web UI/gateway/API:

```bash
hermes gateway status
hermes gateway run
# or
hermes gateway restart
```

Then start the separate Web UI repo/app if needed and reopen the browser URL.

## Planning Flow After Setup

1. Inventory the provided files.
2. Confirm privacy/redaction status.
3. Extract school framework from Sunduck SIGNATURE/SD materials.
4. Extract evidence from 생활기록부.
5. Generate candidate axes.
6. Pause for the student to select/revise.
7. Confirm selected subjects under the 2022 revised curriculum.
8. Build roadmap and activity bank.
9. Draft Korean school-facing plan.
10. Run evidence/privacy/tone audit.

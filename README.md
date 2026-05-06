# Korean SIGNATURE Hermes Skills

Korean high-school **SIGNATURE / SD Navigation / 생활기록부 기반 탐구 로드맵** 작성을 돕는 Hermes Agent 스킬 번들입니다.

포함된 스킬:

- `signature-harness` — Sunduck SIGNATURE/SD Navigation 자료와 생활기록부를 근거로 후보축, 로드맵, 초안, 감사 파일을 만드는 하네스
- `korean-high-school-signature-planning` — 한국 고등학교 SIGNATURE/SD Navigation/수행평가/선택과목 기반 로드맵 설계 스킬

> 이 repo는 특정 학생 한 명의 로드맵이 아니라, 여러 학생/학교 자료에 재사용할 수 있도록 범용화한 스킬 묶음입니다.

---

## 전체 진행 순서

처음 사용하는 경우 진행 순서는 아래처럼 잡습니다.

1. **Windows라면 WSL 설치 또는 실행**
   macOS/Linux 사용자는 기존 터미널을 사용하면 됩니다.
2. **WSL/Linux/macOS 환경에 Hermes Agent 설치**
3. **Hermes Web UI 실행 및 접속**
4. **이 repo의 SIGNATURE 스킬 설치/사용**
5. **레퍼런스 파일 제공**
   - Sunduck SIGNATURE / SD Navigation 자료
   - 학생 생활기록부
6. **스킬 실행**
   - 파일 목록 확인
   - 개인정보/민감정보 점검
   - 생활기록부 근거 추출
   - 후보축 생성
   - 학생에게 중간 선택 질문
   - 2022 개정 선택과목 확인
   - 로드맵/활동뱅크/초안/감사 파일 생성

---

## 1. Windows에서 WSL 설치

PowerShell을 관리자 권한으로 열고 실행합니다.

```powershell
wsl --install
```

Windows가 재시작을 요구하면 재시작한 뒤, Ubuntu/WSL 터미널을 열어 Linux 사용자 이름과 비밀번호 설정을 마칩니다.

이미 WSL이 있다면:

```powershell
wsl --status
wsl --update
```

macOS/Linux 사용자는 이 단계를 건너뛰고 터미널을 열면 됩니다.

---

## 2. Hermes Agent 설치

WSL/Linux/macOS 터미널에서 실행합니다.

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
hermes setup
hermes doctor
```

모델/프로바이더를 바꾸려면:

```bash
hermes model
```

---

## 3. Hermes Web UI 사용

사용 중인 Hermes Web UI 또는 gateway/API 구성을 실행한 뒤 브라우저에서 접속합니다.

일반적으로 gateway/API 구성이 필요하면 먼저 다음을 확인합니다.

```bash
hermes gateway setup
hermes gateway run
```

별도 Web UI repo/app을 쓰는 경우에는 그 repo의 README에 적힌 실행 명령을 따르세요. Web UI가 열리면 작업공간을 선택하고, 아래 레퍼런스 파일을 업로드하거나 작업공간 폴더에 넣습니다.

---

## 4. 이 repo의 skill 설치

이 repo를 받은 뒤:

```bash
git clone https://github.com/ilikeadofai/korean-signature-hermes-skills.git
cd korean-signature-hermes-skills
./install.sh
```

설치 후 Hermes를 재시작하거나 새 세션을 열거나 `/reset`을 실행해 스킬 목록을 새로고침합니다.

설치 확인:

```bash
hermes skills list | grep -E 'signature-harness|korean-high-school-signature-planning'
```

---

## 5. 필요한 레퍼런스 파일

분석을 시작하기 전에 작업공간/Web UI에 최소한 아래 파일을 제공해야 합니다.

### 필수

1. **Sunduck SIGNATURE / SD Navigation 자료**
   - 예: SIGNATURE 안내서, SD Navigation 안내서, 워크북, 수행평가 목록, 학교 템플릿, 루브릭
   - 용도: 학교가 요구하는 단계, 양식, 수행평가 연결, 표현 톤 파악

2. **생활기록부**
   - 가능하면 개인정보를 가린 PDF/text/image
   - 이름, 학번, 주민번호, 주소, 전화번호, QR/바코드, 불필요한 교사명, 건강/가족/상담 정보는 제거 또는 마스킹 권장

### 권장

- 2학년 선택과목 목록
- 2학년 워크북/수행평가 안내
- 기존 초안
- 독서/활동 목록
- 교사 피드백

필수 자료가 없으면 스킬은 최종안이 아니라 `자료 제공 전 임시안`으로만 작성해야 합니다.

---

## 6. 사용 예시 프롬프트

Web UI 또는 Hermes 채팅에서:

```text
signature-harness와 korean-high-school-signature-planning 스킬을 사용해서,
이 작업공간의 Sunduck SIGNATURE 자료와 생활기록부를 분석해줘.
후보축을 먼저 만들고, 내가 선택한 뒤 선택과목 기준 로드맵으로 이어가줘.
```

또는:

```text
/signature-harness 를 사용해서 생활기록부 기반 SIGNATURE 방향을 설계해줘.
단, 중간에 후보축을 보여주고 내 선택을 받은 뒤 최종 로드맵을 만들어줘.
```

---

## 7. 컴퓨터 재시작 후 다시 실행하는 법

### Windows / WSL 우선

컴퓨터를 재시작했다면:

1. **Windows Terminal** 열기
2. WSL 진입

```powershell
wsl
```

3. 프로젝트 폴더로 이동

```bash
cd ~/korean-signature-hermes-skills
```

또는 실제 작업 파일이 있는 폴더로 이동합니다.

4. 터미널 채팅을 쓸 경우 Hermes 실행

```bash
hermes
```

5. Web UI/gateway/API를 쓸 경우 필요한 프로세스 재실행

```bash
hermes gateway status
hermes gateway run
# 또는 서비스로 설치한 경우
hermes gateway restart
```

6. 별도 Web UI repo/app이 있다면 그 repo의 README대로 다시 실행하고, Windows 브라우저에서 Web UI 주소를 엽니다.

### macOS / Linux 후순위

터미널을 열고:

```bash
cd ~/korean-signature-hermes-skills
hermes
```

Web UI/gateway/API를 쓴다면:

```bash
hermes gateway status
hermes gateway run
# 또는
hermes gateway restart
```

그 뒤 Web UI repo/app을 다시 실행하고 브라우저에서 접속합니다.

---

## 개인정보 / 안전 원칙

- 생활기록부 원문 전체를 공개 repo에 올리지 마세요.
- 이름, 학번, 주민번호, 주소, 전화번호, 건강/가족/상담 정보는 결과물에 포함하지 마세요.
- 실제 하지 않은 활동, 수상, 논문, 교수 지도, 외부 연구소 경험을 만들어내면 안 됩니다.
- 보안/프라이버시 주제는 절차 안내가 아니라 개념, 구조, 한계, 윤리, trade-off 중심으로 다룹니다.
- API 키, 토큰, 비밀번호, 접속 문자열은 절대 repo에 커밋하지 마세요.

---

## 로컬 검증

```bash
python validate_skills.py
```

정상 예시:

```text
VALID skills/education/signature-harness/SKILL.md
VALID skills/education/korean-high-school-signature-planning/SKILL.md
OK: 2 skills validated
```

---

## Repo 구조

```text
korean-signature-hermes-skills/
  README.md
  LICENSE
  install.sh
  validate_skills.py
  skills/
    education/
      signature-harness/
      korean-high-school-signature-planning/
```

---

## License

MIT

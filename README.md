# Korean SIGNATURE Hermes Skills

한국 고등학교 **SIGNATURE / SD Navigation / 진로탐색 프로젝트 / 수행평가 로드맵**을 도와주는 Hermes Agent용 스킬 모음입니다.

이 저장소는 두 개의 Hermes skill을 배포합니다.

- `signature-harness`
  생활기록부, 학교 SIGNATURE 문서, SD Navigation 문서, 수행평가 자료, 학생 관심사를 바탕으로 **근거 기반 SIGNATURE 방향**, **과목별 로드맵**, **학교 제출용 초안**, **개인정보/표현 감사**까지 진행하는 종합 하네스입니다.

- `korean-high-school-signature-planning`
  한국 고등학교 맥락에 맞춰 **생활기록부 근거 → 중심 탐구축 → 선택과목 수행평가 연결 → 학기별 활동 계획 → 세특식 표현**으로 정리하는 계획 스킬입니다.

> 핵심 목표:
> “AI가 멋대로 그럴듯한 진로 계획을 지어내는 것”이 아니라, **학생이 실제로 한 활동과 실제로 선택한 과목**을 바탕으로 수행 가능한 SIGNATURE 로드맵을 만드는 것입니다.

---

## 0. 처음 진행 순서

처음 사용하는 경우, 전체 흐름을 먼저 이렇게 잡습니다.

```text
1. Windows 사용자: WSL 설치 또는 실행
   - macOS/Linux 사용자는 기존 터미널 사용
2. WSL/Linux/macOS 환경에 Hermes Agent 설치
3. Hermes Web UI / Dashboard 실행 및 접속
4. 이 GitHub repo의 SIGNATURE skill 설치 및 사용
5. 레퍼런스 파일 제공
   - Sunduck SIGNATURE / SD Navigation 자료
   - 학생 생활기록부
6. 그 파일들을 근거로 SIGNATURE harness 실행
   - 자료 확인 → 개인정보 점검 → 후보축 생성 → 학생 선택 질문 → 선택과목 확인 → 로드맵/초안/감사
```

즉, 이 repo는 “그냥 README만 읽고 쓰는 문서”가 아니라 **Hermes Agent 안에 skill로 설치해서**, Web UI나 터미널에서 실제 파일을 읽히며 사용하는 것을 전제로 합니다.

필수 레퍼런스 파일은 최소 두 종류입니다.

- **Sunduck SIGNATURE / SD Navigation 자료**
  예: SIGNATURE 안내문, SD Navigation 안내문, 학교 워크북, 수행평가 목록, 루브릭, 학교 템플릿
- **학생 생활기록부**
  가능하면 이름, 학번, 주민번호, 주소, 전화번호, 건강/가족/상담 정보 등을 가린 버전

이 두 자료가 없으면 최종 로드맵이 아니라 `자료 제공 전 임시안` 수준으로만 진행하는 것이 안전합니다.

## 1. 이 스킬이 구체적으로 해주는 일

이 스킬들은 단순히 “보고서 주제 추천”만 하는 것이 아닙니다. 실제 학교 과제에 맞게 아래 흐름을 도와줍니다.

### 1.1 생활기록부 기반 분석

학생의 1학년 또는 이전 기록에서 다음을 뽑아냅니다.

- 반복해서 등장하는 관심 분야
- 실제로 수행한 활동
- 세특에서 보이는 강점
- 탐구 태도, 문제 해결 방식, 협업 방식
- 다음 학년에서 확장할 수 있는 “씨앗 질문”

단, 이름, 주민번호, 주소, 전화번호, 가족/건강/상담 정보 같은 민감정보는 학교 제출용 결과물에 넣지 않도록 강하게 제한합니다.

### 1.2 SIGNATURE 중심축 설계

여러 관심사가 흩어져 있을 때, 하나의 중심 질문으로 묶어줍니다.

예를 들어 학생의 관심이 다음처럼 흩어져 있다면:

- AI
- 생명과학
- 글쓰기
- 사회문제
- 공학 설계
- 환경
- 수학 모델링

스킬은 바로 결론을 내리지 않고, 후보 축을 2~4개 정도 만든 뒤 학생에게 물어봅니다.

```text
여기서 한 번 멈출게. 후보는 아래처럼 보여.
1. 후보 A — 장점 / 위험 / 결과물
2. 후보 B — 장점 / 위험 / 결과물
3. 후보 C — 장점 / 위험 / 결과물

어느 방향으로 확정할까? 섞고 싶은 후보나 빼고 싶은 방향도 말해줘.
```

이 과정 덕분에 학생 본인의 관심과 어긋난 방향으로 확정되는 것을 줄일 수 있습니다.

### 1.3 2022 개정 교육과정 선택과목 반영

2022 개정 교육과정에서는 학생마다 선택과목이 다릅니다. 그래서 이 스킬은 과목별 로드맵을 만들기 전에 실제 선택과목을 확인합니다.

예시 질문:

```text
2학년 1학기/2학기에 실제 선택한 과목을 알려줘.
모르면 “아직 모름”이라고 해도 돼.
그러면 전체 후보안으로 만들고, 실제 선택과목 확인 후 다시 줄일게.
```

선택과목을 모르는 경우에는 결과물에 다음처럼 표시합니다.

```text
학생 선택과목 확인 전 전체 후보안
```

선택과목이 확인된 경우에는 선택하지 않은 과목을 메인 로드맵에서 제거합니다.

### 1.4 수행평가 연결

학교 워크북이나 수행평가 목록이 있으면, 실제 수행평가명과 연결해서 활동을 제안합니다.

활동 카드 예시:

```text
과목: 영어Ⅱ
실제 수행평가명: 영어 발표 / 글쓰기 수행평가
교육과정 연결 키워드: 다양한 매체 정보 이해, 주장 제시, 요약, 정보 윤리
활동명: 해외 자료 기반 주제 비교 발표
목적: SIGNATURE 중심 주제를 영어 자료와 연결해 설명하기
내용: 공식 문서나 신뢰할 수 있는 영어 자료를 요약하고 관점 차이를 비교함
산출물: 영어 발표문, 시각자료, 출처 목록
생활기록부식 역량 표현: 자료를 비판적으로 선별하고 자신의 탐구 주제와 연결하여 영어로 표현함
주의할 점: 번역기 결과를 그대로 제출하지 않고 핵심 표현을 직접 정리함
```

### 1.5 학교 제출용 초안 작성

학교에 제출할 수 있는 문장으로 정리합니다.

- 과장된 표현 줄이기
- 실제 하지 않은 활동을 한 것처럼 쓰지 않기
- 위험하거나 오해될 수 있는 보안/의학/심리/법률 표현 완화하기
- “완벽한 해결”, “무조건 안전”, “논문급 연구” 같은 단정 피하기

### 1.6 감사/audit

마지막에는 결과물을 점검합니다.

- 개인정보가 들어갔는가?
- 실제 근거 없는 주장이 있는가?
- 선택하지 않은 과목이 섞였는가?
- 학교 제출용으로 위험한 표현이 있는가?
- 최종 판정이 PASS / WARN / BLOCK 중 무엇인가?

---

## 2. 누가 쓰면 좋은가요?

이런 학생에게 특히 유용합니다.

- 고등학교 SIGNATURE / SD Navigation / 진로탐색 프로젝트를 준비하는 학생
- 생활기록부를 바탕으로 2학년 또는 3학년 활동 방향을 잡고 싶은 학생
- 선택과목 수행평가를 하나의 진로 주제로 연결하고 싶은 학생
- 세특에 남을 만한 활동을 “실제로 할 수 있는 수준”으로 설계하고 싶은 학생
- AI에게 무작정 생기부 문장을 써달라고 하기보다, 근거 기반으로 계획을 세우고 싶은 학생

선생님, 멘토, 학부모가 학생의 활동 설계를 도울 때도 사용할 수 있습니다.

---

## 3. 준비물

처음 사용하는 사람 기준으로 필요한 것은 다음입니다.

1. 인터넷이 되는 컴퓨터
2. 터미널 사용 가능 환경
   - Windows라면 WSL 사용을 추천합니다.
   - macOS / Linux는 기본 터미널로 가능합니다.
3. Hermes Agent
4. 사용할 AI 모델 계정 또는 API 키
   - 예: OpenRouter, Anthropic, OpenAI Codex OAuth, Google Gemini 등
5. 필수 레퍼런스 파일
   - **Sunduck SIGNATURE / SD Navigation 자료**
     - SIGNATURE 안내문
     - SD Navigation 안내문
     - 학교 워크북
     - 수행평가 목록 / 루브릭 / 템플릿
   - **학생 생활기록부 PDF 또는 텍스트**
     - 가능하면 개인정보를 가린 버전
6. 권장 자료
   - 본인의 2학년 선택과목 목록
   - 기존 초안
   - 독서 목록 / 활동 목록
   - 교사 피드백

> 중요: 생활기록부나 학교 자료를 넣기 전에 이름, 주민번호, 주소, 전화번호, 가족/건강/상담 정보 등은 가능한 한 지우고 사용하세요.
>
> Sunduck SIGNATURE/SD Navigation 자료와 생활기록부가 없으면, 스킬은 최종안이 아니라 `자료 제공 전 임시안`으로만 작성해야 합니다.
---

## 4. Hermes Agent 설치하기

Hermes Agent는 터미널, Web Dashboard, 메신저, IDE 등에서 사용할 수 있는 AI agent입니다. 이 스킬들은 Hermes Agent 안에서 작동합니다.

### 4.1 Linux / macOS / WSL에서 설치

터미널을 열고 아래 명령어를 실행합니다.

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

설치가 끝나면 터미널을 껐다가 다시 열거나, 안내에 따라 PATH를 새로고침합니다.

설치 확인:

```bash
hermes --version
```

정상이라면 대략 이런 식으로 버전이 나옵니다.

```text
Hermes Agent v0.x.x
```

### 4.2 Windows 사용자를 위한 WSL 설치법

Windows에서는 Hermes를 그냥 `cmd`나 PowerShell에 바로 설치하기보다 **WSL**을 사용하는 것을 추천합니다. WSL은 Windows 안에서 Ubuntu 같은 Linux 환경을 실행하는 기능입니다.

쉽게 말하면:

```text
Windows 컴퓨터 안에 작은 Linux 개발 환경을 하나 만든다
→ 그 Linux 안에 Hermes를 설치한다
→ 브라우저는 Windows에서 열고, 명령어는 WSL 터미널에서 실행한다
```

#### Step 1. Windows 버전 확인

Windows 10 최신 버전 또는 Windows 11이면 대부분 WSL을 사용할 수 있습니다.

먼저 Windows 검색창에 `PowerShell`을 검색합니다.

- `Windows PowerShell` 또는 `터미널`을 찾습니다.
- 가능하면 **관리자 권한으로 실행**합니다.

PowerShell에서 아래 명령어를 입력합니다.

```powershell
wsl --status
```

이미 WSL이 설치되어 있으면 상태 정보가 나옵니다. 설치되어 있지 않으면 다음 단계로 진행합니다.

#### Step 2. WSL 설치

PowerShell을 관리자 권한으로 열고 아래 명령어를 실행합니다.

```powershell
wsl --install
```

보통 이 명령 하나로 Ubuntu까지 함께 설치됩니다.

설치가 끝나면 Windows를 재부팅하라는 안내가 나올 수 있습니다. 그 경우 재부팅하세요.

만약 Ubuntu가 자동으로 설치되지 않았다면 아래처럼 설치할 수 있습니다.

```powershell
wsl --install -d Ubuntu
```

설치 가능한 Linux 목록을 보고 싶으면:

```powershell
wsl --list --online
```

#### Step 3. Ubuntu 처음 실행

Windows 시작 메뉴에서 `Ubuntu`를 검색해서 실행합니다.

처음 실행하면 Linux 사용자 이름과 비밀번호를 만들라고 나옵니다.

예시:

```text
Enter new UNIX username: student
New password:
Retype new password:
```

주의할 점:

- 비밀번호를 입력해도 화면에 글자가 보이지 않는 것이 정상입니다.
- Windows 비밀번호와 같을 필요는 없습니다.
- 잊어버리지 않을 비밀번호를 사용하세요.

#### Step 4. Ubuntu 업데이트

Ubuntu 창이 열리면 아래 명령어를 실행합니다.

```bash
sudo apt update
sudo apt upgrade -y
```

`sudo`를 처음 쓰면 방금 만든 Linux 비밀번호를 물어볼 수 있습니다.

기본 도구도 설치합니다.

```bash
sudo apt install -y curl git ca-certificates
```

#### Step 5. Hermes 설치

이제 Ubuntu 터미널 안에서 Hermes 설치 명령어를 실행합니다.

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

설치 후 터미널을 완전히 닫았다가 다시 열거나, 아래 명령어를 실행합니다.

```bash
source ~/.bashrc
```

설치 확인:

```bash
hermes --version
```

정상이라면 Hermes 버전이 출력됩니다.

#### Step 6. Hermes 초기 설정

```bash
hermes setup
```

또는 모델 설정만 하려면:

```bash
hermes model
```

여기서 사용할 AI provider를 고릅니다. 예를 들어 OpenRouter, Anthropic, OpenAI Codex OAuth, Gemini 등을 사용할 수 있습니다.

설정 후 상태 확인:

```bash
hermes status --all
```

문제가 있으면:

```bash
hermes doctor
```

#### Step 7. Windows 브라우저에서 Hermes Dashboard 열기

WSL의 Ubuntu 터미널에서 아래 명령어를 실행합니다.

```bash
hermes dashboard --tui
```

그러면 보통 Windows 브라우저에서 자동으로 열리거나, 아래 주소로 접속할 수 있습니다.

```text
http://127.0.0.1:9119
```

자동으로 안 열리면 Windows의 Chrome, Edge, Firefox 주소창에 직접 입력하세요.

브라우저를 자동으로 열지 않게 하려면:

```bash
hermes dashboard --tui --no-open
```

포트가 이미 사용 중이면:

```bash
hermes dashboard --tui --port 9120
```

그 경우 접속 주소는 다음입니다.

```text
http://127.0.0.1:9120
```

#### Step 8. WSL 안에서 이 저장소 설치

Ubuntu 터미널에서 아래 명령어를 실행합니다.

```bash
cd ~
git clone https://github.com/ilikeadofai/korean-signature-hermes-skills.git
cd korean-signature-hermes-skills
./install.sh
```

설치 확인:

```bash
hermes skills list | grep -E 'signature-harness|korean-high-school-signature-planning'
```

Hermes를 다시 시작하거나, Hermes 채팅 안에서 `/reset`을 입력하면 새 스킬이 인식됩니다.

#### Step 9. WSL에서 스킬 사용

터미널에서 바로 시작하려면:

```bash
hermes -s signature-harness
```

또는 Web Dashboard의 Chat/TUI 입력창에서:

```text
/skill signature-harness
```

그 다음 이렇게 요청할 수 있습니다.

```text
SIGNATURE 방향 설계를 도와줘. 후보축을 먼저 만들고, 바로 최종안으로 가지 말고 내가 선택하게 해줘.
```

#### Step 10. Windows 파일과 WSL 파일 위치 이해하기

WSL을 처음 쓰면 파일 위치가 헷갈릴 수 있습니다.

Ubuntu 안의 홈 폴더는 보통 다음과 같습니다.

```text
/home/내사용자이름/
```

Windows의 C 드라이브는 WSL에서 다음 위치로 보입니다.

```text
/mnt/c/
```

예를 들어 Windows의 다운로드 폴더는 보통 다음처럼 접근합니다.

```bash
cd /mnt/c/Users/윈도우사용자이름/Downloads
```

하지만 가능하면 프로젝트 파일은 WSL 홈 폴더 안에 두는 것을 추천합니다.

좋은 위치:

```text
/home/내사용자이름/signature-project/
```

비추천 위치:

```text
/mnt/c/Users/.../Desktop/signature-project/
```

이유는 WSL 안의 Linux 파일 시스템이 보통 더 빠르고, 권한 문제도 적기 때문입니다.

#### Step 11. 생활기록부/학교 자료를 WSL로 옮기는 방법

가장 쉬운 방법은 Windows 파일 탐색기에서 WSL 폴더를 여는 것입니다.

Ubuntu 터미널에서 아래 명령어를 실행합니다.

```bash
explorer.exe .
```

그러면 현재 WSL 폴더가 Windows 파일 탐색기로 열립니다. 여기에 PDF나 텍스트 파일을 드래그해서 넣으면 됩니다.

예시 프로젝트 폴더 만들기:

```bash
mkdir -p ~/signature-project
cd ~/signature-project
explorer.exe .
```

그 다음 Windows 파일 탐색기 창에 다음 자료를 복사합니다.

```text
redacted_record.pdf
signature_guide.pdf
sd_navigation.pdf
workbook.pdf
selected_subjects.txt
```

Hermes에게는 이렇게 말할 수 있습니다.

```text
자료는 ~/signature-project 폴더에 있어.
생활기록부는 redacted_record.pdf,
SIGNATURE 안내문은 signature_guide.pdf,
수행평가 자료는 workbook.pdf야.
```

#### Step 12. WSL 사용 시 자주 생기는 문제

`wsl: command not found`가 뜨는 경우:

- PowerShell이 아니라 아주 오래된 터미널 환경일 수 있습니다.
- Windows 10/11 업데이트가 필요할 수 있습니다.
- 관리자 권한 PowerShell에서 다시 시도하세요.

`hermes: command not found`가 뜨는 경우:

```bash
source ~/.bashrc
~/.local/bin/hermes --version
```

그래도 안 되면 PATH에 `~/.local/bin`이 안 잡힌 것입니다. 아래 줄을 `~/.bashrc`에 추가할 수 있습니다.

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

Dashboard 주소가 안 열리는 경우:

```bash
hermes dashboard --status
hermes dashboard --tui --no-open
```

그리고 Windows 브라우저에서 직접 접속합니다.

```text
http://127.0.0.1:9119
```

WSL이 꼬인 것 같으면 PowerShell에서 WSL을 재시작할 수 있습니다.

```powershell
wsl --shutdown
```

그 다음 Ubuntu를 다시 실행하세요.

파일 경로에 공백이 있어서 문제가 생기는 경우:

```bash
cd "/mnt/c/Users/Your Name/Downloads"
```

처럼 따옴표를 사용하세요. 그래도 초보자라면 `~/signature-project`처럼 공백 없는 WSL 홈 폴더를 쓰는 것이 가장 편합니다.

### 4.3 처음 설정하기

처음에는 Hermes가 어떤 AI 모델을 쓸지 설정해야 합니다.

```bash
hermes setup
```

또는 모델만 따로 설정하려면:

```bash
hermes model
```

설정 과정에서 사용할 provider와 model을 고릅니다.

예시 provider:

- OpenRouter
- Anthropic
- OpenAI Codex OAuth
- Google Gemini
- DeepSeek
- local/custom provider

설정 후 상태 확인:

```bash
hermes status --all
```

문제가 있으면:

```bash
hermes doctor
```

---

## 5. Hermes 기본 사용법

### 5.1 터미널에서 대화 시작

```bash
hermes
```

그러면 Hermes와 채팅할 수 있습니다.

한 번만 질문하고 끝내고 싶다면:

```bash
hermes chat -q "안녕, 작동 확인해줘"
```

또는 최신 Hermes에서는 one-shot 옵션을 쓸 수 있습니다.

```bash
hermes -z "안녕, 작동 확인해줘"
```

### 5.2 스킬 불러오기

Hermes 채팅 안에서 다음처럼 입력합니다.

```text
/skill signature-harness
```

또는 시작할 때 미리 불러올 수도 있습니다.

```bash
hermes -s signature-harness
```

두 스킬을 함께 불러오고 싶다면:

```bash
hermes -s signature-harness,korean-high-school-signature-planning
```

---

## 6. Web UI / Dashboard 사용법

터미널이 익숙하지 않다면 Hermes의 Web Dashboard를 사용할 수 있습니다.

### 6.1 Dashboard 실행

아래 명령어를 실행합니다.

```bash
hermes dashboard --tui
```

기본 주소는 다음입니다.

```text
http://127.0.0.1:9119
```

자동으로 브라우저가 열리지 않으면 직접 위 주소를 주소창에 입력하세요.

브라우저를 자동으로 열지 않고 실행하려면:

```bash
hermes dashboard --tui --no-open
```

포트를 바꾸고 싶다면:

```bash
hermes dashboard --tui --port 9120
```

그 경우 주소는 다음처럼 바뀝니다.

```text
http://127.0.0.1:9120
```

### 6.2 Dashboard에서 할 수 있는 일

Hermes Dashboard에서는 보통 다음 작업을 할 수 있습니다.

- 설정 확인
- API key / provider 설정 확인
- 세션 확인
- Hermes 상태 확인
- 브라우저에서 Hermes와 대화
- TUI Chat 탭을 통해 터미널처럼 Hermes 사용

버전에 따라 화면 구성은 조금 다를 수 있습니다. 그래도 기본 흐름은 같습니다.

1. `hermes dashboard --tui` 실행
2. 브라우저에서 `http://127.0.0.1:9119` 열기
3. Chat 또는 TUI 관련 탭으로 이동
4. Hermes에게 메시지 입력
5. 필요하면 `/skill signature-harness` 입력

### 6.3 Web UI에서 이 스킬 쓰는 법

Dashboard의 Chat/TUI 입력창에 아래처럼 입력합니다.

```text
/skill signature-harness
```

그 다음 이렇게 요청합니다.

```text
SIGNATURE 방향 설계를 도와줘. 내 생활기록부와 학교 수행평가 자료를 바탕으로 근거 기반 후보를 먼저 만들고, 후보를 보여준 뒤 내가 선택하게 해줘.
```

또는 선택과목 로드맵 중심으로 요청할 수도 있습니다.

```text
/skill korean-high-school-signature-planning
내 선택과목 기준으로 수행평가와 연결되는 SIGNATURE 활동 로드맵을 만들어줘.
```

### 6.4 주의: Dashboard를 외부에 공개하지 마세요

기본값인 `127.0.0.1`은 내 컴퓨터에서만 접속됩니다. 안전합니다.

아래 옵션은 조심하세요.

```bash
hermes dashboard --insecure
```

`--insecure`는 다른 기기에서 접속할 수 있게 만들 수 있지만, 설정이나 API 키가 노출될 수 있습니다. 초보자는 사용하지 않는 것을 추천합니다.

---

## 7. 이 저장소의 스킬 설치하기

### 7.1 GitHub에서 내려받기

이 저장소를 clone합니다.

```bash
git clone https://github.com/ilikeadofai/korean-signature-hermes-skills.git
cd korean-signature-hermes-skills
```

### 7.2 자동 설치

```bash
./install.sh
```

설치 위치는 기본적으로 다음입니다.

```text
~/.hermes/skills/education/
```

설치되는 스킬:

```text
~/.hermes/skills/education/signature-harness/
~/.hermes/skills/education/korean-high-school-signature-planning/
```

설치 후 Hermes를 새로 시작하거나, 이미 실행 중이라면 `/reset`을 입력하세요.

### 7.3 설치 확인

```bash
hermes skills list | grep -E 'signature-harness|korean-high-school-signature-planning'
```

정상이라면 두 스킬 이름이 보입니다.

### 7.4 수동 설치

자동 설치가 안 되면 아래처럼 직접 복사할 수 있습니다.

```bash
mkdir -p "${HERMES_HOME:-$HOME/.hermes}/skills/education"
cp -R skills/education/signature-harness "${HERMES_HOME:-$HOME/.hermes}/skills/education/"
cp -R skills/education/korean-high-school-signature-planning "${HERMES_HOME:-$HOME/.hermes}/skills/education/"
```

그 후 Hermes를 재시작하세요.

---

## 8. 가장 쉬운 사용 예시

### 8.1 SIGNATURE 전체 설계

Hermes를 실행합니다.

```bash
hermes -s signature-harness
```

그리고 이렇게 말합니다.

```text
고등학교 SIGNATURE 방향 설계를 도와줘.
내 1학년 생활기록부와 학교 SIGNATURE 안내문, 수행평가 자료를 바탕으로 분석해줘.
먼저 후보축을 3개 정도 만들고, 바로 최종안으로 가지 말고 나에게 선택하게 해줘.
```

Hermes는 보통 다음을 물어봅니다.

```text
1. 이번 작업의 목적은 뭐야?
2. 현재 관심 분야나 희망 진로가 있어?
3. 생기부와 자료에서 개인정보는 지웠어?
4. 피하고 싶은 방향은 뭐야?
5. 최종 결과물은 어떤 형태가 현실적이야?
```

자료가 준비되어 있다면 파일 경로를 알려주면 됩니다.

```text
자료는 ./my-records/ 안에 있어.
생활기록부는 redacted_record.pdf,
학교 SIGNATURE 안내문은 signature_guide.pdf,
수행평가 목록은 workbook.pdf야.
```

### 8.2 선택과목 기준 수행평가 로드맵 만들기

```bash
hermes -s korean-high-school-signature-planning
```

요청 예시:

```text
내 SIGNATURE 주제는 아직 확정 전이야.
1학년 기록과 내 관심사를 바탕으로 후보를 만들고,
내 2학년 선택과목 기준으로 수행평가와 연결되는 활동을 추천해줘.
선택과목은 다음과 같아.
1학기: 문학, 영어Ⅰ, 대수, 물리학, 생명과학
2학기: 화법과 언어, 영어Ⅱ, 미적분Ⅱ, 과학과제연구
```

### 8.3 생활기록부 없이 관심사만으로 임시 설계

생활기록부가 아직 준비되지 않았다면 이렇게 할 수 있습니다.

```text
아직 생활기록부 파일은 없어.
내 관심사는 생명과학, AI, 환경 문제야.
학생 확인 전 임시안으로 SIGNATURE 후보축을 만들어줘.
나중에 생기부를 넣으면 근거 기반으로 다시 수정할게.
```

이 경우 결과물은 반드시 임시안으로 봐야 합니다. 실제 제출 전에는 생활기록부와 학교 수행평가 자료로 다시 검증하는 것이 좋습니다.

---

## 9. 추천 작업 흐름

처음부터 최종 글을 쓰려고 하지 말고, 아래 순서로 진행하는 것을 추천합니다.

### Step 1. 자료 준비

가능하면 다음 자료를 준비합니다.

```text
project-folder/
  redacted_record.pdf
  signature_guide.pdf
  sd_navigation.pdf
  workbook_or_assessment_list.pdf
  selected_subjects.txt
```

개인정보는 미리 가립니다.

### Step 2. 후보축 만들기

```text
/skill signature-harness
내 자료를 바탕으로 SIGNATURE 후보축을 3개 만들어줘.
각 후보마다 장점, 위험, 가능한 산출물을 알려주고 거기서 멈춰줘.
```

### Step 3. 학생이 방향 선택

후보를 보고 학생이 직접 말합니다.

```text
1번과 3번을 섞고 싶어.
AI보다는 생명과학 쪽을 더 살리고 싶고,
너무 공학적으로만 보이지 않게 해줘.
```

### Step 4. 선택과목 확인

```text
내 선택과목은 다음과 같아.
1학기: ...
2학기: ...
```

### Step 5. 과목별 수행평가 로드맵 생성

```text
이제 선택과목 기준으로 과목별 활동 카드와 수행평가 연결표를 만들어줘.
```

### Step 6. 학교 제출용 초안 작성

```text
학교 제출용 SIGNATURE 계획안으로 자연스럽게 정리해줘.
너무 과장하지 말고 실제 할 수 있는 활동처럼 써줘.
```

### Step 7. 감사/audit

```text
개인정보, 근거 없는 주장, 위험한 표현, 선택과목 오류가 있는지 감사해줘.
PASS/WARN/BLOCK으로 판정해줘.
```

---

## 10. 결과물 예시

`signature-harness`는 전체 실행 시 다음과 같은 파일을 만들도록 설계되어 있습니다.

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
  16_expanded_subject_activity_bank_ko.md
  final_signature_ko.md
```

각 파일의 역할은 대략 다음과 같습니다.

- `05_evidence_ledger.md`
  생활기록부나 자료에서 뽑은 근거 목록

- `06_claim_ledger.md`
  “이 학생은 이런 경향이 있다” 같은 해석이 어떤 근거에서 나왔는지 정리

- `09_theme_candidates.md`
  SIGNATURE 후보축 목록

- `10_feasibility_critique.md`
  각 후보의 현실성, 차별성, 위험 요소 분석

- `13_subject_roadmap_ko.md`
  선택과목 기준 학기별 활동 계획

- `14_korean_draft.md`
  학교 제출용 한국어 초안

- `15_privacy_evidence_tone_audit.md`
  개인정보, 근거, 표현 수위 감사

- `final_signature_ko.md`
  최종 요약본

---

## 11. 개인정보 보호 가이드

생활기록부나 학교 자료를 AI에게 줄 때는 조심해야 합니다.

### 11.1 넣지 말아야 할 정보

가능하면 아래 정보는 삭제하거나 가리고 사용하세요.

- 이름
- 주민등록번호
- 주소
- 전화번호
- 학번, 반, 번호
- 학교명과 교사명
- 가족 정보
- 건강, 진단, 상담, 약물 관련 정보
- 타인의 개인정보
- 계정, 비밀번호, API 키, 토큰
- 문서확인번호, QR 코드, 바코드

### 11.2 안전한 방식

좋은 예:

```text
1학년 정보 과목에서 서버 구조와 운영체제에 관심을 보였음.
과학 활동에서 환경 문제를 조사하고 발표함.
국어 활동에서 사회적 쟁점에 대한 비평문을 작성함.
```

나쁜 예:

```text
홍길동, 2학년 3반 15번, 주민번호 ..., 전화번호 ...
상담 기록에서 ...
가족 상황은 ...
```

### 11.3 학교 제출용 주의

학교 제출용 결과물에는 다음을 피하는 것이 좋습니다.

- 실제 하지 않은 활동을 한 것처럼 표현
- 외부 연구소, 교수 지도, 논문, 수상 등을 허위로 언급
- “완벽한 해결”, “무조건 안전”, “세계 최초” 같은 과장
- 보안/해킹/우회/침투 절차처럼 보이는 표현
- 의학적 진단이나 심리 분석처럼 보이는 표현

---

## 12. 검증하기

이 저장소에는 간단한 검증 스크립트가 포함되어 있습니다.

```bash
python validate_skills.py
```

정상 결과 예시:

```json
{
  "issues": [],
  "status": "PASS"
}
```

이 스크립트는 다음을 확인합니다.

- 두 스킬 디렉터리가 존재하는지
- `SKILL.md` frontmatter가 있는지
- `name`, `description`이 있는지
- description 길이가 Hermes 제한을 넘지 않는지
- 특정 사용자에게만 해당하는 문자열이 남아 있지 않은지
- obvious secret pattern이 없는지

---

## 13. 컴퓨터 재시작 후 다시 실행하는 법

### 13.1 Windows / WSL 우선

컴퓨터를 재시작했다면 Windows 기준으로는 아래 순서로 다시 시작합니다.

1. **Windows Terminal**을 엽니다.
2. WSL로 들어갑니다.

```powershell
wsl
```

3. 작업 폴더로 이동합니다.

```bash
cd ~/korean-signature-hermes-skills
```

실제 생활기록부나 Sunduck SIGNATURE 자료를 다른 작업공간에 넣어 두었다면, 그 폴더로 이동해도 됩니다.

```bash
cd ~/path/to/signature-workspace
```

4. 터미널 채팅으로 사용할 경우 Hermes를 실행합니다.

```bash
hermes
```

5. Web UI / Dashboard를 사용할 경우 Dashboard를 다시 실행합니다.

```bash
hermes dashboard --tui
```

브라우저가 자동으로 열리지 않으면 Windows 브라우저에서 직접 접속합니다.

```text
http://127.0.0.1:9119
```

포트를 바꾸고 싶으면:

```bash
hermes dashboard --tui --port 9120
```

6. Web UI / Dashboard에서 같은 작업공간을 선택하고, Sunduck SIGNATURE/SD Navigation 자료와 생활기록부가 있는지 확인한 뒤 스킬을 실행합니다.

### 13.2 macOS / Linux 후순위

macOS/Linux에서는 터미널을 열고 다음처럼 실행합니다.

```bash
cd ~/korean-signature-hermes-skills
hermes
```

Dashboard를 쓸 경우:

```bash
hermes dashboard --tui
```

그 뒤 브라우저에서 Dashboard 주소를 열고 같은 작업공간을 선택합니다.

---

## 14. 자주 생기는 문제

### Q1. `hermes: command not found`가 떠요.

설치 후 터미널을 새로 열어보세요. 그래도 안 되면 PATH 문제일 수 있습니다.

```bash
~/.local/bin/hermes --version
```

이 명령이 되면 `~/.local/bin`을 PATH에 추가해야 합니다.

### Q2. 스킬을 설치했는데 Hermes에서 안 보여요.

Hermes를 재시작하거나 채팅 안에서 `/reset`을 입력하세요.

확인:

```bash
hermes skills list | grep signature
```

### Q3. Web Dashboard가 안 열려요.

먼저 상태를 확인하세요.

```bash
hermes dashboard --status
```

다시 실행:

```bash
hermes dashboard --tui --no-open
```

브라우저에서 직접 접속:

```text
http://127.0.0.1:9119
```

포트가 이미 사용 중이면 다른 포트를 쓰세요.

```bash
hermes dashboard --tui --port 9120
```

### Q4. AI가 파일을 못 읽어요.

파일 경로를 정확히 알려주세요.

좋은 예:

```text
자료는 /home/user/signature-project/redacted_record.pdf 에 있어.
```

또는 Hermes를 해당 폴더에서 실행하세요.

```bash
cd /home/user/signature-project
hermes -s signature-harness
```

### Q5. 생기부 PDF가 스캔본이라 텍스트 추출이 안 돼요.

스캔본은 OCR 또는 vision 처리가 필요할 수 있습니다. 이 경우 개인정보가 외부 모델로 전달될 수 있으므로 반드시 먼저 민감정보를 가리고, Hermes가 추가 확인을 요청하면 내용을 이해한 뒤 승인하세요.

### Q6. 결과가 너무 그럴듯하지만 근거가 약해요.

이렇게 요청하세요.

```text
각 주장마다 근거 ID를 붙여줘.
근거 없는 부분은 가설이라고 표시해줘.
```

또는:

```text
학교 제출 전 감사해줘. 근거 없는 주장, 과장된 표현, 개인정보, 선택과목 오류를 찾아줘.
```

---

## 15. 저장소 구조

```text
korean-signature-hermes-skills/
  README.md
  LICENSE
  install.sh
  validate_skills.py
  DISTRIBUTION_AUDIT.md
  skills/
    education/
      korean-high-school-signature-planning/
        SKILL.md
        references/
          curriculum-grounded-activity-bank.md
          generic-signature-harness-productionization.md
          privacy-ai-os-integrity-roadmap.md
      signature-harness/
        SKILL.md
        references/
          improved_harness.md
          output_schemas.md
          privacy_policy.md
          korean_final_output_template.md
          subagent_plan.md
          test_cases.md
          scanned-record-vision-ocr-workflow.md
          privacy-data-sovereignty-axis.md
          selected-subject-activity-expansion.md
```

---

## 16. 기여하기

개선 아이디어가 있다면 issue나 pull request를 열어주세요.

좋은 기여 예시:

- 더 쉬운 설치 설명
- 학교 현장에서 자주 쓰는 수행평가 유형 추가
- 개인정보 보호 체크리스트 개선
- 2022 개정 교육과정 과목별 anchor 보강
- 안전한 예시 프롬프트 추가
- 오타 수정

주의할 점:

- 실제 학생의 생활기록부 원문을 issue에 올리지 마세요.
- 이름, 학교명, 전화번호, 상담/건강/가족 정보 등은 반드시 제거하세요.
- 특정 학생 한 명에게만 맞는 로드맵을 기본값으로 넣지 마세요.
- 위험한 보안 절차나 우회법 설명은 넣지 마세요.

---

## 17. 라이선스

MIT License입니다. 자세한 내용은 `LICENSE` 파일을 확인하세요.

---

## 18. 한 줄 요약

이 저장소는 한국 고등학생이 Hermes Agent를 이용해 **생활기록부 근거 기반 SIGNATURE 주제**, **선택과목 수행평가 로드맵**, **학교 제출용 초안**, **개인정보/표현 감사**를 안전하게 만들 수 있도록 돕는 스킬 모음입니다.

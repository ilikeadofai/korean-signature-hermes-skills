# 미적분 수행평가: AI 노래 음성 합성·비브라토 변화율 주제 노트

## When to use

Use when a Korean high-school student asks for a 미적분Ⅰ/Ⅱ 수행평가 report topic that should combine:

- AI / 음성합성 / VOCALOID / 보컬로이드 / AI 커버 / 음악 관심
- 미적분Ⅰ의 변화율, 도함수, 평균변화율, 그래프 해석
- 진로/전공적합성과 창의성 균형

This is especially useful when the student is torn between a conventional AI topic such as loss-function decrease and a more creative music/voice topic.

## Recommended framing

Best balanced title:

> AI 노래 음성 합성에서 음정·음량 변화율과 자연스러운 표현의 관계 분석: 비브라토를 중심으로

Shorter school-facing title:

> AI 음성 합성에서 비브라토 변화율과 자연스러움의 관계 분석

Core inquiry question:

> AI 노래 음성 합성에서 비브라토의 폭과 빠르기는 음정 변화율을 어떻게 바꾸며, 이는 자연스러운 표현과 어떤 관련이 있는가?

Core hypothesis:

> 비브라토의 폭과 빠르기가 증가할수록 음정 변화율의 최댓값은 커질 것이다. 그러나 변화율이 지나치게 크면 자연스럽기보다는 과장되거나 기계적인 표현으로 들릴 수 있다. 따라서 자연스러운 AI 노래 음성에는 적절한 비브라토 폭과 변화율 범위가 필요할 것이다.

## 2022 개정 미적분Ⅰ curriculum anchor

When the user explicitly asks for *actual 2022 교육과정상 미적분Ⅰ 단원명/학습 내용*, verify against NCIC rather than relying on memory.

Authoritative NCIC path used successfully:

```text
NCIC 국가교육과정정보센터
→ 우리나라 교육과정
→ 2022 개정 시기
→ 고등학교(2022.12)
→ 수학
→ 미적분Ⅰ
→ 2. 내용 체계 및 성취기준
```

The NCIC tree can be queried programmatically via `POST https://ncic.re.kr/api/inv/inventoryNodeList.do` with `type=ogi4`, `nowTblType=org`, `menuType=1`, then expand `2022 개정 시기 → 고등학교(2022.12) → 수학 → 미적분Ⅰ`. In the observed tree, `미적분Ⅰ` had `ref=10069854`; `2. 내용 체계 및 성취기준` had `ref=10069872`. The detail page can be opened through `/inv/org/view.do` with `openYear=2022`, `seq=10069872`, `orgType=ogi4`, `menuType=1`.

NCIC content summary for 미적분Ⅰ:

- 영역/범주: `함수의 극한과 연속`, `미분`, `적분`.
- `함수의 극한과 연속`: 함수의 극한, 함수의 연속. 핵심 아이디어: 함수의 극한은 함수의 국소적 성질을 이해하는 도구이며, 함수의 연속은 함수의 극한을 통해 설명된다.
- `미분`: 미분계수, 도함수, 도함수의 활용. 핵심 아이디어: 미분은 함수의 순간적인 변화를 나타내는 도구이며 함수의 그래프와 이동하는 물체의 움직임 탐구에 활용된다.
- `적분`: 부정적분, 정적분, 정적분의 활용. 핵심 아이디어: 부정적분은 미분과 역관계에 있고 정적분 계산에 이용되며, 정적분은 도형의 넓이와 물체의 이동 거리 등에 활용된다.
- 과정·기능에는 공학 도구를 이용한 극한/연속/미분/적분 탐구, 실생활·타 교과 연결, 식·그래프·기호 표현 등이 포함된다.
- 가치·태도에는 변화하는 현상을 이해하는 도구로서 미적분의 유용성 인식이 포함된다.

For this AI singing/vibrato topic, choose the interest unit as:

```text
미적분Ⅰ — 미분: 평균변화율, 순간변화율, 미분계수, 도함수, 도함수의 활용
```

Rationale: vocal pitch is modeled as a time-varying quantity `P(t)`, and the inquiry is about how fast pitch changes during vibrato. That maps directly to average rate of change, instantaneous rate of change, derivative, and derivative-as-change-speed.

## 미적분Ⅰ scope guard

Do **not** make 삼각함수 미분 the main required mathematics for a 미적분Ⅰ-only performance assessment. A sine vibrato model is intuitive, but trig derivatives can look outside the target course depending on the school sequence. Safer main analysis:

1. Extract or simulate pitch data `P(t)` from three controlled samples: no/weak/strong vibrato.
2. Compute interval average rates:

```tex
\frac{P(t_2)-P(t_1)}{t_2-t_1}
```

3. Interpret shorter-interval average rates as approximations to instantaneous rate/m분계수.
4. Optionally approximate selected pitch-contour segments with a simple polynomial and use 미적분Ⅰ 도함수 tools.
5. Present `P(t)=P_0+A\sin(2\pi ft)` and `|P'(t)|_{max}=2\pi Af` only as an extension/simplified model if it fits the class context.

For the early two-item submission, use this compact wording:

- 관심 단원: `미적분Ⅰ의 미분 단원(평균변화율, 순간변화율, 미분계수, 도함수, 도함수의 활용)`.
- 탐구 주제: `AI 노래 음성 합성에서 비브라토의 음정 변화율과 자연스러운 표현의 관계 분석`.

## Math model

Basic vibrato model:

```tex
P(t)=P_0+A\sin(2\pi ft)
```

- `P(t)`: time-varying pitch
- `P_0`: base pitch
- `A`: vibrato depth/amplitude
- `f`: vibrato rate/frequency

Derivative:

```tex
P'(t)=2\pi Af\cos(2\pi ft)
```

Maximum pitch-change rate:

```tex
|P'(t)|_{max}=2\pi Af
```

Interpretation:

- larger `A` → wider pitch wobble and larger pitch-change rate
- larger `f` → faster pitch wobble and larger pitch-change rate
- overly large change rate may sound exaggerated/mechanical, but do **not** claim this is universally true; naturalness is subjective and also depends on loudness, timbre, pronunciation, and context.

If 삼각함수 미분 feels outside the current class scope, keep the main analysis to interval average rates from extracted/simulated pitch data:

```tex
\frac{P(t_2)-P(t_1)}{t_2-t_1}
```

and present the sine model as a simplified extension.

## Feasible activity designs

### Most recommended: controlled synthetic comparison

1. Create an original 4–8 bar melody and simple lyric/phoneme phrase.
2. Generate the same melody with the same voice/singer under 3 settings:
   - no vibrato
   - weak vibrato
   - strong vibrato
3. Export WAV files.
4. Extract pitch contour `F0(t)`.
5. Compare pitch graphs, vibrato depth, vibrato rate, and interval average rates or approximate derivative.
6. Discuss naturalness cautiously and include limitations.

Why this is best:

- avoids copyrighted song-cover complications
- controls variables better than comparing different songs/models
- keeps the math centered on change rate

### Optional extension: human vs AI comparison

Record the student singing the same short melody and compare with AI/VOCALOID output. Treat as an extension because microphone quality, singing ability, room noise, and performance variation are confounders.

### Avoid as main design: many commercial voicebanks/models comparison

Different voicebanks/engines vary in timbre, tuning defaults, phoneme handling, and smoothing. Use only as a follow-up, not as the main controlled experiment.

## Tooling

On CachyOS/Arch, useful packages exist in repos:

```bash
sudo pacman -S python-librosa python-matplotlib python-scipy python-soundfile ffmpeg praat sonic-visualiser audacity
```

Observed baseline in this session: `ffmpeg` was installed; `librosa`, `matplotlib`, `scipy`, `soundfile`, and `parselmouth` were not installed in the system Python.

Tool options:

- Sonic Visualiser: easiest visual pitch/spectrogram inspection and report screenshots.
- Praat: established phonetics/speech analysis tool; good for pitch contour and intensity.
- Python + librosa: best for CS/AI-aligned report; can extract pitch, compute rates, plot graphs, and export CSV/figures.

## Prior research found

Use these as evidence that the topic is real, not as mandatory reading dumps.

Vibrato/naturalness/singing synthesis:

- Suzuki, Banno, Asahi. “Investigation of Effect on Naturalness of Vibrato of Singing Voice by Difference of Vibrato Waveform.” IEEJ Transactions on Electronics, Information and Systems, 2019. DOI: `10.1541/ieejeiss.139.1440`.
- Liu, Wen, Lu. “Vibrato Learning in Multi-Singer Singing Voice Synthesis.” IEEE ASRU, 2021. DOI: `10.1109/ASRU51503.2021.9688029`.
- Meron, Hirose. “Synthesis of vibrato singing.” IEEE ICASSP, 2000. DOI: `10.1109/ICASSP.2000.859067`.
- Gu, Lin. “Mandarin singing voice synthesis using ANN vibrato parameter models.” ICMLC, 2008. DOI: `10.1109/ICMLC.2008.4620973`.
- Song et al. “Singing Voice Synthesis with Vibrato Modeling and Latent Energy Representation.” IEEE MMSP, 2022. DOI: `10.1109/MMSP55362.2022.9948936`.

AI singing voice synthesis background:

- Liu et al. “DiffSinger: Singing Voice Synthesis via Shallow Diffusion Mechanism.” AAAI, 2022. DOI: `10.1609/aaai.v36i10.21350`.
- Zhang et al. “VISinger: Variational Inference with Adversarial Learning for End-to-End Singing Voice Synthesis.” ICASSP, 2022. DOI: `10.1109/ICASSP43922.2022.9747664`.
- Nishimura et al. “Singing Voice Synthesis Based on Deep Neural Networks.” Interspeech, 2016. DOI: `10.21437/Interspeech.2016-1027`.
- Nose, Kanemoto, Koriyama. “HMM-based expressive singing voice synthesis with singing style control and robust pitch modeling.” Computer Speech & Language, 2015. DOI: `10.1016/j.csl.2015.04.001`.

## Other voice features that can extend the project

Keep vibrato as the core for 미적분Ⅰ. Add at most 1–2 of these as extension/future work.

1. Portamento / pitch transition
   - `P'(t)` measures how quickly pitch moves between notes.
   - Question: does a too-sudden pitch transition sound mechanical?

2. Loudness / dynamics
   - Let energy/loudness be `E(t)`; `E'(t)` is loudness-change rate.
   - Useful for crescendo, decrescendo, attack/release.

3. Attack/release of notes
   - Analyze early/late loudness envelope slope.
   - Too sharp may sound hard; too slow may blur articulation.

4. Pitch accuracy vs expressiveness trade-off
   - Define pitch deviation `D(t)=P(t)-P_target`.
   - Key claim: perfectly zero deviation is not always natural in singing; controlled temporal variation can be expressive.

5. Timbre/formant/spectral-centroid change
   - Possible, but too advanced for a 미적분Ⅰ main report; keep as future research.

6. Pronunciation timing / consonant-vowel transitions
   - Good AI voice topic, but less directly calculus-centered; keep as future research.

## School-safe limitations and wording

Use cautious wording:

- “자연스러움은 주관적이며, 본 탐구는 그중 비브라토의 음정 변화율이라는 한 요소에 한정한다.”
- “사인함수 모델은 실제 노래 음성을 단순화한 모델이다.”
- “실제 AI 음성 합성은 음정뿐 아니라 음량, 발음, 음색, 데이터셋, 모델 구조의 영향을 받는다.”
- “기존 곡 커버보다 직접 만든 짧은 멜로디와 직접 생성한 합성 음성을 사용해 저작권·라이선스 문제를 줄인다.”

Avoid claiming:

- a specific change-rate threshold universally determines naturalness
- AI singing is natural/unnatural solely because of vibrato
- commercial voicebank/model comparisons are controlled unless variables are actually controlled

## Six-item 수행평가 skeleton

1. 관심 단원: 미분계수와 도함수, 함수의 변화율.
2. 탐구 주제: AI 음성 합성에서 비브라토 변화율과 자연스러움의 관계 분석.
3. 탐구 가설: `A`와 `f`가 커질수록 `|P'(t)|_max=2πAf`가 커지며, 적절한 변화율 범위가 자연스러운 표현과 관련될 것이다.
4. 동기: AI·음악·음성합성 관심에서 출발; 자연스러운 노래는 음정 정확도뿐 아니라 시간에 따른 음정 변화가 중요하다고 봄.
5. 보여주고 싶은 능력: 음악적 현상을 수학적으로 모델링하고, AI 음성 합성 기술을 변화율/도함수로 해석하는 융합적 사고력과 모델 한계 인식.
6. 추후 탐구: 실제 pitch contour 추출, 사람/AI 비교, loudness·attack·portamento 확장, 청취자 평가와 변화율 지표 비교.

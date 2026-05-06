# Scanned Korean Student Record Vision-OCR Workflow

Use this reference when a Korean school record PDF is image-based/scanned and local text extraction fails.

## Trigger
- `pdftotext`, PyMuPDF, or an existing `.txt` extraction returns empty/near-empty text.
- Rendered page images already exist, or the PDF can be rendered locally.
- Local OCR such as `tesseract`, `ocrmypdf`, `easyocr`, `paddleocr`, `marker`, or `surya` is unavailable or too heavy to install.

## Privacy-first sequence
1. Confirm the text extraction failure and source inventory.
2. Check available local OCR commands/libraries before external processing.
3. If local OCR is unavailable, ask the student for explicit approval before using vision/OCR on page images.
4. In every vision prompt, instruct the tool to exclude direct identifiers:
   - student name, school name, class/number, student ID, resident number, address, phone, document confirmation numbers, teacher names, photos/facial description.
5. Ask vision to return structured, school-safe extraction only:
   - page type/section
   - subject/activity summaries
   - concrete verbs
   - interest keywords/competencies
   - Grade 11 SIGNATURE seeds
   - OCR uncertainty
6. Use minimal non-identifying quotes only.
7. Mark final outputs `학생 확인 전 임시안` unless the student confirms direction and facts.

## Suggested page prompt
```text
이 이미지는 한국 고등학교 생활기록부 페이지입니다. 개인정보 보호: 학생 이름, 학번, 생년월일, 주소, 연락처, 학교명, 반/번호, 교사명, 문서확인번호, 사진/외모 묘사 등 직접 식별자는 출력하지 마세요. 페이지 전체를 OCR하되, 최종 답에는 학교 제출용 분석에 필요한 비식별 정보만 정리하세요. 형식: 1) 페이지 유형/섹션, 2) 과목/활동 항목별 핵심 내용, 3) 구체 동사, 4) 관심 키워드/역량, 5) 2학년 SIGNATURE 씨앗, 6) OCR 불확실성. 짧은 원문 인용은 개인정보 없이 최소만.
```

## Artifact discipline
- Keep all run artifacts under one run directory such as `signature-harness-run/`.
- Subagents or helper audits must not write root-level stray files; if they do, move/remove them after user approval and consolidate into the run directory.
- Store evidence ledgers as redacted summaries, not raw OCR dumps.

## Verification
- Run a final scan for common identifier patterns and forbidden overclaim phrases.
- Pattern hits for words like `주민등록번호`, `주소`, `문서확인번호` may be acceptable in privacy-checklist contexts, but not as actual values.
- Confirm final draft includes `학생 확인 전 임시안` and an audit verdict.

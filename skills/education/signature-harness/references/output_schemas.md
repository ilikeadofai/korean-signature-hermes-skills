# Output Schemas for the Generic SIGNATURE Harness

These schemas define the major artifacts produced by the improved harness. Internal field names are English for portability. Korean values are used where the content is student-facing.

## 1. Shared enums

```json
{
  "PrivacyLevel": ["public", "school_facing", "private_redacted", "private_sensitive", "forbidden"],
  "SourceKind": ["student_record", "student_statement", "school_document", "teacher_feedback", "performance_assessment", "generated_hypothesis"],
  "SupportStrength": ["direct", "derived", "weak", "unsupported"],
  "ReviewVerdict": ["PASS", "WARN", "BLOCK"],
  "RunMode": ["full_interactive", "provisional_best_effort", "audit_only", "school_framework_only"]
}
```

## 2. Run manifest

File: `00_run_manifest.md`

```json
{
  "run_metadata": {
    "run_id": "string",
    "run_mode": "full_interactive",
    "goal": "school_submission | roadmap | theme_generation | self_analysis | audit_only | other",
    "student_alias": "Student A",
    "created_by": "Hermes Agent",
    "language_policy": {
      "internal_docs": "English",
      "student_facing_outputs": "Korean"
    }
  },
  "status": {
    "completed_stages": [],
    "current_stage": "string",
    "next_required_action": "string",
    "is_provisional": false,
    "blocking_reasons": [],
    "open_questions_ko": []
  },
  "capabilities": {
    "file_tools": true,
    "pdf_text_extraction": "available | unavailable | unknown",
    "ocr_or_vision": "available | unavailable | unknown",
    "web_or_browser": "available | unavailable | unknown",
    "subagents": "available | unavailable | unknown",
    "mcp_servers": []
  }
}
```

## 3. Source inventory

File: `02_source_inventory.md`

```json
{
  "provided_files": [
    {
      "file_id": "SRC001",
      "filename": "string",
      "source_kind": "school_document",
      "processed": true,
      "processing_method": "read_file | pdftotext | OCR | vision | manual_excerpt | not_processed",
      "privacy_level": "public",
      "redaction_status": "not_needed | redacted | unredacted | unknown",
      "notes": "string"
    }
  ],
  "student_preferences": {
    "current_interests_ko": [],
    "preferred_artifacts_ko": [],
    "directions_to_avoid_ko": [],
    "tone_preference_ko": "학교 제출용 | 자기분석용 | 편한 설명 | 미정"
  },
  "sensitive_data_check": {
    "pii_detected": false,
    "sensitive_data_detected": [],
    "required_user_action_ko": []
  }
}
```

## 4. Extraction log

File: `03_extraction_log.md`

```json
{
  "extractions": [
    {
      "file_id": "SRC001",
      "method": "pdftotext",
      "pages_processed": "1-5",
      "extracted_character_count": 0,
      "quality": "high | medium | low",
      "ocr_uncertainties": [],
      "limitations": [],
      "requires_manual_review": false
    }
  ]
}
```

## 5. School framework summary

File: `04_school_framework_summary.md`

```json
{
  "signature": {
    "discovery": {
      "required_actions": [],
      "deliverables": []
    },
    "enhancement": {
      "deep_dive_requirements": [],
      "cross_over_requirements": []
    },
    "masterpiece": {
      "academic_persona_requirements": [],
      "roadmap_requirements": [],
      "final_artifact_options": []
    }
  },
  "sd_navigation": {
    "starting_point": [],
    "route_tracking": [],
    "destination_or_artifact": []
  },
  "performance_assessments": [
    {
      "subject_ko": "string",
      "semester": "1학기 | 2학기 | unknown",
      "task_name_ko": "string",
      "possible_artifacts_ko": [],
      "notes": "string"
    }
  ],
  "risky_wording": [],
  "useful_school_phrases_ko": []
}
```

## 6. Evidence ledger

File: `05_evidence_ledger.md`

```json
{
  "evidence_items": [
    {
      "evidence_id": "E001",
      "source_kind": "student_record",
      "source_file_id": "SRC001",
      "location": {
        "page": null,
        "section": "교과세특: 정보",
        "line_or_excerpt_ref": "string"
      },
      "quote_ko": "minimal Korean quote or redacted excerpt",
      "paraphrase_en": "English internal paraphrase",
      "category": "activity | keyword | action_verb | limitation | interest | subject_strength | school_requirement",
      "subject_area_ko": "string",
      "concrete_actions_ko": ["설계", "비교", "분석"],
      "concepts_or_tools": [],
      "outcome_or_limit_ko": "string",
      "privacy_level": "school_facing",
      "usable_for_school_draft": true,
      "confidence": "high | medium | low"
    }
  ]
}
```

Markdown table form:

```md
| Evidence ID | Source | Location | Quote/summary | Category | Concrete action | Outcome/limit | Privacy | Confidence |
|---|---|---|---|---|---|---|---|---|
```

## 7. Claim ledger

File: `06_claim_ledger.md`

```json
{
  "claims": [
    {
      "claim_id": "C001",
      "claim_text_ko": "string",
      "claim_type": "activity | trait | interest | career_direction | roadmap | draft_sentence",
      "evidence_ids": ["E001"],
      "support_strength": "direct",
      "is_student_confirmed": false,
      "risk_flags": {
        "privacy": [],
        "hallucination": [],
        "psychology": [],
        "tone": []
      },
      "required_action": "keep | soften | ask_student | remove",
      "safe_rewrite_ko": "string"
    }
  ]
}
```

## 8. Activity and interest profile

File: `07_activity_interest_profile.md`

```json
{
  "activity_patterns": [
    {
      "pattern_name_en": "data_verification",
      "pattern_name_ko": "데이터 검증형",
      "evidence_ids": ["E001", "E002"],
      "confidence": "medium",
      "grade11_use_ko": "string",
      "risks_ko": []
    }
  ],
  "interest_clusters": [
    {
      "cluster_name_ko": "string",
      "evidence_ids": [],
      "student_statement_ids": [],
      "confirmation_needed": true
    }
  ],
  "directions_to_avoid_ko": []
}
```

## 9. Learning profile

File: `08_learning_profile.md`

```json
{
  "profile_scope": "non_diagnostic_activity_design_only",
  "observations": [
    {
      "observation_id": "LP001",
      "framework": "RIASEC | self_determination_theory | mastery_goal | workflow | Big_Five_behavioral_indicator",
      "hypothesis_en": "string",
      "student_facing_summary_ko": "string",
      "evidence_ids": ["E001"],
      "confidence": "low | medium | high",
      "workflow_implication_ko": "string",
      "school_facing_allowed": false
    }
  ],
  "cautions": [
    "No clinical diagnosis.",
    "Do not include health/family details in school-facing drafts."
  ]
}
```

## 10. Theme candidates

File: `09_theme_candidates.md`

```json
{
  "theme_candidates": [
    {
      "candidate_id": "T001",
      "axis_name_ko": "string",
      "one_line_definition_ko": "나는 [문제]를 [방법]으로 탐구하는 학생이다.",
      "evidence_fit": {
        "score": 1,
        "evidence_ids": ["E001"],
        "notes_ko": "string"
      },
      "interest_fit": {
        "score": 1,
        "needs_student_confirmation": true,
        "notes_ko": "string"
      },
      "subject_fit": {
        "score": 1,
        "subjects_ko": [],
        "performance_assessment_paths_ko": []
      },
      "feasibility": {
        "score": 1,
        "timebox": "2-4 weeks",
        "minimal_artifact_ko": "string",
        "required_tools": []
      },
      "differentiation": {
        "score": 1,
        "generic_risk": "low | medium | high",
        "narrowing_suggestion_ko": "string"
      },
      "safety": {
        "privacy_risk": "low | medium | high",
        "psychology_risk": "low | medium | high",
        "hallucination_risk": "low | medium | high"
      },
      "student_question_ko": "string",
      "review_verdict": "PASS | WARN | BLOCK"
    }
  ]
}
```

Markdown table form:

```md
| 후보 | 근거 적합 | 관심 적합 | 과목 적합 | 가능성 | 차별성 | 최소 결과물 | 위험 | 학생에게 물어볼 것 |
|---|---:|---:|---:|---:|---:|---|---|---|
```

## 11. Feasibility critique

File: `10_feasibility_critique.md`

```json
{
  "candidate_reviews": [
    {
      "candidate_id": "T001",
      "verdict": "PASS | WARN | BLOCK",
      "too_broad": false,
      "too_generic": false,
      "high_school_feasible": true,
      "artifact_is_concrete": true,
      "failure_is_analyzable": true,
      "subject_link_quality": "strong | plausible | forced | missing",
      "privacy_or_ethics_risk": "low | medium | high",
      "recommended_narrowing_ko": "string",
      "student_question_ko": "string"
    }
  ],
  "recommended_shortlist": ["T001"],
  "blocked_candidates": []
}
```

## 12. Student questions and decision log

Files:

- `11_student_questions_ko.md`
- `12_student_decision_log.md`

```json
{
  "questions": [
    {
      "question_id": "Q001",
      "question_ko": "아래 후보 중 실제로 가장 해보고 싶은 방향은 뭐야?",
      "choices_ko": [],
      "why_needed_en": "theme confirmation"
    }
  ],
  "decisions": [
    {
      "decision_id": "D001",
      "question_id": "Q001",
      "student_answer_ko": "string",
      "selected_candidate_id": "T001",
      "rejected_options": [],
      "constraints_added_ko": [],
      "remaining_uncertainties_ko": []
    }
  ]
}
```

## 13. Subject roadmap

File: `13_subject_roadmap_ko.md`

```json
{
  "selected_axis": "T001",
  "semester_1": [
    {
      "subject_ko": "string",
      "performance_assessment_ko": "string",
      "activity_plan_ko": "string",
      "artifact_ko": "string",
      "evidence_ids": [],
      "assumption_status": "supplied | inferred | needs_confirmation"
    }
  ],
  "semester_2": [],
  "creative_experiential_activities": [],
  "final_artifact_plan_ko": "string",
  "what_not_to_do_ko": []
}
```

## 14. Korean draft

File: `14_korean_draft.md`

Required structure:

```md
# Project SIGNATURE Draft

> 상태: 학생 확인 완료 / 학생 확인 전 임시안

## STEP 1. Signature Discovery
### 핵심 역량 1
### 핵심 역량 2
### 핵심 역량 3
### Seed 1
### Seed 2
### Seed 3

## STEP 2. Signature Enhancement
### Deep-Dive
### Critical Thinking
### Cross-Over 1
### Cross-Over 2
### Cross-Over 3

## STEP 3. Signature Masterpiece
### 학술적 페르소나
### 1학기 로드맵
### 2학기 로드맵
### 최종 결과물
### 하지 않을 것

## 학생 확인 필요 부분
```

## 15. Evidence/privacy/tone audit

File: `15_privacy_evidence_tone_audit.md`

```json
{
  "audit_id": "AUDIT_FINAL",
  "draft_version": "v1",
  "claim_reviews": [
    {
      "claim_id": "C001",
      "draft_claim_ko": "string",
      "evidence_ids": ["E001"],
      "support_strength": "direct",
      "risk": "none | privacy | overstatement | unsupported | diagnostic | tone",
      "required_fix": "keep | soften | remove | ask_student",
      "safe_rewrite_ko": "string"
    }
  ],
  "unsupported_claims_to_remove": [],
  "overstated_claims_to_soften": [],
  "privacy_leaks_to_remove": [],
  "tone_revisions": [],
  "final_verdict": "PASS | WARN | BLOCK"
}
```

## 16. Final Korean output

File: `final_signature_ko.md`

```json
{
  "status_ko": "최종안 | 학생 확인 전 임시안",
  "one_line_identity_ko": "string",
  "core_capabilities_ko": [],
  "central_question_ko": "string",
  "selected_project_ko": "string",
  "grade11_roadmap_summary_ko": "string",
  "final_artifact_ko": "string",
  "school_record_verbs_ko": [],
  "what_not_to_do_ko": [],
  "remaining_questions_ko": []
}
```

## 17. Scoring rubric reminder

Use 1–5 scoring for:

- evidence fit
- interest fit
- school framework fit
- subject/performance fit
- feasibility
- differentiation
- artifact clarity
- ethical/privacy safety
- extensibility

A recommended main axis should normally have no score below 3 unless the weakness is explicitly addressed.

# Distribution Audit

- Status: PASS
- Package: `korean-signature-hermes-skills`
- Validator: `python validate_skills.py` PASS, dependency-free
- External publishing status at package time: ready for GitHub publication

## Included skills

```json
{
  "korean-high-school-signature-planning": {
    "version": "1.0.1",
    "description_len": 188,
    "role": "General Korean high-school SIGNATURE / SD Navigation planning skill"
  },
  "signature-harness": {
    "version": "1.0.0",
    "description_len": 213,
    "role": "Production-style evidence/privacy/checkpoint/audit harness"
  }
}
```

## Validation scope

The validator checks:

- expected skill directories exist
- each `SKILL.md` starts with frontmatter
- `name` and `description` are present
- description length is within the Hermes limit
- skill bodies are non-empty
- common user-specific strings and obvious secret patterns are absent from skill Markdown files

## Notes

- No real student records are included.
- No API keys, provider tokens, passwords, or credential files are included.
- This package is intended as a public, reusable skill bundle.

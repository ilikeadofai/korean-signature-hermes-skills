# Distribution Audit

## Package

- Repository: `ilikeadofai/korean-signature-hermes-skills`
- Skills:
  - `signature-harness`
  - `korean-high-school-signature-planning`

## Checks

- [x] Complete skill directories copied, including `references/` files.
- [x] README explains WSL → Hermes install → Web UI → repo skill usage.
- [x] README states that Sunduck SIGNATURE/SD Navigation materials and 생활기록부 are required reference files.
- [x] README includes Windows/WSL restart instructions before macOS/Linux.
- [x] `install.sh` uses `${HERMES_HOME:-$HOME/.hermes}`.
- [x] `validate_skills.py` is dependency-free.
- [x] Validator checks frontmatter, size, empty body, obvious secrets, and local/private strings.

## Privacy Notes

This repository must not include actual student records, generated private run artifacts, API keys, tokens, passwords, or local-only personal paths.

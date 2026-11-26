# Security policy

## Supported versions

This project is in early development. No stable release or security support commitment has been established.

## Reporting a vulnerability

Use GitHub private vulnerability reporting if enabled. Do not post exploitable details, credentials or private logs in public issues. If private reporting is unavailable, request a private reporting channel through a public issue without disclosing sensitive details.

## Safe development

- Never commit credentials, tokens, private configurations or production logs.
- Use synthetic data and placeholder configuration values.
- Review dependencies and scan changes and Git history for secrets.
- Apply least privilege and keep administrative interfaces off the public internet.
- Test hardware and administrative controls in an isolated environment before deployment.

If a secret is exposed, revoke or rotate it immediately. Removing it from the latest commit alone is insufficient.

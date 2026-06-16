# Security Checklist

## Authentication
- Hash passwords using Argon2id or bcrypt with strong parameters.
- Support MFA for owners/admins.
- Use short-lived JWT access tokens and rotating refresh tokens, or secure server sessions.
- Lock or throttle repeated failed logins.

## Authorization
- Enforce company tenant isolation on every query.
- Use RBAC permissions, not only role names.
- Require elevated permission for posting journals, locking periods, exporting reports, deleting users.

## Application security
- Validate all input with Pydantic.
- Use SQLAlchemy parameterization to prevent SQL injection.
- Configure CORS to explicit origins only.
- Use CSRF protection if using cookie-based sessions.
- Add API rate limiting on auth, uploads, exports, and public endpoints.
- Secure file uploads: extension allowlist, MIME sniffing, size limits, malware scanning in production.
- Store secrets in Azure Key Vault, AWS Secrets Manager, or Render secrets.
- Encrypt backups and object storage.

## Audit and compliance
- Immutable audit logs for financial postings, voids, reversals, period locks, exports, logins.
- Store before/after snapshots for sensitive changes.
- Never physically delete posted accounting records.

## Backups
- Daily automated DB backups, point-in-time recovery, periodic restore drills.
- Separate retention for audit logs and attachments.
- Export company data in CSV/JSON for account closure.

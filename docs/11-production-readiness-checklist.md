# Production Readiness Checklist

- [ ] Accountant reviewed accounting rules and reports.
- [ ] Tenant isolation tested across all endpoints.
- [ ] RBAC permission matrix implemented and tested.
- [ ] Journal posting cannot create unbalanced entries.
- [ ] Locked periods block modifications.
- [ ] Audit logs are append-only for financial actions.
- [ ] Database migrations run in CI and staging.
- [ ] Backups are automated and restore-tested.
- [ ] Secrets are stored in a managed secret store.
- [ ] Logs include correlation IDs and exclude sensitive data.
- [ ] File uploads have size/type limits and scanning plan.
- [ ] API rate limits configured.
- [ ] Dependency and container scanning enabled.
- [ ] Monitoring alerts for errors, latency, worker failures, DB usage.
- [ ] Terms, privacy policy, data retention, and export/delete process prepared.

# DevOps and Deployment Plan

## Local development
- Docker Compose: API, PostgreSQL, Redis, worker.
- Alembic migrations for schema changes.
- Seed data for demo company.

## CI/CD
Pipeline stages:
1. Install dependencies.
2. Run formatting and linting.
3. Run unit tests.
4. Run integration tests with PostgreSQL service.
5. Build Docker image.
6. Scan dependencies and image.
7. Push image.
8. Deploy to staging.
9. Run smoke tests.
10. Promote to production.

## Azure deployment option
- Azure Container Apps or App Service for API.
- Azure Database for PostgreSQL Flexible Server.
- Azure Cache for Redis.
- Azure Blob Storage for attachments.
- Azure Key Vault for secrets.
- Application Insights for logs/metrics.

## AWS deployment option
- ECS Fargate for API and worker.
- RDS PostgreSQL.
- ElastiCache Redis.
- S3 for attachments.
- Secrets Manager.
- CloudWatch.

## Render deployment option
- Web Service for API.
- Background Worker for Celery.
- Managed PostgreSQL and Redis.
- External object storage for production attachments.

## Production readiness
- Run migrations on deployment.
- Health endpoint and readiness checks.
- Blue/green or rolling deployments.
- Backup and restore procedures.
- Observability dashboards and alerts.

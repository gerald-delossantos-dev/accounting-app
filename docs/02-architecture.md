# Software Architecture

## Recommended stack
- Backend: Python 3.14, FastAPI, SQLAlchemy 2, Alembic, Pydantic v2, Celery, Redis, PostgreSQL.
- Frontend: Next.js/React with TypeScript, reusable components, responsive layouts, dark/light mode.
- Storage: local for dev, S3/Azure Blob in production.
- Deployment: Docker, Azure Container Apps/App Service, AWS ECS/Fargate, or Render.

## Clean architecture layers
- API layer: FastAPI routers, auth dependencies, request/response mapping.
- Application layer: use cases/services, accounting workflow orchestration.
- Domain layer: entities, enums, accounting invariants, domain exceptions.
- Infrastructure layer: SQLAlchemy repositories, file storage, email, workers.
- Cross-cutting: logging, audit, validation, permissions, metrics.

## Backend folder structure
```text
backend/app
  api/v1/                 # Routes/controllers
  core/                   # config, auth, security, logging, permissions
  domain/                 # entities, enums, value objects, rules
  schemas/                # Pydantic DTOs
  services/               # use cases and accounting workflows
  repositories/           # data access abstractions and SQLAlchemy implementations
  db/                     # session, migrations, seed data
  workers/                # Celery app and tasks
  utils/                  # helpers
  main.py
```

## Key design choices
- Use UUID primary keys to support distributed systems and safe public identifiers.
- Store money as `NUMERIC(18,2)` or currency-specific precision, never float.
- Enforce journal balancing in both Pydantic validation and service layer.
- Use append-only audit logs for posted financial records.
- Use soft delete for master data, but do not hard-delete posted financial transactions.
- Use background jobs for PDF generation, recurring invoices, emails, report exports, and reminders.

## Error handling
- 400: malformed business request.
- 401: unauthenticated.
- 403: authenticated but insufficient permission.
- 404: entity not found or inaccessible tenant.
- 409: duplicate number, locked period, stale version conflict.
- 422: validation/accounting rule failure.
- 500: unexpected error with correlation ID.

## Logging and monitoring
- Structured JSON logs with request ID, user ID, company ID, route, latency, status code.
- Audit logs for financial operations and report exports.
- Metrics: request latency, DB pool use, failed logins, worker queue depth, report duration.

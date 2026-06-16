# LedgerPro SMB Accounting SaaS

Production-ready architecture starter for a Python accounting application for small businesses, freelancers, agencies, and service companies.

## Recommended current stack
- Python 3.14.x target runtime, using FastAPI, SQLAlchemy 2, Alembic, Pydantic v2, PostgreSQL 18.x-compatible SQL.
- Frontend scaffold: React/Next.js-style component plan. Replace with actual Next.js install when starting implementation.
- Docker Compose for API, PostgreSQL, Redis, and worker.

FastAPI provides automatic OpenAPI/Swagger docs and is built around Python type hints. PostgreSQL major versions are supported by the PostgreSQL project for five years, so production deployments should track a currently supported major version.

## Quick start
```bash
cp .env.example .env
docker compose up --build
# API: http://localhost:8000
# Swagger: http://localhost:8000/docs
```

## What is included
- Product requirements document
- Architecture document
- Database schema and constraints
- REST API specification
- UI/UX plan
- Accounting rules and workflows
- Security checklist
- Testing plan
- DevOps deployment plan
- Implementation roadmap
- Sample FastAPI modules, SQLAlchemy models, Pydantic schemas, services, repositories, seed data, tests, Docker, and CI workflow

## Important accounting note
This scaffold enforces core double-entry rules in application services and database constraints where practical. Before selling as accounting SaaS, have a licensed accountant review reports, tax treatment, localization, and compliance rules for each target country.

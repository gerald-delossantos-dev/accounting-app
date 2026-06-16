# Testing Plan

## Unit tests
- Pydantic validation for journal lines and invoices.
- Accounting service balancing, posting, reversing, locked period checks.
- Tax calculation and rounding.
- Payment allocation edge cases.

## Integration tests
- API endpoint tests with test PostgreSQL database.
- Tenant isolation checks.
- Invoice to journal posting flow.
- Bank CSV import and reconciliation.

## Security tests
- Unauthorized and cross-tenant access attempts.
- Rate limit behavior.
- Upload validation.
- RBAC permission matrix.

## Report tests
- P&L, balance sheet, trial balance, aging reports with known fixture data.
- Ensure trial balance debits equal credits.

## QA acceptance scenarios
- New company onboarding creates default chart of accounts.
- User creates invoice, sends PDF, receives partial payment, AR aging updates.
- User creates vendor bill, pays partially, AP aging updates.
- Accountant posts adjusting journal and locks period.
- Owner exports P&L and balance sheet.

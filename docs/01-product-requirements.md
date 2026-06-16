# Product Requirements Document

## Product vision
LedgerPro is a SaaS accounting platform for freelancers, agencies, service companies, and small to medium businesses. It provides invoicing, expenses, double-entry accounting, reports, bank reconciliation, taxes, audit trails, and role-based collaboration.

## Personas
- Business owner: wants revenue, cash, profit, invoice status, and tax readiness.
- Accountant: wants accurate ledgers, journal entries, auditability, locked periods, and financial statements.
- Bookkeeper: records bills, payments, expenses, receipts, and reconciliations.
- Viewer/investor: needs read-only reports and dashboards.

## Core modules
1. Dashboard: revenue, expenses, profit/loss, cash flow, A/R, A/P, recent transactions, health indicators, charts.
2. Company Setup: profile, tax, fiscal year, currency, numbering, payment terms, logo.
3. Chart of Accounts: account types, codes, hierarchy, active/inactive.
4. Double-entry Accounting: journals, general ledger, trial balance, posting, reversals, period locking.
5. Invoicing: draft/sent/paid/overdue/void, PDF, email, recurring.
6. Customers: profiles, addresses, credit limits, statements, payment history.
7. Payments Received: partial, overpayment, allocation, receipts.
8. Expenses/Vendor Bills: categories, attachments, recurring, billable, approvals.
9. Vendors/AP: vendor balances, bill due dates, aging.
10. AR: customer balances, aging, reminders.
11. Banking: accounts, transfers, CSV import, reconciliation.
12. Taxes: rates, VAT/GST/sales tax, reports, liability.
13. Reports: P&L, balance sheet, cash flow, trial balance, general ledger, aging, sales, expenses, tax, statements.
14. Inventory optional: products/services, stock, valuation, COGS.
15. Users/Permissions: RBAC and custom roles.
16. Audit Trail: immutable financial activity logs.
17. Attachments: secure file upload and metadata.
18. Notifications: overdue, due soon, recurring, reports.
19. Settings: company, users, accounting, tax, invoice templates, email, backup/export.

## SaaS monetization readiness
- Multi-tenant company model.
- Plans: Free, Solo, Business, Accountant, Enterprise.
- Usage limits: users, invoices/month, companies, storage, bank imports, reports.
- Billable add-ons: extra storage, advanced reports, inventory, multi-currency, accountant portal.

## Non-functional requirements
- Security: hashed passwords, JWT/session auth, RBAC, rate limiting, audit logging, secure uploads.
- Scalability: stateless API, background workers, read-optimized reports, indexes, async jobs.
- Availability: automated backups, health checks, deployment rollback, monitoring.
- Compliance: immutable audit logs, exportable records, locked periods, data retention settings.

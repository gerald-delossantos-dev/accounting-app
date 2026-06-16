# UI/UX Screen-by-Screen Plan

## Login page
Layout: centered auth card, brand logo, email/password, remember device, forgot password.
Actions: login, password reset, switch company after login.
Validation: required email, valid email format, password required.
States: loading spinner on submit, invalid credentials error, account locked warning.

## Dashboard
Layout: sidebar navigation, top company switcher, KPI cards, charts, recent transactions.
Components: revenue card, expense card, profit card, cash flow chart, AR/AP aging widgets, alerts.
Actions: create invoice, record expense, add payment, import bank CSV.
Empty state: checklist for company setup and chart of accounts.

## Chart of accounts
Layout: searchable hierarchical table with account type tabs.
Fields: code, name, type, normal balance, parent account, active.
Actions: create, edit, deactivate, export.
Validation: unique code per company; parent account compatible.

## General ledger
Layout: account selector, date range filters, ledger table, running balance.
Actions: export CSV/PDF, drill into journal source.
States: loading skeleton, no transactions message.

## Create journal entry
Layout: header details and editable debit/credit grid.
Fields: date, memo, account, description, debit, credit.
Validation: at least two lines, debits equal credits, locked period warning.
Actions: save draft, post, attach document.

## Invoice list
Layout: tabs by status, searchable table, aging badges.
Actions: create, send, mark paid, void, download PDF.
Empty state: CTA to create first invoice.

## Create invoice
Layout: customer selector, invoice metadata, line-item grid, totals panel.
Fields: customer, invoice date, due date, item, description, quantity, price, discount, tax.
Validation: positive amount, due date after invoice date, customer required.

## Customer profile
Layout: profile header, balance card, open invoices, payments, statement tab.
Actions: create invoice, receive payment, send statement.

## Vendor profile
Layout: vendor details, bills, payments, balance.
Actions: create bill, record payment, upload contract.

## Expense entry
Layout: simple form with receipt upload.
Fields: vendor/payee, date, category/account, amount, tax, billable, customer/project.
Validation: amount positive, receipt type/size valid.

## Bill entry
Layout: vendor selector and bill line grid.
Actions: save draft, approve, schedule payment.

## Bank reconciliation
Layout: bank statement side and ledger transactions side.
Actions: match, create adjustment, mark reconciled.
Validation: statement ending balance must equal cleared balance.

## Reports page
Layout: report gallery cards and favorites.
Actions: run, save preset, export PDF/CSV, schedule email.
States: background generation progress.

## Settings page
Layout: vertical sections for company, tax, invoice templates, email, backup/export.
Validation: tax rates cannot be deleted if used; fiscal changes require admin.

## User management
Layout: users table, role badges, permission drawer.
Actions: invite, disable, assign role, create custom role.
Validation: at least one active admin/owner per company.

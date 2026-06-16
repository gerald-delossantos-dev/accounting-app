# Database Schema Design

## Core tables
- companies: tenant/business entity.
- users: global user identities.
- company_users: membership and role per company.
- roles, permissions, role_permissions: custom RBAC.
- accounts: chart of accounts with parent-child hierarchy.
- accounting_periods: fiscal periods, lock status.
- journal_entries, journal_lines: double-entry ledger source of truth.
- customers, vendors: AR/AP counterparties.
- invoices, invoice_lines: sales invoices.
- payments_received, payment_allocations: customer payments and invoice allocation.
- bills, bill_lines, bill_payments: vendor bills and payment history.
- expenses: direct expenses and billable expenses.
- bank_accounts, bank_transactions, bank_reconciliations, reconciliation_lines.
- tax_rates, tax_groups, tax_group_lines, tax_transactions.
- products_services, inventory_movements for optional inventory.
- attachments: file metadata linked to entities.
- notifications: due/overdue/report events.
- audit_logs: immutable audit trail.
- settings: company/user preferences.

## Important constraints
- accounts: unique(company_id, code).
- journal_entries: unique(company_id, entry_no).
- journal_lines: debit >= 0, credit >= 0, not both debit and credit > 0.
- invoices: unique(company_id, invoice_no).
- payment_allocations: allocated_amount > 0.
- accounting_periods: no posting if locked.
- posted journals must never be physically deleted.

## Important indexes
- journal_entries(company_id, entry_date, status)
- journal_lines(account_id, journal_entry_id)
- invoices(company_id, status, due_date)
- bills(company_id, status, due_date)
- bank_transactions(company_id, bank_account_id, transaction_date)
- audit_logs(company_id, occurred_at DESC)
- attachments(company_id, entity_type, entity_id)

## Entity relationships
- Company has many users through company_users.
- Company has many accounts, journals, customers, vendors, invoices, bills, bank accounts.
- JournalEntry has many JournalLines.
- Invoice belongs to Customer and has many InvoiceLines.
- PaymentReceived can allocate to many Invoices through PaymentAllocation.
- Bill belongs to Vendor and has many BillLines.
- BankReconciliation groups BankTransactions and ledger matches.

## Double-entry validation
A journal is valid only when:
1. It has at least two lines.
2. Each line references an active account.
3. Each line has either debit or credit, not both.
4. Total debits equal total credits.
5. Entry date is not in a locked period.
6. Source document is valid and not voided.

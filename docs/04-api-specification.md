# REST API Design Specification

Base path: `/api/v1`

## Endpoint summary
| Module | Method | Route | Purpose |
|---|---:|---|---|
| Auth | POST | /auth/register | Create user account |
| Auth | POST | /auth/login | Issue access/refresh token |
| Auth | POST | /auth/refresh | Refresh access token |
| Auth | POST | /auth/logout | Revoke refresh token |
| Users | GET | /users | List company users |
| Users | POST | /users/invite | Invite user |
| Users | PATCH | /users/{id}/role | Update role |
| Companies | GET | /companies/{id} | Get company profile |
| Companies | PATCH | /companies/{id} | Update settings |
| Accounts | GET | /accounts | List chart of accounts |
| Accounts | POST | /accounts | Create account |
| Accounts | PATCH | /accounts/{id} | Update account |
| Journals | POST | /journal-entries | Create draft journal |
| Journals | POST | /journal-entries/{id}/post | Post journal |
| Journals | POST | /journal-entries/{id}/reverse | Reverse posted journal |
| Customers | GET/POST | /customers | List/create customers |
| Vendors | GET/POST | /vendors | List/create vendors |
| Invoices | GET/POST | /invoices | List/create invoices |
| Invoices | POST | /invoices/{id}/send | Email invoice |
| Invoices | POST | /invoices/{id}/void | Void invoice |
| Payments | POST | /payments-received | Record customer payment |
| Bills | GET/POST | /bills | List/create bills |
| Expenses | GET/POST | /expenses | List/create expenses |
| Banking | GET/POST | /bank-accounts | List/create bank accounts |
| Banking | POST | /bank-transactions/import-csv | Import CSV |
| Reconciliation | POST | /reconciliations | Start reconciliation |
| Reports | GET | /reports/profit-and-loss | P&L report |
| Reports | GET | /reports/balance-sheet | Balance sheet |
| Reports | GET | /reports/cash-flow | Cash flow |
| Taxes | GET/POST | /tax-rates | List/create tax rates |
| Attachments | POST | /attachments | Upload file |
| Settings | GET/PATCH | /settings/company | Company settings |

## Example: create journal entry
POST `/api/v1/journal-entries`
```json
{
  "company_id": "00000000-0000-0000-0000-000000000001",
  "entry_date": "2026-06-17",
  "memo": "Owner capital contribution",
  "lines": [
    {"account_id": "00000000-0000-0000-0000-000000000102", "debit": "50000.00", "credit": "0.00"},
    {"account_id": "00000000-0000-0000-0000-000000000301", "debit": "0.00", "credit": "50000.00"}
  ]
}
```
Response:
```json
{
  "id": "generated-uuid",
  "company_id": "00000000-0000-0000-0000-000000000001",
  "entry_no": "JE-000001",
  "entry_date": "2026-06-17",
  "memo": "Owner capital contribution",
  "status": "draft",
  "lines": []
}
```
Validation rules: at least two lines, one side per line, no negative amount, debit total equals credit total, active accounts only, unlocked period.

## Example: create invoice
POST `/api/v1/invoices`
```json
{
  "customer_id": "customer-uuid",
  "invoice_date": "2026-06-17",
  "due_date": "2026-07-17",
  "payment_terms": "Net 30",
  "lines": [
    {"description": "Website design package", "quantity": 1, "unit_price": "35000.00", "tax_rate_id": "tax-uuid"}
  ]
}
```
Response includes invoice number, subtotal, tax total, total, status `draft`.
Validation: due date >= invoice date, positive quantity and unit price, customer active, tax valid.

## Example: record payment
POST `/api/v1/payments-received`
```json
{
  "customer_id": "customer-uuid",
  "payment_date": "2026-06-20",
  "amount": "10000.00",
  "method": "bank_transfer",
  "deposit_account_id": "bank-account-uuid",
  "allocations": [
    {"invoice_id": "invoice-uuid", "amount": "10000.00"}
  ]
}
```
Validation: allocation total <= payment amount, invoice not void, company matches, overpayment tracked as customer credit.

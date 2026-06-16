-- Sample seed data. Use deterministic UUIDs in actual migrations/fixtures.
INSERT INTO companies (id, name, legal_name, base_currency, fiscal_year_start_month, created_at, updated_at)
VALUES ('00000000-0000-0000-0000-000000000001', 'Acme Creative Studio', 'Acme Creative Studio LLC', 'PHP', 1, now(), now());

INSERT INTO accounts (id, company_id, code, name, account_type, normal_balance, is_active, created_at, updated_at) VALUES
('00000000-0000-0000-0000-000000000101','00000000-0000-0000-0000-000000000001','1000','Cash on Hand','asset','debit',true,now(),now()),
('00000000-0000-0000-0000-000000000102','00000000-0000-0000-0000-000000000001','1010','Bank Account','asset','debit',true,now(),now()),
('00000000-0000-0000-0000-000000000103','00000000-0000-0000-0000-000000000001','1100','Accounts Receivable','asset','debit',true,now(),now()),
('00000000-0000-0000-0000-000000000201','00000000-0000-0000-0000-000000000001','2000','Accounts Payable','liability','credit',true,now(),now()),
('00000000-0000-0000-0000-000000000301','00000000-0000-0000-0000-000000000001','3000','Owner Equity','equity','credit',true,now(),now()),
('00000000-0000-0000-0000-000000000401','00000000-0000-0000-0000-000000000001','4000','Service Revenue','revenue','credit',true,now(),now()),
('00000000-0000-0000-0000-000000000501','00000000-0000-0000-0000-000000000001','5000','Software Subscriptions','expense','debit',true,now(),now());

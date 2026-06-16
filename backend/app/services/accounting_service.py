from decimal import Decimal
from sqlalchemy.orm import Session
from app.domain.models import JournalEntry, JournalLine
from app.domain.enums import JournalStatus
from app.schemas.journal import JournalEntryCreate

class AccountingError(Exception):
    pass

class AccountingService:
    def __init__(self, db: Session):
        self.db = db

    def create_journal_entry(self, payload: JournalEntryCreate) -> JournalEntry:
        debit_total = sum(line.debit for line in payload.lines)
        credit_total = sum(line.credit for line in payload.lines)
        if debit_total != credit_total:
            raise AccountingError("Debits and credits must be equal before posting.")
        entry = JournalEntry(
            company_id=payload.company_id,
            entry_no=self._next_entry_no(payload.company_id),
            entry_date=payload.entry_date,
            memo=payload.memo,
            status=JournalStatus.DRAFT,
        )
        for line in payload.lines:
            entry.lines.append(JournalLine(
                account_id=line.account_id,
                description=line.description,
                debit=line.debit,
                credit=line.credit,
            ))
        self.db.add(entry)
        self.db.commit()
        self.db.refresh(entry)
        return entry

    def post_journal_entry(self, entry: JournalEntry) -> JournalEntry:
        if entry.status != JournalStatus.DRAFT:
            raise AccountingError("Only draft entries can be posted.")
        debit_total: Decimal = sum((l.debit for l in entry.lines), Decimal("0.00"))
        credit_total: Decimal = sum((l.credit for l in entry.lines), Decimal("0.00"))
        if debit_total != credit_total:
            raise AccountingError("Cannot post an unbalanced journal entry.")
        entry.status = JournalStatus.POSTED
        self.db.commit()
        self.db.refresh(entry)
        return entry

    def _next_entry_no(self, company_id) -> str:
        # Replace with database sequence per company in production.
        return "JE-000001"

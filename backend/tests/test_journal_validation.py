from datetime import date
from decimal import Decimal
from uuid import uuid4
import pytest
from pydantic import ValidationError
from app.schemas.journal import JournalEntryCreate

def test_balanced_journal_entry_validates():
    payload = JournalEntryCreate(
        company_id=uuid4(),
        entry_date=date.today(),
        lines=[
            {"account_id": uuid4(), "debit": Decimal("100.00"), "credit": Decimal("0.00")},
            {"account_id": uuid4(), "debit": Decimal("0.00"), "credit": Decimal("100.00")},
        ],
    )
    assert sum(l.debit for l in payload.lines) == sum(l.credit for l in payload.lines)

def test_unbalanced_journal_entry_rejected():
    with pytest.raises(ValidationError):
        JournalEntryCreate(
            company_id=uuid4(),
            entry_date=date.today(),
            lines=[
                {"account_id": uuid4(), "debit": Decimal("100.00"), "credit": Decimal("0.00")},
                {"account_id": uuid4(), "debit": Decimal("0.00"), "credit": Decimal("90.00")},
            ],
        )

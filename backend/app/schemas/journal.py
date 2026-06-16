from datetime import date
from decimal import Decimal
from uuid import UUID
from pydantic import BaseModel, Field, model_validator

class JournalLineCreate(BaseModel):
    account_id: UUID
    description: str | None = None
    debit: Decimal = Field(default=Decimal("0.00"), ge=0)
    credit: Decimal = Field(default=Decimal("0.00"), ge=0)

    @model_validator(mode="after")
    def only_one_side(self):
        if self.debit > 0 and self.credit > 0:
            raise ValueError("A journal line cannot contain both debit and credit.")
        if self.debit == 0 and self.credit == 0:
            raise ValueError("A journal line must contain either debit or credit.")
        return self

class JournalEntryCreate(BaseModel):
    company_id: UUID
    entry_date: date
    memo: str | None = None
    lines: list[JournalLineCreate]

    @model_validator(mode="after")
    def must_balance(self):
        debit_total = sum(line.debit for line in self.lines)
        credit_total = sum(line.credit for line in self.lines)
        if len(self.lines) < 2:
            raise ValueError("A journal entry requires at least two lines.")
        if debit_total != credit_total:
            raise ValueError(f"Journal entry is not balanced: debits={debit_total}, credits={credit_total}.")
        return self

class JournalEntryRead(BaseModel):
    id: UUID
    company_id: UUID
    entry_no: str
    entry_date: date
    memo: str | None
    status: str
    lines: list[JournalLineCreate]
    model_config = {"from_attributes": True}

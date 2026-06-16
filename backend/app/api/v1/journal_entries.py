from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.journal import JournalEntryCreate, JournalEntryRead
from app.services.accounting_service import AccountingService, AccountingError
from app.domain.models import JournalEntry

router = APIRouter(prefix="/journal-entries", tags=["Journal Entries"])

@router.post("", response_model=JournalEntryRead, status_code=201)
def create_journal_entry(payload: JournalEntryCreate, db: Session = Depends(get_db)):
    try:
        return AccountingService(db).create_journal_entry(payload)
    except AccountingError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc

@router.post("/{entry_id}/post", response_model=JournalEntryRead)
def post_journal_entry(entry_id: UUID, db: Session = Depends(get_db)):
    entry = db.get(JournalEntry, entry_id)
    if not entry:
        raise HTTPException(status_code=404, detail="Journal entry not found")
    try:
        return AccountingService(db).post_journal_entry(entry)
    except AccountingError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc

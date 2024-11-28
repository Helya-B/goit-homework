from typing import List

from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.database.models import User
from src.schemas import ContactModel, ContactResponse
from src.repository import contacts as repository_contacts
from src.helpers.auth import get_current_user

router = APIRouter(prefix='/contacts', tags=["contacts"])

@router.get("/", response_model=List[ContactResponse])
async def read_contacts(current_user: User = Depends(get_current_user),
                        skip: int = 0,
                        limit: int = 100,
                        search: str | None = None,
                        with_close_bithdate: bool = False,
                        db: Session = Depends(get_db)):
    contacts = await repository_contacts.get_contacts(current_user.id, skip, limit, search, with_close_bithdate, db)
    return contacts


@router.get("/{contact_id}", response_model=ContactResponse)
async def read_contact( contact_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    contact = await repository_contacts.get_contact(current_user.id, contact_id, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact


@router.post("/", response_model=ContactResponse)
async def create_contact(body: ContactModel,
                         current_user: User = Depends(get_current_user),
                         db: Session = Depends(get_db)):
    return await repository_contacts.create_contact(current_user.id, body, db)


@router.put("/{contact_id}", response_model=ContactResponse)
async def update_contact(body: ContactModel,
                         contact_id: int,
                         current_user: User = Depends(get_current_user),
                         db: Session = Depends(get_db)):
    contact = await repository_contacts.update_contact(current_user.id, contact_id, body, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact


@router.delete("/{contact_id}", response_model=ContactResponse)
async def remove_contact(contact_id: int,
                         current_user: User = Depends(get_current_user),
                         db: Session = Depends(get_db)):
    contact = await repository_contacts.remove_contact(current_user.id, contact_id, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="contact not found")
    return contact

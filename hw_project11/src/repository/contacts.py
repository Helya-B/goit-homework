import datetime
from typing import List

from sqlalchemy.orm import Session
from sqlalchemy import or_, between

from src.database.models import Contact
from src.schemas import ContactModel


async def get_contacts(skip: int, limit: int, search: str | None, with_close_bithdate: bool, db: Session) -> List[
    Contact]:
    query = db.query(Contact)

    if search:
        query = query.filter(or_(Contact.name.ilike(f"%{search}%"),
                                 Contact.email.ilike(f"%{search}%"),
                                 Contact.phone.ilike(f"%{search}%")))

    if with_close_bithdate:
        query = query.filter(
            between(Contact.birthdate, datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(days=7)))

    return query.offset(skip).limit(limit).all()


async def get_contact(contact_id: int, db: Session) -> Contact:
    return db.query(Contact).filter(Contact.id == contact_id).first()


async def create_contact(body: ContactModel, db: Session) -> Contact:
    contact = Contact(
        name=body.name,
        email=body.email,
        phone=body.phone,
        birthdate=body.birthdate
    )
    contact.created_at = datetime.datetime.now()
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def update_contact(contact_id: int, body: ContactModel, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        contact.name = body.name
        contact.email = body.email
        contact.phone = body.phone
        contact.birthdate = body.birthdate
        db.commit()
    return contact


async def remove_contact(contact_id: int, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact

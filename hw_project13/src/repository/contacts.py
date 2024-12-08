import datetime
from typing import List

from sqlalchemy.orm import Session
from sqlalchemy import or_, between, and_

from src.database.models import Contact
from src.schemas import ContactModel


async def get_contacts(current_user_id: int, skip: int, limit: int, search: str | None, with_close_bithdate: bool,
                       db: Session) -> List[Contact]:
    """
       Retrieves a list of contacts for a specific user with specified pagination parameters.

       :param current_user_id: The ID of the user to retrieve contacts for.
       :type current_user_id: int
       :param skip: The number of notes to skip.
       :type skip: int
       :param limit: The maximum number of notes to return.
       :type limit: int
       :param search: The search query to filter notes by.
       :type search: str | None
       :param with_close_bithdate: Whether to filter notes by close birthdate.
       :type with_close_bithdate: bool
       :return: A list of Conctacts.
       :rtype: List[Contact]
       """
    query = db.query(Contact)

    query = query.filter(Contact.user_id == current_user_id)

    if search:
        query = query.filter(or_(Contact.name.ilike(f"%{search}%"),
                                 Contact.email.ilike(f"%{search}%"),
                                 Contact.phone.ilike(f"%{search}%")))

    if with_close_bithdate:
        query = query.filter(
            between(Contact.birthdate, datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(days=7)))

    return query.offset(skip).limit(limit).all()


async def get_contact(current_user_id, contact_id: int, db: Session) -> Contact:
    """
       Retrieves a single note with the specified ID for a specific user.

       :param contact_id: The ID of the note to retrieve.
       :type contact_id: int
       :param user: The user to retrieve the note for.
       :type user: User
       :param db: The database session.
       :type db: Session
       :return: The note with the specified ID, or None if it does not exist.
       :rtype: Note | None
       """

    return db.query(Contact).filter(and_(Contact.id == contact_id, Contact.user_id == current_user_id)).first()


async def create_contact(current_user_id: int, body: ContactModel, db: Session) -> Contact:
    """
       Creates a new note for a specific user.

       :param body: The data for the note to create.
       :type body: NoteModel
       :param user: The user to create the note for.
       :type user: User
       :param db: The database session.
       :type db: Session
       :return: The newly created note.
       :rtype: Note
       """
    contact = Contact(
        name=body.name,
        email=body.email,
        phone=body.phone,
        birthdate=body.birthdate,
        user_id=current_user_id
    )
    contact.created_at = datetime.datetime.now()
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def update_contact(current_user_id: int, contact_id: int, body: ContactModel, db: Session) -> Contact | None:
    """
       Updates a single note with the specified ID for a specific user.

       :param contact_id: The ID of the note to update.
       :type contact_id: int
       :param body: The updated data for the note.
       :type body: NoteUpdate
       :param user: The user to update the note for.
       :type user: User
       :param db: The database session.
       :type db: Session
       :return: The updated note, or None if it does not exist.
       :rtype: Note | None
       """
    contact = db.query(Contact).filter(and_(Contact.id == contact_id, Contact.user_id == current_user_id)).first()
    if contact:
        contact.name = body.name
        contact.email = body.email
        contact.phone = body.phone
        contact.birthdate = body.birthdate
        db.commit()
    return contact


async def remove_contact(current_user_id: int, contact_id: int, db: Session) -> Contact | None:
    """
      Removes a single note with the specified ID for a specific user.

      :param contact_id: The ID of the note to remove.
      :type contact_id: int
      :param contact_id: The user to remove the note for.
      :type contact_id: User
      :param db: The database session.
      :type db: Session
      :return: The removed note, or None if it does not exist.
      :rtype: Note | None
      """
    contact = db.query(Contact).filter(and_(Contact.id == contact_id, Contact.user_id == current_user_id)).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact

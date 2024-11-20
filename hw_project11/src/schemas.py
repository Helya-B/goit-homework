from datetime import datetime
from pydantic import BaseModel, Field


class ContactModel(BaseModel):
    name: str = Field(max_length=150)
    email: str = Field(max_length=100)
    phone: str = Field(max_length=12)
    birthdate: datetime


class ContactResponse(ContactModel):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

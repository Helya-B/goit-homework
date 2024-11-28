from sqlalchemy import Column, Integer, String, func, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.orm import mapped_column

Base = declarative_base()

class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(12), nullable=False)
    user_id = mapped_column(ForeignKey("users.id"))
    birthdate = Column('birthdate', DateTime, default=func.now())
    created_at = Column('created_at', DateTime, default=func.now())


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False)
    password = Column(String(100), nullable=False)
    created_at = Column('created_at', DateTime, default=func.now())
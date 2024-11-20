from sqlalchemy import Column, Integer, String, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()

class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(12), nullable=False)
    birthdate = Column('birthdate', DateTime, default=func.now())
    created_at = Column('created_at', DateTime, default=func.now())

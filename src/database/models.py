from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey, \
    Boolean
from sqlalchemy.orm import relationship

from .db import engine, Base


class Contact(Base):

    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    phone_number = Column(String)
    birthday = Column(DateTime, nullable=True)
    additional_data = Column(String, nullable=True)
    user_id = Column(
        'user_id',
        ForeignKey('users.id', ondelete='CASCADE'),
        default=None
    )
    user = relationship('User', backref="contacts")


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    created_at = Column('crated_at', DateTime, default=func.now())
    refresh_token = Column(String(255), nullable=True)
    confirmed = Column(Boolean, default=False)
    avatar = Column(String(255), nullable=True)


Base.metadata.create_all(bind=engine)
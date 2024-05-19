from sqlalchemy import Column, String, Integer, Boolean, ARRAY, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.types import UUID, JSON
from uuid import uuid4


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    email = Column(String(255), unique=True, index=True, nullable=False)
    first_name = Column(String(30), nullable=True)
    last_name = Column(String(30), nullable=True)
    location = Column(String(100), nullable=True)
    is_premium = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)
    password_hash = Column(String, nullable=False)

    dogs = relationship("Dog", back_populates="owner", cascade='save-update, merge, delete')
    feed_filter = relationship("Feed", back_populates="user", uselist=False, cascade='save-update, merge, delete')

class Dog(Base):
    __tablename__ = 'dog'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    photo_url = Column(String(100), nullable=False)
    sex = Column(String(50), nullable=False) 
    age = Column(Integer, nullable=False)
    breed = Column(String(50), nullable=False)
    tags = Column(ARRAY(String), nullable=True)
    description = Column(String(500), nullable=True)

    owner_id = Column(UUID(as_uuid=True), ForeignKey('user.id'))
    owner = relationship("User", back_populates="dogs")

class Feed(Base):
    __tablename__ = 'feed'
    id = Column(Integer, primary_key=True)
    current_filter = Column(JSON, nullable=True)
    total_cards = Column(Integer, default=0)
    current_card = Column(Integer, default=0)
    history = Column(ARRAY(Integer), nullable=True)

    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id'))
    user = relationship("User", back_populates="feed_filter")

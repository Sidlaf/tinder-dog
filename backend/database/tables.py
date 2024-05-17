from sqlalchemy import ForeignKey
from datetime import datetime
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy import String
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

Base = declarative_base()

class User(Base):
     __tablename__ = 'user'

     id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
     email: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
     email_validated: Mapped[bool] = mapped_column(default=False)
     first_name: Mapped[str] = mapped_column(String(30))
     last_name: Mapped[str] = mapped_column(String(30))
     location: Mapped[str] = mapped_column(String(30))
     is_active: Mapped[bool] = mapped_column(default=True)
     refresh_tokens: Mapped[list["Token"]] = relationship(
     foreign_keys="[token.authenticates_id]", back_populates="authenticates", lazy="dynamic"
     )
     registered_at: Mapped[str] = mapped_column(default=datetime.now, nullable=False)
     dogs: Mapped[list["Dog"]] = mapped_column(ForeignKey("dog.id"))


class Dog(Base):
     __tablename__ = 'dog'

     id: Mapped[int] = mapped_column(primary_key=True)
     name: Mapped[str] = mapped_column(String(30))
     photo_url: Mapped[str] = mapped_column(String(100), nullable=False)
     is_male: Mapped[bool] = mapped_column(nullable=False)
     age: Mapped[int] = mapped_column(nullable=False)
     breed: Mapped[str] = mapped_column(String(30), nullable=False)
     tags: Mapped[list[str]] = mapped_column(String(30), nullable=True)
     description: Mapped[str] = mapped_column(String(500), nullable=True)
     is_premium: Mapped[bool] = mapped_column(default=False)


class Token(Base):                                                                                                                                                                                                     
     __tablename__ = 'token'

     token: Mapped[str] = mapped_column(primary_key=True, index=True)
     authenticates_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("user.id"))
     authenticates: Mapped["User"] = relationship(back_populates="refresh_tokens")

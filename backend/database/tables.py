from sqlalchemy import (ForeignKey)
from datetime import datetime
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy import String
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

class Base(DeclarativeBase):
     pass

class User(Base):
    __tablename__ = 'user'

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    email: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    email_validated: Mapped[bool] = mapped_column(default=False)
#     username: Mapped[str] = mapped_column(String(32),nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True)
    refresh_tokens: Mapped[list["Token"]] = relationship(
        foreign_keys="[Token.authenticates_id]", back_populates="authenticates", lazy="dynamic"
    )
    registered_at: Mapped[str] = mapped_column(default=datetime.now, nullable=False)

class Token(Base):

    token: Mapped[str] = mapped_column(primary_key=True, index=True)
    authenticates_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("user.id"))
    authenticates: Mapped["User"] = relationship(back_populates="refresh_tokens")
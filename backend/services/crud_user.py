from typing import Any, Optional
from schemas.user import UserCreate, User
from database import tables
from database.db import get_session
from sqlalchemy.orm import Session
from fastapi import Depends
from sqlalchemy.orm import Session



def get_by_id(session: Session, id: Any):
    return session.query(User).filter(User.id == id).first()

def get_by_email(session: Session, email: str) -> Optional[User]:
    return session.query(User).filter(User.email == email).first()

def create(session: Session, obj_in: UserCreate) -> User:
    db_obj = User(
        email=obj_in.email,
    )
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj

def is_active(user: User) -> bool:
    return user.is_active

def validate_email(self, session: Session, db_obj: User) -> User:
    setattr(db_obj, "email_validated", True)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj

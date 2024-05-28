from sqlalchemy.orm import Session
from schemas.user import UserCreate, User
from schemas.token import Token, RefreshTokenCreate
from database import tables



def create(self, session: Session, *, obj_in: str, user_obj: User) -> Token:
        db_obj = session.query(tables.Token).filter(tables.Token.token == obj_in).first()
        if db_obj and db_obj.authenticates != user_obj:
            raise ValueError("Token mismatch between key and user.")
        obj_in = RefreshTokenCreate(**{"token": obj_in, "authenticates_id": user_obj.id})
        db_obj = obj_in
        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return db_obj
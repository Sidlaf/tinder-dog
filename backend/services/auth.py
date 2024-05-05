import crud_user
import crud_token
import security
import email_service
from schemas.user import UserCreate, User
from database.db import get_session
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from schemas.token import WebToken, Token
from typing import Annotated
from deps import get_magic_token

class AuthService:
    def __init__(self,session: Session = Depends(get_session)):
        self.session = session

    def login_with_magic_link(self, email:str):
        user = crud_user.get_by_email(self.session, email=email)
        if not user:
            user_in = UserCreate(**{"email": email})
            user = crud_user.create(self.session, obj_in=user_in)
        if not crud_user.is_active(user):
            raise HTTPException(status_code=400, detail="A link to activate your account has been emailed.")
        tokens = security.create_magic_tokens(subject=user.id)
        if user.email:
            email_service.send_magic_login_email(email_to=user.email, token=tokens[0])
        return {"claim": tokens[1]}
    
    def validate_magic_link(self, obj_in, magic_in):
        claim_in = get_magic_token(token=obj_in.claim)

        user = crud_user.get_by_id(self.session, id=magic_in.sub)
        if (
            (claim_in.sub == magic_in.sub)
            or (claim_in.fingerprint != magic_in.fingerprint)
            or not user
            or not crud_user.is_active(user)
        ):
            raise HTTPException(status_code=400, detail="Login failed; invalid claim.")

        if not user.email_validated:
            crud_user.validate_email(self.session, db_obj=user)
            refresh_token = security.create_refresh_token(subject=user.id)
            crud_token.create(self.session, obj_in=refresh_token, user_obj=user)
        return {
            "access_token": security.create_access_token(subject=user.id),
            "refresh_token": refresh_token,
            "token_type": "bearer",
        }
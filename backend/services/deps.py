from typing import Generator, Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from schemas.user import UserCreate, User
from sqlalchemy.orm import Session

from schemas.token import MagicTokenPayload
import config


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_magic_token(token: Annotated[str, Depends(oauth2_scheme)]) -> MagicTokenPayload:
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[config.JWT_ALGORITHM])
        token_data = MagicTokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    return token_data

def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    return 

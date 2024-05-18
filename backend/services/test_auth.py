from datetime import datetime, timedelta
from passlib.hash import bcrypt
from jose import jwt, JWTError

from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from schemas.auth import User, Token, UserCreate

from database import tables, db
from sqlalchemy.orm import Session


def validate(token: str) -> User:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentionals",
            headers={'WWW-Authenticate': 'Bearer'},
        )
        try:
            payload = jwt.decode(
                token,
                'secret',
                algorithms=['HS256'],
            )
        except JWTError:
            raise exception from None

        user_data = payload.get('user')

        try:
            user = User.parse_obj(user_data)
        except ValueError:
            raise exception from None

        return user
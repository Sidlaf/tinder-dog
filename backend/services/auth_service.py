from datetime import datetime, timedelta, timezone
from passlib.hash import bcrypt
from jose import jwt, JWTError

from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from schemas.user import BaseUser
from schemas.token import Token

from database import tables, db
from schemas.user import User
from sqlalchemy.orm import Session

from config import SECRET_KEY, JWT_ALGORITHM, ACCESS_TOKEN_EXPIRE_SECONDS


class Auth:

    @classmethod
    def verify_password(cls, plain_passwd: str, hashed_passwd: str) -> bool:
        return bcrypt.verify(plain_passwd, hashed_passwd)

    @classmethod
    def hash_password(cls, password: str) -> str:
        return bcrypt.hash(password)

    @classmethod
    def validate(cls, token: str) -> BaseUser:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentionals",
            headers={'WWW-Authenticate': 'Bearer'},
        )
        try:
            payload = jwt.decode(
                token,
                SECRET_KEY,
                JWT_ALGORITHM,
            )
        except JWTError:
            raise exception from None

        try:
            email = payload.get('email')
        except ValueError:    
            raise exception from None

        return email

    def create_token(cls, user: tables.User) -> Token:

        now = datetime.now(timezone.utc)
        payload = {
            "iat": now, # время выпуска токена
            "nbf": now, # начало его действия
            "exp": now + timedelta(minutes=ACCESS_TOKEN_EXPIRE_SECONDS), # время истечения токена
            'email': user.email
        }
        token = jwt.encode(
            payload,
            SECRET_KEY,
            algorithm=JWT_ALGORITHM,
        )
        return Token(access_token=token)

    #Работа с БД
    def __init__(self,session: Session = Depends(db.get_session)):
        self.session = session

    def register_user(self, user_data: BaseUser) -> Token:
        exception_email = HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="This email is already registered",
            headers={'WWW-Authenticate': 'Bearer'},
        )
        exception_password = HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Passwords do not match!",
            headers={'WWW-Authenticate': 'Bearer'},
        )
        check_email = (
            self.session
            .query(tables.User)
            .filter(tables.User.email == user_data.email)
            .first()
        )
        if (user_data.password != user_data.password_confirmation):
            raise exception_password

        if check_email:
            raise exception_email


        user = tables.User(
            email=user_data.email,
            password_hash = self.hash_password(user_data.password),
        )

        self.session.add(user)
        self.session.commit()

        return self.create_token(user)

    def login_user(self, email: str, password: str) -> Token:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={'WWW-Authenticate': 'Bearer'},
        )
        user = (
            self.session
            .query(tables.User)
            .filter(tables.User.email == email)
            .first()
        )

        if not user:
            raise exception

        if not self.verify_password(password, user.password_hash):
            raise exception

        return self.create_token(user)

#Связующая функция, которая читает токен из header и валидирует его
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def get_current_user(token: str = Depends(oauth2_scheme)) -> tables.User:
    email = Auth.validate(token)

    session = db.session_maker()

    exception = HTTPException(
        status_code=status.HTTP_204_NO_CONTENT,
        detail="User not found",
    )
    user = (
        session
        .query(tables.User)
        .filter(tables.User.email == email)
        .first()
    )
    if not user:
        raise exception
    
    return user
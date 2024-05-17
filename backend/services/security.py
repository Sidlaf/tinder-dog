from datetime import datetime, timedelta
from typing import Any, Union, Optional
from config import ACCESS_TOKEN_EXPIRE_SECONDS, REFRESH_TOKEN_EXPIRE_SECONDS, SECRET_KEY, JWT_ALGORITHM
from jose import jwt
# from passlib.context import CryptContext
# from passlib.totp import TOTP
# from passlib.exc import TokenError, MalformedTokenError
import uuid

def create_magic_tokens(*, subject: Union[str, Any], expires_delta: timedelta = None) -> list[str]:
    if expires_delta:
        expire = datetime.now(datetime.UTC) + expires_delta
    else:
        expire = datetime.now(datetime.UTC) + timedelta(seconds=ACCESS_TOKEN_EXPIRE_SECONDS)
    fingerprint = str(uuid.uuid4())
    magic_tokens = []
    for sub in [subject, uuid.uuid4()]:
        to_encode = {"exp": expire, "sub": str(sub), "fingerprint": fingerprint}
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=JWT_ALGORITHM)
        magic_tokens.append(encoded_jwt)
    return magic_tokens

def create_refresh_token(*, subject: Union[str, Any], expires_delta: timedelta = None) -> str:
    if expires_delta:
        expire = datetime.now(datetime.UTC) + expires_delta
    else:
        expire = datetime.now(datetime.UTC) + timedelta(seconds=REFRESH_TOKEN_EXPIRE_SECONDS)
    to_encode = {"exp": expire, "sub": str(subject), "refresh": True}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=JWT_ALGORITHM)
    return encoded_jwt

def create_access_token(*, subject: Union[str, Any], expires_delta: timedelta = None, force_totp: bool = False) -> str:
    if expires_delta:
        expire = datetime.now(datetime.UTC) + expires_delta
    else:
        expire = datetime.now(datetime.UTC) + timedelta(seconds=ACCESS_TOKEN_EXPIRE_SECONDS)
    to_encode = {"exp": expire, "sub": str(subject), "totp": force_totp}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=JWT_ALGORITHM)
    return encoded_jwt
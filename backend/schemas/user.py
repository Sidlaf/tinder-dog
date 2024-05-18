from typing import Optional
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    location: str

class UserUpdate(UserCreate):
    pass

class User(UserCreate):
    email: EmailStr

class UserExtra(UserCreate):
    is_premium: bool
    dogs: Optional[list[str]]
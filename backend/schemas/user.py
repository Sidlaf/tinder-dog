from typing import Optional
from pydantic import BaseModel, EmailStr, Field, json

class BaseUser(BaseModel):
    email: EmailStr
    password: str
    password_confirmation: str

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    location: str

class UserUpdate(BaseModel):
    first_name: Optional[str] = Field(None)
    last_name: Optional[str] = Field(None)
    location: Optional[str] = Field(None)

class User(UserCreate):
    email: EmailStr

class UserExtra(UserCreate):
    is_premium: bool
    dogs: Optional[list[str]]

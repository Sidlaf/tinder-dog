from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr
from typing_extensions import Annotated

class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    email_validated: Optional[bool] = False

class User(BaseModel):
    first_name: str
    last_name: str
    location: str

class UserUpdate(User):
    pass
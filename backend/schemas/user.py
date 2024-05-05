from typing import Optional
from uuid import UUID
from pydantic import field_validator, StringConstraints, ConfigDict, BaseModel, Field, EmailStr
from typing_extensions import Annotated

class UserBase(BaseModel):
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    full_name: Optional[str] = None

class UserCreate(UserBase):
    email: EmailStr
    email_validated: Optional[bool] = False

class User(UserCreate):
    pass
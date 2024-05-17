from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel, EmailStr
from typing_extensions import Annotated

class DogBase(BaseModel):
    name: str
    is_male: bool
    age: int
    breed: str
    tags: List[str]
    photo_url: str

class Dog(DogBase):
    description: str
    is_premium: bool

class DogCreate(DogBase):
    pass
class DogUpdate(Dog):
    pass
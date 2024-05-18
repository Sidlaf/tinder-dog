from pydantic import BaseModel
from typing import Optional
from enum import Enum


class DogCreate(BaseModel):
    name: str
    sex: str
    age: int
    breed: str
    tags: Optional[list[str]]
    description: Optional[str]

class DogUpdate(DogCreate):
    pass

class Dog(DogCreate):
    photo_url: str
    is_premium: bool

class Tag(str, Enum):
    PASSPORT = "Паспорт"
    VACCINATION = "Сделаны прививки"

class Breed(str, Enum):
    AKITA = "Акита"
    HUSKY = "Хаски"

class Sex(str, Enum):
    MALE = "Самец"
    FEMALE = "Самка"

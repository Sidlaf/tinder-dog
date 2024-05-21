from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class DogCreate(BaseModel):
    name: str
    sex: str
    age: int
    breed: str
    tags: Optional[str] = Field(None)
    description: Optional[str] = Field(None)

class DogUpdate(DogCreate):
    name: Optional[str] = Field(None)
    sex: Optional[str] = Field(None)
    age: Optional[str] = Field(None)
    breed: Optional[str] = Field(None)
    is_visible: Optional[str] = Field(None)

class Dog(DogCreate):
    photo_url: str
    is_premium: bool
    id: int

class Tag(str, Enum):
    PASSPORT = "Паспорт"
    VACCINATION = "Сделаны прививки"

class Breed(str, Enum):
    AKITA = "Акита"
    HUSKY = "Хаски"
    LABRADOR = "Лабрадор"

class Sex(str, Enum):
    MALE = "Самец"
    FEMALE = "Самка"

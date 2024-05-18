from fastapi import APIRouter, Depends
from services import email_service
from fastapi_filter import FilterDepends
from services.feed import DogFilter
from database.db import get_session
from sqlalchemy.orm import Session
from database import tables
from sqlalchemy import select
from schemas.dog import Dog
import json


router = APIRouter(
    prefix='/tester',
    tags=['Проверка'],
    )

@router.get('/feed', response_model=list[Dog])
def list_dog(dog_filters: DogFilter = FilterDepends(DogFilter), 
    session: Session = Depends(get_session)):

    query = dog_filters.filter(select(tables.Dog).outerjoin(tables.User))
    model = dog_filters.model_dump_json()
    a = DogFilter(**json.loads(model))
    query1 = a.filter(select(tables.Dog).outerjoin(tables.User))
    result = session.execute(query1)
    return result.scalars().all()

@router.post('/email')
def post_email(
    recipient: str):

    return email_service.send_magic_login_email(recipient)

@router.post('/premium{email}')
def give_premium(
    email: str):
    
    pass
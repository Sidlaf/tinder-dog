from fastapi import APIRouter, Depends, UploadFile
from services import email_service
from fastapi_filter import FilterDepends
from services.feed import DogFilter
from database.db import get_session
from sqlalchemy.orm import Session
from database import tables
from sqlalchemy import select
from schemas.dog import Dog
import json

from services.auth_service import get_current_user
from services.profile import DogService
from schemas.user import  User

router = APIRouter(
    prefix='/tester',
    tags=['Проверка'],
    )

@router.get('/me')
def get_user(
    user: str = Depends(get_current_user)):
    return user

@router.post('/photo')
def test_photo_upload(
    photo_file: UploadFile,
    photo_service: DogService = Depends()):
    return photo_service.test_photo_upload(photo_file)

@router.get('/feed')
def list_dog(dog_filters: DogFilter = FilterDepends(DogFilter), 
    session: Session = Depends(get_session)):

    query = dog_filters.filter(select(tables.Dog).outerjoin(tables.User))
    result = session.execute(query)
    return result.scalars().all()

@router.post('/email')
def post_email(
    recipient: str):

    return email_service.send_magic_login_email(recipient)

@router.post('/premium{email}')
def give_premium(
    email: str):
    pass
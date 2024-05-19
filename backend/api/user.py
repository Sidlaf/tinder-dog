from fastapi import APIRouter, Depends, status
from services.auth_service import get_current_user
from services.user import UserService
from schemas.user import UserCreate, UserUpdate, User
from database import tables

from typing import Optional

router = APIRouter(
    prefix='/user',
    tags=['Профиль пользователя'],
    )

@router.get('/me')
def get_profile(
    user_service: UserService = Depends(),
    user: tables.User = Depends(get_current_user)):
    return user_service.get_profile(user)

@router.post('/create')
def create_profile(
    user_data: UserCreate = Depends(),
    user_service: UserService = Depends(),
    user: tables.User = Depends(get_current_user)):
    return user_service.create_profile(user_data, user)

@router.put('/update')
def update_profile(
    user_data: UserUpdate = Depends(),
    user_service: UserService = Depends(),
    user: tables.User = Depends(get_current_user)):
    return user_service.update_profile(user_data, user)

@router.delete('/delete', status_code=status.HTTP_204_NO_CONTENT)
def delete_profile(
    user_service: UserService = Depends(),
    user: tables.User = Depends(get_current_user)):
    return user_service.delete_profile(user)


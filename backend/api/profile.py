from fastapi import APIRouter, Depends, UploadFile
from services.profile import ProfileService
from schemas.user import UserCreate

router = APIRouter(
    tags=['Загрузка фото'],
    )

@router.post('/profile', status_code=201)
def add_photos(
    file: UploadFile,
    profile_service: ProfileService = Depends()
):
    return profile_service.upload_photo(file)

@router.post('/create', status_code=201)
def create_user(
    user_data: UserCreate,
    profile_service: ProfileService = Depends()
):
    return profile_service.create_user(user_data)
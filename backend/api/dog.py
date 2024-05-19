from fastapi import APIRouter, Depends, UploadFile, File, status
from services.auth_service import get_current_user
from schemas.dog import Dog, DogCreate, DogUpdate
from schemas.user import User
from services.profile import DogService
from typing import Optional

router = APIRouter(
    prefix='/dog',
    tags=['Анкета питомца'],
    )

@router.post('/create')
def create_dog(
    photo_file: UploadFile,
    dog_data: DogCreate =  Depends(),
    dog_service: DogService =  Depends(),
    user: User = Depends(get_current_user)):
    return dog_service.create_dog(user, dog_data, photo_file)

@router.get('/my')
def get_my_dogs(
    dog_service: DogService =  Depends(),
    user: User = Depends(get_current_user)):
    return dog_service.get_my_dogs(user)

@router.get('/id{id}')
def get_dog_info(
    id: int,
    dog_service: DogService =  Depends()):
    return dog_service.get_dog_by_id(id)

@router.put('/id{id}', response_model=Dog)
def update_my_dog(
    id: int,
    photo_file: UploadFile = None,
    dog_data: DogUpdate = Depends(),
    dog_service: DogService =  Depends(),
    user: User = Depends(get_current_user)):
    return dog_service.update_my_dog(user, id, dog_data, photo_file)

@router.delete('/id{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_dog(
    id: int,
    dog_service: DogService = Depends(),
    user: User = Depends(get_current_user)):
    return dog_service.delete_dog(user, id)

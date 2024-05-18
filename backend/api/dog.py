from fastapi import APIRouter, Depends, UploadFile, File, status
from services.deps import get_current_user
from schemas.dog import Dog, DogCreate
from schemas.user import User
from typing import Optional

router = APIRouter(
    prefix='/dog',
    tags=['Анкета питомца'],
    )

@router.post('/', response_model=Dog, status_code=status.HTTP_201_CREATED)
def create_dog(
    dog_data: DogCreate,
    photo_file: UploadFile,
    user: User = Depends(get_current_user)):
    pass

@router.get('/id{id}', response_model=Dog)
def get_dog_info(
    id: int,
    user: User = Depends(get_current_user)):
    pass

@router.put('/id{id}', response_model=Dog)
def update_dog(
    id: int,
    photo_file: Optional[UploadFile] = File(default=None),
    user: User = Depends(get_current_user)):
    pass

@router.delete('/id{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_dog(
    id: int,
    user: User = Depends(get_current_user)):
    pass

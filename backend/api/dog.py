from fastapi import APIRouter, Depends, UploadFile
from services.profile import ProfileService
from schemas.user import UserCreate
from services.deps import get_current_user
from schemas.user import UserCreate, User
from schemas.dog import Dog, DogCreate

router = APIRouter(
    prefix='/dog',
    tags=['Анкета'],
    )

@router.get('/{id}', response_model=Dog)
def get_dog_info(
    user: User = Depends(get_current_user),
):
    pass

@router.post('/', response_model=DogCreate)
def create_dog(
    user: User = Depends(get_current_user),
):
    pass

@router.put('/{id}', response_model=Dog)
def update_dog_info(
    user: User = Depends(get_current_user),
):
    pass

@router.delete('/{id}', response_model=Dog)
def delete_dog(
    user: User = Depends(get_current_user),):
    pass



# @router.post('/create', status_code=201)
# def add_photos(
#     file: UploadFile,
#     profile_service: ProfileService = Depends()
# ):
#     return profile_service.upload_photo(file)
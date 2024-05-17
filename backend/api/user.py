from fastapi import APIRouter, Depends, UploadFile
from services.profile import ProfileService
from schemas.user import UserCreate
from services.deps import get_current_user
from schemas.user import UserCreate, User

router = APIRouter(
    prefix='/user',
    tags=['Профиль'],
    )

@router.get('/', response_model=User)
def get_information(
    user: User = Depends(get_current_user),
):
    pass

@router.put('/', response_model=User)
def update_information(
    user: User = Depends(get_current_user),
):
    pass

@router.delete('/', response_model=User)
def delete_profile(
    user: User = Depends(get_current_user),
):
    pass

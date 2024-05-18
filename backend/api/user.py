from fastapi import APIRouter, Depends, status
from services.deps import get_current_user
from schemas.user import UserCreate, UserUpdate, User


router = APIRouter(
    prefix='/user',
    tags=['Профиль пользователя'],
    )

@router.get('/', response_model=User)
def create_profile(
    user_data: UserCreate,
    user: User = Depends(get_current_user)):
    pass

@router.put('/', response_model=User)
def update_profile(
    user_data: UserUpdate,
    user: User = Depends(get_current_user)):
    pass

@router.delete('/', response_model=User) # status_code=status.HTTP_204_NO_CONTENT)
def delete_profile(
    user: User = Depends(get_current_user)):
    pass

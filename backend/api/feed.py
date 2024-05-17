from fastapi import APIRouter, Depends, UploadFile
from services.profile import ProfileService
from schemas.user import UserCreate
from services.deps import get_current_user
from schemas.user import UserCreate, User

router = APIRouter(
    prefix='/feed',
    tags=['Лента'],
    )

@router.post('/')
def apply_filter(
    user: User = Depends(get_current_user),
):
    pass
# return card

@router.get('/swipe_left')
def swipe_left(
    user: User = Depends(get_current_user),
):
    pass

@router.get('/swipe_right')
def swipe_right(
    user: User = Depends(get_current_user),
):
    pass
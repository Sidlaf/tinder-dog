from fastapi import APIRouter, Depends
from services.auth_service import get_current_user
from schemas.user import  User
from schemas.dog import Dog
from fastapi_filter import FilterDepends


from services.feed import DogFilter
from services.filter import FilterService


router = APIRouter(
    prefix='/feed',
    tags=['Лента анкет'],
    )


@router.post('/set_filter')
def set_filter(
    user: User = Depends(get_current_user),
    filter_service: FilterService = Depends(),
    dog_filter: DogFilter = FilterDepends(DogFilter)):
    return filter_service.set_filter(user, dog_filter)

@router.get('/all', response_model=list[Dog])
def get_all_cards(
    filter_service: FilterService = Depends(),
    user: User = Depends(get_current_user)):
    return filter_service.get_all_cards(user)

@router.get('/next')
def get_next_card(
    filter_service: FilterService = Depends(),
    user: User = Depends(get_current_user)):
    return filter_service.get_next_card(user)

@router.get('/like')
def like_card(
    filter_service: FilterService = Depends(),
    user: User = Depends(get_current_user)):
    return filter_service.like_card(user)

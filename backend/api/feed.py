from fastapi import APIRouter, Depends
from services.deps import get_current_user
from schemas.user import  User
from schemas.dog import Dog
from fastapi_filter import FilterDepends


from services.feed import DogFilter
from database.db import get_session
from sqlalchemy.orm import Session
from database import tables
from sqlalchemy import select
import json

router = APIRouter(
    prefix='/feed',
    tags=['Лента анкет'],
    )

@router.get('/test', response_model=list[Dog])
def list_dog(dog_filters: DogFilter = FilterDepends(DogFilter), 
    session: Session = Depends(get_session)):
    query = dog_filters.filter(select(tables.Dog).outerjoin(tables.User))
    model = dog_filters.model_dump_json()
    a = DogFilter(**json.loads(model))
    query1 = a.filter(select(tables.Dog).outerjoin(tables.User))
    result = session.execute(query1)
    return result.scalars().all()

@router.get('/', response_model=Dog)
def get_card(
    user: User = Depends(get_current_user)):
    pass

@router.get('/dislike')
def dislike_card(
    user: User = Depends(get_current_user)):
    pass

@router.get('/like')
def like_card(
    user: User = Depends(get_current_user)):
    pass

@router.post('/filter')
def set_filter(
    user: User = Depends(get_current_user),
    dog_filter: DogFilter = FilterDepends(DogFilter)):
    pass


# @router.get('/')
# def list_dog(
#     filters: DogQuery = Depends(),
#     db: Session = Depends(get_session),
# ) -> List[DogOutput]:
#     filter_set = DogFilter(db, select(Dog))
#     filter_params = parse_obj_as(DogFilterSchema, filters)
#     filtered_products = filter_set.filter(filter_params.dict(exclude_none=True))
#     return parse_obj_as(list[DogOutput], filtered_products)

# @router.get('/')
# def list_dog(
#     filters: DogQuery = Depends(),
#     db: Session = Depends(get_session),
# )-> list[Dog]:
#     filter_set = DogFilter(db, select(Dog))
#     filter_params = parse_obj_as(DogOutputSchema, filters)
#     filtered_products = filter_set.filter(filter_params.dict(exclude_none=True))
#     return parse_obj_as(list[DogOutputSchema], filtered_products)

# @router.post('/')
# def apply_filter(
#     user: User = Depends(get_current_user),
# ):
#     pass
# # return card

# @router.get('/swipe_left')
# def swipe_left(
#     user: User = Depends(get_current_user),
# ):
#     pass

# @router.get('/swipe_right')
# def swipe_right(
#     user: User = Depends(get_current_user),
# ):
#     pass
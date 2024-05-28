from database.tables import Dog, User
from schemas.dog import Tag, Breed
from fastapi import Query
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field
import dataclasses
from fastapi_filter.contrib.sqlalchemy import Filter
from sqlalchemy import select
from database.db import get_session
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi_filter import FilterDepends, with_prefix



class UserFilter(Filter):
    location: Optional[str] = Field(None, alias='location')
    # is_premium: Optional[bool]

    class Constants(Filter.Constants):
        model = User

class DogFilter(Filter):
    age__in: Optional[list[int]] = Field(None, alias='age__in')
    breed: Optional[Breed] = Field(None, alias='breed')
    sex:  Optional[str] = Field(None, alias='sex')
    user: Optional[UserFilter] = FilterDepends(with_prefix("user", UserFilter))

    class Constants(Filter.Constants):
        model = Dog


class FilterService:

    def __init__(self, session: Session = Depends(get_session)) -> Session:
        self.session = session

    def apply_filter(self,  user_id: int, dog_filter: DogFilter):
        pass
    # def get_products_filter(self, product_filter: DogFilter) -> list:
    #     query_filter = product_filter.filter(select(Dog))
    #     print(query_filter)
    #     return self.session.execute(query_filter).all()
    
# def get_products_filter(self, product_filter: DogFilter,
#                         page: int, size: int) -> list:
#     offset_min = page * size
#     offset_max = (page + 1) * size
#     query_filter = product_filter.filter(select(Product))
#     filtered_data = self.session.exec(query_filter).all()
#     response = filtered_data[offset_min:offset_max] + [
#         {
#             "page": page,
#             "size": size,
#             "total": math.ceil(len(filtered_data) / size) - 1,
#         }
#     ]

#     return response

# from sqlalchemy_filterset import (
#     Filter,
#     FilterSet,
#     RangeFilter,
#     LimitOffsetFilter,
#     RelationJoinStrategy)

# #Filter
# class DogFilter(FilterSet):
#     sex = Filter(Dog.sex)
#     breed = Filter(Dog.breed)
#     age = RangeFilter(Dog.age)
#     tags = Filter(Dog.tags)

#     location = Filter(User.location, strategy=RelationJoinStrategy(
#             User,
#             User.id == Dog.owner_id,
#         ))
#     is_premium = Filter(User.is_premium, strategy=RelationJoinStrategy(
#             User,
#             User.id == Dog.owner_id,
#         ))
#     limit_offset = LimitOffsetFilter()

#Query

# @dataclasses.dataclass
# class DogQuery:
#     sex: str | None = Query(None)
#     breed: str | None = Query(None)
#     location: str | None = Query(None)
#     is_premium: bool | None = Query(None)
#     tags: list[Tag] | None = Query(None)
#     age_min: int | None = Query(None)
#     age_max: int | None = Query(None)
#     limit: int | None = Query(None)
#     offset: int | None = Query(None)

#     @property
#     def limit_offset(self) -> tuple[int | None, int | None] | None:
#         if self.limit or self.offset:
#             return self.limit, self.offset
#         return None

#     @property
#     def age(self) -> tuple[float, float] | None:
#         if self.age_min and self.age_max:
#             return self.age_min, self.age_max
#         return None
    
# #Output schema
# from pydantic import BaseModel


# class DogOutput(BaseModel):
#     sex: str
#     breed: str
#     tags: list[str]
#     age: int
#     location: str
#     is_premium: bool

#     class Config:
#         orm_mode = True

# class DogFilterSchema(BaseModel):
#     sex: str | None
#     breed: str | None
#     tags: list[str] | None
#     age: int | None
#     location: str | None
#     is_premium: bool | None
#     limit_offset: tuple[int | None, int | None] | None

#     class Config:
#         orm_mode = True
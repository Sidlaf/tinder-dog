from services.feed import DogFilter
from schemas.dog import Dog
from schemas.feed import Feed
from database import tables
from database.db import get_session
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from sqlalchemy import select
import json

from services.email_service import send_like_email

class FilterService:
    def __init__(self,session: Session = Depends(get_session)):
        self.session = session

    def get_all_cards(self, user: tables.User):
        exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
            detail="The user must be registered",
            )
        query_filter = (
            self.session
            .query(tables.Feed)
            .filter(tables.Feed.user_id == user.id)
            .first()
        )
        if not query_filter:
            raise exception
        current_filter = DogFilter(**json.loads(query_filter.current_filter))
        query = current_filter.filter(select(tables.Dog).outerjoin(tables.User))
        dogs = self.session.execute(query).scalars().all()
        result = []
        for dog in dogs:
            result.append(
                Dog(
                    id = dog.id,
                    name = dog.name,
                    sex = dog.sex,
                    age = dog.age, 
                    breed = dog.breed, 
                    tags = dog.tags,
                    description = dog.description,
                    photo_url = dog.photo_url,
                    is_premium = dog.owner.is_premium
                )
            )
        print(type(result))
        return result
    
    def get_row_cards(self, user: tables.User):
        exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
            detail="The user must be registered",
            )
        query_filter = (
            self.session
            .query(tables.Feed)
            .filter(tables.Feed.user_id == user.id)
            .first()
        )
        if not query_filter:
            raise exception
        current_filter = DogFilter(**json.loads(query_filter.current_filter))
        query = current_filter.filter(select(tables.Dog).outerjoin(tables.User))
        dogs = self.session.execute(query).scalars().all()
        result = []
        for dog in dogs:
            result.append(dog)
        return result
    
    def get_cards_len_by_filter(self, current_filter: json):
        exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
            detail="The user must be registered",
            )
        current_filter = DogFilter(**json.loads(current_filter))
        query = current_filter.filter(select(tables.Dog).outerjoin(tables.User))
        dogs = self.session.execute(query).scalars().all()
        return len(dogs)
    
    def set_filter(self, user: tables.User, dog_filter: DogFilter):
        exception = HTTPException(
        status_code=status.HTTP_204_NO_CONTENT,
            detail="The dog not found",
            )
        json_filter = dog_filter.model_dump_json()
        # json_filter = json.dumps(model_filter))
        query_feed = (
            self.session
            .query(tables.Feed)
            .filter(tables.Feed.user_id == user.id)
            .first()
        )
        if not query_feed:
            raise exception
        filter_lenght = self.get_cards_len_by_filter(json_filter)

        current_feed = Feed(
            total_cards=filter_lenght,
            current_card=0,
            history = []
        )
        try:
            for field, value in current_feed:
                setattr(query_feed, field, value)
            query_feed.current_filter = json_filter
            self.session.commit()
        except Exception:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT)

    def get_next_card(self, user: tables.User):
        exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
            detail="The user must be registered",
            )
        exception_NO_CONTENT = HTTPException(
        status_code=status.HTTP_204_NO_CONTENT,
            detail="No cards",
            )
        query_feed = (
            self.session
            .query(tables.Feed)
            .filter(tables.Feed.user_id == user.id)
            .first()
        )
        if not query_feed:
            raise exception
        current_card = query_feed.current_card
        total_cards = query_feed.total_cards
        if current_card + 1 > total_cards:
            raise exception_NO_CONTENT
        dog_slice = self.get_row_cards(user)[current_card: current_card + 1]
        dog = dog_slice[0]
        card = Dog(
                    id = dog.id,
                    name = dog.name,
                    sex = dog.sex,
                    age = dog.age, 
                    breed = dog.breed, 
                    tags = dog.tags,
                    description = dog.description,
                    photo_url = dog.photo_url,
                    is_premium = dog.owner.is_premium
                )
        new_history = query_feed.history.copy()
        new_history.append(dog.id)

        try:
            setattr(query_feed, "current_card", current_card + 1)
            # self.session.commit()
        except Exception:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT)
        query_feed.history = new_history
        self.session.commit()
        return card
    
    def like_card(self, user: tables.User):
        exception_NO_CONTENT = HTTPException(
        status_code=status.HTTP_204_NO_CONTENT,
            detail="No cards",
            )
        query_feed = (
            self.session
            .query(tables.Feed)
            .filter(tables.Feed.user_id == user.id)
            .first()
        )
        if not query_feed:
            raise exception_NO_CONTENT
        
        history = query_feed.history.copy()
        
        if history:
            liked_dog_id = history[-1]
        
        query_dog = (
            self.session
            .query(tables.Dog)
            .filter(tables.Dog.id == liked_dog_id)
            .first()
        )
        onwer_email = query_dog.owner.email
        # send_like_email(onwer_email, user.email)
        return f"email sent to {onwer_email}"
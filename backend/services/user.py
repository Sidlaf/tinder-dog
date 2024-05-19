import boto3
import config
from schemas.user import UserCreate, User
from database import tables
from database.db import get_session
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
import json

class UserService:
    def __init__(self,session: Session = Depends(get_session)):
        self.session = session

    def get_profile(self, user: tables.User):
        exception = HTTPException(
        status_code=status.HTTP_204_NO_CONTENT,
            detail="USER NOT FOUND",
            )
        query_user = (
            self.session
            .query(tables.User)
            .filter(tables.User.id == user.id)
            .first()
        )
        if not query_user:
            raise exception
        
        return query_user

    def create_profile(self, user_data: UserCreate, user: tables.User):
        exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
            detail="The user has already been created",
            )
        if user.is_verified:
            raise exception from None
        query_user = (
            self.session
            .query(tables.User)
            .filter(tables.User.id == user.id)
            .first()
        )
        data = user_data.model_dump()
        data["is_verified"] = True
        try:
            for field, value in data.items():
                setattr(query_user, field, value)
        except Exception:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT)
        dict_current_filter={"age__in": None,
                            "breed": None,
                            "sex": None,
                            "user": {
                                "location": None
                                }
                            }
        default_filter = json.dumps(dict_current_filter)
        new_feed = tables.Feed(
            current_filter=default_filter,
            user=query_user
        )
        self.session.add(new_feed)
        self.session.commit()

        return query_user
    
    def update_profile(self, user_data: UserCreate, user: tables.User):
        exception = HTTPException(
        status_code=status.HTTP_409_CONFLICT,
            detail="The user not found",
            )
        query_user = (
            self.session
            .query(tables.User)
            .filter(tables.User.id == user.id)
            .first()
        )
        if not query_user:
            raise exception
        print(user_data.model_dump())
        try:
            for field, value in user_data:
                if value:
                    setattr(query_user, field, value)
            self.session.commit()
        except Exception:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT)

        return query_user
    
    def delete_profile(self, user: tables.User):
        exception = HTTPException(
        status_code=status.HTTP_409_CONFLICT,
            detail="The user not found",
            )
        query_user = (
            self.session
            .query(tables.User)
            .filter(tables.User.id == user.id)
            .first()
        )
        if not query_user:
            raise exception
        self.session.delete(query_user)
        self.session.commit()

        return query_user
import boto3
import config
from schemas.dog import DogCreate, Dog, DogUpdate
from database import tables
from database.db import get_session
from sqlalchemy.orm import Session
from fastapi import Depends, UploadFile, HTTPException, status
from datetime import datetime

class DogService:
    def __init__(self,session: Session = Depends(get_session)):
        self.session = session

    def upload_photo(self, file: UploadFile):
        session = boto3.session.Session()
        session = boto3.Session(
            aws_access_key_id=(config.TOKEN),
            aws_secret_access_key=(config.KEY_VALUE),
            region_name="ru-central1",
        )
        now = datetime.now()
        s3 = session.client("s3", endpoint_url=config.ENDPOINT)
        file_name = f"{now.strftime('%H-%M-%S')}_{file.filename}"
        s3.upload_fileobj(
            file.file,                                  # Поток файла для загрузки
            config.S3_BUCKET_NAME,                      # Имя корзины S3
            file_name,
            ExtraArgs={'ContentType': 'image/jpeg'}                                # Имя, под которым файл будет сохранен в корзине S3
        )

        url = f"{config.ENDPOINT}/{config.S3_BUCKET_NAME}/{file_name}"
        return url
    
    def create_dog(self, user: tables.User, dog_data: DogCreate, photo_file: UploadFile):
        exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
            detail="The user must be registered",
            )
        if not user.is_verified:
            raise exception from None
        
        url = self.upload_photo(photo_file)
        dog = tables.Dog(**dog_data.model_dump(), 
                         photo_url = url,
                         owner_id = user.id,
                         owner = user)
        self.session.add(dog)
        self.session.commit()
        return dog
    
    def get_my_dogs(self, user: tables.User):
        exception = HTTPException(
        status_code=status.HTTP_204_NO_CONTENT,
            detail="Dogs not found",
            )
        query_dogs = (
            self.session
            .query(tables.Dog)
            .filter(tables.Dog.owner_id == user.id)
            .all()
        )
        if not query_dogs:
            raise exception
        result =[]
        for dog in query_dogs:
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
        return result
    def get_dog_by_id(self, id: int):
        exception = HTTPException(
        status_code=status.HTTP_204_NO_CONTENT,
            detail="Dog not found",
            )
        query_dog = (
            self.session
            .query(tables.Dog)
            .filter(tables.Dog.id == id)
            .first()
        )
        if not query_dog:
            raise exception

        result = Dog(
            id = query_dog.id,
            name = query_dog.name,
            sex = query_dog.sex,
            age = query_dog.age, 
            breed = query_dog.breed, 
            tags = query_dog.tags,
            description = query_dog.description,
            photo_url = query_dog.photo_url,
            is_premium = query_dog.owner.is_premium
        )
        return result
    
    def update_my_dog(self, user: tables.User, id: int, 
                      dog_data: DogUpdate, photo_file: UploadFile):
        exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
            detail="ACTION FORBIDDEN",
            )
        query_dog = (
            self.session
            .query(tables.Dog)
            .filter(tables.Dog.id == id)
            .first()
        )
        if query_dog.owner_id != user.id:
            raise exception
        data = dog_data.model_dump()
        if photo_file:
            url = self.upload_photo(photo_file)
            data["photo_url"] = url
        try:
            for field, value in data.items():
                if value:
                    setattr(query_dog, field, value)
            self.session.commit()
        except Exception:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT)
        return self.get_dog_by_id(user, id)

    def delete_dog(self, user: tables.User, id: int):
        exception_FORBIDDEN = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
            detail="ACTION FORBIDDEN",
            )
        exception_NO_CONTENT = HTTPException(
        status_code=status.HTTP_204_NO_CONTENT,
            detail="The dog not found",
            )
        query_dog = (
            self.session
            .query(tables.Dog)
            .filter(tables.Dog.id == id)
            .first()
        )
        if not query_dog:
            raise exception_NO_CONTENT
        elif query_dog.owner_id != user.id:
            raise exception_FORBIDDEN
        self.session.delete(query_dog)
        self.session.commit()
        
        return query_dog

    def test_photo_upload(self, photo_file: UploadFile):
        return self.upload_photo(photo_file)
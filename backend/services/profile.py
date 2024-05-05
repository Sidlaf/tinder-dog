import boto3
import config
from schemas.user_schemas import UserCreate, BaseUser
from database import tables
from database.db import get_session
from sqlalchemy.orm import Session
from fastapi import Depends, UploadFile

class ProfileService:
    def __init__(self,session: Session = Depends(get_session)):
        self.session = session

    def upload_photo(self, file: UploadFile):
        session = boto3.session.Session()
        session = boto3.Session(
            aws_access_key_id=(config.TOKEN),
            aws_secret_access_key=(config.KEY_VALUE),
            region_name="ru-central1",
        )

        s3 = session.client("s3", endpoint_url=config.ENDPOINT)
        s3.upload_fileobj(
            file.file,                                  # Поток файла для загрузки
            config.S3_BUCKET_NAME,                      # Имя корзины S3
            file.filename                               # Имя, под которым файл будет сохранен в корзине S3
        )
        return
    
    def create_user(self, user_data: UserCreate):
        user = tables.User(
            email=user_data.email,
            username = user_data.username,
            password = user_data.password
        )
        self.session.add(user)
        self.session.commit()
        return user
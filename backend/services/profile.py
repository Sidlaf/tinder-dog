import boto3
import config
from fastapi import UploadFile
class ProfileService:
    # def __init__(self, session: Session = Depends(get_session)):
    #     self.session = session
    def upload_photo(self, file: UploadFile):
        session = boto3.session.Session()
        s3 = session.client(
            service_name='s3',
            endpoint_url='https://storage.yandexcloud.net'
        )
        bucket = s3.Bucket(name=config.S3_BUCKET_NAME)
        bucket.upload_fileobj(file.file, file.filename)
        return
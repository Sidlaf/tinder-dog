from dotenv import load_dotenv
import os

load_dotenv()

#project
PROJECT_NAME = "ГАВ!"

#uvicorn
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8000

#token
ACCESS_TOKEN_EXPIRE_SECONDS = 3600

#PostgreSQL
DB_HOST =  os.environ.get("DB_HOST")
DB_PORT =  os.environ.get("DB_PORT")
DB_NAME =  os.environ.get("DB_NAME")
DB_USER =  os.environ.get("DB_USER")
DB_PASS =  os.environ.get("DB_PASS")

#ObjectStorage
ENDPOINT = "https://storage.yandexcloud.net"
S3_BUCKET_NAME =  os.environ.get("S3_BUCKET_NAME")
TOKEN = os.environ.get("TOKEN")
KEY_VALUE = os.environ.get("KEY_VALUE")


#email_secrets
EMAIL_TEMPLATES_DIR = r"/home/wafer/tinder-dog/backend/static/email_templates/"
EMAILS_FROM_EMAIL = os.environ.get("EMAILS_FROM_EMAIL")
EMAILS_FROM_NAME = os.environ.get("EMAILS_FROM_NAME")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")
SMTP_USER = os.environ.get("SMTP_USER")
SMTP_HOST = os.environ.get("SMTP_HOST")
SERVER_NAME = os.environ.get("SERVER_NAME")
SERVER_BOT = os.environ.get("SERVER_BOT")
SMTP_PORT = 465
SMTP_SSL = True
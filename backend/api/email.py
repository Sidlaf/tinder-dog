from fastapi import APIRouter, Depends
from services import email_service

router = APIRouter(
    tags=['Отправка по почте'],
    )

@router.post('/email')
def post_email(
    recipient: str,
):
    return email_service.send_magic_login_email(recipient)
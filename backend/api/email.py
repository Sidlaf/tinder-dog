from fastapi import APIRouter, Depends
from services.email_service import EmailService

router = APIRouter(
    tags=['Отправка по почте'],
    )

@router.post('/email')
def post_email(
    recipient: str,
    email_service: EmailService = Depends()
):
    return email_service.send_magic_login_email(recipient)
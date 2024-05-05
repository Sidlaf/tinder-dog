from fastapi import APIRouter, Depends
from services.auth import AuthService
from schemas.token import WebToken, Token
from typing import Annotated
from services.deps import get_magic_token

router = APIRouter(
    tags=['Авторизация'],
    )

@router.post('/magic/{email}', status_code=WebToken)
def login_with_magic_link(
    email: str,
    auth_service: AuthService
):
    return auth_service.login_with_magic_link(email)

@router.post("/claim", response_model=Token)
def validate_magic_link(
    web_token: WebToken,
    magic_in: Annotated[bool, Depends(get_magic_token)],
    auth_service: AuthService
):
    return auth_service.validate_magic_link(web_token, magic_in)
  
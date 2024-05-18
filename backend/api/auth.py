from fastapi import APIRouter, Depends
# from services.auth import AuthService
# from schemas.token import WebToken, Token
# from typing import Annotated
# from services.deps import get_magic_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    tags=['Авторизация'],
    )

# @router.post('/magic/{email}', response_model=WebToken)
# def login_with_magic_link(
#     email: str,
#     auth_service: AuthService = Depends()):

#     return auth_service.login_with_magic_link(email)

# @router.post("/claim", response_model=Token)
# def validate_magic_link(
#     web_token: WebToken,
#     magic_in: Annotated[bool, Depends(get_magic_token)],
#     auth_service: AuthService = Depends()
# ):
#     return auth_service.validate_magic_link(web_token, magic_in)

@router.post('/login')
def login(
    email: str,
    auth_data: OAuth2PasswordRequestForm = Depends()):
    return 1


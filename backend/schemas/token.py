from typing import Optional
from pydantic import BaseModel
from uuid import UUID

class WebToken(BaseModel):
    claim: str

class MagicTokenPayload(BaseModel):
    sub: Optional[UUID] = None
    fingerprint: Optional[UUID] = None

class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'
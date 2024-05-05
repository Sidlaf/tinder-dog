from typing import Optional
from pydantic import BaseModel
from uuid import UUID

class WebToken(BaseModel):
    claim: str

class Token(BaseModel):
    access_token: str
    refresh_token: Optional[str] = None
    token_type: str

class MagicTokenPayload(BaseModel):
    sub: Optional[UUID] = None
    fingerprint: Optional[UUID] = None

class RefreshTokenBase(BaseModel):
    token: str
    authenticates_id: Optional[UUID] = None


class RefreshTokenCreate(RefreshTokenBase):
    authenticates_id: UUID
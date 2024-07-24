from datetime import datetime

from pydantic import BaseModel, EmailStr, SecretStr, StrictStr

from .typing import AccountId


class AccountRequest(BaseModel):
    email: EmailStr
    password: SecretStr


class JwtPayload(BaseModel):
    sub: AccountId
    exp: datetime


class Token(BaseModel):
    access_token: StrictStr
    refresh_token: StrictStr

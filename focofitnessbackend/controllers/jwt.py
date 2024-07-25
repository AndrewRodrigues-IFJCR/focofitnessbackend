from datetime import datetime
from typing import Any, Dict, Literal, TypeAlias

from jose import exceptions, jwt

from ..settings import JWTSettings
from .schemas import JwtPayload

settings = JWTSettings()

ClaimsString: TypeAlias = Literal['sub', 'exp']


def jwt_encode_access_token(
    claims: JwtPayload | Dict[ClaimsString, Any]
) -> str:
    return jwt.encode(
        {
            'sub': claims['sub'],
            'exp': datetime.now() + settings.access_token_expires,
        },
        key=settings.access_token_secret_key,
    )


def jwt_encode_refresh_token(
    claims: JwtPayload | Dict[ClaimsString, Any]
) -> str:
    return jwt.encode(
        {
            'sub': claims['sub'],
            'exp': datetime.now() + settings.refresh_token_expires,
        },
        key=settings.refresh_token_secret_key,
    )


def jwt_decode_access_token(token: str) -> JwtPayload:
    payload = jwt.decode(token=token, key=settings.access_token_secret_key)
    return JwtPayload(sub=payload['sub'], exp=payload['exp'])


def jwt_decode_refresh_token(token: str) -> JwtPayload:
    payload = jwt.decode(token=token, key=settings.refresh_token_secret_key)
    return JwtPayload(sub=payload['sub'], exp=payload['exp'])

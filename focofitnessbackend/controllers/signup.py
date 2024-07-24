from fastapi import Depends

from ..models.account import Account
from ..models.connection import get_async_session_maker
from .jwt import jwt_encode_access_token, jwt_encode_refresh_token
from .schemas import AccountRequest
from .security import generate_password_hash


async def signup(
    account_req: AccountRequest,
    async_session_maker=Depends(get_async_session_maker),
):
    with async_session_maker() as session:
        account = Account(
            email=account_req.email,
            password_hash=generate_password_hash(account_req.password),
        )
        session.add(account)
        await session.commit()
        await session.refresh(account)

    return account

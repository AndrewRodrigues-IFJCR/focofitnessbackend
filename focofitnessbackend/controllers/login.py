# -*- encoding: utf-8 -*-
from fastapi import Depends

from ..models.connection import get_async_session_maker
from .schemas import LoginRequest


async def login(
    login_req: LoginRequest,
    async_session_maker=Depends(get_async_session_maker),
):
    with async_session_maker() as session:
        result = session
    return

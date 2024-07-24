from pwdlib import PasswordHash

from .typing import PasswordStr

PasswordHandler = PasswordHash.recommended()


def generate_password_hash(password: PasswordStr) -> str:
    return PasswordHandler.hash(password.get_secret_value())


def verify_password(password: PasswordStr, password_hash: str):
    if not PasswordHandler.verify(password.get, password_hash):
        raise Exception

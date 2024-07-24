import secrets
from datetime import timedelta

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

load_dotenv()


class APISettings(BaseSettings):
    ...


class DatabaseSettings(BaseSettings):
    database_connection_string: str


class JWTSettings(BaseSettings):
    access_token_expires: timedelta = Field(default='3:0:0')
    refresh_token_expires: timedelta = Field(default='3:0:0')

    access_token_secret_key: str = Field(default=secrets.token_hex(256))
    refresh_token_secret_key: str = Field(default=secrets.token_hex(256))

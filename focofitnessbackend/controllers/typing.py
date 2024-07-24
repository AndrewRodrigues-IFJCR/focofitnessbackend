from pydantic import BaseModel, Field, SecretStr
from typing_extensions import Annotated

AccountId = Annotated[int, Field(gt=0)]


class PasswordStr(SecretStr):
    ...

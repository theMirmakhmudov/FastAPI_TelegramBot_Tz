from typing import Optional

from pydantic import BaseModel, ConfigDict

class CreateUserFrom(BaseModel):
    user_id: int
    fullname: str
    username: Optional[str] = None
    phone_number: str
    is_verified: bool = False


class UserOut(BaseModel):
    id: int
    user_id: int
    fullname: str
    username: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)
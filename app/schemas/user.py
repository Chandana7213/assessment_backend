from pydantic import BaseModel
from typing import List, Optional

class UserCreate(BaseModel):
    name:str
    email: str
    password: str
    is_admin: Optional[bool] = False



class UserOut(BaseModel):
    id: int
    name:str
    email: str

class ChangePassword(BaseModel):
    old_password: str
    new_password: str
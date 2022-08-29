from pydantic import BaseModel

class AuthUserModel(BaseModel):
    id: int = None
    is_authenticated: bool = False

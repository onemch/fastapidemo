from pydantic import BaseModel


class User(BaseModel):
    id: int = None
    username: str
    password: str
    email: str
    sex: bool

    class Config:
        orm_mode = True

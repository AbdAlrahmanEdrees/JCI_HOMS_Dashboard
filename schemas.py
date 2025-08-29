from pydantic import BaseModel

class SetUser(BaseModel):
    name:str
    email:str
    password:str

class GetUser(BaseModel):
    id:int
    name:str
    email:str
    password:str
    class Config:
        orm_mode=True
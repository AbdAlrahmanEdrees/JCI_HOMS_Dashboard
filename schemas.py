from pydantic import BaseModel

class CreateUserData(BaseModel):
    name:str
    email:str
    
class SendingUserData(BaseModel):
    id:int
    name: str
    email:str
    class Config:
        orm_mode=True
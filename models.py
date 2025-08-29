from database import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,unique=True,autoincrement=True)
    name=Column(String(50), nullable=False)
    email=Column(String(50), nullable=False, index=True)
    password=Column(String(50),nullable=False)
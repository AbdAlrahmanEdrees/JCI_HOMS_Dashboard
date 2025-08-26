from sqlalchemy import Column,Integer, String
from sqlalchemy.orm import declarative_base
from database import engine

Base=declarative_base()

def createTables():
    Base.metadata.create_all(bind=engine)

class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(50), nullable=False)
    email=Column(String(50), unique=True, index=True, nullable=False)
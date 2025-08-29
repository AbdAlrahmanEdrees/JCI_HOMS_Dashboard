from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine

database_url='mysql+pymysql://AbdAlrahman:password@localhost/jci_homs'

Base=declarative_base()

engine=create_engine(database_url, echo=True)
session=sessionmaker(bind=engine)

def create_all_tables():
    Base.metadata.create_all(bind=engine)




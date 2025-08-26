from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

url='mysql+pymysql://root:@localhost/jci_homs_back'

engine=create_engine(url,echo=True)
#echo=True: to print the sql instructions

session=sessionmaker(bind=engine)
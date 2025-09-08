from sqlalchemy import text,create_engine
from sqlalchemy.orm import sessionmaker


db_url='mysql+pymysql://AbdAlrahman:password@localhost/jci_homs'

engine=create_engine(db_url, echo=True)
session=sessionmaker(bind=engine)



def sql_query():
    connection=engine.connect()
    query=text('''
    INSERT INTO users (name,email)
    VALUES ('abdalrahman','123@gmail.com') ;
    ''')
    connection.execute(query)
    connection.commit()
    connection.close()
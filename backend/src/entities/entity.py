from datetime import datetime
from sqlalchemy import create_engine, Column, String,Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import update

db_url = 'localhost:5432'
db_name = 'delivery'
db_user = 'postgres'
db_password = 'toalha28'
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')
Session = sessionmaker(bind=engine)

Base = declarative_base()

class Entity:
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    last_upgrated_by = Column(String)

    def __init__(self):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        
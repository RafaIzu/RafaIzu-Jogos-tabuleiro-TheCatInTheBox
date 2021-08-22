from sqlalchemy import Column, String
from .entity import Entity, Base

class Consumer(Entity, Base):
    __tablename__ = 'cliente'

    name = Column(String)
    email = Column(String)
    password = Column(String)
    cpf = Column(String)

    def __init__(self, name, email, password, cpf):
        self.name = name
        self.email = email
        self.password = password
        self.cpf = cpf
        super().__init__()



    


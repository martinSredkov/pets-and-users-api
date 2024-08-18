from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserModel(Base):
    __tablename__= "accounts"
    id = Column("user_id", Integer, primary_key=True)
    name = Column("name", String(30))
    age = Column("age", Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"ID(id={self.id!r}, name={self.name!r}, age={self.age!r})"
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PetModel(Base):
    __tablename__ = "pets"
    pet_id = Column("pet_id", Integer, primary_key=True)
    name = Column("name", String(30))
    breed = Column("breed", String(30))
    age = Column("age", Integer)
    owner_id = Column("owner_id", Integer)

    def __init__(self, name, breed, age, owner_id):
        self.name = name
        self.breed = breed
        self.age = age
        self.owner_id = owner_id

    def __repr__(self) -> str:
        return f"ID(id={self.pet_id!r}, name={self.name!r}, age={self.age!r}, breed={self.breed!r}, owner_id={self.owner_id!r})"

from sqlalchemy.orm import Session
from sqlalchemy import Engine
from model.pet_model import PetModel
from dto.pet import Pet

class PetRepository:
    def __init__(self, engine: Engine):
        self.engine = engine
        self.session = Session(engine)

    def get_pet_by_id(self, pet_id):
        self.refresh_session()
        pet = self.session.query(PetModel).filter(PetModel.pet_id == pet_id).first()
        if not pet:
            return None
        return pet

    def get_all_pets(self):
        self.refresh_session()
        result = self.session.query(PetModel).all()
        return result

    def create_pet(self, pet_data: PetModel):
        self.refresh_session()
        self.session.add(pet_data)
        self.session.commit()
        return pet_data

    def delete_pet(self, pet_id):
        self.refresh_session()
        selected_pet = self.get_pet_by_id(pet_id)
        if selected_pet:
            self.session.delete(selected_pet)
            self.session.commit()
            return f"Pet {pet_id} deleted."
        return "No such ID"

    def get_all_pets_for_user(self, user_id):
        self.refresh_session()
        found_pets = self.session.query(PetModel).filter(PetModel.owner_id == user_id).all()
        if not found_pets:
            return []
        return found_pets

    def change_owner_for_pet(self, pet_id, new_owner_id):
        self.refresh_session()
        selected_pet = self.get_pet_by_id(pet_id)
        if selected_pet:
            selected_pet.owner_id = new_owner_id
            self.session.commit()
            return selected_pet
        return None

    def refresh_session(self):
        self.session.close()
        self.session = Session(self.engine)






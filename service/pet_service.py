from dto.pet import Pet
from model.pet_model import PetModel
from repository.pet_repository import PetRepository
from repository.user_repository import UserRepository
from util.util import *


class PetService:
    def __init__(self, pet_repository:PetRepository, user_repository:UserRepository):
        self.pet_repository = pet_repository
        self.user_repository = user_repository

    def create_pet_for_user(self, pet_dto:Pet, user_id):
        if not self.user_repository.get_user_by_id(user_id):
            raise  Exception("Invalid user ID")
        if not validate_age(pet_dto.age):
            raise Exception("Age is not valid!")
        if not validate_name(pet_dto.name):
            raise  Exception("Name is not valid!")
        pet_dto.owner_id = user_id
        pet_model = map_pet_dto_to_model(pet_dto)
        created_pet = self.pet_repository.create_pet(pet_model)
        return map_pet_model_to_dto(created_pet)



    def move_pet_between_users(self, pet_id, sender_user_id, recipient_user_id):
        if not self.user_repository.get_user_by_id(sender_user_id):
            raise Exception("Sender user id is not valid!")
        if not self.user_repository.get_user_by_id(recipient_user_id):
            raise Exception("Recipient user id is not valid!")
        pet = self.pet_repository.get_pet_by_id(pet_id)
        if not pet:
            raise  Exception("Pet id is not valid!")
        if str(pet.owner_id) != str(sender_user_id):
            raise  Exception("User has no pet with given id!")
        new_pet = self.pet_repository.change_owner_for_pet(pet_id, recipient_user_id)
        return map_pet_model_to_dto(new_pet)


    def get_all_pets_for_user(self, user_id):
        if not self.user_repository.get_user_by_id(user_id):
            raise  Exception("User id is not valid!")
        pet_models = self.pet_repository.get_all_pets_for_user(user_id)
        dtos = []
        for model in pet_models:
            dto = map_pet_model_to_dto(model)
            dtos.append(dto)
        return dtos

    def get_pet(self, pet_id):
        pet = self.pet_repository.get_pet_by_id(pet_id)
        if not pet:
            raise Exception("Pet id is not valid!")
        return map_pet_model_to_dto(pet)


    def get_all_pets(self):
        dtos = []
        for model in self.pet_repository.get_all_pets():
            dtos.append(map_pet_model_to_dto(model))
        return dtos

    def delete_pet(self, pet_id):
        return self.pet_repository.delete_pet(pet_id)
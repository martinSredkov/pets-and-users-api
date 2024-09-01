from repository.user_repository import UserRepository
from repository.pet_repository import PetRepository
from json_util.util import validate_age, validate_name, map_user_model_to_dto, map_user_dto_to_model
from dto.user import User

class UserService:
    def __init__(self, user_repository: UserRepository, pet_repository: PetRepository):
        self.user_repository = user_repository
        self.pet_repository = pet_repository

    def cascade_delete(self, user_id):
        all_pets = self.pet_repository.get_all_pets_for_user(user_id)
        for pet in all_pets:
            self.pet_repository.delete_pet(pet.pet_id)
        return self.user_repository.delete_user(user_id)

    def create_user(self, user_dto: User):
        if not validate_age(user_dto.age):
            raise Exception("Age is not valid!")
        if not validate_name(user_dto.name):
            raise  Exception("Name is not valid!")
        created_user_model = self.user_repository.create_user(map_user_dto_to_model(user_dto))
        return map_user_model_to_dto(created_user_model)


    def get_user(self, user_id):
        user = self.user_repository.get_user_by_id(user_id)
        if not user:
            raise  Exception("Invalid user ID")
        return map_user_model_to_dto(user)

    def get_all_users(self):
        dtos = []
        for dto in self.user_repository.get_all_users():
            dtos.append(map_user_model_to_dto(dto))
        return dtos

    def delete_user(self, user_id):
        return self.user_repository.delete_user(user_id)

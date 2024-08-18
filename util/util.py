import json

from dto.pet import Pet
from dto.user import User
from model.pet_model import PetModel
from model.user_model import UserModel

def map_pet_model_to_dto(pet_model:PetModel):
    pet_dto = Pet(
        pet_model.pet_id,
        pet_model.name,
        pet_model.breed,
        pet_model.age,
        pet_model.owner_id
    )
    return pet_dto

def map_pet_dto_to_model(pet_dto:Pet):
    pet_model = PetModel(
        pet_dto.name,
        pet_dto.breed,
        pet_dto.age,
        pet_dto.owner_id
    )
    return pet_model

def map_user_model_to_dto(user_model:UserModel):
    user_dto = User(
        user_model.id,
        user_model.name,
        user_model.age
    )
    return user_dto

def map_user_dto_to_model(user_dto: User):
    user_model = UserModel(
        user_dto.name,
        user_dto.age
    )
    return user_model

def validate_name(name: str):
    return name.isalpha()


def validate_age(age):
    return 0 < age < 100

def serialize_struct(serializable):
    return json.dumps(serializable.__dict__)

def json_msg_from_msg(msg:str):
    return json.dumps({
        "message": msg
    })

def serialize_list_of_structs(serializables):
    return json.dumps([el.__dict__ for el in serializables])

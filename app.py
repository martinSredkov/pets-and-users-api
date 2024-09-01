import os
from flask import Flask, request
from dotenv import load_dotenv
from sqlalchemy import create_engine
from dto.pet import Pet
from dto.user import User
from repository.user_repository import UserRepository
from repository.pet_repository import PetRepository
from service.pet_service import PetService
from service.user_service import UserService
from json_util.util import serialize_struct, json_msg_from_msg, serialize_list_of_structs

load_dotenv()
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


connection_string = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(connection_string)


pet_repo = PetRepository(engine)
user_repository = UserRepository(engine)
pet_service = PetService(pet_repo, user_repository)
user_service = UserService(user_repository, pet_repo)

app = Flask(__name__)


'''endpoints/handlers/routes for:
create user = POST /user
get user = GET /user/{id}
update user = PUT /user/{id}
delete user = DELETE /user/{id}
^
same for pets

additional endpoints for:
transfer pet between users -> /transfer/{pet_id}/ where the body cointains sender and recipient user IDs
endpoint for create pet should validate that the user to whom the pet is created exists'''



@app.after_request
def add_header(response):
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route("/user", methods=["POST"])
def create_user():
    data = request.get_json()
    try:
        created = user_service.create_user(User.from_dict(data))
        return serialize_struct(created)
    except TypeError as e:
        return json_msg_from_msg(repr(e))

@app.route("/user/<user_id>", methods=["GET"])
def get_user(user_id):
    try:
        user = user_service.get_user(user_id)
        return serialize_struct(user)
    except TypeError as e:
        return json_msg_from_msg(repr(e))

@app.route("/user/<user_id>/add-pet", methods=["POST"])
def create_pet(user_id):
    data = request.get_json()
    try:
        created = pet_service.create_pet_for_user(Pet.from_dict(data), user_id)
        return serialize_struct(created)
    except TypeError as e:
        return json_msg_from_msg(repr(e))


@app.route("/pet/<pet_id>", methods=["GET"])
def get_pet(pet_id):
    try:
        pet = pet_service.get_pet(pet_id)
        return serialize_struct(pet)
    except TypeError as e:
        return json_msg_from_msg(repr(e))

@app.route("/pets", methods=["GET"])
def get_all_pets():
    try:
        all_pets = pet_service.get_all_pets()
        return serialize_list_of_structs(all_pets)
    except TypeError as e:
        return json_msg_from_msg(repr(e))


@app.route("/pet/<pet_id>/<sid>/<rid>", methods=["POST"])
def transfer_pet(pet_id, sid, rid):
    try:
        transfered = pet_service.move_pet_between_users(pet_id, sid, rid)
        return serialize_struct(transfered)
    except TypeError as e:
        return json_msg_from_msg(repr(e))

@app.route("/user/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    return json_msg_from_msg(user_service.cascade_delete(user_id))

@app.route("/pets/<user_id>", methods=["GET"])
def get_all_pets_for_user(user_id):
    try:
        all_pets = pet_service.get_all_pets_for_user(user_id)
        return serialize_list_of_structs(all_pets)
    except TypeError as e:
        return json_msg_from_msg(repr(e))

@app.route("/health")
def health():
    return "{ \"message\": \"ok\" }"

if __name__ == "__main__":
    app.run()

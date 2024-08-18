from sqlalchemy.orm import Session
from sqlalchemy import Engine
from model.user_model import UserModel
from dto.user import User

class UserRepository:
    def __init__(self, engine: Engine):
        self.engine = engine
        self.session = Session(engine)

    def get_user_by_id(self, user_id):
        user = self.session.query(UserModel).filter(UserModel.id == user_id).first()
        if not user:
            return None
        return user

    def get_all_users(self):
        result = self.session.query(UserModel).all()
        return result

    def create_user(self, user_data: UserModel):
        self.session.add(user_data)
        self.session.commit()
        return user_data

    def delete_user(self, user_id):
        selected_user = self.get_user_by_id(user_id)
        if selected_user:
            self.session.delete(selected_user)
            self.session.commit()
            return f"User {user_id} deleted."
        return "No such ID"






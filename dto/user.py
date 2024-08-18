class User:
    def __init__(self, user_id, name, age):
        self.user_id = user_id
        self.name = name
        self.age = age

    @staticmethod
    def from_dict(data_dict):
        user = User(
            data_dict["id"],
            data_dict["name"],
            data_dict["age"]
        )
        return user

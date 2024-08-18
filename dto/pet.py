class Pet:
    def __init__(self, pet_id, name, breed, age, owner_id):
        self.pet_id = pet_id
        self.name = name
        self.breed = breed
        self.age = age
        self.owner_id = owner_id

    @staticmethod
    def from_dict(data_dict):
        pet = Pet(
            data_dict["id"],
            data_dict["name"],
            data_dict["breed"],
            data_dict["age"],
            data_dict["owner_id"]
        )
        return pet

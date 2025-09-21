class User:
    def __init__(self, name, age, hobby, fav_animal):
        self.name = name
        self.age = age
        self.hobby = hobby
        self.fav_animal = fav_animal

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "hobby": self.hobby,
            "fav_animal": self.fav_animal
        }
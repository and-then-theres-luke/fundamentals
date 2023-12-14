from pet import Pet

class Cat(Pet):
    def __init__(self, name, type_of_animal, tricks, health, energy):
        super().__init__(name, type_of_animal, tricks, health, energy)
        self.lives = 9
        self.type_of_animal = "Cat"


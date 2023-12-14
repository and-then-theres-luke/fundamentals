from pet import Pet
from cat import Cat

class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
    
    
    # walk() - walks the ninja's pet invoking the pet play() method
    
    def walk(self):
        self.pet.play()
        return self
    
    # feed() - feeds the ninja's pet invoking the pet eat() method
    
    def feed(self):
        self.pet.eat()
        return self
        
    # bathe() - cleans the ninja's pet invoking the pet noise() method
    
    def bathe(self):
        print(f'''{self.pet.name} needs a bath.''')
        print(f'''Scrub scrub!''')
        self.pet.noise()
        return self
        



butters = Pet("Butters","Dog",["Sit","Down","Belly"], 50, 50)


luke = Ninja("Luke", "Thayer", butters, 10, 10)

#luke.walk().feed().bathe()

geoffrey = Cat("Geoff", "Cat", ["Sleep"], 50, 50)

print(geoffrey.name)

luke.pet = geoffrey

luke.bathe()


class Pet:
    def __init__(self, name, type_of_animal, tricks, health, energy):
        self.name = name
        self.type_of_animal = type_of_animal
        self.tricks = tricks
        self.health = health
        self.energy = energy
    
    def energy_up(self, amount):
        difference = 100 - self.energy
        self.energy += amount
        if self.energy > 100:
            self.energy = 100
        if difference < amount:
            print(f'''{self.name} recovered {difference} energy!''')
        else:
            print(f'''{self.name} recovered {amount} energy!''')
        return self
    
    def health_up(self, amount):
        difference = 100 - self.health
        self.health += amount
        if self.health > 100:
            self.health = 100
        if difference < amount:
            print(f'''{self.name} recovered {difference} health!''')
        else:
            print(f'''{self.name} recovered {amount} health!''')
        return self

    def print_energy_health(self):
        print(f'''{self.name} is currently at {self.health}/100 health and {self.energy}/100 energy''')
        
    # sleep() - increases the pets energy by 25
    def sleep(self):
        print(f'''{self.name} is ready for a nap...''')
        self.energy_up(25)
        self.print_energy_health()
        return self
        
    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        print(f'''Let's feed {self.name}!''')
        self.energy_up(5).health_up(10)
        print(f'''{self.name} ate the whole thing.''')
        self.print_energy_health()
        return self
        
    # play() - increases the pet's health by 5
    def play(self):
        print(f'''Play time for {self.name}!''')
        self.health_up(5)
        self.print_energy_health()
        return self
    
    # noise() - prints out the pet's sound
    def noise(self):
        if self.type_of_animal == "Dog":
            print("Woof woof!")
        elif self.type_of_animal == "Cat":
            print("Meow!")
        elif self.type_of_animal == "Bird":
            print("Chirp!")
        elif self.type_of_animal == "Fred":
            print("I'm not your pet, leave me alone.")
        return self
    
class Cat(Pet):
    super().__init__(name, tricks, health, energy, type_of_animal="Cat")
    lives = 9
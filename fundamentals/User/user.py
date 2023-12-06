class User:
    def __init__(self,first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print("First Name: " + self.first_name)
        print("Last Name: " + self.last_name)
        print("Email: " + self.email)
        print("Age: " + str(self.age))
        print("Rewards Member? " + str(self.is_rewards_member))
        print("Gold Card Points: " + str(self.gold_card_points))
        return self

    def enroll(self):
        if self.is_rewards_member == True:
            print("Unable to perform action: Already A Rewards Member")
            return self
        else:
            self.gold_card_points += 200
            self.is_rewards_member = True
            return self

    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("Unable to perform action: Insufficient Points")
            return self
        else:
            self.gold_card_points-=amount
            return self

luke = User("Luke", "Thayer", "lthayer.freelance@gmail.com", 33)
hutch = User("Hutch", "Persons", "unlisted", 32)
kelila = User("Kelila","Kasim", "unlisted", 39)
luke.display_info()
luke.enroll()
print(luke.is_rewards_member)
print(luke.gold_card_points)
luke.spend_points(1)
print(luke.gold_card_points)
luke.spend_points(50)
print(luke.gold_card_points)
hutch.enroll()
hutch.spend_points(80)
luke.display_info()
hutch.display_info()
kelila.display_info()


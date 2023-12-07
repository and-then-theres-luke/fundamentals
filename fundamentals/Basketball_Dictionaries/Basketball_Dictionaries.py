players = [
    {
        "name" : "Kevin Durant",
        "age" : 34,
        "position" : "Small Forward",
        "team" : "Brooklyn Nets",
    },
    {
        "name" : "Jason Tatum",
        "age" : 24,
        "position" : "Small Forward",
        "team" : "Boston Celtics",
    },
    {
        "name" : "Kyrie Irving",
        "age" : 24,
        "position" : "Point Guard",
        "team" : "Brooklyn Nets",
    },
    {
        "name" : "Damien Lillard",
        "age" : 33,
        "position" : "Point Guard",
        "team" : "Portland Trailblazers",
    },
    {
        "name" : "Joel Embiid",
        "age" : 32,
        "position" : "Power Forward",
        "team" : "Philedelphia 76ers",
    },
    {
        "name" : "",
        "age" : 16,
        "position" : "P",
        "team" : "en",
    }
]

class Player:
    
    def __init__(self, dictionary):
        self.name = dictionary["name"]
        self.age = dictionary["age"]
        self.team = dictionary["team"]
        self.position = dictionary["position"]
    
    def print_info(self):
        print(f'''Name: {self.name}''')
        print(f'''Age: {self.age}''')
        print(f'''Team: {self.team}''')
        print(f'''Position: {self.position}''')
    
    @classmethod
    def get_team(cls,team_list):
        new_list = []
        for i in team_list:
            new_list.append(Player(i))
        return new_list


player_roster = []

def construct_objects_from_dictionaries(player_roster, players):
    print("Initializing construction...")
    for i in players:
        player_roster.append(Player(i))
    print("Construction complete.")
    return player_roster

player_roster = construct_objects_from_dictionaries(player_roster, players)

print(player_roster[0].name)

kevin = player_roster[0]
jason = player_roster[1]
kyrie = player_roster[2]

kyrie.print_info()

new_list = Player.get_team(players)

for i in new_list:
    i.print_info()
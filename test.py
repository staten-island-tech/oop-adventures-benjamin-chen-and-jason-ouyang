class wizard:
    def __init__(self, name, atk, defense, range, health):
        self.name = name
        self.atk = atk
        self.defense = defense
        self.range = range
        self.health = health

    def attack(self):
        self.atk == 35
        self.range == 25
        self.defense -= 5
        print(f"{self.name} chanted {user_input}.")
        print(f"{self.name} inflicted {self.atk} damage.")
    
    def defensive_spell(self):
        self.atk += 0
        self.range -= 15
        self.defense += 35

    def ramge_buff(self):
        self.atk -= 34
        self.range += 100
        self.defense -= 10

Wizard = wizard("Wizard", 35, 15, 25, 100)

user_input 
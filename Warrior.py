class warrior: 
    def __init__(self, name, atk, hp):
        self.name = name
        self.atk = atk
        self.hp = hp

    def status(self):
        print(f"Name: {self.name}")
        print(f"Attack: {self.atk} dmg: When HP (Hit_point) falls below 50, {self.name} inflicts {self.atk*2} dmg.")
        print(f"Health: {self.hp}")

    def half_status(self):
        print(f"Attack: {self.atk}")
        print(f"Health: {self.hp}")

    def basic_attack(self):
        if self.hp <= 50:
            self.atk += 25
            print(f"{self.name} went on a rampage dealing {self.atk*2} dmg: [doubled dmg].")
        elif self.hp >= 50:
            self.atk == 25
            self.hp -= 5
            print(f"{self.name} swung his sword dealing {self.atk} dmg: [weak impact].")

    def Lethal_attack(self):
        self.hp -= 25
        self.atk += 75
        print(f"{self.name} charged a Lethal_attack, dealing {self.atk} dmg and is left with {self.hp}: [impactful].")

Warrior = warrior("Warrior", 25, 150)

while True:

    if Warrior.hp <= 0:
        print(f"Warrior has died, hitpoint > 0, [ENDED]:")
        break

    print("1: basic_attack: [Basic_attack] [Enraged: Basic_attack]")
    print("2: Show_Status: [Name] [Attack] [Range] [Health]")
    print("3: Lethal_attack: [Self_Inflicts 25 HP]")

    Warrior_options = int(input("Input an option:"))

    if Warrior_options == 1:
        Warrior.basic_attack()
    if Warrior_options == 2:
        Warrior.status()
    if Warrior_options == 3:
        Warrior.Lethal_attack()
        Warrior.atk -= 75
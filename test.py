class BOSS:
    def __init__(self, name, atk, range, hp):
        self.atk = atk
        self.name = name
        self.range = range
        self.hp = hp

    def attack(self):
        self.atk == 50
        print(f"{self.name} chanted {Game_Input}")
        print(f"Enemy took {self.atk} dmg.")

    def buff(self):
        if self.hp <= 200:
            self.atk += 50
            print("Damage Triggered.")
    
    def health_point(self):
        if self.hp >= 0 and self.hp <= 50:
            self.hp += 100 
            print(f"{self.name} triggered Rampage")

    def health_death(self):
        if self.hp >= 0:
            print(f"{self.name} has died...")

Morph = BOSS("Morph", 50, 50, 500)     #Morph = BOSS("Morph", 50, 50, 500)

while True:

    print("1: attack")

    Inputs_input = int(input("Enter an option:"))

    if Inputs_input == 1:
        Game_Input = input("Input a spell:")
        Morph.attack()

class wizard:
    def __init__(self, name, atk, health):
        self.name = name
        self.atk = atk
        self.health = health

    def attack(self):
        if self.health <= 25 and self.health >= 2:
            print(f"{self.name} inflicted {self.atk*2}: [DOUBLE DMG]")
        elif self.health >= 50:
            self.atk == 25
            print(f"{self.name} unleased a {user_input}: INFLICTED {self.atk} dmg.")
        elif self.health == 0:
            print(f"{self.name} activated self destruct:{self.atk*4} dmg:")

    def Status(self):
        print(f"Name: {self.name}")
        print(f"Attack [DMG]: {self.atk}, {self.atk*2}, {self.atk*4}")
        print(f"Health: {self.health}")
        

Wizard = wizard("Wizard", 25, 50)

while True:

    print("1: atk")
    print("2: Status")

    Inputs = int(input("Input an option:"))

    if Inputs == 1:
        user_input = input("Input a spell.")
        if Wizard.health > 0:
            Wizard.attack()
        if Wizard.health == 0:
            print("Would you like to...?")
            print("1: Yes")
            print("2: Yes")
            Game_input = int(input("Input a number:"))
            if Game_input == 1 or 2:
                Wizard.attack()
                print("Wizard has died : Game Restart :")
                break
    elif Inputs == 2: 
        Wizard.Status()

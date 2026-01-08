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
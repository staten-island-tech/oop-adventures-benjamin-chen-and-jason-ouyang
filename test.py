class BOSS:
    def __init__(self, atk, range, hp):
        self.atk = atk
        self.range = range
        self.hp = hp

    def attack(self):
        self.atk == 50
        print(f"{self.name} chanted {Game_Input}")

    def buff(self):
        if self.hp <= 200:
            self.atk += 50
            print("Damage Triggered.")
    
    def health_point(self):
        if self.hp >= 0 and self.hp <= 50:
            self.hp += 100 
            print(f"{self.name} triggered Rampage")

Morph = BOSS("Morph", 50, 50, 500)

while True:

    print("1: attack")

    Enter = int(input("Enter an option:"))

    if Enter == 1:
        Game_Input = input("Input a spell:")
        Morph.atk()
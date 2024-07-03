import random

class character:
    def __init__(self, name, atk, damage, ac, hp, credits):
        self.name = name
        self.atk = atk
        self.damage = damage
        self. ac = ac
        self.hp = hp
        self.credits = credits

    def update_hp(self, value_int):
        hp_int = int(self.hp)
        hp_int = hp_int + value_int
        hp_string = str(hp_int)
        self.hp = hp_string
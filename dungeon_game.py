import random

class Player():
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.mana = 100
        self.damage = 3

class Monster():
    def __init__(self, name, hp, mana):
        Player.__init__(self, name)
        self.hp = hp
        

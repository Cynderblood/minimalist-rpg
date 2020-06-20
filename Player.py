from Level import *

###    Races    ###
class Player:
    def __init__(self, name):
        self.name = name

class Race(Player):
    def __init__(self, race, stats):
        self.race = race
        self.stats = stats

class Human(Race, Level):
    def __init__(self):
        super(Race).__init__('Human', {'strength': 5, 'agility': 4, 'intelligence': 6})
        self.Class = None
        self.specialization = None
        self.level = 1
        self.xp = 0
        self.mainStats = ['strength', 'agility']
        super(Level).__init__(self)
        self.strength = self.stats['strength']
        self.agility = self.stats['agility']
        self.intelligence = self.stats['intelligence']
        self.hp = self.strength * 20
        self.damage = (self.strength + self.agility) * 3
        self.skills = []
        self.items = []
        self.coins = []

    def updateStats(self):
        self.hp = self.strength * 20
        self.damage = (self.strength + self.agility) * 3

class Elf(Race, Level):
    def __init__(self):
        super(Race).__init__('Elf', {'strength': 3, 'agility': 5, 'intelligence': 6})
        self.Class = None
        self.specialization = None
        self.level = 1
        self.xp = 0
        self.mainStats = ['agility', 'intelligence']
        super(Level).__init__(self)
        self.strength = self.stats['strength']
        self.agility = self.stats['agility']
        self.intelligence = self.stats['intelligence']
        self.hp = self.strength * 20
        self.damage = (self.agility + self.intelligence) * 3
        self.skills = []
        self.items = []
        self.coins = []

    def updateStats(self):
        self.hp = self.strength * 20
        self.damage = (self.agility + self.intelligence) * 3

class Orc(Race, Level):
    def __init__(self):
        super(Race).__init__('Orc', {'strength': 6, 'agility': 2, 'intelligence': 4})
        self.Class = None
        self.specialization = None
        self.level = 1
        self.xp = 0
        self.mainStats = ['strength', 'intelligence']
        super(Level).__init__(self)
        self.strength = self.stats['strength']
        self.agility = self.stats['agility']
        self.intelligence = self.stats['intelligence']
        self.hp = self.strength * 20
        self.damage = (self.strength + self.intelligence) * 3
        self.skills = []
        self.items = []
        self.coins = []

    def updateStats(self):
        self.hp = self.strength * 20
        self.damage = (self.strength + self.intelligence) * 3

class Gnome(Race, Level):
    def __init__(self):
        super(Race).__init__('Human', {'strength': 5, 'agility': 4, 'intelligence': 5})
        self.Class = None
        self.specialization = None
        self.level = 1
        self.xp = 0
        self.mainStats = ['strength', 'intelligence']
        super(Level).__init__(self)
        self.strength = self.stats['strength']
        self.agility = self.stats['agility']
        self.intelligence = self.stats['intelligence']
        self.hp = self.strength * 20
        self.damage = (self.strength + self.agility) * 3
        self.skills = []
        self.items = []
        self.coins = []

    def updateStats(self):
        self.hp = self.strength * 20
        self.damage = (self.strength + self.agility) * 3


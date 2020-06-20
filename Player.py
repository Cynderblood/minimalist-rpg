from Level import *

###    Races    ###
class Player:
    def __init__(self, name):
        self.name = name
    def pick_race(self):
        races_list = [Human(), Elf(), Orc(), Gnome()]
        races_text = ['Human', 'Elf', 'Orc', 'Gnome']
        while True:
            print('Choose your character\'s race:')
            for i in range(1, len(races_text) + 1):
                print('{}) {}'.format(i, races_text[i - 1]))
            choose = int(input('>> '))
            if choose >= 1 and choose <= 4:
                return races_list[choose - 1]
            else:
                print('Write num from 1 to 3')
                continue

class Race(Player):
    def __init__(self, race, stats):
        self.race = race
        self.stats = stats

class Human(Race, Level):
    def __init__(self):
        super(Human, self).__init__(race='Human', stats={'strength': 5, 'agility': 4, 'intelligence': 6})
        self.Class = None
        self.specialization = None
        self.level = 1
        self.xp = 0
        self.mainStats = ['strength', 'agility']
        super(Level, self).__init__()
        self.strength = self.stats['strength']
        self.agility = self.stats['agility']
        self.intelligence = self.stats['intelligence']
        self.hp = self.strength * 20
        self.damage = (self.strength + self.agility) * 3
        self.items = []
        self.coins = []

    def updateStats(self):
        self.hp = self.strength * 20
        self.damage = (self.strength + self.agility) * 3

    def pickClass(self):
        main_classes = [Warrior(), Mage(), Assasin(), Archer(), Berserk()]
        text_classes = ['Warrior', 'Mage', 'Assasin', 'Archer', 'Berserk']
        while True:
            counter = 1
            for i in range(5):
                print('{}) {}'.format(counter, text_classes[i]))
                counter += 1
            try:
                choose = int(input('Choose your class: '))
                if choose >= 1 and choose <= len(main_classes):
                    pass
                else:
                    print('Write number from 1 to {}'.format(len(main_classes)))
                    continue
            except:
                print('Write number!')

            self.Class = main_classes[choose - 1]
            print('You chose {}.'.format(text_classes[choose - 1]))
class Elf(Race, Level):
    def __init__(self):
        super(Elf, self).__init__('Elf', {'strength': 3, 'agility': 5, 'intelligence': 6})
        self.Class = None
        self.specialization = None
        self.level = 1
        self.xp = 0
        self.mainStats = ['agility', 'intelligence']
        super(Level, self).__init__()
        self.strength = self.stats['strength']
        self.agility = self.stats['agility']
        self.intelligence = self.stats['intelligence']
        self.hp = self.strength * 20
        self.damage = (self.agility + self.intelligence) * 3
        self.items = []
        self.coins = []

    def updateStats(self):
        self.hp = self.strength * 20
        self.damage = (self.agility + self.intelligence) * 3

    def pickClass(self):
        main_classes = [Warrior(), Mage(), Assasin(), Archer(), Berserk()]
        text_classes = ['Warrior', 'Mage', 'Assasin', 'Archer', 'Berserk']
        while True:
            counter = 1
            for i in range(5):
                print('{}) {}'.format(counter, text_classes[i]))
                counter += 1
            try:
                choose = int(input('Choose your class: '))
                if choose >= 1 and choose <= len(main_classes):
                    pass
                else:
                    print('Write number from 1 to {}'.format(len(main_classes)))
                    continue
            except:
                print('Write number!')

            self.Class = main_classes[choose - 1]
            print('You chose {}.'.format(text_classes[choose - 1]))
class Orc(Race, Level):
    def __init__(self):
        super(Orc, self).__init__('Orc', {'strength': 6, 'agility': 2, 'intelligence': 4})
        self.Class = None
        self.specialization = None
        self.level = 1
        self.xp = 0
        self.mainStats = ['strength', 'intelligence']
        super(Level, self).__init__()
        self.strength = self.stats['strength']
        self.agility = self.stats['agility']
        self.intelligence = self.stats['intelligence']
        self.hp = self.strength * 20
        self.damage = (self.strength + self.intelligence) * 3
        self.items = []
        self.coins = []

    def updateStats(self):
        self.hp = self.strength * 20
        self.damage = (self.strength + self.intelligence) * 3

    def pickClass(self):
        main_classes = [Warrior(), Mage(), Assasin(), Archer(), Berserk()]
        text_classes = ['Warrior', 'Mage', 'Assasin', 'Archer', 'Berserk']
        while True:
            counter = 1
            for i in range(5):
                print('{}) {}'.format(counter, text_classes[i]))
                counter += 1
            try:
                choose = int(input('Choose your class: '))
                if choose >= 1 and choose <= len(main_classes):
                    pass
                else:
                    print('Write number from 1 to {}'.format(len(main_classes)))
                    continue
            except:
                print('Write number!')

            self.Class = main_classes[choose - 1]
            print('You chose {}.'.format(text_classes[choose - 1]))
class Gnome(Race, Level):
    def __init__(self):
        super(Gnome, self).__init__('Gnome', {'strength': 5, 'agility': 4, 'intelligence': 5})
        self.Class = None
        self.specialization = None
        self.level = 1
        self.xp = 0
        self.mainStats = ['strength', 'intelligence']
        super(Level, self).__init__()
        self.strength = self.stats['strength']
        self.agility = self.stats['agility']
        self.intelligence = self.stats['intelligence']
        self.hp = self.strength * 20
        self.damage = (self.strength + self.intelligence) * 3
        self.items = []
        self.skills = []
        self.coins = []

    def updateStats(self):
        self.hp = self.strength * 20
        self.damage = (self.strength + self.agility) * 3

    def pickClass(self):
        main_classes = [Warrior(), Mage(), Assasin(), Archer(), Berserk()]
        text_classes = ['Warrior', 'Mage', 'Assasin', 'Archer', 'Berserk']
        while True:
            counter = 1
            for i in range(5):
                print('{}) {}'.format(counter, text_classes[i]))
                counter += 1
            try:
                choose = int(input('Choose your class: '))
                if choose >= 1 and choose <= len(main_classes):
                    pass
                else:
                    print('Write number from 1 to {}'.format(len(main_classes)))
                    continue
            except:
                print('Write number!')

            self.Class = main_classes[choose - 1]
            print('You chose {}.'.format(text_classes[choose - 1]))

    def AddClassBonuses(self):
        self.strength += self.Class.additional_strength
        self.agility += self.Class.additional_agility
        self.intelligence += self.Class.additional_intelligence
        self.skills = self.Class.skills

class PlayerClass:
    def __init__(self, str, agl, intel, skills=None, bonuses=None):
        self.additional_strength = str
        self.additional_agility = agl
        self.additional_intelligence = intel
        self.skills = skills
        self.bonuses = bonuses


class Warrior(PlayerClass):
    def __init__(self):
        super().__init__(5, 5, 5)


class Mage(PlayerClass):
    def __init__(self):
        super().__init__(5, 5, 5)


class Assasin(PlayerClass):
    def __init__(self):
        super().__init__(5, 5, 5)


class Archer(PlayerClass):
    def __init__(self):
        super().__init__(5, 5, 5)


class Berserk(PlayerClass):
    def __init__(self):
        super().__init__(5, 5, 5)

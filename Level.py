from random import *
class Level:
    def __init__(self, player):
        self.xpBoost = 0
        self.XpToNextLevel = player.level * 1000
        self.isLevelUp = False

    def LevelUp(self, player):
        if player.xp >= self.XpToNextLevel and not self.isLevelUp:
            self.UpdateLevel(player)
        self.isLevelUp = False

    def BoostXP(self, player, gotXp):
        player.xp += self.xpBoost * gotXp

    def UpdateLevel(self, player):
        player.xp = 0
        player.strength += 3
        player.agility += 3
        player.intelligence += 3
        player.level += 1
        self.XpToNextLevel = player.level * 1000
        self.isLevelUp = True
        player.updateStats()
'''
File:PyroMage.py
Description:
Author:Lv Yifan
StudentID: 2218040126
This is my own work as defined by the University's Academic Misconduct Policy
'''
from Mage import Mage
class PyroMage(Mage):
    '''
    火焰法师具有一个 flameBoost 值，可以增加他们的伤害。
    如果火焰法师有 40 或更多的魔法值，他们将施放超级加热 (SuperHeat)。
    如果他们的魔法值少于 40 但多于 10，他们将施放火焰爆裂 (FireBlast)。
    每次火焰法师施放法术时，他们还会根据他们的回复速度 (regenValue) 恢复魔法值。
    '''

    def __init__(self, name, maxHealth, strength, defense, ranged, magic):
        super().__init__(name, maxHealth, strength, defense, ranged, magic)
        self.__flameBoost = 1
    def castSpell(self):
        if self.mana >= 40:
            return self.castSuperHeat()
        elif self.mana >= 10:
            return self.castFireBlast()
        else:
            return 0
    def castFireBlast(self):
        self.mana -= 10
        return (self.strength * self.flame_boost) + 10
    def castSuperHeat(self):
        self.mana -= 40
        self.flame_boost += 1
        return (self.strength * self.flame_boost)

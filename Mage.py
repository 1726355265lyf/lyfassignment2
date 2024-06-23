'''
File:Mage.py
Description:
Author:Lv Yifan
StudentID: 2218040126
This is my own work as defined by the University's Academic Misconduct Policy
'''
from Combatant import Combatant
from abc import ABC ,abstractmethod
class Mage(Combatant,ABC):
    '''
    法师必须专攻火焰魔法或冰霜魔法。不管选择哪种魔法，他们都有两个独特的属性：
    魔法值 (mana)：他们的魔法等级
    回复速度 (regenRate)：魔法等级 / 4
    每种法师类施放法术的方式不同，但都通过 castSpell 方法计算他们的魔法强度。
    resetValues 方法应同时重置他们的魔法值。
    '''
    def __init__(self,name, maxHealth, strength, defense, magic, ranged):
        self._mana = magic
        self._regenRate = magic / 4
        super().__init__(name, maxHealth, strength, defense, magic, ranged)
    def calculatePower(self):
        return self.castSpell()
    @abstractmethod
    def castSpell(self):
        raise TypeError("")
    def resetValues(self):
        super().resetValues()
        self.mana = self.magic

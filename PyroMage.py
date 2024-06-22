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
    def __init__(self,flameBoost):
        self.__flameBoost = flameBoost
    def castSpell(self):
        pass
    def castFireBlast(self):
        pass
    def castSuperHeat(self):
        pass

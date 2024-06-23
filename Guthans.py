'''
File:Guthans.py
Description:
Author:Lv Yifan
StudentID: 2218040126
This is my own work as defined by the University's Academic Misconduct Policy
'''
from Warrior import Warrior
class Guthans(Warrior):
    '''
    在战斗中治愈的有福战士!
    古萨人每次计算自己的攻击力量时，治疗自己的力量等级/5。
    '''
    def __init__(self,name,maxHealth,strength,defense,ranged,magic,armourValue):
        super().__init__(name,maxHealth,strength,defense,ranged, magic,armourValue)
    def calculatePower(self):
        power = super().calculatePower()
        self.heal()
        return power

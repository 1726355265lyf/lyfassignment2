'''
File:Dharok.py
Description:
Author:Lv Yifan
StudentID: 2218040126
This is my own work as defined by the University's Academic Misconduct Policy
'''
from Warrior import Warrior
class Dharok(Warrior):
    '''
    受祝福的战士，血量越少造成的伤害越大达罗克每失去一个生命值，就会造成额外伤害(如果治疗过度，就会失去
    伤害!)
    '''
    def __init__(self,name,maxHealth,strength,defense,ranged,magic,armourValue):
        super().__init__(name,maxHealth,strength,defense,ranged, magic,armourValue)
    def calculatePower(self):
        missing_health = self.max_health - self.health
        return super().calculatePower() + missing_health

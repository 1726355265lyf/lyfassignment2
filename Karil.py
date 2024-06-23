'''
File:Karil.py
Description:
Author:Lv Yifan
StudentID: 2218040126
This is my own work as defined by the University's Academic Misconduct Policy
'''
from Warrior import Warrior
class Karil(Warrior):
    '''
    一个被祝福的战士，利用他们的远程技能来提高他们的能力。
    除了战士通常的手段外，卡里尔还会根据他们的射程等级来提高他们的伤害。
    '''
    def __init__(self,name,maxHealth,strength,defense,ranged,magic,armourValue):
        super().__init__(name,maxHealth,strength,defense,ranged, magic,armourValue)
    def calculatePower(self):
        """
        计算 Karil 的战斗力。Karil 的战斗力由其战士的力量等级和射程等级共同决定。
        """
        return self._strength + self._ranged


    def details(self):
        return f"{self.name} is a Karil and has the following stats \nHealth:{self.getHealth()}\nStrength:{self.getStrength()}\ndefense:{self.getDefense()}\nMagic:{self.getMagic()}\nRanged:{self.getRanged()}\n"
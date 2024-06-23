'''
File:Ranger.py
Description:
Author:Lv Yifan
StudentID: 2218040126
This is my own work as defined by the University's Academic Misconduct Policy
'''
from Combatant import Combatant
class Ranger(Combatant):
    '''
    游侠有 3 支箭，可以射出造成大量伤害。
    如果游侠射出了最后一支箭，屏幕上应显示一条消息。
    重置游侠的值会将箭数重置为 3。
    '''
    def __init__(self,name, maxHealth, strength, defense, magic, ranged):
        super().__init__(name, maxHealth, strength, defense, magic, ranged)
    def calculatePower(self):
        if self.arrows > 0:
            return self.ranged
        else:
            return self.strength
    def resyValues(self):
        super().resetValues()
        self.arrows = 3  # Reset arrows to 3

    def details(self):
        return f"{self.name} is a Ranger and has the following stats \nHealth:{self.getHealth()}\nStrength:{self.getStrength()}\ndefense:{self.getDefense()}\nMagic:{self.getMagic()}\nRanged:{self.getRanged()}\n"
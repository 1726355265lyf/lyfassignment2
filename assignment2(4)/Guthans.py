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
        if super().getHealth() >0:
            super().setHealth(int(super().getHealth()+super().getStrength()/5))
            print(f"The power of Guthans activates healing {self.name} for {int(super().getStrength()/5)}")
        return power
    def takeDamage(self,damage):
        if super().getarmoutValue() > 0:
            print(f"{self.name}'s arrmour blocked {super().getarmoutValue()} damage!")
            damage -= super().getarmoutValue()

            super().setarmoutValue(super().getarmoutValue()-5)
            if super().getarmoutValue() < 0:
                super().setarmoutValue(0)
            if super().getarmoutValue() == 0:
                print( "Armour  shattered!")
        actual_damage = max(0, damage - self.getDefense())
        if (self.getHealth()- actual_damage) > 0:
            self.setHealth(self.getHealth()- actual_damage)
            if actual_damage > 0:
                print(f"{self.name}’s defence level blocked {self.getDefense()} damage")
                print(f"{self.name} took {actual_damage} damage and has {self.getHealth()} health remaining\n")
        else:
            self.setHealth(-1)
            print(f"{self.name}’s defence level blocked {self.getDefense()} damage")
            print(f"{self.name} has been knocked out!\n")
    def attackEnemy(self,enemy):
        damage = self.calculatePower()
        print(f"{self.name} attacks for {damage} damage!")

        enemy.takeDamage(damage)

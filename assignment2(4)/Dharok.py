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
        missing_health = super().getMaxHealth() - super().getHealth()
        print(f"The power of Dharok activates adding {super().getMaxHealth() - super().getHealth()} damage")
        return super().calculatePower() + missing_health
    def takeDamage(self,damage):

        if super().getarmoutValue() > 0:
            print(f"{self.name}'s arrmour blocked {super().getarmoutValue()} damage")
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
            print(f"{self.name} has been knocked out!")

    def attackEnemy(self,enemy):
        damage = self.calculatePower()
        print(f"{self.name} attacks for {damage} damage!")

        enemy.takeDamage(damage)



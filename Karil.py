'''
File:Karil.py
Description:Karil
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

        base_power = super().calculatePower()
        return base_power + self.getRanged()


    def details(self):
        return f"{self.name} is a Karil and has the following stats \nHealth:{self.getHealth()}\nStrength:{self.getStrength()}\ndefense:{self.getDefense()}\nMagic:{self.getMagic()}\nRanged:{self.getRanged()} \n"

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
                print(f"The power of Karil activates adding {self.getRanged()} damage!")
        else:
            self.setHealth(-1)
            print(f"{self.name} has been knocked out!")

    def attackEnemy(self, enemy):
        damage = self.calculatePower()
        print(f"{self.name} attacks for {damage} damage!")

        enemy.takeDamage(damage)


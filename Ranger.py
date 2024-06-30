'''
File:Ranger.py
Description:Ranger
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
        self.arrows = 3


    def calculatePower(self):
        if self.arrows > 0:
            self.arrows -= 1
            damage = self.getRanged()
            if self.arrows == 0:
                print(f"")
            return damage
        else:
            return self.getStrength()

    def resetValues(self):
        super().resetValues()
        self.arrows = 3
    def attackEnemy(self,enemy):
        damage = self.calculatePower()
        print(f"{self.name} attacks for {damage} damage")

        enemy.takeDamage(damage)
    def takeDamage(self,damage):
        actual_damage = max(0, damage - self.getDefense())
        if (self.getHealth() - actual_damage) > 0:
            self.setHealth(self.getHealth() - actual_damage)
            if actual_damage > 0:
                print(f"{self.name}’s defence level blocked {self.getDefense()} damage!")
                print(f"{self.name} took {actual_damage} damage and has {self.getHealth()} health remaining\n")
            else:

                print("'Ting' 0 damage!\n")
        else:
            print(f"{self.name} has been knocked out!")
            self.setHealth(-1)
    def details(self):
        return f"{self.name} is a Ranger and has the following stats \nHealth:{self.getHealth()}\nStrength:{self.getStrength()}\ndefense:{self.getDefense()}\nMagic:{self.getMagic()}\nRanged:{self.getRanged()}\n "


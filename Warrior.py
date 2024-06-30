'''
File:Warrior.py
Description:
Author:Lv Yifan
StudentID: 2218040126
This is my own work as defined by the University's Academic Misconduct Policy
'''
from Combatant import Combatant
class Warrior(Combatant):
    '''
    一个专注于力量的战斗人员。
    战士装备有护甲，除了他们的防御等级外，这个护甲还可以减少他们受到的伤害。
    每次战士受到伤害时，护甲会减少5点，并在护甲破碎时显示适当的消息。
    重置战士时，他们的护甲值将恢复到10。
    战士通过他们的力量等级来计算他们的战斗力。
    '''
    def __init__(self,name,maxHealth,strength,defense,magic,ranged,armourValue):

        super().__init__(name,maxHealth,strength,defense,magic,ranged)
        self.__armourValue = armourValue
    def calculatePower(self):
        """计算战士的战斗力。战士的战斗力由他们的力量等级决定。"""
        return self.getStrength()
    def takeDamage(self,damage):
        """计算战斗人员受到的实际伤害并减少健康值。护甲值每次减少 5。"""
        if self.__armourValue > 0:
            print(f"{self.name}'s arrmour blocked 5 damage")
            damage -= self.__armourValue

            self.__armourValue -= 5
            if self.__armourValue < 0:
                self.__armourValue = 0
            if self.__armourValue == 0:
                print( "Armour  shattered!")
        actual_damage = max(0, damage - self.getDefense())
        if (self.getHealth() - actual_damage) > 0:
            self.setHealth(self.getHealth() - actual_damage)
            if actual_damage > 0:
                print(f"{self.name}’s defence level blocked {self.getDefense()} damage")
                print(f"{self.name} took {actual_damage} damage and has {self.getHealth()} health remaining ")
            else:
                print(f"{self.name}’s defence level blocked {self.getDefense()} damage")
                print("'Ting' 0 damage!\n")
        else:
            print(f"{self.name} has been knocked out!")
    def attackEnemy(self,enemy):
        damage = self.calculatePower()
        print(f"{self.name} attacks for {damage} damage")
        print(f"{enemy.name}’s defence level blocked {enemy.getDefense()} damage")
        enemy.takeDamage(damage)
    def restValues(self):
        super().resetValues()
        self.__armourValue = 10
    def setarmoutValue(self,armouValue):
        self.__armourValue = armouValue
    def getarmoutValue(self):
        return self.__armourValue
    def details(self):
        return f"{self.name} is a Warrior and has the following status \nHealth:{self.getHealth()}\nStrength:{self.getStrength()}\ndefense:{self.getDefense()}\nMagic:{self.getMagic()}\nRanged:{self.getRanged()}装价值{self.getarmoutValue()}\n"


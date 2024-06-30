'''
File:Combatant.py
Description:Combatant
Author:Lv Yifan
StudentID: 2218040126
This is my own work as defined by the University's Academic Misconduct Policy
'''
class Combatant:
    '''
    战斗人员
    战斗人员是可以在竞技场中战斗的角色。每个战斗人员都有一组属性，用于确定他们造成或受到的伤害。
    战斗人员可以通过计算他们将造成的伤害量并将其施加给敌人来攻击敌人。然而，每个战斗人员角色计算其伤害的方式不同。
    所有战斗人员在基础层面上以相同的方式受到伤害： 伤害 - 防御等级
    如果没有受到伤害，或者战斗人员被击倒，应显示适当的消息。
    重置应将他们的生命值恢复到最大值。
    Details方法返回一个包含战斗人员的名字、类别和属性的字符串。
    '''
    def __init__(self,name,maxHealth,strength,defense,magic,ranged):
        self.name = name
        self.__maxHealth = maxHealth
        self.__health = maxHealth
        self.__strength = strength
        self.__defense = defense
        self.__magic = magic
        self.__ranged = ranged


    def details(self):
        return f"Name:{self.name},Health:{self.__health},Strength:{self.__strength},Defense:{self.__defense},Magic:{self.__magic},Ranged:{self.__ranged}"
    def calculatePower(self):
        return self.__strength
    def attackEnemy(self,enemy):
        damage = self.calculatePower()
        print(f"{self.name} attacks for {damage} damage")

        enemy.takeDamage(damage)

    def takeDamage(self, damage):

        damage = damage - self.__defense

        if damage > 0:
            if (self.getHealth() - damage)>0:
                print(f"{self.name}’s defence level blocked {self.getDefense()} damage")
                print(f"{self.name} took {damage} damage and has {self.getHealth()} remaining\n")
            else:
                print(f"{self.name}’s defence level blocked {self.getDefense()} damage")
                print(f"{self.name} has been knocked out!")
        else:
            print(f"'TIng' 0 damage!\n")
            damage = 0
        self.setHealth(self.getHealth() - damage)
    def resetValues(self):
        self.__health = self.__maxHealth
    def getMaxHealth(self):
        return self.__maxHealth
    def getHealth(self):
        return self.__health
    def setHealth(self,hp):
        self.__health = hp
    def getStrength(self):
        return self.__strength
    def getDefense(self):
        return self.__defense
    def getRanged(self):
        return self.__ranged
    def getMagic(self):
        return self.__magic
'''
File:Arena.py
Description:
Author:Lv Yifan
StudentID: 2218040126
This is my own work as defined by the University's Academic Misconduct Policy
'''
from Field import Field
from Combatant import Combatant
class Arena:
    '''
    竞技场类是所有动作发生的地方。
    一个竞技场包含一个战斗人员列表和一个在竞技场创建时确定的场地。
    并且能够添加和移除竞技场中的战斗人员。
    '''
    def __init__(self,name):
        self.filed = Field(name)
        self.combatants = []
    def addCombatant(self,fighter):
        if fighter not in self.combatants:
            self.combatants.append(fighter)
            print(f"{fighter.name} was added to {self.filed.name}")
    def removeCombatant(self,fighter):
        '''
        list方法显示所有战斗人员的详细信息。
        '''
        if fighter not in self.combatants:
            self.combatants.remove(fighter)
    def listCombatants(self):
        for fighter in self.combatants:
            print(fighter.details())
    def restoreCombatants(self):
        '''
        restore方法重置所有战斗人员。
        '''
        for fighter in self.combatants:
            fighter.health = fighter.maxHealth
    def checkValidCombatant(self,fighter):
        if fighter in self.combatants:
            return True
        else:
            return False
    def duel(self,fighter1,fighter2):
        print(f"----- Battle has taken place in {self.filed.name} on the Castle Walls between {fighter1.name} and {fighter2.name} -----\n")
        print("Round 1")



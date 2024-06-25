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
        self.field = Field(name)
        self.combatants = []
    def addCombatant(self,fighter):
        if fighter not in self.combatants:
            self.combatants.append(fighter)
            print(f"{fighter.name} was added to {self.field.name}")
        elif fighter.getHealth() <= 0:
            print(f"{fighter.name} has no health to battle")
    def removeCombatant(self,fighter):
        if fighter not in self.combatants:
            print(f"{fighter.name} cannot be removed as they were not found in the arena")
        elif fighter in self.combatants:
            print(f"{fighter.name} was removed from {self.field.name}")
            self.combatants.remove(fighter)
    def listCombatants(self):
        for fighter in self.combatants:
            print(fighter.details())
    def restoreCombatants(self):
        '''
        restore方法重置所有战斗人员。
        '''
        print("----- RESTING -----")
        for fighter in self.combatants:
            fighter.setHealth(fighter.getMaxHealth())
    def checkValidCombatant(self,fighter):
        if fighter in self.combatants:
            return True
        else:
            return False
    def duel(self,fighter1,fighter2):
         if fighter1 in self.combatants and fighter2 in self.combatants:
            if fighter1.getHealth()> 0 and fighter2.getHealth() > 0:
                print(f"----- Battle has taken place in {self.field.name} on the Castle Walls between {fighter1.name} and {fighter2.name} -----\n")
                round_count = 1
                while fighter1.getHealth()> 0 and fighter2.getHealth() > 0 and round_count <= 10:
                    print(f"Round {round_count}\n")
                    if self.field.name == "Castle Walls":
                        pass
                    self.field.fieldEffect(fighter1,fighter2)
                    fighter1.attackEnemy(fighter2)
                    fighter2.attackEnemy(fighter1)
                    round_count += 1
                    if round_count==11:
                        print("The battle ran out of time!")
                print(f"---------- END BATTLE ----------")
            elif fighter1.getHealth() <= 0:
                print(f"{fighter1.name} has no health to battle")
            elif fighter2.getHealth() <= 0:
                print(f"{fighter2.name} has no health to battle")
         elif fighter1 not in self.combatants:
             print(f"{fighter1.name} was not found in {self.field.name}'s list of fighters")

         elif fighter2 not in self.combatants:
             print(f"{fighter2.name} was not found in {self.field.name}'s list of fighters")


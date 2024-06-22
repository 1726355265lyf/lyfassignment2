'''
File:Arena.py
Description:
Author:Lv Yifan
StudentID: 2218040126
This is my own work as defined by the University's Academic Misconduct Policy
'''
class Arena:
    '''
    竞技场类是所有动作发生的地方。
    一个竞技场包含一个战斗人员列表和一个在竞技场创建时确定的场地。
    并且能够添加和移除竞技场中的战斗人员。
    '''
    def __int__(self,name,combatants,filed):
        self.name = name
        self.combatants = combatants
        self.filed = filed
    def addCombatant(self):
        pass
    def removeCombatant(self):
        '''
        list方法显示所有战斗人员的详细信息。
        '''
        pass
    def listCombatants(self):
        pass
    def restoreCombatants(self):
        '''
        restore方法重置所有战斗人员。
        '''
        pass
    def checkValidCombatant(self):
        pass
    def duel(self):
        pass


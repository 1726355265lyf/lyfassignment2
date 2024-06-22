'''
File:Arena.py
Description:
Author:Lv Yifan
StudentID: 2218040126
This is my own work as defined by the University's Academic Misconduct Policy
'''
class Arena:
    '''
    战斗人员
    战斗人员是可以在竞技场中战斗的角色。每个战斗人员都有一组属性，用于确定他们造成或受到的伤害。
    战斗人员可以通过计算他们将造成的伤害量并将其施加给敌人来攻击敌人。然而，每个战斗人员角色计算其伤害的方式不同。
    所有战斗人员在基础层面上以相同的方式受到伤害： 伤害 - 防御等级
    如果没有受到伤害，或者战斗人员被击倒，应显示适当的消息（请参阅本文档末尾的示例）。
    重置应将他们的生命值恢复到最大值。
    Details方法返回一个包含战斗人员的名字、类别和属性的字符串。
    '''
    def __int__(self,name,combatants,filed):
        self.name = name
        self.combatants = combatants
        self.filed = filed
    def addCombatant(self):
        pass
    def removeCombatant(self):
        pass
    def listCombatants(self):
        pass
    def restoreCombatants(self):
        pass
    def checkValidCombatant(self):
        pass
    def duel(self):
        pass


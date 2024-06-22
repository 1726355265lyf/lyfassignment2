'''
File:Warrior.py
Description:
Author:Lv Yifan
StudentID: 2218040126
This is my own work as defined by the University's Academic Misconduct Policy
'''
import Combatant
class Warrior(Combatant):
    '''
    一个专注于力量的战斗人员。
    战士装备有护甲，除了他们的防御等级外，这个护甲还可以减少他们受到的伤害。
    每次战士受到伤害时，护甲会减少5点，并在护甲破碎时显示适当的消息。
    重置战士时，他们的护甲值将恢复到10。
    战士通过他们的力量等级来计算他们的战斗力。
    '''
    def __int__(self,armourValue):
        self.__armourValue = armourValue
    def calculatePower(self):
        pass
    def takeDamage(self):
        pass
    def restValues(self):
        pass


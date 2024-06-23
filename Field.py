'''
File:Field.py
Description:
Author:Lv Yifan
StudentID: 2218040126
This is my own work as defined by the University's Academic Misconduct Policy
'''
import random
class Field:
    '''
    场地类
    场地类包含场地的名称。场地类型在类创建时确定，并且可以通过调用 changeField 方法进行修改，该方法随机选择3个场地中的一个。这三种随机场地类型及其效果如下：
    毒性荒地 – 每个战斗人员受到5点伤害，无视任何防御
    疗愈草地 – 每个战斗人员恢复5点生命值（这可以超过他们的最大生命值）
    城墙 – 无效果
    '''
    def __init__(self, name):
        self.name = name
    def changeField(self):
        fileds = list["Toxic Wasteland","Healing Meadows","Castle Walls"]
        self.filed = random.choice(fileds)
        return self.filed
    def fieldEffect(self):
        pass
    def getName(self):
        return self.name
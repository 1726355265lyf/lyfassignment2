'''
File:FrostMage.py
Description:
Author:Lv Yifan
StudentID: 2218040126
This is my own work as defined by the University's Academic Misconduct Policy
'''
from Mage import Mage
class FrostMage(Mage):
    '''
    冰霜法师具有一个名为 iceBlock 的属性，当该属性激活时，可以将下一次攻击的所有伤害减少到0
    冰块在阻挡一次攻击后会消失。每次冰霜法师受到攻击时，即使他们没有受到任何伤害，他们也会根据其 regenValue 恢复魔法值。
    冰霜法师可以施放两种不同的法术。如果冰霜法师有50点魔法值，他们可以设置一个冰块。
    如果他们的魔法值少于50但多于10，他们将施放冰霜弹幕。
    冰块 (IceBlock)：消耗50点魔法值，设置 iceBlock 属性为 True
    冰霜弹幕 (IceBarrage)：消耗10点魔法值，额外造成30点伤害
    '''
    def __init__(self,name,maxHealth,strength,defense,ranged,magic):
        super().__init__(name,maxHealth,strength,defense,ranged, magic)
        self.__iceBlock = False
    def takeDamage(self,damage):
        if self.ice_block:
            damage = 0
            self.ice_block = False
        else:
            damage = max(0, damage - self.defense)

        super().takeDamage(damage)
        # Regenerate mana based on regen_rate
        self.mana += self.regen_rate
    def castSpell(self):
        if self.mana >= 50:
            return self.iceBlock()
        elif self.mana >= 10:
            return self.iceBarrage()
        else:
            return 0
    def iceBarrage(self):
        self.mana -= 10
        return (self.magic / 4) + 30
    def iceBlock(self):
        self.mana -= 50
        self.ice_block = True
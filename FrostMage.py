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
        if self.__iceBlock==True:
            self._mana = self._mana + self.getMagic() / 4
            self.__iceBlock = False
            print(f"{self.name} ice Block absorbed all the damage!")
            print("ice Block has faded\n")
        else:
            self._mana = self._mana + self.getMagic() / 4
            damage = damage - self.getDefense()
            if (self.getHealth() - damage) > 0:
                self.setHealth(self.getHealth() - damage)
                if damage > 0:
                    print(f"{self.name}’s defence level blocked {self.getDefense()} damage")
                    print(f"{self.name} took {damage} damage and has {self.getHealth()} health remaining\n")

            else:
                self.setHealth(-1)
                print(f"{self.name}’s defence level blocked {self.getDefense()} damage")
                print(f"{self.name} has been knocked out!\n")




    def castSpell(self):
        if self._mana >= 50:
            self.iceBlock()
            return -1

        elif self._mana < 50 and self._mana >10:
            self.iceBarrage()
            return  -2
    def iceBarrage(self):
        print(f"Jania casts Ice Barrage!")
        self._mana -= 10

    def iceBlock(self):
        print(f"Jania casts Ice Block!")
        self._mana -= 50
        self.__iceBlock = True
    def calculatePower(self):
        return super().getStrength()

    def attackEnemy(self, enemy):
        b = self.castSpell()
        if b==-1:

            damage = int(self.getMagic()/4)
            print(f"{self.name} attacks for {damage} damage!")
            enemy.takeDamage(damage)
        elif b==-2:
            damage = int(self.getMagic()/4+30)
            print(f"{self.name} attacks for {damage} damage!")

            enemy.takeDamage(damage)
        else:
            damage = self.getMagic()/4
            print(f"{self.name} attacks for {damage} damage!")

            enemy.takeDamage(damage)

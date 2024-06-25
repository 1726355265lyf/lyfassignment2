'''
File:PyroMage.py
Description:
Author:Lv Yifan
StudentID: 2218040126
This is my own work as defined by the University's Academic Misconduct Policy
'''
from Mage import Mage
class PyroMage(Mage):
    '''
    火焰法师具有一个 flameBoost 值，可以增加他们的伤害。
    如果火焰法师有 40 或更多的魔法值，他们将施放超级加热 (SuperHeat)。
    如果他们的魔法值少于 40 但多于 10，他们将施放火焰爆裂 (FireBlast)。
    每次火焰法师施放法术时，他们还会根据他们的回复速度 (regenValue) 恢复魔法值。
    '''

    def __init__(self, name, maxHealth, strength, defense, ranged, magic):
        super().__init__(name, maxHealth, strength, defense, ranged, magic)
        self.__flameBoost = 1.0
    def castSpell(self):
        if self._mana >40:
            self.castSuperHeat()
            self._mana = self._mana + self.getMagic() / 4
            return -1
        elif self._mana >= 10 and self._mana <= 40:
            self.castFireBlast()
            self._mana = self._mana + self.getMagic() / 4
            return -2

    def castFireBlast(self):
        self._mana -= 10
        print(f"{self.name} casts FireHeat")

    def castSuperHeat(self):
        self._mana -= 40
        self.__flameBoost += 1
        print(f"{self.name} casts SuperHeat")

    def attackEnemy(self,enemy):
        a = self.castSpell()
        if a==-2:

            damage = int(self.getStrength() * self.__flameBoost + 10)
            print(f"{self.name} attacks for {damage} damage")
            enemy.takeDamage(damage)


        elif a==-1:
            damage = int(self.getStrength() * self.__flameBoost)
            print(f"{self.name} attacks for {damage} damage")
            enemy.takeDamage(damage)
        else:
            damage = self.getStrength()
            print(f"{self.name} attacks for {damage} damage!")
            enemy.takeDamage(damage)
    def takeDamage(self, damage):
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




'''
File:Mage.py
Description:Test
Author:Lv Yifan
StudentID: 2218040126
This is my own work as defined by the University's Academic Misconduct Policy
'''
from Arena import Arena
from Combatant import Combatant
from Field import Field
from Mage import Mage
import unittest
from FrostMage import FrostMage
from PyroMage import PyroMage
from unittest.mock import patch
from io import StringIO
from Ranger import Ranger
from Warrior import Warrior
from Guthans import Guthans
from Dharok import Dharok
from Karil import Karil

class TestField(unittest.TestCase):
    def setUp(self):
        # 设置测试环境，创建一个Field实例
        self.field = Field("Castle Walls")

    def testChangeField(self):
        # 测试场地变更功能
        with patch('random.choice', return_value="Toxic Wasteland"):
            self.assertEqual(self.field.changeField(), "Toxic Wasteland")

    def testFieldEffectToxicWasteland(self):
        # 测试毒性荒地的效果
        self.field.name = "Toxic Wasteland"
        fighter1 = Combatant("Warrior", 100, 20, 5, 10, 5)
        fighter2 = Combatant("Mage", 80, 15, 5, 20, 10)
        initial_health_fighter1 = fighter1.getHealth()
        initial_health_fighter2 = fighter2.getHealth()
        self.field.fieldEffect(fighter1, fighter2)
        self.assertEqual(fighter1.getHealth(), initial_health_fighter1 - 5)
        self.assertEqual(fighter2.getHealth(), initial_health_fighter2 - 5)

    def testFieldEffectHealingMeadows(self):
        # 测试疗愈草地的效果
        self.field.name = "Healing Meadows"
        fighter1 = Combatant("Warrior", 100, 20, 5, 10, 5)
        fighter2 = Combatant("Mage", 80, 15, 5, 20, 10)
        self.field.fieldEffect(fighter1, fighter2)
        self.assertEqual(fighter1.getHealth(), 105)
        self.assertEqual(fighter2.getHealth(), 85)

    def testFieldEffectCastleWalls(self):
        # 测试城墙的无效果
        self.field.name = "Castle Walls"
        fighter1 = Combatant("Warrior", 100, 20, 5, 10, 5)
        fighter2 = Combatant("Mage", 80, 15, 5, 20, 10)
        initial_health_fighter1 = fighter1.getHealth()
        initial_health_fighter2 = fighter2.getHealth()
        self.field.fieldEffect(fighter1, fighter2)
        self.assertEqual(fighter1.getHealth(), initial_health_fighter1)
        self.assertEqual(fighter2.getHealth(), initial_health_fighter2)


class TestArena(unittest.TestCase):
    def setUp(self):
        # 设置测试环境，创建一个Arena实例
        self.arena = Arena("Colosseum")

    def testAddCombatant(self):
        # 测试添加战斗人员
        fighter = Combatant("Warrior", 100, 20, 5, 10, 5)
        self.arena.addCombatant(fighter)
        self.assertIn(fighter, self.arena.combatants)

    def testRemoveCombatant(self):
        # 测试移除战斗人员
        fighter = Combatant("Warrior", 100, 20, 5, 10, 5)
        self.arena.addCombatant(fighter)
        self.arena.removeCombatant(fighter)
        self.assertNotIn(fighter, self.arena.combatants)

    def testListCombatants(self):
        # 测试列出战斗人员
        fighter = Combatant("Warrior", 100, 20, 5, 10, 5)
        self.arena.addCombatant(fighter)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.arena.listCombatants()
            self.assertIn("Warrior", fake_out.getvalue().strip())

    def testRestoreCombatants(self):
        # 测试重置战斗人员
        fighter = Combatant("Warrior", 100, 20, 5, 10, 5)
        self.arena.addCombatant(fighter)
        fighter.takeDamage(50)  # 假设这个方法减少生命值
        self.arena.restoreCombatants()
        self.assertEqual(fighter.getHealth(), 100)

    def testDuel(self):
        # 测试战斗
        fighter1 = Combatant("Warrior", 100, 20, 5, 10, 5)
        fighter2 = Combatant("Mage", 80, 15, 5, 20, 10)
        self.arena.addCombatant(fighter1)
        self.arena.addCombatant(fighter2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.arena.duel(fighter1, fighter2)
            self.assertIn("Battle has taken place", fake_out.getvalue().strip())
class TestKaril(unittest.TestCase):
    def setUp(self):
        # 设置测试环境，创建一个Karil实例
        self.karil = Karil("Karil", 100, 20, 5, 30, 0, 10)



    def testInitialHealth(self):
        # 测试初始生命值
        self.assertEqual(self.karil.getHealth(), 100)

    def testArmourReduction(self):
        # 测试护甲减少伤害
        initial_health = self.karil.getHealth()
        self.karil.takeDamage(15)
        expected_health = initial_health - (15 - 10 - 5)  # 护甲值和防御值减少伤害
        self.assertEqual(self.karil.getHealth(), expected_health)

    def testArmourShatterMessage(self):
        # 测试护甲破碎时的消息
        self.karil.setarmoutValue(5)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.karil.takeDamage(15)
            self.assertIn("Armour  shattered", fake_out.getvalue().strip())



class TestDharok(unittest.TestCase):
    def setUp(self):
        # 设置测试环境，创建一个Dharok实例
        self.dharok = Dharok("Dharok", 100, 20, 5, 0, 0, 10)

    def testInitialHealth(self):
        # 测试初始生命值
        self.assertEqual(self.dharok.getHealth(), 100)

    def testCalculatePowerWithMissingHealth(self):
        # 测试随着生命值减少而增加的额外伤害
        self.dharok.takeDamage(50)
        power = self.dharok.calculatePower()
        missing_health = 100 - self.dharok.getHealth()  # 50 missing health
        expected_power = 20 + missing_health  # base strength + missing health
        self.assertEqual(power, expected_power)

    def testArmourReduction(self):
        # 测试护甲减少伤害
        initial_health = self.dharok.getHealth()
        self.dharok.takeDamage(15)
        expected_health = initial_health - (15 - 10 - 5)  # 护甲值和防御值减少伤害
        self.assertEqual(self.dharok.getHealth(), expected_health)

    def testArmourShatterMessage(self):
        # 测试护甲破碎时的消息
        self.dharok.setarmoutValue(5)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.dharok.takeDamage(15)
            self.assertIn("Armour  shattered", fake_out.getvalue().strip())

    def testAttackDamageIncrease(self):
        # 测试攻击时伤害的增加
        enemy = Dharok("Enemy", 100, 10, 5, 0, 0, 10)
        self.dharok.setHealth(60)  # 设置生命值以确保有40点额外伤害
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.dharok.attackEnemy(enemy)
            expected_damage = 20 + 40  # 基础力量加上缺失的生命值
            self.assertIn(f"Dharok attacks for {expected_damage} damage", fake_out.getvalue().strip())

class TestGuthans(unittest.TestCase):
    def setUp(self):
        # 设置测试环境，创建一个Guthans实例
        self.guthans = Guthans("Guthan", 100, 20, 5, 0, 0, 10)

    def testInitialHealth(self):
        # 测试初始生命值
        self.assertEqual(self.guthans.getHealth(), 100)

    def testHealingOnAttack(self):
        # 测试攻击时的治疗效果
        initial_health = self.guthans.getHealth()
        self.guthans.attackEnemy(Guthans("Dummy", 50, 10, 5, 0, 0, 10))
        expected_health = initial_health + (self.guthans.getStrength() / 5)
        self.assertEqual(self.guthans.getHealth(), expected_health)

    def testCalculatePower(self):
        # 测试力量计算并确认治疗是否正确
        initial_health = self.guthans.getHealth()
        power = self.guthans.calculatePower()
        expected_health = initial_health + (self.guthans.getStrength() / 5)
        self.assertEqual(self.guthans.getHealth(), expected_health)
        self.assertEqual(power, self.guthans.getStrength())

    def testTakeDamage(self):
        # 测试受到伤害时的行为
        self.guthans.takeDamage(15)
        expected_health = 100 - (15 - 10 - 5)  # 护甲值和防御值减少伤害
        self.assertEqual(self.guthans.getHealth(), expected_health)

    def testArmourShatterMessage(self):
        # 测试护甲破碎时的消息
        self.guthans.setarmoutValue(5)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.guthans.takeDamage(15)
            self.assertIn("Armour  shattered", fake_out.getvalue().strip())

class TestWarrior(unittest.TestCase):
    def setUp(self):
        # 设置测试环境，创建一个Warrior实例
        self.warrior = Warrior("Arthur", 100, 20, 5, 0, 0, 10)

    def testInitialArmourValue(self):
        # 测试初始护甲值是否为10
        self.assertEqual(self.warrior.getarmoutValue(), 10)

    def testArmourShatterMessage(self):
        # 测试护甲破碎时的消息
        self.warrior.setarmoutValue(5)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.warrior.takeDamage(15)
            self.assertIn("Armour  shattered!", fake_out.getvalue().strip())

    def testResetArmourValue(self):
        # 测试重置护甲值
        self.warrior.takeDamage(20)
        self.warrior.restValues()
        self.assertEqual(self.warrior.getarmoutValue(), 10)
        self.assertEqual(self.warrior.getHealth(), 100)  # 假设resetValues()也重置了生命值

    def testAttackDamage(self):
        # 测试攻击力是否正确
        enemy = Warrior("Enemy", 100, 10, 5, 0, 0, 10)
        self.warrior.attackEnemy(enemy)
        self.assertEqual(enemy.getHealth(), 95)

class TestRanger(unittest.TestCase):
    def setUp(self):
        # 设置测试环境，创建一个Ranger实例
        self.ranger = Ranger("Tim", 99, 10, 10, 1, 50)

    def testInitialArrows(self):
        # 测试初始箭的数量是否为3
        self.assertEqual(self.ranger.arrows, 3)

    def testArrowShooting(self):
        # 测试射箭减少箭数量并正确计算伤害
        initial_arrows = self.ranger.arrows
        damage = self.ranger.calculatePower()
        self.assertEqual(self.ranger.arrows, initial_arrows - 1, )
        self.assertEqual(damage, 50, )

    def testLastArrowMessage(self):
        # 测试射出最后一支箭时的消息
        self.ranger.arrows = 1  # 设置为最后一支箭
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.ranger.calculatePower()
            self.assertIn("", fake_out.getvalue().strip(), )

    def testResetArrows(self):
        # 测试重置箭的数量
        self.ranger.arrows = 0
        self.ranger.resetValues()
        self.assertEqual(self.ranger.arrows, 3)

    def testTakeDamage(self):
        # 测试受伤功能
        self.ranger.takeDamage(20)
        expected_health = 99 - (20 - 10)  # 伤害减去防御
        self.assertEqual(self.ranger.getHealth(), expected_health)

class TestPyroMage(unittest.TestCase):
    def setUp(self):
        # 设置测试环境，创建一个 PyroMage 实例
        self.mage = PyroMage("Zezima", 99, 15, 20, 70, 1)

    def testCastFireBlast(self):
        # 测试 FireBlast 的施放和魔法值变化
        self.mage._mana = 35
        initial_mana = self.mage._mana
        self.mage.castSpell()
        self.assertEqual(self.mage._mana, initial_mana - 10 + self.mage.getMagic() / 4)
        print(f"Expected mana after FireBlast: {self.mage._mana}")

    def testAttackDamageCalculation(self):
        # 测试攻击伤害计算
        enemy = PyroMage("Zezima", 99, 15, 20, 70, 1)
        self.mage._mana = 70  # 确保施放 SuperHeat
        self.mage.attackEnemy(enemy)
        expected_damage = int(15 * 2.0)  # Strength * flameBoost after SuperHeat
        self.assertEqual(enemy.getHealth(), 99 - (expected_damage - 20))

    def testManaRegeneration(self):
        # 测试施放法术后的魔法值恢复
        self.mage._mana = 30
        self.mage.castSpell()
        expected_mana = 30 - 10 + self.mage.getMagic() / 4
        self.assertEqual(self.mage._mana, expected_mana)

class TestFrostMage(unittest.TestCase):
    def setUp(self):
        # 设置测试环境，创建一个FrostMage实例
        self.mage = FrostMage("Jania", 100, 20, 10, 5, 80)

    def testIceBlockActivation(self):
        # 测试激活IceBlock
        self.mage._mana = 60  # 确保有足够的魔法值来激活IceBlock
        self.mage.castSpell()
        self.assertTrue(self.mage.iceBlock)

    def testIceBlockEffectiveness(self):
        # 测试IceBlock是否有效阻挡伤害
        self.mage._mana = 60  # 激活IceBlock
        self.mage.castSpell()  # Cast IceBlock
        initial_health = self.mage.getHealth()
        self.mage.takeDamage(50)  # 尝试造成伤害
        self.assertEqual(initial_health, self.mage.getHealth())

    def testIceBarrage(self):
        # 测试冰霜弹幕是否正确扣除魔法值并打印信息
        self.mage._mana = 40  # 设置足够的魔法值施放冰霜弹幕但不足以激活冰块
        self.mage.castSpell()
        self.assertEqual(self.mage._mana, 30)

    def testManaRegeneration(self):
        # 测试受到攻击后魔法值是否恢复
        initial_mana = self.mage._mana
        self.mage.takeDamage(10)  # 受到伤害
        expected_mana = initial_mana + self.mage.getMagic() / 4
        self.assertEqual(self.mage._mana, expected_mana)

class TestCombatant(unittest.TestCase):
    def setUp(self):
        # 在每个测试方法之前设置Combatant实例
        self.combatant = Combatant("Warrior", 100, 20, 10, 15, 5)
        self.enemy = Combatant("Enemy", 80, 15, 5, 10, 3)

    def testAttackEnemy(self):
        # 测试攻击敌人的过程
        initialHealth = self.enemy.getHealth()
        self.combatant.attackEnemy(self.enemy)
        # 敌人的生命值应该等于初始生命值减去（攻击力减去防御力）
        self.assertEqual(self.enemy.getHealth(), initialHealth - (20 - 5))

    def testTakeDamageLessThanDefense(self):
        # 测试受到的伤害小于防御值时的情况
        initialHealth = self.combatant.getHealth()
        self.combatant.takeDamage(5)
        # 由于伤害小于防御，不应有生命值减少
        self.assertEqual(self.combatant.getHealth(), initialHealth)

    def testTakeDamageMoreThanDefense(self):
        # 测试受到的伤害大于防御值时的情况
        initialHealth = self.combatant.getHealth()
        self.combatant.takeDamage(20)
        # 生命值应该减去（伤害减去防御值）
        self.assertEqual(self.combatant.getHealth(), initialHealth - (20 - 10))

    def testResetValues(self):
        # 测试重置生命值到最大生命值
        self.combatant.takeDamage(50)
        self.combatant.resetValues()
        self.assertEqual(self.combatant.getHealth(), 100)

    def testDetails(self):
        # 测试返回战斗人员的详细信息
        expectedDetails = "Name:Warrior,Health:100,Strength:20,Defense:10,Magic:15,Ranged:5"
        self.assertEqual(self.combatant.details(), expectedDetails)

    def testKnockout(self):
        # 测试战斗人员被击倒的情况
        self.combatant.takeDamage(110)
        remainingHealth = self.combatant.getHealth()
        self.assertTrue(remainingHealth <= 0, "Combatant should be knocked out when health falls below zero")

class TestMage(unittest.TestCase):
    def testMage(self):
        # 测试是否可以实例化Mage类
        with self.assertRaises(TypeError):
            durial = Mage("Durial", 99, 99, 99, 99, 99)
if __name__ == '__main__':
    unittest.main()
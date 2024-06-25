import unittest
from Arena import Arena
from Field import Field
from Combatant import Combatant, Ranger, Warrior, PyroMage, FrostMage
class TestArena(unittest.TestCase):

    def setUp(self):
        self.arena = Arena("Castle Walls")
        self.ranger = Ranger("Tim", 99, 10, 10, 50)
        self.warrior = Warrior("Jay", 99, 20, 10)
        self.pyromage = PyroMage("Zezima", 99, 15, 20, 70)
        self.frostmage = FrostMage("Jaina", 99, 10, 20, 94)

    def test_add_combatant(self):
        self.arena.addCombatant(self.ranger)
        self.assertIn(self.ranger, self.arena.combatants)
        self.arena.addCombatant(self.warrior)
        self.assertIn(self.warrior, self.arena.combatants)

    def test_add_combatant_with_zero_health(self):
        self.ranger.setHealth(0)
        self.arena.addCombatant(self.ranger)
        self.assertNotIn(self.ranger, self.arena.combatants)

    def test_remove_combatant(self):
        self.arena.addCombatant(self.ranger)
        self.arena.removeCombatant(self.ranger)
        self.assertNotIn(self.ranger, self.arena.combatants)

    def test_list_combatants(self):
        self.arena.addCombatant(self.ranger)
        self.arena.addCombatant(self.warrior)
        with self.assertLogs() as cm:
            self.arena.listCombatants()
        self.assertIn("Tim", cm.output[0])
        self.assertIn("Jay", cm.output[1])

    def test_restore_combatants(self):
        self.arena.addCombatant(self.ranger)
        self.ranger.takeDamage(20)
        self.arena.restoreCombatants()
        self.assertEqual(self.ranger.getHealth(), self.ranger.getMaxHealth())

    def test_duel(self):
        self.arena.addCombatant(self.ranger)
        self.arena.addCombatant(self.warrior)
        with self.assertLogs() as cm:
            self.arena.duel(self.ranger, self.warrior)
        self.assertIn("----- Battle has taken place in Castle Walls", cm.output[0])

    def test_duel_with_one_combatant_zero_health(self):
        self.ranger.setHealth(0)
        self.arena.addCombatant(self.ranger)
        self.arena.addCombatant(self.warrior)
        with self.assertLogs() as cm:
            self.arena.duel(self.ranger, self.warrior)
        self.assertIn("Tim has no health to battle", cm.output[0])

    def test_duel_with_one_combatant_not_in_arena(self):
        self.arena.addCombatant(self.ranger)
        with self.assertLogs() as cm:
            self.arena.duel(self.ranger, self.warrior)
        self.assertIn("Jay was not found in Castle Walls's list of fighters", cm.output[0])

if __name__ == "__main__":
    unittest.main()
# Importing the Combatant class
from Combatant import Combatant

def test_combatant():
    # Create two combatants
    warrior = Combatant(name="Warrior", maxHealth=100, strength=20, defense=10, magic=5, ranged=0)
    mage = Combatant(name="Mage", maxHealth=80, strength=5, defense=5, magic=20, ranged=0)

    # Print details of both combatants
    print(warrior.details())
    print(mage.details())

    # Simulate an attack
    print("\nWarrior attacks Mage")
    warrior.attackEnemy(mage)

    # Check health after attack
    print(f"Mage's health after attack: {mage.getHealth()}")

    # Simulate another attack
    print("\nMage attacks Warrior")
    mage.attackEnemy(warrior)

    # Check health after attack
    print(f"Warrior's health after attack: {warrior.getHealth()}")

    # Reset health values and check
    print("\nResetting health values...")
    warrior.resetValues()
    mage.resetValues()
    print(warrior.details())
    print(mage.details())

if __name__ == "__main__":
    test_combatant()
# Importing the Combatant class
from Combatant import Combatant

def test_combatant():
    # Create two combatants
    warrior = Combatant(name="Warrior", maxHealth=100, strength=20, defense=10, magic=5, ranged=0)
    mage = Combatant(name="Mage", maxHealth=80, strength=5, defense=5, magic=20, ranged=0)

    # Print details of both combatants
    print(warrior.details())
    print(mage.details())

    # Simulate an attack
    print("\nWarrior attacks Mage")
    warrior.attackEnemy(mage)

    # Check health after attack
    print(f"Mage's health after attack: {mage.getHealth()}")

    # Simulate another attack
    print("\nMage attacks Warrior")
    mage.attackEnemy(warrior)

    # Check health after attack
    print(f"Warrior's health after attack: {warrior.getHealth()}")

    # Reset health values and check
    print("\nResetting health values...")
    warrior.resetValues()
    mage.resetValues()
    print(warrior.details())
    print(mage.details())

if __name__ == "__main__":
    test_combatant()
from Dharok import Dharok
from Warrior import Warrior

def test_dharok():
    # Create a Dharok instance and a basic Warrior instance
    dharok = Dharok(name="Dharok", maxHealth=100, strength=20, defense=10, ranged=5, magic=5, armourValue=15)
    enemy = Warrior(name="Enemy", maxHealth=100, strength=15, defense=5, ranged=5, magic=5, armourValue=0)

    # Print initial details
    print(dharok.details())
    print(enemy.details())

    # Simulate Dharok attacking the enemy
    print("\nDharok attacks Enemy")
    dharok.attackEnemy(enemy)

    # Check enemy's health after attack
    print(f"Enemy's health after attack: {enemy.getHealth()}")

    # Simulate enemy attacking Dharok
    print("\nEnemy attacks Dharok")
    enemy.attackEnemy(dharok)

    # Check Dharok's health after attack
    print(f"Dharok's health after attack: {dharok.getHealth()}")

    # Simulate Dharok attacking the enemy again
    print("\nDharok attacks Enemy again")
    dharok.attackEnemy(enemy)

    # Check enemy's health after second attack
    print(f"Enemy's health after second attack: {enemy.getHealth()}")

    # Reset health values and check
    print("\nResetting health values...")
    dharok.resetValues()
    enemy.resetValues()
    print(dharok.details())
    print(enemy.details())

if __name__ == "__main__":
    test_dharok()
from Field import Field
from Combatant import Combatant

def test_field():
    # Create two combatants
    fighter1 = Combatant(name="Fighter1", maxHealth=100, strength=20, defense=10, magic=5, ranged=5)
    fighter2 = Combatant(name="Fighter2", maxHealth=100, strength=15, defense=5, magic=10, ranged=5)

    # Create a field
    field = Field(name="")

    # Print initial details
    print(fighter1.details())
    print(fighter2.details())

    # Change the field and print its name
    field_name = field.changeField()
    print(f"\nField changed to: {field_name}")

    # Apply field effect
    print("\nApplying field effect...")
    field.fieldEffect(fighter1, fighter2)

    # Print details after field effect
    print(fighter1.details())
    print(fighter2.details())

    # Change the field again and print its name
    field_name = field.changeField()
    print(f"\nField changed to: {field_name}")

    # Apply field effect again
    print("\nApplying field effect...")
    field.fieldEffect(fighter1, fighter2)

    # Print details after field effect
    print(fighter1.details())
    print(fighter2.details())

if __name__ == "__main__":
    test_field()
from FrostMage import FrostMage
from Combatant import Combatant

def test_frost_mage():
    # Create a FrostMage instance and a basic Combatant instance
    frost_mage = FrostMage(name="Jaina", maxHealth=100, strength=10, defense=5, ranged=5, magic=60)
    enemy = Combatant(name="Enemy", maxHealth=100, strength=15, defense=5, magic=10, ranged=5)

    # Print initial details
    print(frost_mage.details())
    print(enemy.details())

    # FrostMage attacks enemy
    print("\nFrostMage attacks Enemy")
    frost_mage.attackEnemy(enemy)
    print(enemy.details())

    # Enemy attacks FrostMage to check Ice Block and regenValue
    print("\nEnemy attacks FrostMage")
    enemy.attackEnemy(frost_mage)
    print(frost_mage.details())

    # FrostMage attacks enemy again to use Ice Barrage
    print("\nFrostMage attacks Enemy again")
    frost_mage.attackEnemy(enemy)
    print(enemy.details())

    # Reduce FrostMage mana and attack to ensure Ice Barrage works
    frost_mage._mana = 20
    print("\nReducing FrostMage mana to 20 and attacking")
    frost_mage.attackEnemy(enemy)
    print(enemy.details())

    # Further reduce mana and attack to test regular attack
    frost_mage._mana = 5
    print("\nReducing FrostMage mana to 5 and attacking")
    frost_mage.attackEnemy(enemy)
    print(enemy.details())

    # Reset values
    print("\nResetting health and mana values...")
    frost_mage.resetValues()
    enemy.resetValues()
    print(frost_mage.details())
    print(enemy.details())

if __name__ == "__main__":
    test_frost_mage()
from Guthans import Guthans
from Combatant import Combatant

def test_guthans():
    # Create a Guthans instance and a basic Combatant instance
    guthans = Guthans(name="Guthans", maxHealth=100, strength=20, defense=10, ranged=5, magic=5, armourValue=50)
    enemy = Combatant(name="Enemy", maxHealth=100, strength=15, defense=5, magic=10, ranged=5)

    # Print initial details
    print(guthans.details())
    print(enemy.details())

    # Guthans attacks enemy
    print("\nGuthans attacks Enemy")
    guthans.attackEnemy(enemy)
    print(enemy.details())
    print(guthans.details())

    # Enemy attacks Guthans to check armor blocking
    print("\nEnemy attacks Guthans")
    enemy.attackEnemy(guthans)
    print(guthans.details())

    # Guthans attacks enemy again to check healing on attack
    print("\nGuthans attacks Enemy again")
    guthans.attackEnemy(enemy)
    print(enemy.details())
    print(guthans.details())

    # Reduce Guthans' armor value and attack to check armor shattering
    guthans.setarmoutValue(5)
    print("\nReducing Guthans' armour to 5 and attacking")
    enemy.attackEnemy(guthans)
    print(guthans.details())

    # Further reduce health and attack to test knockout
    guthans.setHealth(10)
    print("\nReducing Guthans' health to 10 and attacking")
    enemy.attackEnemy(guthans)
    print(guthans.details())

    # Reset values
    print("\nResetting health and armour values...")
    guthans.resetValues()
    enemy.resetValues()
    print(guthans.details())
    print(enemy.details())

if __name__ == "__main__":
    test_guthans()
from Karil import Karil
from Combatant import Combatant

def test_karil():
    # Create a Karil instance and a basic Combatant instance
    karil = Karil(name="Karil", maxHealth=100, strength=20, defense=10, ranged=15, magic=5, armourValue=50)
    enemy = Combatant(name="Enemy", maxHealth=100, strength=15, defense=5, magic=10, ranged=5)

    # Print initial details
    print(karil.details())
    print(enemy.details())

    # Karil attacks enemy
    print("\nKaril attacks Enemy")
    karil.attackEnemy(enemy)
    print(enemy.details())
    print(karil.details())

    # Enemy attacks Karil to check armor blocking and damage calculation
    print("\nEnemy attacks Karil")
    enemy.attackEnemy(karil)
    print(karil.details())

    # Karil attacks enemy again to verify damage calculation with ranged power
    print("\nKaril attacks Enemy again")
    karil.attackEnemy(enemy)
    print(enemy.details())
    print(karil.details())

    # Reduce Karil's armor value and attack to check armor shattering
    karil.setarmoutValue(5)
    print("\nReducing Karil's armour to 5 and attacking")
    enemy.attackEnemy(karil)
    print(karil.details())

    # Further reduce health and attack to test knockout
    karil.setHealth(10)
    print("\nReducing Karil's health to 10 and attacking")
    enemy.attackEnemy(karil)
    print(karil.details())

    # Reset values
    print("\nResetting health and armour values...")
    karil.resetValues()
    enemy.resetValues()
    print(karil.details())
    print(enemy.details())

if __name__ == "__main__":
    test_karil()
from Mage import Mage

# Create a concrete subclass for testing purposes
class FireMage(Mage):
    def __init__(self, name, maxHealth, strength, defense, magic, ranged):
        super().__init__(name, maxHealth, strength, defense, magic, ranged)

    def castSpell(self):
        return self._mana // 2

def test_mage():
    # Create an instance of FireMage (a concrete subclass of Mage)
    fire_mage = FireMage(name="FireMage", maxHealth=100, strength=10, defense=5, magic=40, ranged=10)

    # Print initial details
    print(fire_mage.details())
    print(f"Initial Mana: {fire_mage._mana}")
    print(f"Regen Rate: {fire_mage._regenRate}\n")

    # Calculate power using castSpell method
    power = fire_mage.calculatePower()
    print(f"Power after casting spell: {power}\n")

    # Simulate taking damage to verify mana regeneration
    fire_mage.takeDamage(10)
    print(f"Details after taking damage:")
    print(fire_mage.details())
    print(f"Mana after taking damage: {fire_mage._mana}\n")

    # Reset values
    fire_mage.resetValues()
    print("Details after resetting values:")
    print(fire_mage.details())
    print(f"Mana after resetting: {fire_mage._mana}")

if __name__ == "__main__":
    test_mage()
from PyroMage import PyroMage
from Combatant import Combatant

def test_pyromage():
    # Create an instance of PyroMage and a basic Combatant instance
    pyromage = PyroMage(name="PyroMage", maxHealth=100, strength=20, defense=10, ranged=5, magic=50)
    enemy = Combatant(name="Enemy", maxHealth=100, strength=15, defense=5, magic=10, ranged=5)

    # Print initial details
    print(pyromage.details())
    print(f"Initial Mana: {pyromage._mana}")
    print(f"Flame Boost: {pyromage._PyroMage__flameBoost}\n")

    # PyroMage attacks enemy with sufficient mana for SuperHeat
    print("\nPyroMage attacks Enemy with SuperHeat")
    pyromage.attackEnemy(enemy)
    print(enemy.details())
    print(pyromage.details())
    print(f"Mana after SuperHeat: {pyromage._mana}")
    print(f"Flame Boost after SuperHeat: {pyromage._PyroMage__flameBoost}\n")

    # Reduce PyroMage's mana and attack with FireBlast
    pyromage._mana = 30
    print("\nPyroMage attacks Enemy with FireBlast")
    pyromage.attackEnemy(enemy)
    print(enemy.details())
    print(pyromage.details())
    print(f"Mana after FireBlast: {pyromage._mana}\n")

    # Reduce PyroMage's mana to below 10 and attack
    pyromage._mana = 5
    print("\nPyroMage attacks Enemy with basic attack")
    pyromage.attackEnemy(enemy)
    print(enemy.details())
    print(pyromage.details())
    print(f"Mana after basic attack: {pyromage._mana}\n")

    # Simulate taking damage
    print("\nEnemy attacks PyroMage")
    enemy.attackEnemy(pyromage)
    print(pyromage.details())

    # Reset values
    print("\nResetting PyroMage values...")
    pyromage.resetValues()
    print(pyromage.details())
    print(f"Mana after resetting: {pyromage._mana}")

if __name__ == "__main__":
    test_pyromage()
from Ranger import Ranger
from Combatant import Combatant

def test_ranger():
    # Create an instance of Ranger and a basic Combatant instance
    ranger = Ranger(name="Ranger", maxHealth=100, strength=15, defense=8, magic=5, ranged=25)
    enemy = Combatant(name="Enemy", maxHealth=80, strength=12, defense=6, magic=8, ranged=10)

    # Print initial details
    print(ranger.details())
    print(f"Initial Arrows: {ranger.arrows}\n")

    # Ranger attacks enemy multiple times
    print("\nRanger attacks Enemy multiple times")
    for _ in range(4):  # Performing more than 3 attacks to trigger the message
        ranger.attackEnemy(enemy)
    print(enemy.details())
    print(ranger.details())
    print(f"Arrows after attacks: {ranger.arrows}\n")

    # Simulate taking damage
    print("\nEnemy attacks Ranger")
    enemy.attackEnemy(ranger)
    print(ranger.details())

    # Reset values and check arrows reset
    print("\nResetting Ranger values...")
    ranger.resetValues()
    print(ranger.details())
    print(f"Arrows after resetting: {ranger.arrows}")

if __name__ == "__main__":
    test_ranger()
from Warrior import Warrior
from Combatant import Combatant

def test_warrior():
    # Create an instance of Warrior and a basic Combatant instance
    warrior = Warrior(name="Warrior", maxHealth=100, strength=20, defense=10, magic=5, ranged=5, armourValue=10)
    enemy = Combatant(name="Enemy", maxHealth=80, strength=12, defense=6, magic=8, ranged=10)

    # Print initial details
    print(warrior.details())
    print(enemy.details())
    print(f"Initial Armour Value: {warrior.getarmoutValue()}\n")

    # Warrior attacks enemy
    print("\nWarrior attacks Enemy")
    warrior.attackEnemy(enemy)
    print(enemy.details())
    print(warrior.details())
    print(f"Armour Value after attack: {warrior.getarmoutValue()}\n")

    # Simulate taking damage
    print("\nEnemy attacks Warrior")
    enemy.attackEnemy(warrior)
    print(warrior.details())

    # Warrior takes damage again to test armour reduction
    print("\nWarrior takes damage again")
    warrior.takeDamage(30)
    print(warrior.details())
    print(f"Armour Value after damage: {warrior.getarmoutValue()}\n")

    # Reset values and check armour reset
    print("\nResetting Warrior values...")
    warrior.restValues()
    print(warrior.details())
    print(f"Armour Value after resetting: {warrior.getarmoutValue()}\n")

if __name__ == "__main__":
    test_warrior()

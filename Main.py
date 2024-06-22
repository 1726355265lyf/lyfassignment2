'''
File:Main.py
Description:
Author:Lv Yifan
StudentID: 2218040126
This is my own work as defined by the University's Academic Misconduct Policy
'''
import Arena
import Combatant
import Dharok
import Filed
import FrostMage
import Guthans
import Karil
import Mage
import PyroMage
import Ranger
import Warrior
# Creating the different combatant objects
# name, maxHealth, strength, defence, mage, range and armourValue for warriors
tim = Ranger("Tim", 99, 10, 10, 1, 50)
jay = Warrior("Jay", 99, 1, 99, 1, 1, 1)
kevin = Dharok("Kevin", 99, 45, 25, 25, 25, 10)
zac = Guthans("Zac", 99, 45, 30, 1, 1, 10)
jeff = Karil("Jeff", 99, 50, 40, 1, 10, 5)
try:
    durial = Mage("Durial", 99, 99, 99, 99, 99)
except TypeError:
    print("Mages must be specialized!")
jaina = FrostMage("Jaina", 99, 10, 20, 94, 10)
zezima = PyroMage("Zezima", 99, 15, 20, 70, 1)
# setting up the first arena
falador = Arena("Falador")
falador.addCombatant(tim)
falador.addCombatant(jeff)
falador.listCombatants()
# duel between ranger and karil
falador.duel(tim, jeff)
# showcasing incorrect duels
falador.duel(tim, jeff)
falador.duel(jeff, zezima)
# showcasing restoring combatants
falador.listCombatants()
falador.restoreCombatants()
falador.listCombatants()
# showcasing removing from arena
falador.removeCombatant(jeff)
falador.removeCombatant(jeff)
# setting up the second arena
varrock = Arena("Varrock")
varrock.addCombatant(kevin)
varrock.addCombatant(zac)
# duel between guthans and dharok.. note guthans does not heal on the final round as Zac was KO'd
varrock.duel(kevin, zac)
# setting up the third arena
wilderness = Arena("Wilderness")
wilderness.addCombatant(jaina)
wilderness.addCombatant(zezima)
# duel between a pyro and frost mage... double ko?!?!?
wilderness.duel(jaina, zezima)
# setting up final arena
lumbridge = Arena("Lumbridge")
lumbridge.addCombatant(jaina)
lumbridge.addCombatant(jay)
lumbridge.addCombatant(tim)
# showcasing health carries over from arenas
lumbridge.duel(jaina, jay)
# showcasing a duel that takes too long...
# tims arrows should also be reset to 3 from the restoing at the falador arena above
lumbridge.duel(jay, tim)


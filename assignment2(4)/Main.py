from Ranger import Ranger
from Warrior import Warrior
from Dharok import Dharok
from Guthans import Guthans
from Karil import Karil
from Mage import Mage
from FrostMage import FrostMage
from PyroMage import PyroMage
from Arena import Arena
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
zezima = PyroMage("Zezima", 99, 15, 20, 70, 1)# setting up the first arena
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


# setting up the first arena
falador = Arena("Wilderness")
falador.addCombatant(jaina)
falador.addCombatant(zezima)
falador.duel(jaina,zezima)

falador = Arena("Lumbridge")
falador.addCombatant(jaina)
falador.addCombatant(jay)
falador.addCombatant(tim)
falador.addCombatant(jaina)
falador.duel(jay,tim)


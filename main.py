### Imports ###

import classes as C, battle_engine as BE

###############

### Start Up ###

print("Welcome to Minecraft Battle Simulator!")
player_name = input("Enter your desired name here: ")

################

### Initialize Player Characters ###

warrior = C.Warrior('Warrior', 45, 30, 250, 'Sword Slash','Rock Throw', 80)
archer = C.Archer('Archer', 30, 20, 200, 'Bow Shot','Triple Shot', 100)
mage = C.Mage('Mage', 40, 10, 175, 'Insant Damage Potion','Lightning Strike', 115)

####################################

### Pick character ###

warrior.stats()
archer.stats()
mage.stats()




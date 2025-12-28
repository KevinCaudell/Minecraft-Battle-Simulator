### Imports ###

import classes as C, battle_engine as BE

###############

### Start Up ###

print("Welcome to Minecraft Battle Simulator!")
player_name = input("Enter your username here: ")

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

while True:
    character_choice = input('Select your character by typing their name: ').lower().strip()

    if character_choice not in ('warrior','archer','mage'):
        print('Not a valid character choice!')
        continue

    if character_choice == 'warrior':
        player = warrior
    elif character_choice == 'archer':
        player = archer
    else:
        player = mage

    print(f'You selected {player._name}!')
    break




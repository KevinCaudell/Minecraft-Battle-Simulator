### Imports ###

import classes as C
from time import sleep
from random import choice 

###############

### Battle Sequence ###

def fight(player, mob):
    """Fight loop to enact the trade-off of attacks between mob and player."""
    player_counter_bool = False
    mob_counter_bool = False

    while True:

        if player.ability_counter >= player.max_ability_counter:
            action = input(f"[A]ttack or [H]eal or [S]pecial Attack: ").strip().lower()
            print()
        else:
            action = input(f"[A]ttack or [H]eal: ").strip().lower()
            print()

        if action not in ('a', 'h'):
            if action == 's' and player.ability_counter < player.max_ability_counter:
                print('Invalid selection.')
                continue
            elif action == 's':
                break
            print('Invalid selection.')
            continue
        break

    if action == 'a':
        dmg = player.attack(mob)
        sleep(1)
        mob.take_damage(dmg)
        mob.healthBar()
        player.ability_counter += 1
    elif action == 's':
        dmg = player.special_attack(mob)
        sleep(1)
        player.ability_counter = 0
        mob.take_damage(dmg)
        mob.healthBar()
        player_counter_bool = True
    else:
        player.heal()
        player.healthBar()
    
    if not mob.is_alive():
        return None

    sleep(1)
    if mob.ability_counter >= mob.max_ability_counter:
        dmg = mob.special_attack(player)
        sleep(1)
        mob.ability_counter = 0
        player.take_damage(dmg)
        player.healthBar()
        mob_counter_bool = True
    else:
        dmg = mob.attack(player)
        sleep(1)
        player.take_damage(dmg)
        player.healthBar()
        mob.ability_counter += 1

    if player_counter_bool == True:
        player_counter_bool = False
        player.ability_counter = 0

    if mob_counter_bool == True:
        mob_counter_bool = False
        mob.ability_counter = 0

def battle(player, mob):
    """A battle loop for each individual encounter between a player and a mob.
       Return True if mob was killed, False if player was killed."""
    
    mob_messages = [f"A {mob.name} has appeared!", f"You are approaching a {mob.name}"]
    sleep(0.5)
    print(choice(mob_messages), '\n')

    while True:
        fight(player,mob)
        if not mob.is_alive():
            sleep(0.5)
            print(f"\n{mob.name} has been slayed.")
            return True
        if not player.is_alive():
            sleep(0.5)
            print(f"\n{player.name} has died.")
            return False
            
def single_realm_gamemode(realms, player):
    realm_dict = {'overworld': 0, 'nether': 1, 'end': 2}

    while True:       
        print('\nPick which realm to fight!')
        print('\n' + 'Overworld | Nether | End ')
        while True: 
            choosen_realm = input('Type in realm here: ').lower().strip()
            if choosen_realm not in realm_dict:
                print('\nInvalid realm choice!')
                continue

            print(f"\nYou've chosen the {choosen_realm.capitalize()} realm!")
            break

        print(f'\n--- The {choosen_realm.capitalize()} ---\n\n') # Displays Choosen Realm

        ### Battle Loop ###

        for mob in realms[realm_dict[choosen_realm]]:
            result = battle(player, mob)

            if result == False: # Player Died
                player.skill_exp = 0
                return False
            
            check_skill(player, mob)
            
        ####################
            
        print('Would you like to keep playing Single Realm gamemode?')
        answer = input('[C]hange mode | [K]eep playing | [Q]uit').lower().strip()
        while True:
            if answer not in ('c','k','q'):
                print('Invalid Choice')
                continue
            break
        if answer == 'k':
            continue
        elif answer == 'c':
            return False
        else:
            return 'quit'      

def campaign_gamemode(realms, player):
    print('\n--- Campaign ---\n\n')
    while True:
        input('Realm: Overworld')
        for mob in realms[0]:
            result = battle(player, mob)

            if result == False: # Player Died
                    return False
            
        input("You've conquered the Overworld Realm!")
        input('Realm: Nether')
        for mob in realms[1]:
            result = battle(player, mob)

            if result == False: # Player Died
                    return False
            
        input("You've conquered the Nether Realm!")
        input("Realm: End")
        for mob in realms[2]:
            result = battle(player, mob)

            if result == False: # Player Died
                    return False
            
        input("You've completed the Campaign!")

        print('Would you like to keep playing Campaign?')
        answer = input('[C]hange mode | [K]eep playing | [Q]uit').lower().strip()
        while True:
            if answer not in ('c','k','q'):
                print('Invalid Choice')
                continue
            break
        if answer == 'k':
            continue
        elif answer == 'c':
            return False
        else:
            return 'quit'

def The_Pit_gamemode(realms, player):
    all_mobs = [] # Stores all mobs in 1 list to be choosen from
    for realm in realms:
        for mob in realm:
            all_mobs.append(mob)

    print('\n--- The Pit ---\n\n')

    while True:
        all_mobs1 = all_mobs
        while len(all_mobs1) > 0:
            mob = choice(all_mobs1)
            result = battle(player, mob)
            all_mobs1.remove(mob)

            if result == False: # Player Died
                    break

        print('Would you like to keep playing Campaign?')
        answer = input('[C]hange mode | [K]eep playing | [Q]uit').lower().strip()
        while True:
            if answer not in ('c','k','q'):
                print('Invalid Choice')
                continue
            break
        if answer == 'k':
            continue
        elif answer == 'c':
            return False
        else:
            return 'quit'

def check_skill(player, mob):
    player.skill_exp += mob.exp
    
    while True:
        if player.skill_exp >= player.max_skill_exp:
            player.skill()
            player.skill_exp -= player.max_skill_exp
    
        if player.skill_exp < player.max_skill_exp:
            break
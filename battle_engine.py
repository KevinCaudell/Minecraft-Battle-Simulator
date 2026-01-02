### Imports ###

import classes as C
from time import sleep
from random import choice 
from game_setup import check_skill

###############

def fight(player, mob):
    """Fight loop interaction between attack trade-offs between mob and player."""
    player_counter_bool = False
    mob_counter_bool = False

    while True:

        if player.ability_counter >= player.max_ability_counter: # Checks if players special attack is available for use.
            action = input(f"[A]ttack or [H]eal or [S]pecial Attack: ").strip().lower()
            print()
        else: # If special attack is not available, then display default input.
            action = input(f"[A]ttack or [H]eal: ").strip().lower()
            print()

        if action not in ('a', 'h'): # Checks to see if action input is not a or h
            if action == 's' and player.ability_counter < player.max_ability_counter: # checks if action input is equal 
                                                                                      # to s and if special attack is available
                print('Invalid selection.')
                continue
            elif action == 's':
                break
            print('Invalid selection.')
            continue
        break

    if action == 'a':                      # Uses attack method for player object
        dmg = player.attack(mob)
        sleep(1)
        mob.take_damage(dmg)
        mob.healthBar()
        player.ability_counter += 1
    elif action == 's':                    # Uses special attack method for player object
        dmg = player.special_attack(mob)
        sleep(1)
        player.ability_counter = 0
        mob.take_damage(dmg)
        mob.healthBar()
        player_counter_bool = True
    else:                                  # Heals player object
        player.heal()
        player.healthBar()
    
    if not mob.is_alive():
        return None

    sleep(1)
    if mob.ability_counter >= mob.max_ability_counter: # Checks to see if mob's special attack is 
                                                       # available, if so it uses their special attack.
        dmg = mob.special_attack(player)
        sleep(1)
        mob.ability_counter = 0
        player.take_damage(dmg)
        player.healthBar()
        mob_counter_bool = True
    else:                                              # Uses mob's attack method
        dmg = mob.attack(player)
        sleep(1)
        player.take_damage(dmg)
        player.healthBar()
        mob.ability_counter += 1

    if player_counter_bool == True:                    # Checks if player used their speciall attack, 
                                                       # if so it resets their special attack counter
        player_counter_bool = False
        player.ability_counter = 0

    if mob_counter_bool == True:                       # Checks if player used their speciall attack, 
                                                       # if so it resets their special attack counter
        mob_counter_bool = False
        mob.ability_counter = 0

def battle(player, mob):
    """A battle loop for each individual encounter between a player and a mob.
       Return True if mob was killed, False if player was killed."""
    
    mob_messages = [f"A {mob.name} has appeared!", f"You are approaching a {mob.name}"] # Different display messages for variations.
    sleep(0.5)
    print(choice(mob_messages), '\n') 

    while True:                                         # Loops through fight scenario until either the mob or player dies.
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
    realm_dict = {'overworld': 0, 'nether': 1, 'end': 2}               # Used to link select realm with correct 
                                                                       # list in mob's realm_container class

    while True:       
        print('\nPick which realm to fight!')
        print('\n' + 'Overworld | Nether | End ')
        while True:                                                         # Asks player to select realm and makes sure it's one of the options.
            chosen_realm = input('Type in realm here: ').lower().strip()
            if chosen_realm not in realm_dict:
                print('\nInvalid realm choice!')
                continue

            print(f"\nYou've chosen the {chosen_realm.capitalize()} realm!")
            break

        print(f'\n--- The {chosen_realm.capitalize()} ---\n\n') # Displays Choosen Realm

        for mob in realms[realm_dict[chosen_realm]][:]:                   # loops through select realms mob list and runs a battle 
                                                                          # loop until the player dies or kills all mobs.
            result = battle(player, mob)

            if result == False: # Player Died
                player.skill_exp = 0
                return False
            
            realms[realm_dict[chosen_realm]].remove(mob)
            
            
            check_skill(player, mob)
            
        while True:                                                                              # A loop to make sure the player selects if they want to change modes, 
                                                                                                 # keep playing this mode, or quit the program.
            print('Would you like to keep playing Single Realm gamemode?')
            answer = input('[C]hange mode | [K]eep playing | [Q]uit').lower().strip()
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
        for mob in realms[0][:]:                                # Loop for Overworld realm
            result = battle(player, mob)

            if result == False: # Player Died
                    return False
            
            realms[0].remove(mob)
            check_skill(player, mob)
            
        input("You've conquered the Overworld Realm!")
        input('Realm: Nether')
        for mob in realms[1][:]:                               # Loop for Nether realm
            result = battle(player, mob)

            if result == False: # Player Died
                    return False
            
            realms[1].remove(mob)
            check_skill(player, mob)
            
        input("You've conquered the Nether Realm!")
        input("Realm: End")
        for mob in realms[2][:]:                              # Loop for End realm
            result = battle(player, mob)

            if result == False: # Player Died
                    return False
            
            realms[2].remove(mob)
            check_skill(player, mob)
            
        input("You've completed the Campaign!")

        while True:                                                                       # A loop to make sure the player selects if they want to change modes, 
                                                                                          # keep playing this mode, or quit the program.
            print('Would you like to keep playing Campaign?')
            answer = input('[C]hange mode | [K]eep playing | [Q]uit').lower().strip()
        
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
    all_mobs = []                                                   # Stores all mobs in 1 list to be choosen from
    for realm in realms:                                            # appends all mobs from mob container class into functions list.
        for mob in realm:
            all_mobs.append(mob)

    print('\n--- The Pit ---\n\n')

    while True:
        all_mobs1 = all_mobs[:]                                     # Creates a copy of the function list to be used to iterate over.
        while len(all_mobs1) > 0:                                   # loop to battle each mob at a random choice.
            mob = choice(all_mobs1)
            result = battle(player, mob)
            all_mobs1.remove(mob)

            if result == False: # Player Died
                    break
            
            check_skill(player, mob)

        while True:                                                # A loop to make sure the player selects if they want to change modes, 
                                                                   # keep playing this mode, or quit the program.
            print('Would you like to keep playing Campaign?')
            answer = input('[C]hange mode | [K]eep playing | [Q]uit').lower().strip()
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


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
    
    mob_messages = [f"A {mob._name} has appeared!", f"You are approaching a {mob._name}"]
    sleep(0.5)
    print(choice(mob_messages), '\n')

    while True:
        fight(player,mob)
        if not mob.is_alive():
            sleep(0.5)
            print(f"\n{mob._name} has been slayed.")
            player.skill_counter += 1
            return True
        if not player.is_alive():
            sleep(0.5)
            print(f"\n{player._name} has died.")
            player.skill_counter = 0
            return False
            






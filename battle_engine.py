### Imports ###

import classes as C
from time import sleep
from random import choice 

###############

### Battle Sequence ###

def fight(player, mob):
    """Fight loop to enact the trade-off of attacks between mob and player."""
    while True:
        action = input(f"[A]ttack or [H]eal: ").strip().lower()
        print()
        if action not in ('a', 'h'):
            print('Invalid selection.')
            continue
        break

    if action == 'a':
        sleep(0.5)
        dmg = player.attack(mob)
        sleep(0.5)
        mob.take_damage(dmg)
        mob.healthBar()
    else:
        sleep(0.5)
        player.heal()
        player.healthBar()
    
    if not mob.isAlive():
        return None

    sleep(0.5)
    dmg = mob.attack(player)
    sleep(0.5)
    player.take_damage(dmg)
    player.healthBar()
    

def battle(player, mob):
    """A battle loop for each individual encounter between a player and a mob.
       Return True if mob was killed, False if player was killed."""
    
    mob_messages = [f"A {mob._name} has appeared!", f"You are approaching a {mob._name}"]
    sleep(0.5)
    print(choice(mob_messages))

    while True:
        fight(player,mob)
        if not mob.isAlive():
            sleep(0.5)
            print(f"\n{mob._name} has been slayed.")
            return True
        if not player.isAlive():
            sleep(0.5)
            print(f"\n{player._name} has died.")
            return False
            






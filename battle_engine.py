### Imports ###

import classes as C
import random as R

###############

### Battle Sequence ###

def fight(player, mob):
    """Fight loop to enact the trade-off of attacks between mob and player."""
    while True:
        action = input(f"[A]ttack or [H]eal: ").strip().lower()
        if action not in ('a', 'h'):
            print('Invalid selection.')
            continue
        break

    if action == 'a':
        dmg = player.attack(mob)
        mob.take_damage(dmg)
    else:
        player.heal()
    
    if not mob.isAlive():
        return None

    dmg = mob.attack(player)
    player.take_damage(dmg)
    

def battle(player, mob):
    """A battle loop for each individual encounter between a player and a mob.
       Return True if mob was killed, False if player was killed."""
    
    mob_messages = [f"A {mob._name} has appeared!", f"You are approaching a {mob._name}"]
    print(R.choice(mob_messages))

    while True:
        fight(player,mob)
        if not mob.isAlive():
            print(f"\n{mob._name} has been slayed.")
            return True
        if not player.isAlive():
            print(f"\n{player._name} has died.")
            return False
            






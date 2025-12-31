### Imports ###

import classes as C
from battle_engine import battle
from random import choice 

###############


def initiliaze_game():
    ### Initialize Player Characters ###

    warrior = C.Warrior('Warrior', 45, 30, 250, 'Sword Slash','Rock Throw', 100)
    archer = C.Archer('Archer', 30, 20, 200, 'Bow Shot','Triple Shot', 120)
    mage = C.Mage('Mage', 40, 10, 175, 'Insant Damage Potion','Lightning Strike', 115)

    ### Initliaze Mob Characters ###

    Zombie = C.Zombie('Zombie', 35, 10, 200, 'Claw Slash', 'Infected Bite', 75,'non-boss')
    Skeleton = C.Skeleton('Skeleton', 32, 2, 175, 'Bow Shot', 'Poison Arrow', 90, 'non-boss')
    Spider = C.Spider('Spider', 35, 4, 215, 'Venomous Bite', 'Web Shot', 65, 'non-boss')
    Creeper = C.Creeper('Creeper', 24, 10, 165, 'Ignite Hit', 'Supercharged Blow', 135, 'non-boss')
    Witch = C.Witch('Witch', 28, 0, 200, 'Potion Throw', 'Instant Damage Potion', 110, 'non-boss')
    Pillager = C.Pillager('Pillager', 43, 15, 225, 'Axe Swing', 'Multi Axe Slash', 90, 'non-boss')
    Warden = C.Warden('Warden', 40, 18, 315, 'Ground Slam', 'Superbeam', 75, 'boss')
    Blaze = C.Blaze('Blaze', 33, 5, 175, 'Fireball', 'Blaze Storm', 87, 'non-boss')
    WitherSkeleton = C.WitherSkeleton('Wither Skeleton', 42, 13, 225, 'Sword Slash', 'Lifesteal', 99, 'non-boss')
    Hoglin = C.Hoglin('Hoglin', 30, 6, 250, 'Horn Penetration', 'Charging Horn', 88, 'non-boss')
    Ghast = C.Ghast('Ghast', 25, 0, 150, 'Fireball', 'Screaming Siren', 80, 'non-boss')
    MagmaCube = C.MagmaCube('Magma Cube', 20, 17, 200, 'Jump Slam', 'Duplicated Slam', 65, 'non-boss')
    Brute = C.Brute('Brute', 38, 11, 225, 'Axe Slash', 'Golden Axe Throw', 110, 'non-boss')
    Wither = C.Wither('Wither', 43, 8, 475, 'Skull Throw', 'Supercharge detonation', 150, 'boss')
    Enderman = C.Enderman('Enderman', 37, 3, 180, 'Block Smash', 'Teleportation Block Throw', 100, 'non-boss')
    Silverfish = C.Silverfish('Silver Fish', 18, 0, 125, 'Ankle Bite', 'Stone Roll', 90, 'non-boss')
    Endermite = C.Endermite('Endermite', 22, 0, 125, 'Ankle Bite', 'Teleportation Bite', 88, 'non-boss')
    Shulker = C.Shulker('Shulker', 10, 15, 250, 'Air Slam', 'Multi-Shulker Attack', 110, 'non-boss')
    EnderDragon = C.EnderDragon('Ender Dragon', 650, 20, 525, 'Sweeping Wing', 'Ender Fireball', 132, 'boss')

    ### Append to realm container class ###

    realms = C.MobRealms()

    realms.append(Zombie)
    realms.append(Skeleton)
    realms.append(Spider)
    realms.append(Creeper)
    realms.append(Witch)
    realms.append(Pillager)
    realms.append(Warden)
    realms.append(Blaze)
    realms.append(WitherSkeleton)
    realms.append(Hoglin)
    realms.append(Ghast)
    realms.append(MagmaCube)
    realms.append(Brute)
    realms.append(Wither)
    realms.append(Enderman)
    realms.append(Silverfish)
    realms.append(Endermite)
    realms.append(Shulker)
    realms.append(EnderDragon)

    return realms, warrior,archer,mage

def choose_gamemode():
    modes = ('Single Realm', 'Campaign', 'The Pit')
    dict1 = {1: 'Single Realm', 2: 'Campaign', 3: 'The Pit'}
    print(f"Gamemodes: {modes[0]} [1] | {modes[1]} [2] | {modes[2]} [3]")
    while True:
        selected_mode = int(input('Select gamemode: '))
        print()
        if selected_mode not in (1,2,3):
            print('Invalid Choice.')
            continue
        break

    return dict1[selected_mode]

def choose_character(warrior, archer, mage):
    while True:
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

            print(f"\nYou selected {player.name}!")
            return player

### Imports ###

import classes as C, battle_engine as BE

###############

def initiliaze_game():
    ### Initialize Player Characters ###

    warrior = C.Warrior('Warrior', 45, 30, 250, 'Sword Slash','Rock Throw', 80)
    archer = C.Archer('Archer', 30, 20, 200, 'Bow Shot','Triple Shot', 100)
    mage = C.Mage('Mage', 40, 10, 175, 'Insant Damage Potion','Lightning Strike', 115)

    ### Initliaze Mob Characters ###

    Zombie = C.Zombie('Zombie', 35, 10, 200, 'Claw Slash', 'Infected Bite', 75,'non-boss')
    Skeleton = C.Skeleton('Skeleton', 32, 2, 175, 'Bow Shot', 'Poison Arrow', 90, 'non-boss')
    Spider = C.Spider('Spider', 35, 4, 215, 'Venomous Bite', 'Web Shot', 65, 'non-boss')
    Creeper = C.Creeper('Creeper', 24, 10, 165, 'Ignite Hit', 'Supercharged Blow', 135, 'non-boss')
    Witch = C.Witch('Witch', 28, 0, 200, 'Potion Throw', 'Instant Damage Potion', 110, 'non-boss')
    Pillager = C.Pillager('Pillager', 43, 15, 225, 'Axe Swing', 'Multi Axe Slash', 90, 'non-boss')
    Warden = C.Warden('Warden', 55, 18, 315, 'Ground Slam', 'Superbeam', 75, 'boss')
    Blaze = C.Blaze('Blaze', 33, 5, 175, 'Fireball', 'Blaze Storm', 87, 'non-boss')
    WitherSkeleton = C.WitherSkeleton('Wither Skeleton', 42, 13, 225, 'Sword Slash', 'Lifesteal', 99, 'non-boss')
    Hoglin = C.Hoglin('Hoglin', 30, 6, 250, 'Horn Penetration', 'Charging Horn', 88, 'non-boss')
    Ghast = C.Ghast('Ghast', 25, 0, 150, 'Fireball', 'Screaming Siren', 80, 'non-boss')
    MagmaCube = C.MagmaCube('Magma Cube', 20, 17, 200, 'Jump Slam', 'Duplicated Slam', 65, 'non-boss')
    Brute = C.Brute('Brute', 52, 11, 225, 'Axe Slash', 'Golden Axe Throw', 110, 'non-boss')
    Wither = C.Wither('Wither', 45, 8, 475, 'Skull Throw', 'Supercharge detonation', 150, 'boss')
    Enderman = C.Enderman('Enderman', 37, 3, 180, 'Block Smash', 'Teleportation Block Throw', 100, 'non-boss')
    Silverfish = C.Silverfish('Silver Fish', 18, 0, 125, 'Ankle Bite', 'Stone Roll', 90, 'non-boss')
    Endermite = C.Endermite('Endermite', 22, 0, 125, 'Ankle Bite', 'Teleportation Bite', 88, 'non-boss')
    Shulker = C.Shulker('Shulker', 10, 15, 250, 'Air Slam', 'Multi-Shulker Attack', 110, 'non-boss')
    EnderDragon = C.EnderDragon('Ender Dragon', 60, 20, 525, 'Sweeping Wing', 'Ender Fireball', 132, 'boss')

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

    ####################################

def game(realms, warrior, archer, mage):
    ### Pick character ###
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

            print(f"\nYou selected {player._name}!")
            break

        #######################

        ### Pick Realm ###

        realm_dict = {'overworld': 0, 'nether': 1, 'end': 2}
        print('\nPick which realm to fight!')
        print('\n' + 'Overworld | Nether | End ')
        while True: 
            choosen_realm = input('Type in realm here: ').lower().strip()
            if choosen_realm not in realm_dict:
                print('\nInvalid realm choice!')
                continue

            print(f"\nYou've chosen the {choosen_realm.capitalize()} realm!")
            break

        ### Display Chosen Realm ###

        print(f'\n--- The {choosen_realm.capitalize()} ---\n\n\n')

        ############################

        ### Fight ###

        for mob in realms[realm_dict[choosen_realm]]:
            result = BE.battle(player, mob)

            if result == False:
                return None
        

    #############

def main():
    ### Start Up ###

    print("Welcome to Minecraft Battle Simulator!")
    player_name = input("Enter your username here: ")

    ################
    
    while True:
        realms, warrior, archer, mage = initiliaze_game()
        game(realms, warrior, archer, mage)
        print("Would you like to keep playing?")
        while True:
            answer = input("[Y]es or [N]o\n").lower().strip()
            if answer not in ('y','n'):
                print('Not a valid choice.')
                continue
            break
        if answer == 'n':
            break
        
    print("\n\n\nMinecraft Battle Simulator Stopped")

if __name__ == '__main__':
    main()


    



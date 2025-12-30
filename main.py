### Imports ###

import classes as C
from battle_engine import battle
from game_setup import initiliaze_game

###############

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

            print(f"\nYou selected {player.name}!")
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

        print(f'\n--- The {choosen_realm.capitalize()} ---\n\n')

        ############################

        ### Fight ###

        for mob in realms[realm_dict[choosen_realm]]:
            result = battle(player, mob)

            if result == False:
                return None
            
        break
        

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


    



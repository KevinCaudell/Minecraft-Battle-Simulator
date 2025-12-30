### Imports ###

import classes as C
from battle_engine import battle
from game_setup import initiliaze_game, choose_gamemode, single_realm_gamemode

###############

def main():

    print("Welcome to Minecraft Battle Simulator!")
    player_name = input("Enter your username here: ")

    
    while True:
        realms, warrior, archer, mage = initiliaze_game()
        single_realm_gamemode(realms, warrior, archer, mage)
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


    



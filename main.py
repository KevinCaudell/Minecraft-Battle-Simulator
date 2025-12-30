### Imports ###

import classes as C
from battle_engine import battle
from game_setup import initiliaze_game, choose_gamemode, single_realm_gamemode, campaign_gamemode, The_Pit_gamemode

###############

def main():
    print("Welcome to Minecraft Battle Simulator!")
    player_name = input("Enter your username here: ")
    
    while True:
        realms, warrior, archer, mage = initiliaze_game() # Initiliazes mobs and characters.

        gamemode = choose_gamemode() # Selects gamemode.
        if gamemode == 'Single Realm':
            option = single_realm_gamemode(realms, warrior, archer, mage)
        elif gamemode == 'Campaign':
            option = campaign_gamemode
        else:
            option = The_Pit_gamemode

        if option == 'quit':
            return None

        if option == False:
            print('Would You like to continue playing Minecraft Battle Simulator?\nOr Exit')
            player_answer = input('[q] to quit | [any key] to continue.')
            if player_answer == 'q':
                return None
            continue

if __name__ == '__main__':
    main()
    print("\n\n\nMinecraft Battle Simulator Stopped")


    



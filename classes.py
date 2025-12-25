### IMPORTS ###

import math

### PLAYER CLASSES ###
class Player:
    skill_counter = 3
    def __init__(self, name, attack_damage, defense, health, attack_name, 
                 special_ability_name, special_ability_damage):
        self.__name = name
        self.__attack_damage = attack_damage
        self.__defense = defense
        self.__health = health
        self.__max_health = health
        self.__attack_name = attack_name
        self.__special_ability_name = special_ability_name
        self.__special_ability_damage = special_ability_damage

    def attack(self, enemy):
        """Applied damage to enemy object."""
        enemy.__health -= self.__attack_damage
        print(f'{self.__name} attacked {enemy.__name} using {self.__attack_name} dealing {self.__attack_damage}')
        return None
    
    def isAlive(self):
        """Checks to see if the character is alive."""
        if self.__health <= 0:
            return False
        return True

    def heal(self):
        """Adds at most 50 health points to character."""
        if self.__health == self.__max_health:
            print('Health is full')
            return None
        
        if self.__health <= self.__max_health - 50:
            self.__health += 50
            print(f'Healed 50hp\nPlayer health at {self.__health}')
            return None
        
        print(f'Healed {self.__max_health - self.__health}hp\nPlayer health is full')
        self.__health = self.__max_health

    def special_attack(self, enemy):
        """Uses special ability on enemy dealing unique damage to them."""
        enemy.__health -= self.__special_ability_damage
        print(f'{self.__name} attacked {enemy.__name} using {self.__special_ability_name} dealing {self.__special_ability_damage}')
        return None

    def health_bar(self):
        """Prints a health bar for the characters health to max health ratio"""
        bar_length = 10
        health_ratio = self.__health / self.__max_health
        filled_length = int(bar_length * health_ratio)
        bar_health = '[#]' * filled_length + '[ ]' * (bar_length - filled_length)
        print(f"{self.__name}'s Health Bar: {bar_health} {self.__health}/{self.__max_health}\n")

    def stats(self):
        """Displays statistics for character type."""
        print(f'Name: {self.__name}')
        print(f'Health: {self.__max_health}')
        print(f'Defense: {self.__defense}')
        print(f'Attack Damage: {self.__attack_damage}')
        print(f'Ability Damage: {self.__special_ability_damage}')

    def take_damage(self, damage):
        self.__health -= damage
        return None

class Warrior(Player):
    def __init__(self, name, attack_damage, defense, health, attack_name, 
                 special_ability_name, special_ability_damage):
        super.__init__(name, attack_damage, defense, health, attack_name, 
                       special_ability_name, special_ability_damage)

    def skill():
        '''Adds extra resistence to oncoming attacks to reduce damage taken.'''
        self.__defense += 10
        print(f'{self.__name}\'s defense has been increased by 10.')


class Archer(Player):
    def __init__(self, name, attack_damage, defense, health, attack_name, 
                 special_ability_name, special_ability_damage):
        super.__init__(name, attack_damage, defense, health, attack_name, 
                       special_ability_name, special_ability_damage)

    def skill():
        """Dodges oncoming attack to avoid taking damage."""


class Mage(Player):
    def __init__(self, name, attack_damage, defense, health, attack_name, 
                 special_ability_name, special_ability_damage):
        super.__init__(name, attack_damage, defense, health, attack_name, 
                       special_ability_name, special_ability_damage)

    def skill():
        """Blocking the enemy attack and counter attacks the enemy with their own attack for 75% of it's original damage."""


### MOB CLASSES ###
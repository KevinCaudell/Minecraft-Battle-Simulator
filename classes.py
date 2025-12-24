import math

class Player:
    def __init__(self, name, attack_damage, defense, health, attack_name, 
                 special_ability_name, special_ability_damage, special_ability_counter):
        self.__name = name
        self.__attack_damage = attack_damage
        self.__defense = defense
        self.__health = health
        self.__max_health = health
        self.__attack_name = attack_name
        self.__special_ability_name = special_ability_name
        self.__special_ability_damage = special_ability_damage
        self.__special_ability_counter = special_ability_counter

    def attack(self, enemy):
        enemy.__health -= self.__attack_damage
        print(f'{self.__name} attacked {enemy.__name} dealing {self.__attack_damage}')
        return None
    
    def isAlive(self):
        if self.__health <= 0:
            return False
        return True

    def heal(self):
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
        enemy.__health -= self.__special_ability_damage
        print(f'{self.__name} attacked {enemy.__name} using {self.__special_ability_name} dealing {self.__special_ability_damage}')
        return None

    def health_bar(self):
        bar_length = 10
        health_ratio = self.__health / self.__max_health
        filled_length = int(bar_length * health_ratio)
        bar_health = '[#]' * filled_length + '[ ]' * (bar_length - filled_length)
        print(f"{self.__name}'s Health Bar: {bar_health} {self.__health}/{self.__max_health}\n")

    def stats(self):
        print(f'Name: {self.__name}')
        print(f'Health: {self.__max_health}')
        print(f'Defense: {self.__defense}')
        print(f'Attack Damage: {self.__attack_damage}')
        print(f'Ability Damage: {self.__special_ability_damage}')

### PLAYER CLASSES ###
class Player:
    skill_counter = 3

    def __init__(self, name, attack_damage, defense, health, attack_name, 
                 special_ability_name, special_ability_damage):
        self._name = name
        self._attack_damage = attack_damage
        self._defense = defense
        self._health = health
        self._max_health = health
        self._attack_name = attack_name
        self._special_ability_name = special_ability_name
        self._special_ability_damage = special_ability_damage

    def attack(self, enemy):
        """Applied damage to enemy object."""
        enemy._health -= self._attack_damage
        print(f'{self._name} attacked {enemy._name} using {self._attack_name} dealing {self._attack_damage}')
        return None
    
    def isAlive(self):
        """Checks to see if the character is alive."""
        return self._health > 0

    def heal(self):
        """Heals up to 50 health points to character."""
        if self._health == self._max_health:
            print('Health is full')
            return None
        
        if self._health <= self._max_health - 50:
            self._health += 50
            print(f'Healed 50hp\nPlayer health at {self._health}')
            return None
        
        print(f'Healed {self._max_health - self._health}hp\nPlayer health is full')
        self._health = self._max_health
        return None

    def special_attack(self, enemy):
        """Uses special ability on enemy dealing unique damage to them."""
        enemy._health -= self._special_ability_damage
        print(f'{self._name} used {self._special_ability_name} on {enemy._name} dealing {self._special_ability_damage}')
        return None

    def health_bar(self):
        """Prints a health bar for the characters health to max health ratio"""
        bar_length = 10
        health_ratio = self._health / self._max_health
        filled_length = int(bar_length * health_ratio)
        bar_health = '[#]' * filled_length + '[ ]' * (bar_length - filled_length)
        print(f"{self._name}'s Health: {bar_health} {self._health}/{self._max_health}\n")

    def stats(self):
        """Displays statistics for character type."""
        print(f'Name: {self._name}')
        print(f'Health: {self._max_health}')
        print(f'Defense: {self._defense}')
        print(f'Attack Damage: {self._attack_damage}')
        print(f'Ability Damage: {self._special_ability_damage}')

    def take_damage(self, damage):
        """Applies damage to character from enemies attack."""
        self._health -= damage
        return None

class Warrior(Player):
    def __init__(self, *args):
        super().__init__(*args)

    def skill(self):
        '''Gains resistence by increasing defense by 10.'''
        self._defense += 10
        print(f'{self._name}\'s defense has been increased by 10!')
        return None

class Archer(Player):
    def __init__(self, *args):
        super().__init__(*args)

    def skill(self):
        """Dodges attack."""
        print(f'{self._name} dodged attack!')
        return None

class Mage(Player):
    def __init__(self, *args):
        super().__init__(*args)

    def skill(self, enemy, damage):
        """Blocking the enemy attack and counter attacks the enemy with their own attack for 25% of it's original damage."""
        return_damage = round(damage * 0.25)
        enemy._health -= return_damage
        print(f'{self._name} blocked attack and countered, dealing {return_damage}hp to {enemy._name}')


### MOB CLASSES ###

class Mob:
    ability_count = 4

    def __init__(self, name, attack_damage, defense, health, attack_name, special_ability_name, 
                 special_ability_damage, type):
        self._name = name
        self._attack_damage = attack_damage
        self._defense = defense
        self._health = health
        self._attack_name = attack_name
        self._special_ability_name = special_ability_name
        self._special_ability_damage = special_ability_damage
        self._type = type

    def attack(self, player):
        """Applied damage to player object."""
        player._health -= self._attack_damage
        print(f'{self._name} attacked {player._name} using {self._attack_name} dealing {self._attack_damage}')
        return None

    def isAlive(self):
        """Checks to see if the mob is alive."""
        return self._health > 0

    def special_attack(self, player):
        """Uses special ability on player dealing unique damage to them."""
        player._health -= self._special_ability_damage
        print(f'{self._name} used {self._special_ability_name} on {player._name} dealing {self._special_ability_damage}')
        return None

    def healthBar(self):
        """Prints a health bar for the mobs health to max health ratio"""
        bar_length = 10
        health_ratio = self._health / self._max_health
        filled_length = int(bar_length * health_ratio)
        bar_health = '[#]' * filled_length + '[ ]' * (bar_length - filled_length)
        print(f"{self._name}'s Health: {bar_health} {self._health}/{self._max_health}\n")

    def take_damage(self, damage):
        """Applies damage to mob from player attack."""
        self._health -= damage
        return None

class Zombie(Mob):
    pass

class Skeleton(Mob):
    pass

class Spider(Mob):
    pass

class Creeper(Mob):
    pass

class Witch(Mob):
    pass

class Pillager(Mob):
    pass

class Warden(Mob):
    pass

class Blaze(Mob):
    pass

class WitherSkeleton(Mob):
    pass

class Hoglin(Mob):
    pass

class Ghast(Mob):
    pass

class MagmaCube(Mob):
    pass

class Brute(Mob):
    pass

class Wither(Mob):
    pass

class Enderman(Mob):
    pass

class Silverfish(Mob):
    pass

class Endermite(Mob):
    pass

class Skulker(Mob):
    pass

class EnderDragon(Mob):
    pass

### Mob Container Class ###

class MobRealms(list):
    Overworld = []
    Nether = []
    End = []

    def __init__(self, name='Mob Realm Container'):
        super().__init__()
        self._name = name
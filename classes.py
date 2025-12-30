### Imports ###

from random import randint

###############

### PLAYER CLASSES ###
class Player:
    skill_counter = 0
    ability_counter = 0
    max_skill_counter = 4
    max_ability_counter = 3

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
        dmg = randint(self._attack_damage, self._attack_damage + 10)
        print(f'{self._name} attacked {enemy.name} using {self._attack_name} dealing {dmg}\n')
        return int(dmg)
    
    def is_alive(self):
        """Checks to see if the character is alive."""
        return self._health > 0

    def heal(self):
        """Heals up to 75 health points to character."""
        if self._health == self._max_health:
            print('Health is full\n')
            return None
        
        if self._health <= self._max_health - 75:
            self._health += 75
            print(f'Healed 75hp\nPlayer health at {self._health}\n')
            return None
        
        print(f'Healed {round(self._max_health - self._health,2)}hp\nPlayer health is full\n')
        self._health = self._max_health
        return None

    def special_attack(self, enemy):
        """Uses special ability on enemy dealing unique damage to them."""
        print(f'{self._name} used {self._special_ability_name} on {enemy.name} dealing {self._special_ability_damage}\n')
        return int(self._special_ability_damage)

    def healthBar(self):
        """Prints a health bar for the characters health to max health ratio"""
        bar_length = 10
        health_ratio = self._health / self._max_health
        filled_length = int(bar_length * health_ratio)
        bar_health = '[#]' * filled_length + '[ ]' * (bar_length - filled_length)
        print(f"{self._name}'s Health: {bar_health} {round(self._health, 2)}/{self._max_health}\n")

    def stats(self):
        """Displays statistics for character type."""
        print(f'Name: {self._name}')
        print(f'    Health: {self._max_health}')
        print(f'    Defense: {self._defense}')
        print(f'    Attack Damage: {self._attack_damage}')
        print(f'    Ability Damage: {self._special_ability_damage}')
        print()

    def take_damage(self, damage):
        """Applies damage to character from enemies attack, based on defense of player."""
        defence_percent = self._defense / 100
        reduced = damage - (damage * defence_percent)
        self._health -= reduced
        return None

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @property
    def max_health(self):
        return self._max_health

    @property
    def defense(self):
        return self._defense

    @property
    def attack_damage(self):
        return self._attack_damage

    @property
    def attack_name(self):
        return self._attack_name

    @property
    def special_ability_name(self):
        return self._special_ability_name

    @property
    def special_ability_damage(self):
        return self._special_ability_damage

class Warrior(Player):
    def __init__(self, *args):
        super().__init__(*args)

    def skill(self):
        '''Gains resistence by increasing defense by 10.'''
        self._defense += 10
        print(f'{self._name}\'s defense has been increased by 10!\n')
        return None

class Archer(Player):
    def __init__(self, *args):
        super().__init__(*args)

    def skill(self):
        """Dodges attack."""
        print(f'{self._name} dodged attack!\n')
        return None

class Mage(Player):
    def __init__(self, *args):
        super().__init__(*args)

    def skill(self):
        """Adds damage to base attack damage"""
        self._attack_damage += 5
        print(f"{self._name}\'s base attack has increased by 5!\n")
        return None

### MOB CLASSES ###

class Mob:
    ability_counter = 0
    max_ability_counter = 4

    def __init__(self, name, attack_damage, defense, health, attack_name, special_ability_name, 
                 special_ability_damage, type):
        self._name = name
        self._attack_damage = attack_damage
        self._defense = defense
        self._health = health
        self._max_health = health
        self._attack_name = attack_name
        self._special_ability_name = special_ability_name
        self._special_ability_damage = special_ability_damage
        self._type = type

    def attack(self, player):
        """Applied damage to player object."""
        dmg = randint(self._attack_damage, self._attack_damage + 5)
        print(f'{self._name} attacked {player.name} using {self._attack_name} dealing {dmg}\n')
        return int(dmg)

    def is_alive(self):
        """Checks to see if the mob is alive."""
        return self._health > 0

    def special_attack(self, player):
        """Uses special ability on player dealing unique damage to them."""
        print(f'{self._name} used {self._special_ability_name} on {player.name} dealing {self._special_ability_damage}\n')
        return int(self._special_ability_damage)

    def healthBar(self):
        """Prints a health bar for the mobs health to max health ratio"""
        bar_length = 10
        health_ratio = self._health / self._max_health
        filled_length = int(bar_length * health_ratio)
        bar_health = '[#]' * filled_length + '[ ]' * (bar_length - filled_length)
        print(f"{self._name}'s Health: {bar_health} {self._health}/{self._max_health}\n")

    def take_damage(self, damage):
        """Applies damage to mob from player attack, based on defense of mob."""
        defence_percent = self._defense / 100
        reduced = damage - (damage * defence_percent)
        self._health -= reduced
        return None
    
    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @property
    def max_health(self):
        return self._max_health

    @property
    def defense(self):
        return self._defense

    @property
    def attack_damage(self):
        return self._attack_damage

    @property
    def attack_name(self):
        return self._attack_name

    @property
    def special_ability_name(self):
        return self._special_ability_name

    @property
    def special_ability_damage(self):
        return self._special_ability_damage


# Overworld Mobs #
class Overworld(Mob):
    def __init__(self, *args):
        super().__init__(*args)

class Zombie(Overworld):
    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player.name} dealing {self._special_ability_damage}!\n")
        return int(self._special_ability_damage)
    
class Skeleton(Overworld):
    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player.name} dealing {self._special_ability_damage}!\n")
        return int(self._special_ability_damage)
    
class Spider(Overworld):
    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player.name} dealing {self._special_ability_damage}!\n")
        return int(self._special_ability_damage)

class Creeper(Overworld):
    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player.name} dealing {self._special_ability_damage}!\n")
        return int(self._special_ability_damage)

class Witch(Overworld):
    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player.name} dealing {self._special_ability_damage}!\n")
        return int(self._special_ability_damage)

class Pillager(Overworld):
    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player.name} dealing {self._special_ability_damage}!\n")
        return int(self._special_ability_damage)

class Warden(Overworld):
    max_ability_count = 6
    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player.name} dealing {self._special_ability_damage}!\n")
        return int(self._special_ability_damage)

# Nether Mobs #

class Nether(Mob):
    def __init__(self, *args):
        super().__init__(*args)

class Blaze(Nether):
    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player.name} dealing {self._special_ability_damage}!\n")
        return int(self._special_ability_damage)

class WitherSkeleton(Nether):
    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player.name} dealing {self._special_ability_damage}!\n")
        return int(self._special_ability_damage)

class Hoglin(Nether):
    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player.name} dealing {self._special_ability_damage}!\n")
        return int(self._special_ability_damage)

class Ghast(Nether):
    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player.name} dealing {self._special_ability_damage}!\n")
        return int(self._special_ability_damage)

class MagmaCube(Nether):
    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player.name} dealing {self._special_ability_damage}!\n")
        return int(self._special_ability_damage)

class Brute(Nether):
    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player.name} dealing {self._special_ability_damage}!\n")
        return int(self._special_ability_damage)

class Wither(Nether):
    max_ability_count = 6
    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player.name} dealing {self._special_ability_damage}!\n")
        return int(self._special_ability_damage)

# End Mobs #

class End(Mob):
    def __init__(self, *args):
        super().__init__(*args)

class Enderman(End):
    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player.name} dealing {self._special_ability_damage}!\n")
        return int(self._special_ability_damage)

class Silverfish(End):
    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player.name} dealing {self._special_ability_damage}!\n")
        return int(self._special_ability_damage)

class Endermite(End):
    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player.name} dealing {self._special_ability_damage}!\n")
        return int(self._special_ability_damage)

class Shulker(End):
    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player.name} dealing {self._special_ability_damage}!\n")
        return int(self._special_ability_damage)

class EnderDragon(End):
    max_ability_count = 6

    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player.name} dealing {self._special_ability_damage}!\n")
        return int(self._special_ability_damage)

### Mob Container Class ###

class MobRealms(list):
    def __init__(self, name='Mob Realm Container'):
        super().__init__([[],[],[]])
        self._name = name

    def append(self, mob_obj):
        if not isinstance(mob_obj, Mob):
            return False, 'Object not of class Mob'
        
        if isinstance(mob_obj, Overworld):
            self[0].append(mob_obj)
            return True

        if isinstance(mob_obj, Nether):
            self[1].append(mob_obj)
            return True

        if isinstance(mob_obj, End):
            self[2].append(mob_obj)
            return True

    def remove(self, mob_obj):
        for realm in self:
            if mob_obj in realm:
                realm.remove(mob_obj)
                return True
        return False
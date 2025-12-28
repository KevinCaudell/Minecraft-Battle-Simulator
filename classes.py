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
        print(f'{self._name} attacked {enemy._name} using {self._attack_name} dealing {self._attack_damage}')
        return int(self._attack_damage)
    
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
        print(f'{self._name} used {self._special_ability_name} on {enemy._name} dealing {self._special_ability_damage}')
        return int(self._special_ability_damage)

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
        print(f'    Health: {self._max_health}')
        print(f'    Defense: {self._defense}')
        print(f'    Attack Damage: {self._attack_damage}')
        print(f'    Ability Damage: {self._special_ability_damage}')
        print()

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
        print(f'{self._name} blocked attack and countered, dealing {return_damage}hp to {enemy._name}')
        return return_damage


### MOB CLASSES ###

class Mob:
    ability_count = 4

    def __init__(self, name, attack_damage, defense, health, attack_name, special_ability_name, 
                 special_ability_damage, realm, type):
        self._name = name
        self._attack_damage = attack_damage
        self._defense = defense
        self._health = health
        self._max_health = health
        self._attack_name = attack_name
        self._special_ability_name = special_ability_name
        self._special_ability_damage = special_ability_damage
        self._mob_realm = realm
        self._type = type

    def attack(self, player):
        """Applied damage to player object."""
        print(f'{self._name} attacked {player._name} using {self._attack_name} dealing {self._attack_damage}')
        return int(self._attack_damage)

    def isAlive(self):
        """Checks to see if the mob is alive."""
        return self._health > 0

    def special_attack(self, player):
        """Uses special ability on player dealing unique damage to them."""
        print(f'{self._name} used {self._special_ability_name} on {player._name} dealing {self._special_ability_damage}')
        return int(self._special_ability_damage)

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

# Overworld Mobs #
class Overworld(Mob):
    def __init__(self, *args):
        super().__init__(*args)

class Zombie(Overworld):
    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player._name} dealing {self._special_ability_damage}!")
        return int(self._special_ability_damage)
    
class Skeleton(Overworld):
    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player._name} dealing {self._special_ability_damage}!")
        return int(self._special_ability_damage)
    
class Spider(Overworld):
    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player._name} dealing {self._special_ability_damage}!")
        return int(self._special_ability_damage)

class Creeper(Overworld):
    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player._name} dealing {self._special_ability_damage}!")
        return int(self._special_ability_damage)

class Witch(Overworld):
    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player._name} dealing {self._special_ability_damage}!")
        return int(self._special_ability_damage)

class Pillager(Overworld):
    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player._name} dealing {self._special_ability_damage}!")
        return int(self._special_ability_damage)

class Warden(Overworld):
    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player._name} dealing {self._special_ability_damage}!")
        return int(self._special_ability_damage)

# Nether Mobs #

class Nether(Mob):
    def __init__(self, *args):
        super().__init__(*args)

class Blaze(Nether):
    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player._name} dealing {self._special_ability_damage}!")
        return int(self._special_ability_damage)

class WitherSkeleton(Nether):
    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player._name} dealing {self._special_ability_damage}!")
        return int(self._special_ability_damage)

class Hoglin(Nether):
    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player._name} dealing {self._special_ability_damage}!")
        return int(self._special_ability_damage)

class Ghast(Nether):
    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player._name} dealing {self._special_ability_damage}!")
        return int(self._special_ability_damage)

class MagmaCube(Nether):
    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player._name} dealing {self._special_ability_damage}!")
        return int(self._special_ability_damage)

class Brute(Nether):
    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player._name} dealing {self._special_ability_damage}!")
        return int(self._special_ability_damage)

class Wither(Nether):
    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player._name} dealing {self._special_ability_damage}!")
        return int(self._special_ability_damage)

# End Mobs #

class End(Mob):
    def __init__(self, *args):
        super().__init__(*args)

class Enderman(End):
    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player._name} dealing {self._special_ability_damage}!")
        return int(self._special_ability_damage)

class Silverfish(End):
    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player._name} dealing {self._special_ability_damage}!")
        return int(self._special_ability_damage)

class Endermite(End):
    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player._name} dealing {self._special_ability_damage}!")
        return int(self._special_ability_damage)

class Shulker(End):
    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player._name} dealing {self._special_ability_damage}!")
        return int(self._special_ability_damage)

class EnderDragon(End):
    def __init__(self, *args):
        super().__init__(*args)

    def ability(self, player):
        print(f"{self._name} used {self._special_ability_name} on {player._name} dealing {self._special_ability_damage}!")
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
            return None

        if isinstance(mob_obj, Nether):
            self[1].append(mob_obj)
            return None

        if isinstance(mob_obj, End):
            self[2].append(mob_obj)
            return None

    def remove(self, mob_obj):
        for realm in self:
            if mob_obj in realm:
                realm.remove(mob_obj)
                return True
        return False
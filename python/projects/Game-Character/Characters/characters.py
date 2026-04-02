# Jordan Fitzgerald
# 4/1/2026
# This file defines the base GameCharacter class and the Hero and Villain subclasses, which include properties for health, mana, defense, level, XP, and battle chances (critical hit, block, dodge). It also includes methods for attacking, taking damage, healing, gaining XP, and leveling up.


import random

# Base class for all characters in the game
class GameCharacter:
    def __init__(self, name, health=100, mana=50, defense=25, level=1, crit_chance=10, block_chance=5, dodge_chance=5): # Initialize character with name, health, mana, defense, level, and battle chances
        self._name = name
        self._max_health = health
        self._max_mana = mana
        self._health = health
        self._mana = mana
        self._defense = defense
        self._level = level
        self._xp = 0
        self.role = "Character"
        self._crit_chance = crit_chance
        self._block_chance = block_chance
        self._dodge_chance = dodge_chance

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value <= 0:
            self._health = 0
        elif value >= self._max_health:
            self._health = self._max_health
        else:
            self._health = value

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value):
        if value <= 0:
            self._mana = 0
        elif value >= self._max_mana:
            self._mana = self._max_mana
        else:
            self._mana = value

    @property
    def defense(self):
        return self._defense

    @defense.setter
    def defense(self, value):
        if value <= 0:
            self._defense = 0
        elif value >= 100:
            self._defense = 100
        else:
            self._defense = value

    @property
    def level(self):
        return self._level

    @property
    def xp(self):
        return self._xp

    @xp.setter
    def xp(self, value):
        if value < 0:
            raise ValueError("XP cannot be negative.")
        self._xp = value

    @property
    def crit_chance(self): # Getter for critical hit chance, which determines the likelihood of landing a critical hit during an attack
        return self._crit_chance

    @crit_chance.setter
    def crit_chance(self, value): # Setter for critical hit chance, ensuring it stays within a reasonable range (0-100)
        if value < 0:
            self._crit_chance = 0
        elif value > 100:
            self._crit_chance = 100
        else:
            self._crit_chance = value

    @property
    def block_chance(self): # Getter for block chance, which determines the likelihood of successfully blocking part of an attack
        return self._block_chance

    @block_chance.setter
    def block_chance(self, value): # Setter for block chance, ensuring it stays within a reasonable range (0-100)
        if value < 0:
            self._block_chance = 0
        elif value > 100:
            self._block_chance = 100
        else:
            self._block_chance = value

    @property
    def dodge_chance(self): # Getter for dodge chance, which determines the likelihood of successfully dodging an attack
        return self._dodge_chance

    @dodge_chance.setter
    def dodge_chance(self, value): # Setter for dodge chance, ensuring it stays within a reasonable range (0-100)
        if value < 0:
            self._dodge_chance = 0
        elif value > 100:
            self._dodge_chance = 100
        else:
            self._dodge_chance = value

    def is_alive(self): # Check if the character is still alive (health > 0)
        return self.health > 0

    def calculate_attack_damage(self): # Calculate attack damage and determine whether the hit is critical
        damage = self.basic_attack_damage()
        critical = False

        if random.randint(1, 100) <= self.crit_chance:
            damage *= 2
            critical = True

        return damage, critical

    def take_damage(self, damage): # Calculate actual damage taken after considering dodge, block, and defense, then reduce health
        dodged = False
        blocked = False

        if random.randint(1, 100) <= self.dodge_chance:
            dodged = True
            return 0, dodged, blocked

        if random.randint(1, 100) <= self.block_chance:
            blocked = True
            damage = damage // 2

        actual_damage = max(1, damage - self.defense // 5)
        self.health -= actual_damage
        return actual_damage, dodged, blocked

    def restore_health(self, amount): # Restore health, ensuring it doesn't exceed max health
        self.health += amount

    def restore_mana(self, amount): # Restore mana, ensuring it doesn't exceed max mana
        self.mana += amount

    def gain_xp(self, xp_amount): # Gain XP and handle leveling up if XP reaches 100 or more
        if xp_amount < 0:
            raise ValueError("XP amount cannot be negative.")

        self.xp += xp_amount
        print(f"\n✨ {self.name} gains {xp_amount} XP!")

        while self.xp >= 100:
            self.xp -= 100
            self.level_up()

    def level_up(self): # Increase level and improve stats when leveling up
        self._level += 1
        self._max_health += 10
        self._max_mana += 5
        self.defense += 2
        self.crit_chance += 1
        self.block_chance += 1
        self.dodge_chance += 1
        self.health = self._max_health
        self.mana = self._max_mana
        print(f"⬆️  {self.name} leveled up to level {self.level}!")
        print(f"   Max Health increased to {self._max_health}")
        print(f"   Max Mana increased to {self._max_mana}")
        print(f"   Defense increased to {self.defense}")
        print(f"   Crit Chance increased to {self.crit_chance}%")
        print(f"   Block Chance increased to {self.block_chance}%")
        print(f"   Dodge Chance increased to {self.dodge_chance}%")

    def basic_attack_damage(self): # Calculate basic attack damage based on level (can be overridden by subclasses)
        return 10 + self.level * 2

    def attack(self, target): # Perform a basic attack on the target character, with crit, block, and dodge chances
        damage, critical = self.calculate_attack_damage()
        actual_damage, dodged, blocked = target.take_damage(damage)

        if dodged:
            print(f"💨 {target.name} dodged {self.name}'s attack!")
            return

        message = f"{self.name} attacks {target.name} for {actual_damage} damage!"
        if critical:
            message += " 💥 CRITICAL HIT!"
        if blocked:
            message += f" 🛡️ {target.name} blocked part of the attack!"

        print(message)

    def special_move(self, target): # Placeholder for special move, to be overridden by subclasses
        print(f"{self.name} has no special move.")

    def heal(self): # Heal the character, consuming mana and restoring health based on level
        if self.mana < 10:
            print(f"{self.name} does not have enough mana to heal.")
            return
        heal_amount = 20 + self.level * 3
        self.restore_health(heal_amount)
        self.mana -= 10
        print(f"{self.name} heals for {heal_amount} health!")

    def __str__(self): # String representation of the character showing all stats
        return (
            f"Name: {self.name}\n"
            f"Role: {self.role}\n"
            f"Level: {self.level}\n"
            f"Health: {self.health}/{self._max_health}\n"
            f"Mana: {self.mana}/{self._max_mana}\n"
            f"Defense: {self.defense}\n"
            f"XP: {self.xp}\n"
            f"Crit Chance: {self.crit_chance}%\n"
            f"Block Chance: {self.block_chance}%\n"
            f"Dodge Chance: {self.dodge_chance}%"
        )


class Hero(GameCharacter): # Hero class inherits from GameCharacter and sets the role to "Hero"
    def __init__(self, name, health=100, mana=50, defense=25, level=1, crit_chance=10, block_chance=5, dodge_chance=5):
        super().__init__(name, health, mana, defense, level, crit_chance, block_chance, dodge_chance)
        self.role = "Hero"


class Villain(GameCharacter): # Villain class inherits from GameCharacter and sets the role to "Villain"
    def __init__(self, name, health=100, mana=50, defense=25, level=1, crit_chance=10, block_chance=5, dodge_chance=5):
        super().__init__(name, health, mana, defense, level, crit_chance, block_chance, dodge_chance)
        self.role = "Villain"

    def evil_laugh(self): # Villain-specific method to print an evil laugh
        print(f"{self.name}: Mwahaha! Darkness will win!")

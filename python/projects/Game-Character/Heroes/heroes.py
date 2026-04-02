# Jordan Fitzgerald
# 4/1/2026
# This file defines the Hero subclasses, which include specific stats and special moves for each hero class (Warrior, Mage, Archer, Samurai, Tank, Assassin, Speedster, Agent). Each hero class overrides the basic attack damage and special move methods to provide unique gameplay experiences based on their role and abilities.

from characters import Hero

class Warrior(Hero): # Warrior class inherits from Hero and implements specific stats and special move for the warrior role
    def __init__(self, name):
        super().__init__(name, health=120, mana=40, defense=40, crit_chance=15, block_chance=15, dodge_chance=5)
        self.role = "Warrior"

    def basic_attack_damage(self): # Override basic attack damage for the Warrior class
        return 15 + self.level * 3

    def special_move(self, target): # Override special move for the Warrior class, implementing Power Strike which consumes mana and deals damage based on level
        if self.mana < 15:
            print(f"{self.name} does not have enough mana for Power Strike.")
            return
        damage = 30 + self.level * 5
        actual_damage, dodged, blocked = target.take_damage(damage)
        self.mana -= 15

        if dodged:
            print(f"💨 {target.name} dodged {self.name}'s Power Strike!")
            return

        message = f"{self.name} uses Power Strike on {target.name} for {actual_damage} damage!"
        if blocked:
            message += f" 🛡️ {target.name} blocked part of the special move!"
        print(message)


class Mage(Hero): # Mage class inherits from Hero and implements specific stats and special move for the mage role
    def __init__(self, name):
        super().__init__(name, health=85, mana=90, defense=18, crit_chance=20, block_chance=5, dodge_chance=8)
        self.role = "Mage"

    def basic_attack_damage(self): # Override basic attack damage for the Mage class, which is higher than the base class due to the mage's magical abilities
        return 18 + self.level * 4

    def special_move(self, target): # Override special move for the Mage class, implementing Fireball which consumes mana and deals damage based on level
        if self.mana < 20:
            print(f"{self.name} does not have enough mana for Fireball.")
            return
        damage = 40 + self.level * 6
        actual_damage, dodged, blocked = target.take_damage(damage)
        self.mana -= 20

        if dodged:
            print(f"💨 {target.name} dodged {self.name}'s Fireball!")
            return

        message = f"{self.name} uses Fireball on {target.name} for {actual_damage} damage!"
        if blocked:
            message += f" 🛡️ {target.name} blocked part of the spell!"
        print(message)


class Archer(Hero): # Archer class inherits from Hero and implements specific stats and special move for the archer role
    def __init__(self, name):
        super().__init__(name, health=95, mana=50, defense=28, crit_chance=18, block_chance=8, dodge_chance=15)
        self.role = "Archer"

    def basic_attack_damage(self): # Override basic attack damage for the Archer class, which is higher than the base class due to the archer's precision and skill with a bow
        return 17 + self.level * 3

    def special_move(self, target): # Override special move for the Archer class, implementing Rapid Shot which consumes mana and deals damage based on level
        if self.mana < 12:
            print(f"{self.name} does not have enough mana for Rapid Shot.")
            return
        damage = 28 + self.level * 4
        actual_damage, dodged, blocked = target.take_damage(damage)
        self.mana -= 12

        if dodged:
            print(f"💨 {target.name} dodged {self.name}'s Rapid Shot!")
            return

        message = f"{self.name} uses Rapid Shot on {target.name} for {actual_damage} damage!"
        if blocked:
            message += f" 🛡️ {target.name} blocked part of the attack!"
        print(message)


class Samurai(Hero): # Samurai class inherits from Hero and implements specific stats and special move for the samurai role
    def __init__(self, name):
        super().__init__(name, health=110, mana=35, defense=35, crit_chance=20, block_chance=10, dodge_chance=12)
        self.role = "Samurai"

    def basic_attack_damage(self): # Override basic attack damage for the Samurai class, which is higher than the base class due to the samurai's mastery of swordsmanship
        return 20 + self.level * 4

    def special_move(self, target): # Override special move for the Samurai class, implementing Blade Fury which consumes mana and deals damage based on level
        if self.mana < 12:
            print(f"{self.name} does not have enough mana for Blade Fury.")
            return
        damage = 35 + self.level * 5
        actual_damage, dodged, blocked = target.take_damage(damage)
        self.mana -= 12

        if dodged:
            print(f"💨 {target.name} dodged {self.name}'s Blade Fury!")
            return

        message = f"{self.name} uses Blade Fury on {target.name} for {actual_damage} damage!"
        if blocked:
            message += f" 🛡️ {target.name} blocked part of the attack!"
        print(message)


class Tank(Hero): # Tank class inherits from Hero and implements specific stats and special move for the tank role, which focuses on high health and defense to absorb damage
    def __init__(self, name):
        super().__init__(name, health=150, mana=30, defense=50, crit_chance=8, block_chance=25, dodge_chance=3)
        self.role = "Tank"

    def basic_attack_damage(self): # Override basic attack damage for the Tank class, which is lower than the base class due to the tank's focus on defense rather than offense
        return 12 + self.level * 2

    def special_move(self, target): # Override special move for the Tank class, implementing Shield Slam which consumes mana and deals damage based on level, while also providing a defensive boost
        if self.mana < 10:
            print(f"{self.name} does not have enough mana for Shield Slam.")
            return
        damage = 22 + self.level * 3
        actual_damage, dodged, blocked = target.take_damage(damage)
        self.mana -= 10

        if dodged:
            print(f"💨 {target.name} dodged {self.name}'s Shield Slam!")
            return

        message = f"{self.name} uses Shield Slam on {target.name} for {actual_damage} damage!"
        if blocked:
            message += f" 🛡️ {target.name} blocked part of the attack!"
        print(message)

    def guard(self): # Additional method for the Tank class to raise their guard, increasing defense and block chance for the next turn
        self.defense += 5
        self.block_chance += 5
        print(f"{self.name} raises their guard! Defense and block chance increase.")


class Assassin(Hero): # Assassin class inherits from Hero and implements specific stats and special move for the assassin role, which focuses on high damage and agility
    def __init__(self, name):
        super().__init__(name, health=75, mana=60, defense=15, crit_chance=30, block_chance=5, dodge_chance=25)
        self.role = "Assassin"

    def basic_attack_damage(self): # Override basic attack damage for the Assassin class, which is higher than the base class due to the assassin's focus on dealing high damage quickly
        return 25 + self.level * 5

    def special_move(self, target): # Override special move for the Assassin class, implementing Shadow Strike which consumes mana and deals damage based on level, with a chance to ignore the target's defense
        if self.mana < 20:
            print(f"{self.name} does not have enough mana for Shadow Strike.")
            return
        damage = 50 + self.level * 8
        actual_damage, dodged, blocked = target.take_damage(damage)
        self.mana -= 20

        if dodged:
            print(f"💨 {target.name} dodged {self.name}'s Shadow Strike!")
            return

        message = f"{self.name} uses Shadow Strike on {target.name} for {actual_damage} damage!"
        if blocked:
            message += f" 🛡️ {target.name} blocked part of the strike!"
        print(message)


class Speedster(Hero): # Speedster class inherits from Hero and implements specific stats and special move for the speedster role, which focuses on speed, dodge chance, and quick attacks
    def __init__(self, name):
        super().__init__(name, health=80, mana=65, defense=18, crit_chance=22, block_chance=5, dodge_chance=35)
        self.role = "Speedster"

    def basic_attack_damage(self): # Override basic attack damage for the Speedster class, which is based on speed and quick strikes
        return 16 + self.level * 3

    def special_move(self, target): # Override special move for the Speedster class, implementing Lightning Dash which consumes mana and deals damage based on level
        if self.mana < 15:
            print(f"{self.name} does not have enough mana for Lightning Dash.")
            return
        damage = 30 + self.level * 5
        actual_damage, dodged, blocked = target.take_damage(damage)
        self.mana -= 15

        if dodged:
            print(f"💨 {target.name} dodged {self.name}'s Lightning Dash!")
            return

        message = f"{self.name} uses Lightning Dash on {target.name} for {actual_damage} damage!"
        if blocked:
            message += f" 🛡️ {target.name} blocked part of the dash!"
        print(message)


class Agent(Hero): # Agent class inherits from Hero and implements specific stats and special move for the agent role, which acts as a balanced basic hero equivalent to the henchman
    def __init__(self, name):
        super().__init__(name, health=90, mana=40, defense=22, crit_chance=14, block_chance=10, dodge_chance=12)
        self.role = "Agent"

    def basic_attack_damage(self): # Override basic attack damage for the Agent class, which is balanced and tactical
        return 14 + self.level * 3

    def special_move(self, target): # Override special move for the Agent class, implementing Tactical Strike which consumes mana and deals damage based on level
        if self.mana < 10:
            print(f"{self.name} does not have enough mana for Tactical Strike.")
            return
        damage = 24 + self.level * 4
        actual_damage, dodged, blocked = target.take_damage(damage)
        self.mana -= 10

        if dodged:
            print(f"💨 {target.name} dodged {self.name}'s Tactical Strike!")
            return

        message = f"{self.name} uses Tactical Strike on {target.name} for {actual_damage} damage!"
        if blocked:
            message += f" 🛡️ {target.name} blocked part of the move!"
        print(message)

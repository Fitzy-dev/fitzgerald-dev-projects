# Jordan Fitzgerald
# 4/1/2026
# This file defines the Villain subclasses, which include specific stats and special moves for each villain
from characters import Villain


class Necromancer(Villain): # Necromancer class inherits from Villain and implements specific stats and special move for the necromancer role, which focuses on dark magic and summoning undead minions
    def __init__(self, name):
        super().__init__(name, health=90, mana=100, defense=20, crit_chance=18, block_chance=5, dodge_chance=8)
        self.role = "Necromancer"

    def basic_attack_damage(self): # Override basic attack damage for the Necromancer class, which is higher than the base class due to the necromancer's mastery of dark magic
        return 18 + self.level * 4

    def special_move(self, target): # Override special move for the Necromancer class, implementing Raise Dead which consumes mana and deals damage based on level, with a chance to summon an undead minion that attacks the target
        if self.mana < 25:
            print(f"{self.name} does not have enough mana for Raise Dead.")
            return
        damage = 45 + self.level * 6
        actual_damage, dodged, blocked = target.take_damage(damage)
        self.mana -= 25

        if dodged:
            print(f"💨 {target.name} dodged {self.name}'s Raise Dead!")
            return

        message = f"{self.name} uses Raise Dead on {target.name} for {actual_damage} damage!"
        if blocked:
            message += f" 🛡️ {target.name} blocked part of the dark magic!"
        print(message)


class DarkKnight(Villain): # DarkKnight class inherits from Villain and implements specific stats and special move for the dark knight role, which focuses on heavy armor and powerful melee attacks
    def __init__(self, name):
        super().__init__(name, health=125, mana=45, defense=32, crit_chance=16, block_chance=15, dodge_chance=6)
        self.role = "Dark Knight"

    def basic_attack_damage(self): # Override basic attack damage for the DarkKnight class, which is higher than the base class due to the dark knight's focus on powerful melee attacks
        return 20 + self.level * 5

    def special_move(self, target): # Override special move for the DarkKnight class, implementing Dark Slash which consumes mana and deals damage based on level, with a chance to reduce the target's defense
        if self.mana < 20:
            print(f"{self.name} does not have enough mana for Dark Slash.")
            return
        damage = 40 + self.level * 8
        actual_damage, dodged, blocked = target.take_damage(damage)
        self.mana -= 20

        if dodged:
            print(f"💨 {target.name} dodged {self.name}'s Dark Slash!")
            return

        message = f"{self.name} uses Dark Slash on {target.name} for {actual_damage} damage!"
        if blocked:
            message += f" 🛡️ {target.name} blocked part of the slash!"
        print(message)


class Sorcerer(Villain): # Sorcerer class inherits from Villain and implements specific stats and special move for the sorcerer role, which focuses on powerful spells and magical attacks
    def __init__(self, name):
        super().__init__(name, health=80, mana=110, defense=15, crit_chance=22, block_chance=4, dodge_chance=10)
        self.role = "Sorcerer"

    def basic_attack_damage(self): # Override basic attack damage for the Sorcerer class, which is higher than the base class due to the sorcerer's focus on powerful spells and magical attacks
        return 25 + self.level * 5

    def special_move(self, target): # Override special move for the Sorcerer class, implementing Arcane Blast which consumes mana and deals damage based on level, with a chance to silence the target and prevent them from using special moves for the next turn
        if self.mana < 30:
            print(f"{self.name} does not have enough mana for Arcane Blast.")
            return
        damage = 60 + self.level * 10
        actual_damage, dodged, blocked = target.take_damage(damage)
        self.mana -= 30

        if dodged:
            print(f"💨 {target.name} dodged {self.name}'s Arcane Blast!")
            return

        message = f"{self.name} uses Arcane Blast on {target.name} for {actual_damage} damage!"
        if blocked:
            message += f" 🛡️ {target.name} blocked part of the spell!"
        print(message)


class Rogue(Villain): # Rogue class inherits from Villain and implements specific stats and special move for the rogue role, which focuses on stealth and quick attacks
    def __init__(self, name):
        super().__init__(name, health=70, mana=60, defense=20, crit_chance=24, block_chance=6, dodge_chance=22)
        self.role = "Rogue"

    def basic_attack_damage(self): # Override basic attack damage for the Rogue class, which is higher than the base class due to the rogue's focus on stealth and quick attacks
        return 22 + self.level * 4

    def special_move(self, target): # Override special move for the Rogue class, implementing Backstab which consumes mana and deals damage based on level, with a chance to critically hit
        if self.mana < 15:
            print(f"{self.name} does not have enough mana for Backstab.")
            return
        damage = 35 + self.level * 6
        actual_damage, dodged, blocked = target.take_damage(damage)
        self.mana -= 15

        if dodged:
            print(f"💨 {target.name} dodged {self.name}'s Backstab!")
            return

        message = f"{self.name} uses Backstab on {target.name} for {actual_damage} damage!"
        if blocked:
            message += f" 🛡️ {target.name} blocked part of the attack!"
        print(message)


class Henchman(Villain): # Henchman class inherits from Villain and implements specific stats and special move for the henchman role, which is a basic enemy with moderate stats and a simple special move
    def __init__(self, name):
        super().__init__(name, health=65, mana=35, defense=12, crit_chance=12, block_chance=8, dodge_chance=8)
        self.role = "Henchman"

    def basic_attack_damage(self): # Override basic attack damage for the Henchman class, which is lower than the base class due to the henchman's role as a basic enemy
        return 15 + self.level * 3

    def special_move(self, target): # Override special move for the Henchman class, implementing Brutal Strike which consumes mana and deals damage based on level, with a chance to stun the target for the next turn
        if self.mana < 10:
            print(f"{self.name} does not have enough mana for Brutal Strike.")
            return
        damage = 25 + self.level * 5
        actual_damage, dodged, blocked = target.take_damage(damage)
        self.mana -= 10

        if dodged:
            print(f"💨 {target.name} dodged {self.name}'s Brutal Strike!")
            return

        message = f"{self.name} uses Brutal Strike on {target.name} for {actual_damage} damage!"
        if blocked:
            message += f" 🛡️ {target.name} blocked part of the move!"
        print(message)


class Brute(Villain): # Brute class inherits from Villain and implements specific stats and special move for the brute role, which focuses on high health and powerful melee attacks, but low mana and defense
    def __init__(self, name):
        super().__init__(name, health=135, mana=25, defense=40, crit_chance=10, block_chance=18, dodge_chance=4)
        self.role = "Brute"

    def basic_attack_damage(self): # Override basic attack damage for the Brute class, which is higher than the base class due to the brute's focus on powerful melee attacks, but lower than other villains due to the brute's lack of finesse and magical abilities
        return 30 + self.level * 5

    def special_move(self, target): # Override special move for the Brute class, implementing Earthquake which consumes mana and deals damage based on level, with a chance to knock down the target and reduce their defense for the next turn
        if self.mana < 20:
            print(f"{self.name} does not have enough mana for Earthquake.")
            return
        damage = 50 + self.level * 10
        actual_damage, dodged, blocked = target.take_damage(damage)
        self.mana -= 20

        if dodged:
            print(f"💨 {target.name} dodged {self.name}'s Earthquake!")
            return

        message = f"{self.name} uses Earthquake on {target.name} for {actual_damage} damage!"
        if blocked:
            message += f" 🛡️ {target.name} blocked part of the blow!"
        print(message)


class Overlord(Villain): # Overlord class inherits from Villain and implements specific stats and special move for the overlord role, which is a powerful final boss with high health, mana, and defense, as well as a devastating special move
    def __init__(self, name):
        super().__init__(name, health=160, mana=120, defense=50, crit_chance=20, block_chance=15, dodge_chance=8)
        self.role = "Overlord"

    def basic_attack_damage(self): # Override basic attack damage for the Overlord class, which is higher than the base class due to the overlord's status as a powerful final boss
        return 35 + self.level * 5

    def special_move(self, target): # Override special move for the Overlord class, implementing Apocalypse which consumes mana and deals massive damage based on level, with a chance to instantly defeat the target if their health is below a certain threshold
        if self.mana < 50:
            print(f"{self.name} does not have enough mana for Apocalypse.")
            return
        damage = 100 + self.level * 20
        actual_damage, dodged, blocked = target.take_damage(damage)
        self.mana -= 50

        if dodged:
            print(f"💨 {target.name} dodged {self.name}'s Apocalypse!")
            return

        message = f"{self.name} uses Apocalypse on {target.name} for {actual_damage} damage!"
        if blocked:
            message += f" 🛡️ {target.name} blocked part of the ultimate attack!"
        print(message)

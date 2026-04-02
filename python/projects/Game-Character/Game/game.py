# Jordan Fitzgerald
# 4/1/2026
# This file contains the main game logic, including character creation, combat, and story progression.

from heroes import Warrior, Mage, Archer, Samurai, Tank, Assassin, Speedster, Agent
from villains import Necromancer, DarkKnight, Sorcerer, Rogue, Henchman, Brute, Overlord
from utils import line, small_line, show_character

import random

def choose_side():
    while True:
        print("\nChoose your path:")
        print("1. Hero")
        print("2. Villain")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            return "Hero"
        if choice == "2":
            return "Villain"
        print("Invalid choice. Try again.")


def choose_hero_class(name):
    while True:
        print("\nChoose your hero class:")
        print("1. Warrior")
        print("2. Mage")
        print("3. Archer")
        print("4. Samurai")
        print("5. Tank")
        print("6. Assassin")
        print("7. Speedster")
        print("8. Agent")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            return Warrior(name)
        if choice == "2":
            return Mage(name)
        if choice == "3":
            return Archer(name)
        if choice == "4":
            return Samurai(name)
        if choice == "5":
            return Tank(name)
        if choice == "6":
            return Assassin(name)
        if choice == "7":
            return Speedster(name)
        if choice == "8":
            return Agent(name)
        print("Invalid choice. Try again.")


def choose_villain_class(name):
    while True:
        print("\nChoose your villain class:")
        print("1. Necromancer")
        print("2. Dark Knight")
        print("3. Sorcerer")
        print("4. Rogue")
        print("5. Brute")
        print("6. Overlord")
        print("7. Henchman")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            return Necromancer(name)
        if choice == "2":
            return DarkKnight(name)
        if choice == "3":
            return Sorcerer(name)
        if choice == "4":
            return Rogue(name)
        if choice == "5":
            return Brute(name)
        if choice == "6":
            return Overlord(name)
        if choice == "7":
            return Henchman(name)
        print("Invalid choice. Try again.")


def get_enemy(side, fight_number):
    if side == "Hero":
        villains = [
            Henchman("Grimtooth"),
            Rogue("Shade"),
            DarkKnight("Malzor"),
            Necromancer("Vexis"),
            Brute("Crag"),
            Overlord("Zarok"),
        ]
        enemy = villains[min(fight_number - 1, len(villains) - 1)]
    else:
        heroes = [
            Agent("Cole"),
            Archer("Aerin"),
            Speedster("Volt"),
            Warrior("Leon"),
            Samurai("Takeda"),
            Tank("Brom"),
            Mage("Selene"),
            Assassin("Nyx"),
        ]
        enemy = heroes[min(fight_number - 1, len(heroes) - 1)]

    enemy._level = fight_number
    enemy._max_health += (fight_number - 1) * 10
    enemy._max_mana += (fight_number - 1) * 5
    enemy.health = enemy._max_health
    enemy.mana = enemy._max_mana
    enemy.defense += (fight_number - 1) * 2
    return enemy


def story_choice(player, fight_number):
    line()
    print(f"Before fight {fight_number}, you face a choice...")

    if fight_number == 1:
        print("1. Search an old chest (+15 mana)")
        print("2. Train with your weapon (+6 attack this fight)")
        choice = input("Choose: ").strip()
        if choice == "1":
            player.restore_mana(15)
            print(f"{player.name} found an energy crystal. Mana increased!")
            return 0, 0, 0
        else:
            print(f"{player.name} sharpens their skills.")
            return 6, 0, 0

    if fight_number == 2:
        print("1. Rest by the campfire (+20 health)")
        print("2. Study the enemy (+5 defense this fight)")
        choice = input("Choose: ").strip()
        if choice == "1":
            player.restore_health(20)
            print(f"{player.name} feels refreshed.")
            return 0, 0, 0
        else:
            print(f"{player.name} prepares carefully. Defense increased for this fight!")
            return 0, 5, 0

    if fight_number == 3:
        print("1. Drink a risky potion (+25 health, -10 mana)")
        print("2. Focus your mind (+10% crit chance this fight)")
        choice = input("Choose: ").strip()
        if choice == "1":
            player.restore_health(25)
            player.mana -= 10
            print(f"{player.name} drinks the potion and feels stronger.")
            return 0, 0, 0
        else:
            print(f"{player.name} focuses intensely before the battle.")
            return 0, 0, 10

    return 0, 0, 0


def player_turn(player, enemy, bonus_attack, bonus_defense, bonus_crit):
    small_line()
    print("Your turn:")
    print("1. Basic Attack")
    print("2. Special Move")
    print("3. Heal")
    if isinstance(player, Tank):
        print("4. Guard")

    choice = input("Choose action: ").strip()

    if choice == "1":
        damage = player.basic_attack_damage() + bonus_attack
        critical = False

        if random.randint(1, 100) <= (player.crit_chance + bonus_crit):
            damage *= 2
            critical = True

        actual_damage, dodged, blocked = enemy.take_damage(damage)

        if dodged:
            print(f"💨 {enemy.name} dodged your attack!")
            return

        message = f"{player.name} attacks {enemy.name} for {actual_damage} damage!"
        if critical:
            message += " 💥 CRITICAL HIT!"
        if blocked:
            message += f" 🛡️ {enemy.name} blocked part of the attack!"
        print(message)

    elif choice == "2":
        player.special_move(enemy)
    elif choice == "3":
        player.heal()
    elif choice == "4" and isinstance(player, Tank):
        player.guard()
    else:
        print("Invalid action. You lose your turn.")


def enemy_turn(enemy, player, bonus_defense):
    if not enemy.is_alive():
        return

    small_line()
    print(f"{enemy.name}'s turn:")

    original_defense = player.defense
    player.defense += bonus_defense

    if enemy.mana >= 15 and random.randint(1, 100) <= 35:
        enemy.special_move(player)
    else:
        enemy.attack(player)

    player.defense = original_defense


def battle(player, enemy, fight_number):
    bonus_attack, bonus_defense, bonus_crit = story_choice(player, fight_number)

    line()
    print(f"⚔️  FIGHT {fight_number}: {player.name} vs {enemy.name}")
    line()

    turn_count = 1

    while player.is_alive() and enemy.is_alive():
        print(f"\nTurn {turn_count}")
        show_character(player)
        show_character(enemy)

        player_turn(player, enemy, bonus_attack, bonus_defense, bonus_crit)

        if enemy.is_alive():
            enemy_turn(enemy, player, bonus_defense)

        turn_count += 1

    if player.is_alive():
        line()
        print(f"🏆 {player.name} defeated {enemy.name}!")
        player.gain_xp(50)
        player.restore_health(15)
        player.restore_mana(10)
        print(f"{player.name} recovers a little after the battle.")
        return True
    else:
        line()
        print(f"💀 {player.name} was defeated by {enemy.name}...")
        return False

# Intro function to display the game title and a welcome message, setting the stage for the player to choose their path and character class
def intro():
    line()
    print("█▀▀ █▀█ █▀▄▀█ █▀▀   █▀▄▀█ █ █▄░█ █ █▀▀ ▄▀█ █▀▄▀█ █▀▀")
    print("█▄█ █▄█ █░▀░█ ██▄   █░▀░█ █ █░▀█ █ █▄█ █▀█ █░▀░█ ██▄")
    print("\nWelcome to the Character Path Battle Game!")
    print("Choose your path, survive 3 battles, and shape your fate.")
    line()

# Ending function to display the final outcome of the game based on the player's path and performance, showing a message and the final stats of the character
def ending(player, side):
    line()
    if side == "Hero":
        print(f"🌟 {player.name} has protected the realm and become a legendary hero!")
    else:
        print(f"🔥 {player.name} has conquered all enemies and risen as a feared villain!")
    show_character(player)

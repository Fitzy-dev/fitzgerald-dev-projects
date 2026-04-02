# Jordan Fitzgerald
# 4/1/2026
# This file contains utility functions for the game, including functions to display character stats in a visually appealing way using text-based bars and formatting.
def line():
    print("\n" + "=" * 60)


def small_line():
    print("-" * 60)


def stat_bar(label, current, maximum):
    filled = int((current / maximum) * 20) if maximum > 0 else 0
    empty = 20 - filled
    bar = "█" * filled + "░" * empty
    print(f"{label}: [{bar}] {current}/{maximum}")


def show_character(character):
    line()
    print(f"{character.name} the {character.role}  |  Level {character.level}")
    stat_bar("HP  ", character.health, character._max_health)
    stat_bar("Mana", character.mana, character._max_mana)
    print(f"Defense: {character.defense}   XP: {character.xp}   Crit: {character.crit_chance}%   Block: {character.block_chance}%   Dodge: {character.dodge_chance}%")
    line()

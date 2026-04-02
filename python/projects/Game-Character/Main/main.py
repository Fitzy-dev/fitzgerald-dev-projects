# Jordan Fitzgerald
# 4/1/2026
# This file contains the main game logic, including character creation, combat, and story progression.

import random
from game import choose_side, choose_hero_class, choose_villain_class, get_enemy, battle, ending, intro
from utils import show_character

def main():
    intro()

    name = input("Enter your character name: ").strip()
    if not name:
        name = "Player"

    side = choose_side()

    if side == "Hero":
        player = choose_hero_class(name)
    else:
        player = choose_villain_class(name)

    print(f"\nYou chose the path of the {side}!")
    show_character(player)

    for fight_number in range(1, 4):
        enemy = get_enemy(side, fight_number)
        won = battle(player, enemy, fight_number)

        if not won:
            print("\nGame Over.")
            return

    ending(player, side)


if __name__ == "__main__":
    main()

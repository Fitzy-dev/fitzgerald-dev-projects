File: characters.py

Overview

This file defines the core base classes used throughout the entire game. It contains the GameCharacter class and its two main subclasses: Hero and Villain.

All shared mechanics like health, combat, and leveling are implemented here.

Features
    •    Base character system
    •    Health and mana management
    •    XP and leveling system
    •    Critical hit system
    •    Block and dodge mechanics
    •    Attack and healing system

Concepts Used
    •    Encapsulation using properties (@property)
    •    Inheritance (Hero and Villain extend GameCharacter)
    •    Random probability (crit/block/dodge)
    •    Method overriding (designed for subclasses)

How to Use

This file is not run directly.

It is imported into other files like:
from characters import GameCharacter, Hero, Villain

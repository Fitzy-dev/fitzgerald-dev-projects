File: heroes.py

Overview

This file defines all Hero character classes in the game. Each class inherits from the Hero base class and customizes stats and abilities.

Features
    •    Multiple hero classes:
    •    Warrior
    •    Mage
    •    Archer
    •    Samurai
    •    Tank
    •    Assassin
    •    Speedster
    •    Agent
    •    Unique stats per class
    •    Custom attack damage formulas
    •    Special moves for each class

Concepts Used
    •    Inheritance (class Warrior(Hero))
    •    Polymorphism (overriding basic_attack_damage and special_move)
    •    Game balancing (stat design)

How to Use

Imported into the game logic:
from heroes import Warrior, Mage, Archer

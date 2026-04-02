File: Media Catalogue

Overview

This file builds a small media catalog program in Python. It defines classes for movies and TV series, validates user input, stores media items in a catalog, and prints them in a clean formatted view.

The program demonstrates object-oriented programming by using inheritance, special methods, validation, and list filtering.

Features
    •    Creates a Movie class with:
    •    title
    •    year
    •    director
    •    duration
    •    Validates movie data:
    •    title cannot be empty
    •    year must be 1895 or later
    •    director cannot be empty
    •    duration must be positive
    •    Creates a TVSeries class that inherits from Movie
    •    Adds extra TV series attributes:
    •    seasons
    •    total episodes
    •    Validates TV series data:
    •    seasons must be at least 1
    •    total episodes must be at least 1
    •    Creates a MediaCatalogue class to store items
    •    Adds media items to a list
    •    Filters movies separately from TV series
    •    Uses __str__ methods to format output neatly
    •    Handles invalid input with try / except

Concepts Used
    •    Classes and objects
    •    Constructors with __init__
    •    Inheritance
    •    Method overriding
    •    Encapsulation through validation
    •    Special methods like __str__
    •    Exception handling with ValueError
    •    Lists and list comprehensions
    •    Type checking with type()
    •    Enumeration with enumerate()

How to Run the File

Run the file in Python:
python media_catalogue.py

# General Tic-Tac-Toe

A customizable multiplayer Tic-Tac-Toe game written in C++. Unlike traditional
Tic-Tac-Toe, this program supports multiple players and different board sizes
while tracking player statistics across multiple games.

## Features

- Supports 2–7 players
- Custom board sizes
  - 3–9 rows
  - 3–12 columns
- Each player receives a unique game piece
- Player name validation and formatting
- Validates moves before placing pieces
- Detects horizontal, vertical, and diagonal wins
- Highlights the winning pieces
- Detects draw games
- Tracks wins, losses, and draws
- Supports playing multiple games in one session
- Rotates the starting player between games

## How the Game Works

At the beginning of the program, players enter their names and are assigned
unique game pieces.

Before each game, the players choose the number of rows and columns for the
board.

Players enter moves using a row letter followed by a column number.

Example:

A1
B4
C10

The first player to place three of their pieces consecutively horizontally,
vertically, or diagonally wins the game.

After each game, the program displays updated statistics for every player.

## Compile

Using g++:

```bash
g++ general_tic_tac_toe.cpp -o program
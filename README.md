# Tic-Tac-Toe
## Introduction
This is a two player tic tac toe game, which uses the 
terminal interface. The user selects the position where they
want to play their move by typing the row and column.
The game is resolved when a player has 3 unobstructed
moves in one row or column.

### Getting started with the package
To get started clone this repo and ensure you are in teh right folder.
```bash
git clone https://github.com/mwolinska/Tic-Tac-Toe
cd Tic-Tac-Toe
```

Then, simply install all the dependencies using [poetry](https://python-poetry.org).
```bash
poetry install
```

### Using the package
You can either play a single player game (against a bot):
```bash
play_alone
```
or a two player game (black makes the first move):
```bash
play_together
```
An example run would look something like this:
First the game randomly decides who will start the game. 
Player 1  plays using crosses and Player 2 plays using circles.
If you opt to use `play_alone` the bot plays as Player 2.


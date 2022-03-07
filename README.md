# Tic-Tac-Toe
## Introduction
This is a two player tic tac toe game, which uses the 
terminal interface. The user selects the position where they
want to play their move by typing the row and column.
The game is resolved when a player has 3 unobstructed
moves in one row or column.

### Getting started with the package
To get started clone this repo.
```bash
git clone https://github.com/mwolinska/Tic-Tac-Toe
cd Tic-Tac-Toe
```
Then set up and activate a virtual environment.
```bash
python3 -m venv ./venv
source venv/bin/activate
```
Finally, install all the dependencies.
```bash
pip3 install -r requirements.txt
```

### Using the package
First, ensure you are in the right directory.
```bash
cd Tic-Tac-Toe
```

Run the code as follows:
```bash
python3 main.py
```
An example run would look something like this:
```
Play position row: 0
Play position column: 0
[[1 0 0]
 [0 0 0]
 [0 0 0]]
Play position row: 2
Play position column: 2
[[1 0 0]
 [0 0 0]
 [0 0 2]]
Play position row: 0
Play position column: 1
[[1 1 0]
 [0 0 0]
 [0 0 2]]
Play position row: 1
Play position column: 1
[[1 1 0]
 [0 2 0]
 [0 0 2]]
Play position row: 0
Play position column: 2
[[1 1 1]
 [0 2 0]
 [0 0 2]]
Player1won the game
The game has end, do you want to play again? Type Yes / No: No
Thanks for playing.
```

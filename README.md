# cse230-5

Repository for Cycle Game for Team-j-12pm

Cycle

The best rides are the ones where you
bite off much more than you can chew,
and live through it. --Doug Bradbury--

Overview

Cycle is a game where the players try to cut each other off using cycles that leave a trail behind them.

Rules

Cycle is played according to the following rules.

Players can move up, down, left and right...

Player one moves using the W, S, A and D keys.

Player two moves using the I, K, J and L keys.

Each player's trail grows as they move.

Players try to maneuver so the opponent collides with their trail.

If a player collides with their opponent's trail...

A "winner" message is displayed in the middle of the screen.

The winner earns one point.

In the case of a head-on collision, both players lose one point.

The cycles turn white.

Players keep moving and turning but don't run into each other.

Players can press the Spacebar to continue the game.

Authors: Marcus Ojo-Osasere, Rune Larsen, Julie Antezana

## Getting Started

---

Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.

```
python3 -m pip install raylib
```

After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

python3 cycle

```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the
project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```

root (project root folder)

+-- cycle (source code for game)

+-- game (specific game classes)

+-- **main**.py (entry point for program)

+-- README.md (general info)

```

## Required Technologies

---

* Python 3.8.0

* Raylib Python CFFI 3.7
```

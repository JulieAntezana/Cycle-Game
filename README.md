# cse230-5

Repository for Cycle Game for Team-j-12pm

Cycle
The best rides are the ones where you
bite off much more than you can chew,
and live through it.

- Doug Bradbury -
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
A "game over" message is displayed in the middle of the screen.
The cycles turn white.
Players keep moving and turning but don't run into each other.

Authors: Marcus Ojo-Osasere, Rune Larsen, Julie Antezana

Reuse all the classes from the Snake game.
Add a new class called grow_trail_action.py
class GrowTrailAction(Action):
def execute(self, cast, script):
"""Executes the grow trail action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

    def _grow_trail(self, cast):
        """Add segments to grow the trail of the cycle.

        Args:
            cast (Cast): The cast of Actors in the game.
        """

Add a class to handle scoring, player gets a point if other player collides with a tail (opponent's tail or his own tail)
Edit the method to handle game over - Marcus
Add a second cycle - Julie
Add a second score heads up display -Rune

from game.scripting.action import Action

class GrowTrailAction(Action):
    def execute(self, cast, script):
        """Executes the grow trail action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """        
        self._grow_trail(cast)

    def _grow_trail(self, cast):
        """Add segments to grow the trail of the cycle.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snake = cast.get_first_actor("snakes")
        snake.grow_tail(1)

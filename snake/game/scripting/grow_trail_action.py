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
        cycle1 = cast.get_first_actor("cycle1")
        cycle2 = cast.get_first_actor("cycle2")
        cycle1.grow_tail(1)
        cycle2.grow_tail(1)

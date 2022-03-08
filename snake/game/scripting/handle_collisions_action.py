import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.casting.cycle1 import CycleOne
from game.casting.cycle2 import CycleTwo
from game.services.keyboard_service import KeyboardService
from game.scripting.control_cycle1_action import ControlCycleOneAction
from game.scripting.control_cycle2_action import ControlCycleTwoAction


class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the cycles collide with their own segments, or the segments of it's opponent, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            # self._handle_food_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast, script)

    # def _handle_food_collision(self, cast):
    #     """Updates the score and moves the food if the snake collides with the food.
        
    #     Args:
    #         cast (Cast): The cast of Actors in the game.
    #     """
    #     score = cast.get_first_actor("scores")
    #     food = cast.get_first_actor("foods")
    #     snake = cast.get_first_actor("player1") 
    #     player2 = cast.get_first_actor("player2")           
    #     head = snake.get_head()

    #     if head.get_position().equals(food.get_position()):
    #         points = food.get_points()
    #         snake.grow_tail(points)
    #         score.add_points(points)
    #         food.reset()
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the cycle collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cycle1 = cast.get_first_actor("cycle1")
        head = cycle1.get_segments()[0]
        segments = cycle1.get_segments()[1:]
        
        cycle2 = cast.get_first_actor("cycle2")
        head = cycle2.get_segments()[0]
        segments = cycle2.get_segments()[1:]
        
        for segment in segments:
            if head.get_position().equals(segment.get_position()):
                self._is_game_over = True
        
    def _handle_game_over(self, cast, script):
        """Shows the 'game over' message and turns the cycles white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            old_cycle1 = cast.get_first_actor("cycle1")   
            cast.remove_actor("cycle1", old_cycle1)
            cast.add_actor("cycle1", CycleOne())

            old_cycle2 = cast.get_first_actor("cycle2")   
            cast.remove_actor("cycle2", old_cycle2)
            cast.add_actor("cycle2", CycleTwo())

            keyboard_service = KeyboardService() 


            script.add_action("input", ControlCycleOneAction(keyboard_service))
            script.add_action("input", ControlCycleTwoAction(keyboard_service))

            self._is_game_over = False

            # cycle1 = cast.get_first_actor("cycle1")
            # segments = cycle1.get_segments()

            # x = int(150)
            # y = int(150)
            # position = Point(x, y)

            # cycle2 = cast.get_first_actor("cycle2")
            # segments = cycle2.get_segments()

            # x = int(750)
            # y = int(150)
            # position = Point(x, y)

            # message = Actor()
            # message.set_text("Game Over!")
            # message.set_position(position)
            # cast.add_actor("messages", message)

            # for segment in segments:
            #     segment.set_color(constants.WHITE)
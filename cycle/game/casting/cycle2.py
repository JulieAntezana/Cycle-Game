import constants
from game.casting.actor import Actor
from game.casting.cycle1 import CycleOne
from game.shared.point import Point


class CycleTwo(CycleOne):
    """
    A Cycle is a wheeled vehicle that leaves a trail behind it to indicate the path it has taken.
    
    The responsibility of CycleTwo is to move itself.

    Attributes:
        _points (int): The number of points the collision is worth.
    """
    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("0")
            segment.set_color(constants.YELLOW)
            self._segments.append(segment)
    
    def _prepare_body(self):

        x = int(750)
        y = int(constants.MAX_Y / 2)

        for i in range(constants.CYCLE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * -constants.CELL_SIZE, 0)
            # velocity = Point(1 *-constants.CELL_SIZE, 0)
            # velocity = Point(0, 1 * constants.CELL_SIZE)
            # velocity = Point(0, 1 * constants.CELL_SIZE)
            text = "8" if i == 0 else "0"
            color = constants.RED if i == 0 else constants.YELLOW
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)    
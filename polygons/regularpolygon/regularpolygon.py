
import math
from ..polygon.polygon import Polygon

class RegularPolygon(Polygon):
    """A class representing any regular polygon.
    """

    def __init__(self, sides:int, length:float):
    """Initialize the RegularPolygon class.
    
       :param sides: The number of sides the regular polygon has
       :param length: The length of each side
       :raises ValueError: if sides or length are invalid values
    """
        self.length = length
        lengths = [length] * sides
        angles = [self.angle(sides)] * sides
        super().__init__(sides, lengths, angles)

    @property
    def perimeter(self) -> float:
        """Return the perimiter of the regular polygon.
        """
        return self.sides * self.length

    @property
    def apothem(self) -> float:
        """Return the apothem of the regular polygon.
        """
        tan = math.tan(math.pi / self.sides)
        return self.length / (2 * tan)

    @property
    def area(self) -> float:
        """Return the area of the regular polygon.
        """
        if self.sides == 4:
            return self.length ** 2
        else:
            return (self.apothem * self.perimeter) / 2

    @classmethod
    def angle(self, sides:int) -> float:
        """Return the calculated angle for a regular polygon with the given sides.

           :param sides: The number of sides of the regular polygon
           :raise ValueError: if sides < 3 or not an int
        """
        if sides < 3:
            raise ValueError('cannot calculate angles of polygon with less than 3 sides')
        elif type(sides) != int:
            raise ValueError('sides must be an int')
        angle_sum = 180 * (sides - 2)
        return angle_sum / sides

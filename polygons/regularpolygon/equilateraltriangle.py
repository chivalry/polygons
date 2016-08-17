import math
from .regularpolygon import RegularPolygon

class EquilateralTriangle(RegularPolygon):
    """A class to represent an equilateral triangle.
    """

    def __init__(self, length:float):
        """Initialzie the EquilateralTriangle class.
        """
        super().__init__(3, length)

    @property
    def area(self) -> float:
        """Return the area of the equilateral triangle.
        """
        return (self.length ** 2) * math.sqrt(3) / 4

    @property
    def name(self) -> str:
        """Override Polygon.area function.
        """
        return 'equilateral triangle'

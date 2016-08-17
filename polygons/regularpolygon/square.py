from .regularpolygon import RegularPolygon

class Square(RegularPolygon):
    """A class to represent a square.
    """

    def __init__(self, length:float):
        """Initialize the Square class.
        """
        super().__init__(4, length)

    @property
    def area(self) -> float:
        """Return the area of the square.
        """
        return self.length ** 2

    @property
    def name(self) -> str:
        """Override `Polygon.name` function.
        """
        return 'square'

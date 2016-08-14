import math
from ..polygon.polygon import Polygon

class RegularPolygon(Polygon):
    def __init__(self, sides:int, length:float):
        self.length = length
        lengths = [length] * sides
        angles = [RegularPolygon.angle(sides)] * sides
        super().__init__(sides, lengths, angles)

    @property
    def perimeter(self):
        return self.sides * self.length

    @property
    def apothem(self):
        tan = math.tan(math.pi / self.sides)
        return self.length / (2 * tan)

    @property
    def area(self):
        return (self.apothem * self.perimeter) / 2

    @classmethod
    def angle(self, sides:int):
        angle_sum = 180 * (sides - 2)
        return angle_sum / sides

if __name__ == '__main__':
    hexagon = RegularPolygon(6, 10)
    print('hexagon area: ' + str(hexagon.area))
    print('hexagon name: ' + hexagon.name)
    print('hexagon angles: ' + str(hexagon.angles))

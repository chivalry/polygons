import math
from .regularpolygon import RegularPolygon

class EquilateralTriangle(RegularPolygon):
    def __init__(self, length:float):
        super().__init__(4, length)

    @property
    def area(self):
        return (self.length ** 2) * math.sqrt(3) / 4

    @property
    def name(self):
        return 'equilateral triangle'

if __name__ == '__main__':
    print('triangle area: ' + str(EquilateralTriangle(9).area))

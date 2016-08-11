import math

class Polygon:
    names = {
            3: 'triangle',
            4: 'quadrilateral',
            5: 'pentagon',
            6: 'hexagon',
            7: 'heptagon',
            8: 'octagon',
            9: 'nonagon',
            10: 'decagon',
    }

    def __init__(self, sides:int, lengths:list, angles:list):
        self.sides = sides
        self.lengths = lengths
        self.angles = angles

    @property
    def perimeter(self):
        return sum(self.lengths)

    @property
    def name(self):
        return self.names[self.sides]

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
    def angle(self, sides):
        angle_sum = 180 * (sides - 2)
        return angle_sum / sides

class Square(RegularPolygon):
    def __init__(self, length:float):
        super().__init__(4, length)

    @property
    def area(self):
        return self.length ** 2

    @property
    def name(self):
        return 'square'

class EquilateralTriangle(RegularPolygon):
    def __init__(self, length:float):
        super().__init__(4, length)

    @property
    def area(self):
        return (self.length ** 2) * math.sqrt(3) / 4

    @property
    def name(self):
        return 'equilateral triangle'

hexagon = RegularPolygon(6, 10)
print('hexagon area: ' + str(hexagon.area))
print('hexagon name: ' + hexagon.name)
print('hexagon angles: ' + str(hexagon.angles))

square = Square(10)
print('square area: ' + str(square.area))

triangle = EquilateralTriangle(9)
print('triangle area: ' + str(triangle.area))

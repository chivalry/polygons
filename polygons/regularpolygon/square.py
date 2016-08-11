from .regularpolygon import RegularPolygon

class Square(RegularPolygon):
    def __init__(self, length:float):
        super().__init__(4, length)

    @property
    def area(self):
        return self.length ** 2

    @property
    def name(self):
        return 'square'

if __name__ == '__main__':
    print('square area: ' + str(Square(10).area))

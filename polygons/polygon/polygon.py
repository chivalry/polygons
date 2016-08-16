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
        
        self.confirm_attributes()

    @property
    def perimeter(self):
        return sum(self.lengths)

    @property
    def name(self):
        return self.names[self.sides]

    def confirm_attributes(self):
        if (not isinstance(self.sides, int)) and (not self.sides.is_integer()):
            raise ValueError('sides must be an integer')

        if type(self.lengths) is not list:
            raise ValueError('lengths must be a list')
        if len(self.lengths) != self.sides:
            raise ValueError('lengths count must equal number of sides')
        if not all(isinstance(length, (int, float)) for length in self.lengths):
            raise ValueError('lengths must be numeric')
        if not all(length > 0 for length in self.lengths):
            raise ValueError('lengths must be positive')

        if type(self.angles) is not list:
            raise ValueError('angles must be a list')
        if len(self.angles) != self.sides:
            raise ValueError('angles count must equal number of sides')
        if not all(isinstance(angle, (int, float)) for angle in self.angles):
            raise ValueError('angles must be numeric')
        if sum(self.angles) != ((self.sides - 2) * 180):
            raise ValueError('angles must sum correctly')
        if not all(angle > 0 for angle in self.angles):
            raise ValueError('angles must be positive')

if __name__ == '__main__':
    poly = Polygon(5, [3, 4, 5, 4, 6], [100, 110, 120, 130, 80])
    print('poly name: ' + poly.name)
    print('poly perimiter: ' + str(poly.perimeter))

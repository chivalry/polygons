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

if __name__ == '__main__':
    poly = Polygon(5, [3, 4, 5, 4, 6], [100, 110, 120, 130, 80])
    print('poly name: ' + poly.name)
    print('poly perimiter: ' + str(poly.perimeter))

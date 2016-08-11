from polygons.polygon.polygon import Polygon
from polygons.regularpolygon.regularpolygon import RegularPolygon
from polygons.regularpolygon.square import Square
from polygons.regularpolygon.equilateraltriangle import EquilateralTriangle

poly = Polygon(5, [3, 4, 5, 4, 6], [100, 110, 120, 130, 80])
print('poly name: ' + poly.name)
print('poly perimiter: ' + str(poly.perimeter))

hexagon = RegularPolygon(6, 10)
print('hexagon area: ' + str(hexagon.area))
print('hexagon name: ' + hexagon.name)
print('hexagon angles: ' + str(hexagon.angles))

print('square area: ' + str(Square(10).area))

print('triangle area: ' + str(EquilateralTriangle(9).area))

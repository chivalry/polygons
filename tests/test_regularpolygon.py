import math
from polygons.regularpolygon import RegularPolygon
from polygons.regularpolygon import EquilateralTriangle

def test_square_returns_squared_side_for_area():
    assert RegularPolygon(4, 5).area == 25

def test_triangle_returns_correct_area():
    poly_area = RegularPolygon(3, 5).area
    tri_area = EquilateralTriangle(5).area
    assert math.isclose(poly_area, tri_area, rel_tol=1e-10)

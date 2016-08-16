import math
from polygons.regularpolygon import EquilateralTriangle

def test_equilateral_triangle_area():
    assert math.isclose(EquilateralTriangle(3 ** (1/4)).area, 3/4, rel_tol=1e-2)

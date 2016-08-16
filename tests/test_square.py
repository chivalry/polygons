from polygons.regularpolygon import Square
import math

def test_square_perimeter():
    assert Square(1).perimeter == 4
    assert Square(5).perimeter == 20
    assert Square(1.25).perimeter == 5

def test_square_area():
    assert Square(1).area == 1
    assert Square(5).area == 25
    assert math.isclose(Square(1.5).area, 2.25, rel_tol=1e-2)

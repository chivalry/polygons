from polygons.polygon import Polygon
import pytest

def test_side_requires_int():
    with pytest.raises(ValueError):
        Polygon(3.14, [5, 5, 5], [60, 60, 60])

def test_lengths_requires_list():
    with pytest.raises(ValueError):
        Polygon(3, 5, [60, 60, 60])

def test_angles_requires_list():
    with pytest.raises(ValueError):
        Polygon(3, [5, 5, 5], 1)

def test_length_count_requires_sides_value():
    with pytest.raises(ValueError):
        Polygon(3, [5, 5, 5, 5], [60, 60, 60])

def test_angles_count_requires_sides_value():
    with pytest.raises(ValueError):
        Polygon(3, [5, 5, 5], [60, 60])

def test_lengths_must_be_numeric():
    with pytest.raises(ValueError):
        Polygon(3, ['5', 5, 5], [60, 60, 60])

def test_angles_must_be_numeric():
    with pytest.raises(ValueError):
        Polygon(3, [1, 2, 3], ['60', 60, 60])

def test_angles_must_sum_correctly():
    with pytest.raises(ValueError):
        Polygon(5, [6, 6, 6, 6, 6], [120, 120, 120, 120, 120])

def test_lengths_must_be_positive():
    with pytest.raises(ValueError):
        Polygon(3, [0, 5, 5], [60, 60, 60])

def test_angles_must_be_positive():
    with pytest.raises(ValueError):
        Polygon(3, [5, 5, 5], [0, 120, 60])

def test_valid_names_returned():
    assert Polygon(4, [3, 3, 3, 3], [90, 80, 100, 90]).name == 'quadrilateral'
    assert Polygon(3, [4, 4, 4], [50, 60, 70]).name == 'triangle'
    assert Polygon(10, [1] * 10, [144] * 10).name == 'decagon'

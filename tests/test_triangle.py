import pytest
from Homework.src.triangle import Triangle

def test_triangle_area():
    triangle = Triangle(3, 4, 5)
    assert triangle.get_area() == 6

def test_triangle_perimeter():
    triangle = Triangle(3, 4, 5)
    assert triangle.get_perimeter() == 12

def test_invalid_triangle():
    with pytest.raises(ValueError):
        Triangle(1, 2, 3)
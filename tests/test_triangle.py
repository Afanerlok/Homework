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

@pytest.mark.parametrize(
    "a, b, c",
    [
        (1, 2, 3),
        (0, 0, 0),
        (-1, -1, 2),
    ],
)
def test_invalid_triangle(a, b, c):
    with pytest.raises(ValueError, match="Треугольник с такими сторонами не может существовать."):
        Triangle(a, b, c)
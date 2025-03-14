import pytest
from Homework.src.triangle import Triangle
from Homework.src.square import Square

def test_add_area():
    triangle = Triangle(3, 4, 5)
    square = Square(5)
    assert triangle.add_area(square) == 31

def test_add_area_invalid():
    triangle = Triangle(3, 4, 5)
    invalid_figure = "not a figure"

    with pytest.raises(ValueError, match="Переданный объект не является геометрической фигурой."):
        triangle.add_area(invalid_figure)


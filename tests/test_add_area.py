from Homework.src.triangle import Triangle
from Homework.src.square import Square

def test_add_area():
    triangle = Triangle(3, 4, 5)
    square = Square(5)
    assert triangle.add_area(square) == 31
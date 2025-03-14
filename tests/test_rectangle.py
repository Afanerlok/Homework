import pytest
from Homework.src.rectangle import Rectangle

def test_rectangle_integer():
    rectangle = Rectangle (3,5)
    assert rectangle.get_area() == 15, 'Area should be 15'

def test_rectangle_area():
    rectangle = Rectangle(4, 5)
    assert rectangle.get_area() == 20

def test_rectangle_perimeter():
    rectangle = Rectangle(4, 5)
    assert rectangle.get_perimeter() == 18



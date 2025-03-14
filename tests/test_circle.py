import pytest
from Homework.src.circle import Circle

def test_circle_area():
    circle = Circle(5)
    assert circle.get_area() == pytest.approx(78.5398, rel=1e-4)

def test_circle_perimeter():
    circle = Circle(5)
    assert circle.get_perimeter() == pytest.approx(31.4159, rel=1e-4)
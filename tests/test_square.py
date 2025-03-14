from Homework.src.square import Square

def test_square_area():
    square = Square(5)
    assert square.get_area() == 25

def test_square_perimeter():
    square = Square(5)
    assert square.get_perimeter() == 20
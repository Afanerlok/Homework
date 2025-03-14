from math import sqrt
from Homework.src.figure import Figure

class Triangle(Figure):
    def __init__(self, a, b, c):
        if not self.is_valid_triangle(a, b, c):
            raise ValueError("Triangle sides can't be less than 0")
        self.a = a
        self.b = b
        self.c = c

    def is_valid_triangle(self, a, b, c):
        return a + b > c and a + c > b and b + c > a

    def get_area(self):
        p = self.get_perimeter() / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def get_perimeter(self):
        return self.a + self.b + self.c
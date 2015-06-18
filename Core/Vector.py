__author__ = 'Moritz Moeller'
from math import sqrt


class Vector(object):
    """ Defines a vector, a point or a RGB color """
    def __init__(self, c1, c2, c3):
        self.c1 = float(c1)
        self.c2 = float(c2)
        self.c3 = float(c3)

    def __eq__(self, other):
        return self.c1 == other.c1 and self.c2 == other.c2 and self.c3 == other.c3

    def __add__(self, other):
        return Vector(self.c1 + other.c1, self.c2 + other.c2, self.c3 + other.c3)

    def __repr__(self):
        return "Vector(%s, %s, %s)" % (repr(self.c1), repr(self.c2), repr(self.c3))

    def __iter__(self):
        return
    def __sub__(self, other):
        return Vector(self.c1 - other.c1, self.c2 - other.c2, self.c3 - other.c3)

    def __div__(self, other):
        return Vector(self.c1 / other, self.c2 / other, self.c3 / other)

    def length(self):
        """ Calculates the length of a vector """
        return sqrt(self.c1**2 + self.c2**2 + self.c3**2)

    def dot(self, other):
        """ Calculates the scalar product """
        return self.c1 * other.c1 + self.c2 * other.c2 + self.c3 * other.c3

    def cross(self, other):
        """ Calculates the cross product """
        return Vector(self.c2 * other.c3 - other.c2 * self.c3, self.c3 * other.c1 - other.c3 * self.c1, self.c1 * other.c2 - other.c1 * self.c2)

    def normalized(self):
        """ Normalizes a vector so it has the length of 1 """
        return self/self.length()

    def scale(self, other):
        """ Scales a Vector, a point or a color """
        return Vector(self.c1 * other, self.c2 * other, self.c3 * other)

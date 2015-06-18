__author__ = 'Moritz Moeller'
from Objects.Entity import Entity


class Triangle(Entity):
    def __init__(self , a, b, c, material, reflection):
        Entity.__init__(self, material, reflection)
        self.a = a  # point
        self.b = b  # point
        self.c = c  # point
        self.u = self.b - self.a    # direction vector
        self.v = self.c - self.a    # direction vector

    def __repr__(self):
        return 'Triangle(%s,%s,%s)' %(repr(self.a), repr(self.b), repr(self.c))

    def __eq__(self, other):
        if isinstance(other, Triangle):
            return self.a == other.a and self.b == other.b and self.c == other.c
        return False

    def intersectionParameter(self , ray):
        """ Returns the parameter where the given ray hits the triangle """
        w = ray.origin - self.a
        dv = ray.direction.cross(self.v)
        dvu = dv.dot(self.u)
        if dvu == 0.0:
            return None
        wu = w.cross(self.u)
        r = dv.dot(w) / dvu
        s = wu.dot(ray.direction) / dvu
        if 0 <= r and r <= 1 and 0 <= s and s <= 1 and r+s <= 1:
            return wu.dot(self.v) / dvu
        else:
            return None

    def normalAt(self, p):
        """ Returns the normal of the triangle"""
        return self.u.cross(self.v).normalized()

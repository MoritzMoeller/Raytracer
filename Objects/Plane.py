__author__ = 'Moritz Moeller'
from Objects.Entity import Entity


class Plane(Entity):
    """ Defines a plane """
    def __init__(self, point, normal, material, reflection):
        Entity.__init__(self, material, reflection)
        self.point = point
        self.normal = normal.normalized()

    def __repr__(self):
        return 'Plane(%s,%s)' % (repr(self.point), repr(self.normal))

    def __eq__(self, other):
        if isinstance(other, Plane):
            return self.point == other.point and self.normal == other.normal
        return False

    def intersectionParameter(self, ray):
        """ Returns the parameter where the given ray hits the plane """
        op = ray.origin - self.point
        a = op.dot(self.normal)
        b = ray.direction.dot(self.normal)
        if b:
            return -a/b
        else:
            return None

    def normalAt(self, p):
        """ Returns the normal of the plane """
        return self.normal
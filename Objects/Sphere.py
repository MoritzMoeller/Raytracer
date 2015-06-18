__author__ = 'Moritz Moeller'
import math

from Objects.Entity import Entity


class Sphere(Entity):
    """ Defines a sphere """
    def __init__(self, center, radius, material, reflection):
        Entity.__init__(self, material, reflection)
        self.center = center
        self.radius = radius

    def __repr__(self):
        return 'Sphere(%s,%s)' %(repr(self.center), self.radius)

    def __eq__(self, other):
        if isinstance(other, Sphere):
            return self.center == other.center and self.radius == other.radius
        return False


    def intersectionParameter(self, ray):
        """ Returns the parameter where the given ray hits the sphere """
        co = self.center - ray.origin   # vector camera -> sphere
        v = co.dot(ray.direction)
        discriminant = v*v - co.dot(co) + self.radius * self.radius
        if discriminant < 0:
            return None
        else:
            return v - math.sqrt(discriminant)

    def normalAt(self, point):
        """ Returns the normal of the sphere at given point """
        return (point - self.center).normalized()
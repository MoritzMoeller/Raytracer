__author__ = 'Moritz Moeller'


class Entity(object):
    """ Parent class for geometrical objects """
    def __init__(self, material, reflection):
        self.material = material
        self.reflection = reflection

    def colorAt(self, ray, hitdist, lightSources, objectList):
        """ Returns the color of a point from the given ray at a given distance """
        intersectionPoint = ray.pointAtParameter(hitdist)
        normal = self.normalAt(intersectionPoint).normalized()
        color = self.material.calcColor(lightSources, ray, hitdist, normal, objectList)
        return color
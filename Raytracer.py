__author__ = 'Moritz Moeller'
from PIL import Image

from Core.HitPointData import HitPointData
from Core.Ray import Ray
from Core.Vector import Vector


class Raytracer(object):
    """ The Raytracer class. Handles the main raytracing calculation """
    def __init__(self, camera, objectList, lightSources, wRes, hRes):
        self.objectList = objectList
        self.lightSources = lightSources
        self.wRes = wRes
        self.hRes = hRes
        self.camera = camera
        self.image = Image.new('RGB', (wRes, hRes))
        self.BACKGROUND_COLOR = Vector(0, 0, 0)
        self.maxlevel = 3
        self.reflectionFactor = 0.5

    def run(self):
        """ Starts the raytracing """
        for x in range(self.wRes):
            for y in range(self.hRes):
                ray = self.camera.calcRay(x, y)
                color = self.traceRay(0, ray)
                self.image.putpixel((x, y), (int(color.c1), int(color.c2), int(color.c3)))
        self.image.show()

    def traceRay(self, level, ray):
        """ Traces a given ray to a given reflection level """
        hitPointData = self.intersect(level, ray)
        if hitPointData:
            return self.shade(level, hitPointData, ray)
        return self.BACKGROUND_COLOR

    def shade(self, level, hitPointData, ray):
        """ Calculates the basic and the reflection color at a given intersection distance """
        directColor = hitPointData.object.colorAt(ray, hitPointData.dist, self.lightSources, self.objectList)
        reflectedRay = self.computeReflectedRay(hitPointData, ray)
        reflectedColor = Vector(0, 0, 0)
        if hitPointData.object.reflection:
            reflectedColor += self.traceRay(level + 1, reflectedRay)
        return directColor + reflectedColor.scale(self.reflectionFactor)


    def computeReflectedRay(self, hitPointData, ray):
        """ Returns the reflection ray of a given ray """
        intersectionPoint = ray.pointAtParameter(hitPointData.dist)
        d = ray.direction
        n = hitPointData.object.normalAt(intersectionPoint)
        reflectedVector = d - n.scale(n.dot(d)).scale(2)
        return Ray(intersectionPoint, reflectedVector)

    def intersect(self, level, ray):
        """ Checks if a given ray intersects with one of the objects.  """
        if level == self.maxlevel:
            return None
        maxdist = float('inf')
        hitPointData = None
        for object in self.objectList:
            hitdist = object.intersectionParameter(ray)
            if 0 <= hitdist < maxdist:
                maxdist = hitdist
                hitPointData = HitPointData(maxdist-0.0001, object)
        return hitPointData
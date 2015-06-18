__author__ = 'Moritz Moeller'
from Core.Vector import Vector
from Core.Ray import Ray

class Material(object):
    """ Defines the material of an object """
    def __init__(self, color, constantA, constantD ,constantS, factor):
        self.color = color
        self.constantA = constantA
        self.constantD = constantD
        self.constantS = constantS
        self.factor = factor

    def objectShadow(self, objectList, lightRay):
        """ Checks if an object is between the object itself and the lightsource and return true or false """
        for obj in objectList:
            hit = obj.intersectionParameter(lightRay)
            if hit and 0 < hit:
                return True
        return False

    def calcColor(self, lightSources, ray, hitdist, normal, objectList):
        """ Calculates the basic color at a given point of the object """
        intersectionPoint = ray.pointAtParameter(hitdist-0.00001)
        rayDirection = ray.direction.normalized()
        shadowFactor = 1.0
        ambient = Vector(0, 0, 0)
        diffuse = Vector(0, 0, 0)
        specular = Vector(0, 0, 0)
        ambient += self.baseColorAt(intersectionPoint).scale(self.constantA)
        for light in lightSources:
            lightVector = (light.position - intersectionPoint).normalized()
            lightRay = Ray(intersectionPoint, lightVector)
            if self.objectShadow(objectList, lightRay):
                shadowFactor *= 0.8
            lightVectorReflect = (lightVector - normal.scale(normal.dot(lightVector)).scale(2)).normalized()
            diffuse += light.color.scale(self.constantD * lightVector.dot(normal))
            if normal.dot(lightVector) > 0:
                specular += light.color.scale(self.constantS * (lightVectorReflect.dot(rayDirection.scale(-1)))**self.factor)
        color = (ambient + diffuse + specular).scale(shadowFactor)
        return color

    def baseColorAt(self, p):
        """ Returns the base color """
        return self.color
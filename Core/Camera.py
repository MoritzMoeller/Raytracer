__author__ = 'Moritz Moeller'
import math

from Core.Ray import Ray


class Camera(object):
    """ Defines the position, the field of view and the direction"""
    def calcRay(self, x, y):
        """ Returns a ray from the camera to a given position """
        xcomp = self.s.scale(x * self.pixelWidth - self.width / 2)
        ycomp = self.u.scale(y * self.pixelHeight - self.height / 2)
        return Ray(self.eye, self.f + xcomp + ycomp)

    def __init__(self, eye, center, up, fov, wRes, hRes):
        self.eye = eye
        self.center = center
        self.up = up
        self.fov = fov
        aspectratio = float(wRes)/float(hRes)

        self.f = (center - eye).normalized()
        self.s = (self.f.cross(up)).normalized()
        self.u = self.s.cross(self.f).scale(-1)

        self.alpha = (fov/180.0*math.pi)/2
        self.height = 2 * math.tan(self.alpha)
        self.width = self.height * aspectratio

        self.pixelWidth = self.width / (wRes-1)
        self.pixelHeight = self.height / (hRes-1)

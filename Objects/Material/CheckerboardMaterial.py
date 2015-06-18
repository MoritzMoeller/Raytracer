__author__ = 'Moritz Moeller'
from Material import Material
from Core.Vector import Vector


class CheckerboardMaterial(Material):
    """ Material class for the chess board texture """
    def __init__(self):
        self.baseColor = Vector(255, 255, 255)
        self.otherColor = Vector(0, 0, 0)
        self.constantA = 0.6
        self.constantD = 0.3
        self.constantS = 0.4
        self.checkSize = 1
        self.factor = 20

    def baseColorAt(self, p):
        """ Returns the basic color at a given point """
        v = p
        v.scale(1.0 / self.checkSize)
        if (int(abs(v.c1) + 0.5) + int(abs(v.c2) + 0.5) + int(abs(v.c3) + 0.5)) %2:
            return self.otherColor
        return self.baseColor

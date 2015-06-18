__author__ = 'Moritz Moeller'


class Ray(object):
    """ Defines a ray """
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction.normalized()

    def __repr__(self):
        return 'Ray(%s, %s' % (repr(self.origin), repr(self.direction))

    def pointAtParameter(self, t):
        """ Returns a point on the ray at a given distance """
        return self.origin + self.direction.scale(t)
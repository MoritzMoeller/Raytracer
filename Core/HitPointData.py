__author__ = 'Moritz Moeller'

class HitPointData(object):
    """ Distance and the object a ray hits """
    def __init__(self, dist, object):
        self.dist = dist
        self.object = object
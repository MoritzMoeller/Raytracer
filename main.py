__author__ = 'Moritz Moeller'
from Core.Camera import Camera
from Core.Vector import Vector
from Objects.Triangle import Triangle
from Objects.Sphere import Sphere
from Objects.Plane import Plane
from Core.Light import Light
from Objects.Material.Material import Material
from Objects.Material.CheckerboardMaterial import CheckerboardMaterial
from Raytracer import Raytracer

if __name__ == '__main__':
    """ Main Python script. Instantiates all needed objects and starts the raytracer """
    wRes = 500
    hRes = 500
    ambientConstant = 0.6
    diffuseConstant = 0.3
    specularConstant = 0.4
    shineFactor = 20
    materialA = Material(Vector(0, 255, 0), ambientConstant, diffuseConstant, specularConstant, shineFactor)
    sphereA = Sphere(Vector(-1.5, 2.5, -2), 1.2, materialA, True)
    materialB = Material(Vector(255, 0, -2), ambientConstant, diffuseConstant, specularConstant, shineFactor)
    sphereB = Sphere(Vector(1.5, 2.5, -2), 1.2, materialB, True)
    materialC = Material(Vector(0, 0, 255), ambientConstant, diffuseConstant, specularConstant, shineFactor)
    sphereC = Sphere(Vector(0, 5.5, -2), 1.2, materialC, True)
    materialD = Material(Vector(255, 255, 0), ambientConstant, diffuseConstant, specularConstant, shineFactor)
    triangle = Triangle(sphereA.center, sphereB.center, sphereC.center, materialD, True)
    materialE = CheckerboardMaterial()
    planeA = Plane(Vector(0, 0, 0), Vector(0, 1, 0), materialE, False)
    objectList = [sphereA, sphereB, sphereC, planeA, triangle]
    lightSources = [Light(Vector(25, 20, 10), Vector(255, 255, 255)), Light(Vector(18, 20, 10), Vector(255, 255, 255))]
    fov = 45
    cameraEye = Vector(0, 1.8, 10)
    cameraCenter = Vector(0, 3, 0)
    cameraUp = Vector(0, 1, 0)
    camera = Camera(cameraEye, cameraCenter, cameraUp, fov, wRes, hRes)
    rt = Raytracer(camera, objectList, lightSources, wRes, hRes)
    print "Starting raytracing"
    print "Resolution: " + str(wRes) + " x " + str(hRes)
    print "This will take a moment ..."
    rt.run()


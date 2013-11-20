# Problem 9
import math
from graphics import *

class Sphere:

    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def surfaceArea(self):
        return 4 * math.pi * self.getRadius() ** 2

    def volume(self):
        return 4/3 * math.pi * self.getRadius() ** 3

def main ():
    
    #Introduction
    print ("This program calculates the volume and surface area of a sphere. ")

    #Get input
    radius = eval(input("\nPlease enter the radius of the sphere. "))

    #Create sphere
    sphere = Sphere(radius)

    #Print results
    print ("\nThe volume of the sphere is:", round(sphere.volume()))
    print ("\nThe surface area of the sphere is:", round(sphere.surfaceArea()))



main ()

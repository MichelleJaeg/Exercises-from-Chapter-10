# Problem 10
from graphics import*

class Cube:

    def __init__(self, sidelength):
        self.sidelength=sidelength

    def getSideLength(self):
        return self.sidelength

    def surfaceArea(self):
        return 6 * self.sidelength**2


    def volume(self):
        return self.sidelength**3

def main ():
    #Introduction
    print ("This program calculates the volume and surface area of a cube. ")

    #Get input
    sidelength=eval(input("\nPlease enter the length of a side of the cube. "))

    #Create sphere
    cube=Cube(sidelength)

    #Print results
    print ("\nThe volume of the cube is:", round(cube.volume()))
    print ("\nThe surface area of the cube is:", round(cube.surfaceArea()))



main ()
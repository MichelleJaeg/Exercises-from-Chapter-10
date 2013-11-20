# Problem 10
from graphics import *

class Cube:

    def __init__(self, side_length):
        self.side_length = side_length

    def getSideLength(self):
        return self.side_length

    def surfaceArea(self):
        return 6 * self.side_length ** 2


    def volume(self):
        return self.side_length ** 3

def main ():
    #Introduction
    print ("This program calculates the volume and surface area of a cube. ")

    #Get input
    side_length = eval(input("\nPlease enter the length of a side of the cube. "))

    #Create sphere
    cube = Cube(side_length)

    #Print results
    print ("\nThe volume of the cube is:", round(cube.volume()))
    print ("\nThe surface area of the cube is:", round(cube.surfaceArea()))



main ()

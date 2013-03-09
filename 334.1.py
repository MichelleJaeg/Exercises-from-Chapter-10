# Problem 1
from projectile import Projectile

def main ():
    Introduction()
    angle, vel, hO, time = getInputs()
    cball = Projectile(angle, vel, hO)
    heightlist=[]
    while cball.getY() >=0:
        cball.update(time)
        height=cball.getY()
        heightlist.append(height)
    print ("\nDistance traveled: {0:0.1f} meters.".format(cball.getX()))
    maxheight=max(heightlist)
    print ("Maximum height achieved: {0:0.1f} meters.".format(maxheight))

def Introduction():
    print ("This program calculates the maximum height and distance achieved by a cannonball. ")

def getInputs():
    print ()
    a = eval(input("Enter the launch angle (in degrees): "))
    v = eval(input("Enter the initial velocity (in meters/sec): "))
    h = eval(input("Enter the initial height (in meters): "))
    t = eval(input("Enter the time interval (in seconds) between position calculations: "))
    return a,v,h,t


main ()

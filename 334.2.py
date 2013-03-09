#Problem 2
from graphics import *
from button import Button


def main ():

    #Create graphics window
    win=GraphWin("House",500,500)
    win.setCoords(0.0,0.0,10.0,10.0)

    # Introduction
    Description=Text(Point(5.0,9.5),"This program draws a simple house using five mouse clicks:")
    Description.draw(win)
    House=Text(Point(5.0,8.5), "Please click anywhere to continue. ")
    House.draw(win)

    #Create quit button
    quitbutton=Button(win, Point(2.0, 1.0), 2.0, 2.0,'Click to Quit')

    #Creates the house
    pt=win.getMouse()
    while not quitbutton.clicked(pt):
        House.setText("Click twice to create the frame (bottom left, then upper right)")
        BottomLeftHouse=win.getMouse()
        UpperRightHouse=win.getMouse()
        Rectangle(BottomLeftHouse,UpperRightHouse).draw(win)

    #Creates the door
        House.setText("Click once in the lower left to create a door to the house (your click will be the top of the door)")
        width=abs((BottomLeftHouse.getX())-(UpperRightHouse.getX()))
        doorwidth=width*(1/5)
        Upperdoor=win.getMouse()
        x1=Upperdoor.getX()-doorwidth/2
        y1=Upperdoor.getY()
        x2=Upperdoor.getX()+doorwidth/2
        y2=Upperdoor.getY()
        doorline1=Line(Point(x1,y1),Point(x2,y2))
        doorline1.draw(win)
        doorline2=Line(Point(x1,y1),Point(x1,BottomLeftHouse.getY()))
        doorline2.draw(win)
        doorline3=Line(Point(x2,y2),Point(x2,BottomLeftHouse.getY()))
        doorline3.draw(win)

    #Creates the window
        House.setText("Click once in the upper right of the rectangle to create a window")
        window=win.getMouse()
        windowwidth=doorwidth/2
        x4=window.getX()
        y4=window.getY()
        x5=x4-windowwidth/2
        y5=y4-windowwidth/2
        p5=Point(x5,y5)
        x6=x4+windowwidth/2
        y6=y4+windowwidth/2
        p6=Point(x6,y6)
        Rectangle(p5,p6).draw(win)

    #Creates the roof
        House.setText ("Click once above the house to indicate the height of the roof")
        roofapex=win.getMouse()
        x9=UpperRightHouse.getX()-width/2
        y9=roofapex.getY()
        p9=Point(x9,y9)
        x8=UpperRightHouse.getX()-width
        y8=UpperRightHouse.getY()
        p8=Point(x8,y8)
        triangle=Polygon(UpperRightHouse,p8,p9).draw(win)

    #Allows user to click quit button
        quitbutton.activate()
        pt=win.getMouse()

    #Quit program
    win.close()



main ()




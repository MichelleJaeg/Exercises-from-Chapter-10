#Problem 2

from graphics import *
from button import Button


def main ():

    #Create graphics window
    win = GraphWin("House", 500, 500)
    win.setCoords(0.0, 0.0, 10.0, 10.0)

    # Introduction
    description = Text(Point(5.0, 9.5),"This program draws a simple house using five mouse clicks:")
    description.draw(win)
    message = Text(Point(5.0 ,8.5), "Please click anywhere to continue. ")
    message.draw(win)

    #Create quit button
    quit_button = Button(win, Point(2.0, 1.0), 2.0, 2.0,'Click to Quit')

    #Creates the house
    pt = win.getMouse()
    while not quit_button.clicked(pt):
        message.setText("Click twice to create the frame (bottom left, then upper right)")
        bottom_left_house = win.getMouse()
        upper_right_house = win.getMouse()
        Rectangle(bottom_left_house, upper_right_house).draw(win)

    #Creates the door
        message.setText("Click once in the lower left to create a door to the house (your click will be the top of the door)")
        width = abs((bottom_left_house.getX()) - (upper_right_house.getX()))
        door_width = width * (1 / 5)
        upper_door = win.getMouse()
        x1 = upper_door.getX() - door_width / 2
        y1 = upper_door.getY()
        x2 = upper_door.getX() + door_width / 2
        y2 = upper_door.getY()
        door_line1 = Line(Point(x1,y1), Point(x2,y2))
        door_line1.draw(win)
        door_line2 = Line(Point(x1,y1), Point(x1,bottom_left_house.getY()))
        door_line2.draw(win)
        door_line3 = Line(Point(x2,y2), Point(x2,bottom_left_house.getY()))
        door_line3.draw(win)

    #Creates the window
        message.setText("Click once in the upper right of the rectangle to create a window")
        window = win.getMouse()
        window_width = door_width / 2
        x4 = window.getX()
        y4 = window.getY()
        x5 = x4 - window_width / 2
        y5 = y4 - window_width / 2
        p5 = Point(x5, y5)
        x6 = x4 + window_width / 2
        y6 = y4 + window_width / 2
        p6 = Point(x6, y6)
        Rectangle(p5, p6).draw(win)

    #Creates the roof
        message.setText ("Click once above the house to indicate the height of the roof")
        roof_apex = win.getMouse()
        x9 = upper_right_house.getX() - width / 2
        y9 = roof_apex.getY()
        p9 = Point(x9, y9)
        x8 = upper_right_house.getX() - width
        y8 = upper_right_house.getY()
        p8 = Point(x8, y8)
        triangle = Polygon(upper_right_house, p8, p9).draw(win)

    #Allows user to click quit button
        quit_button.activate()
        pt = win.getMouse()

    #Quit program
    win.close()



main ()




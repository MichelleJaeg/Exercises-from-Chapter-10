# Problem 3
from graphics import *
from button import Button
from random import randrange


def main ():

    #Create graphics window
    win=GraphWin(400,400)
    win.setCoords(0.0,0.0,10.0,10.0)

    #Create Message
    message1=Text(Point(5.0, 9.0),'Welcome to Three Button Monte')
    message1.draw(win)

    #Create buttons
    number1=Button(win, Point(2.0,4.0),1.0,1.0,'Door 1')
    number1.activate()
    number2=Button(win, Point(5.0,4.0),1.0, 1.0, 'Door 2')
    number2.activate()
    number3=Button(win, Point(8.0,4.0),1.0, 1.0, 'Door 3')
    number3.activate()

    #Ask user to pick a door
    message2=Text(Point(5.0,7.5),'One door has been chosen. Click on a door to guess it. ')
    message2.draw(win)
    doorpick=win.getMouse()

    #Report results
    x=pickadoor()
    if x==1 and number1.clicked(doorpick)==True:
        message2.setText('You picked the correct door! ')
    elif x==2 and number2.clicked(doorpick)==True:
        message2.setText('You picked the correct door! ')
    elif x==3 and number3.clicked(doorpick)==True:
        message2.setText('You picked the correct door! ')
    else:
        message1.setText("You did not pick the correct door.")
        message2.setText("The correct door was: ")
        message3=Text(Point(6.5,7.5),x)
        message3.draw(win)

    #Quit program
    message4=Text(Point(5.0,1.0),'Click anywhere to close. ')
    message4.draw(win)
    win.getMouse()
    win.close()

def pickadoor():
    doornumber=randrange(1,4)
    if doornumber==1:
        door=1
    if doornumber==2:
        door=2
    if doornumber==3:
        door=3
    return door








if __name__=='__main__':
    main ()
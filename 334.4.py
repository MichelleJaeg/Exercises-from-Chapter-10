# Problem 4
# This exercise extends the program from the previous problem by allowing the player to play multiple rounds.
from graphics import *
from button import Button
from random import randrange


def main ():

    #Create graphics window
    win = GraphWin(400, 400)
    win.setCoords(0.0, 0.0, 10.0, 10.0)

    #Create Message
    message1 = Text(Point(5.0, 9.0),'Welcome to Three Button Monte')
    message1.draw(win)

    #Create buttons
    number1 = Button(win, Point(2.0, 4.0),1.0, 1.0,'Door 1')
    number1.activate()
    number2 = Button(win, Point(5.0, 4.0),1.0, 1.0, 'Door 2')
    number2.activate()
    number3 = Button(win, Point(8.0, 4.0), 1.0, 1.0, 'Door 3')
    number3.activate()

    #Create quit button
    quit_button = Button(win, Point(2.0, 1.0), 2.0, 2.0,'Click to Quit')
    quit_button.activate()

    #Ask user to pick a door
    message2 = Text(Point(5.0, 7.0),'A door has been chosen. Click on a door to guess it. ')
    message2.draw(win)
    pt = win.getMouse()

    #While user has not chosen to quit
    counter = 0
    while not quit_button.clicked(pt):

        if counter != 0:

    #Ask user to pick a door
            message2.setText('Click on another door. ')
            pt = win.getMouse()

    #Report results to user
        x = pickADoor()
        if x == 1 and number1.clicked(pt) == True:
            message1.setText('You picked the correct door! ')
        elif x == 2 and number2.clicked(pt) == True:
            message1.setText('You picked the correct door! ')
        elif x == 3 and number3.clicked(pt) == True:
            message1.setText('You picked the correct door! ')
        else:
            if x == 1:
                message1.setText("You did not pick the correct door. The correct door was 1")
            if x == 2:
                message1.setText("You did not pick the correct door. The correct door was 2")
            if x == 3:
                message1.setText("You did not pick the correct door. The correct door was 3")
        counter += 1

    #Quit program
    win.close()

def pickADoor():
    door_number = randrange(1, 4)
    if door_number == 1:
        door = 1
    if door_number == 2:
        door = 2
    if door_number == 3:
        door = 3
    return door






if __name__ == '__main__':
    main ()

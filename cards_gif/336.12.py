#Problem 12
import random
from card import Card
from graphics import*

def main ():

    #Introduction
    print ("This program shows five randomly generated playing cards. ")

    #Generate cards
    win=GraphWin("Cards",400,200)
    x=0
    y=80
    center=Point(x,y)
    for i in range(5):
        rank=random.randrange(1,13)
        suit=random.choice(["s","h", "c", "d"])
        card=Card(rank,suit)
        x+=70
        center=Point(x,y)
        card.Draw(win,center)

    #Close window
    win.getMouse()
    win.close()


if __name__=='__main__':
    main ()
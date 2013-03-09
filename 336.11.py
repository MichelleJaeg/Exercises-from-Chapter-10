# Problem 11
import random
from card import Card

def main ():

     #Introduction
     print ("This program prints out n randomly generated playing cards. ")

     #Get input
     n=eval(input("\nHow many cards would you like? "))

     #Generate cards
     for i in range(n):
         rank=random.randrange(1,13)
         suit=random.choice(["s","h", "c", "d"])
         card=Card(rank,suit)
         print ()
         card.__str__()
         print ("The blackjack value of the card is", card.BJValue())


if __name__=='__main__':
    main ()
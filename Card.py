# Card Class
import pygwidgets
import pygame

class Card():

    BACK_OF_CARD_IMAGE = pygame.image.load('images/backOfCard.png')

    def __init__(self, window, rank, suit, value):
        self.window = window
        self.rank = rank
        self.suit = suit
        self.cardName = rank + ' of ' + suit
        self.value = value
        fileName = 'images/' + self.cardName + '.png'
        self.image = pygame.image.load(fileName)
        self.x = 0  
        self.y = 0


        self.conceal()

    def conceal(self):
        self.faceUp = False

    def setLoc(self, loc):
        self.x = loc[0]
        self.y = loc[1]

    def getLoc(self): 
        return((self.x, self.y))

    def reveal(self):
        self.faceUp = True

    def getName(self):
        return self.cardName

    def getValue(self):
        return self.value

    def draw(self):
        if self.faceUp:
            thisImage = self.image
        else:
            thisImage = Card.BACK_OF_CARD_IMAGE
        self.window.blit(thisImage, (self.x, self.y))

    # No need to change this
    def getCardNameAndValue(self):
        return ("CardName", 0)


   

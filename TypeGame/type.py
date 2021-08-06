import pygame
from pygame.locals import *
import sys
import time
import random
import os
print(os.path.abspath(os.getcwd()))


class Game:
    #initialize variables for the speed test
    def __init__(self):
        #sets the size of the window
        self.width = 750
        self.height = 500
        #for reseting the game
        self.reset = True
        self.active = False
        self.input = ''
        self.word = ''
        #the time the game is started at
        self.timeStart = 0
        #runtime of the game
        self.totalTime = 0
        #the total accuracy of the tpying
        self.accuracy = '0%'
        #the words per minute of the typing
        self.wpm = 0
        #this will display the results 
        self.results = 'Time:0 Accuracy:0 WPM:0 '
        pygame.init()
        #this will load the background onto the window
        self.bg = pygame.image.load('background.jpg')
        self.bg = pygame.transform.scale(self.bg, (500,750))

        #this will show the screen
        self.screen = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption('Type Speed test')

        def drawtext(self):
            pass

Game()

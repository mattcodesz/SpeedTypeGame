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
        self.end = False
        pygame.init()
        #this will load the background onto the window
        self.bg = pygame.image.load('background.jpg')
        self.bg = pygame.transform.scale(self.bg, (500,750))

        #this will show the screen
        
        self.screen = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption('Typing Speed test')


    #func to draw text. takes in the screen that text will be drawn on
    #the text to be drawn, y-axis, font size, and color of text
    def drawtext(self, screen, msg, y, fsize, color):
        #uses system default font 
        font = pygame.font.Font(None, fsize)
        #renders the message using the desired font and color, uses aa
        text = font.render(msg, True, color)
        #creates a rectangle for the text to be drawn on
        text_rect = text.get_rect(center=(self.width/2, y))
        #places the text on the rect
        screen.blit(text, text_rect)
        #updates the display
        pygame.display.update()

    #we need a sentence that will be used 
    def getSentence(self):
        #opens the sentence file to read the sentences
        f=open('sentences.txt').read()
        #seperates the sentences by \n and stores them
        sentences = f.split('\n')
        #chooses a single sentence at random
        sentence=random.choice(sentences)
        return sentence
        
    def showResults(self, screen):
        if not self.end:
            self.totalTime = time.time() - self.timeStart
            
        count = 0
        i = 0
        for element in self.word:
            if self.input[i] == element:
                count += 1
                i += 1
            else: i += 1
        self.accuracy = count/len(self.word) * 100

        #words per minute
        self.wpm = len(self.input)*60/(5*self.totalTime)
        self.end = True

        self.results = 'Time:'+str(round(self.totalTime)) +" secs Accuracy:"+ str(round(self.accuracy)) + "%" + ' Wpm: ' + str(round(self.wpm))

        self.drawText(screen, 'Reset', self.height-70, 26, (100,100,100))
        pygame.draw.rect(self.screen,(255,192,25), (self.height/2,300,100,50), 2)

        print(self.results)
        pygame.display.update()

    def run(self):
        self.resetGame()

Game()

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
        self.HEAD_C = (255,213,102)
        self.TEXT_C = (240,240,240)
        self.RESULT_C = (255,70,70)
        pygame.init()
        #this will load the background onto the window
        self.bg = pygame.image.load('background.jpg')
        self.bg = pygame.transform.scale(self.bg, (750,500))

        #this will show the screen
        
        self.screen = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption('Typing Speed test')


    #func to draw text. takes in the screen that text will be drawn on
    #the text to be drawn, y-axis, font size, and color of text
    def drawText(self, screen, msg, y, fsize, color):
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
        for i,c in enumerate(self.word):
            try:
                if self.input[i] == c:
                    count += 1
            except:
                pass
        print(self.word)
        if len(self.word) > 0:
            self.accuracy = count/len(self.word) * 100
        else:
            self.accuracy = 35505

        #words per minute
        self.wpm = len(self.input)*60/(5*self.totalTime)
        self.end = True

        self.results = 'Time:'+str(round(self.totalTime)) +" secs Accuracy:"+ str(round(self.accuracy)) + "%" + ' Wpm: ' + str(round(self.wpm))

        self.drawText(screen, 'Reset', self.height-70, 26, (100,100,100))
        pygame.draw.rect(self.screen,(255,192,25), (325,405,100,50), 2)

        print(self.results)
        pygame.display.update()

    def run(self):
        self.resetGame()

        self.running = True
        while self.running:
            clock = pygame.time.Clock()
            self.screen.fill((0,0,0), (50,250,650,50))
            pygame.draw.rect(self.screen,self.HEAD_C, (50,250,650,50), 2)
            self.drawText(self.screen, self.input, 274, 26, (250,250,250))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    x,y = pygame.mouse.get_pos()
                    #position of input
                    if(x>=50 and x<=510 and y>=250 and y<=300):
                        self.active = True
                        self.input = ''
                        self.timeStart = time.time()
                    if(x>=310 and x<=510 and y>=390 and self.end):
                        self.resetGame()
                        x,y = pygame.mouse.get_pos()
                elif event.type == pygame.KEYDOWN:
                    if self.active and not self.end:
                        if event.key == pygame.K_RETURN:
                            print(self.input)
                            self.showResults(self.screen)
                            print(self.results)
                            self.drawText(self.screen, self.results, 350, 30, self.RESULT_C)
                            self.end = True
                        elif event.key == pygame.K_BACKSPACE:
                            self.input = self.input[:-1]
                        else:
                            try:
                                self.input += event.unicode
                            except:
                                pass
            pygame.display.update()
        clock.tick(60)

    def resetGame(self):
        self.reset = False
        self.end = False
        self.input = ''
        self.word = ''
        self.timeStart = 0
        self.totalTime = 0
        self.wpm = 0

        self.word = self.getSentence()
        self.screen.fill((0,0,0))
        self.screen.blit(self.bg, (0,0))
        msg = 'Speed Typing Test'
        self.drawText(self.screen, msg, 80, 75, self.HEAD_C)
        pygame.draw.rect(self.screen,(255,192,25), (50,250,650,50), 2)

        self.drawText(self.screen, self.word,200, 28,self.TEXT_C)

Game().run()

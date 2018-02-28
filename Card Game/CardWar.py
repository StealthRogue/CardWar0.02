#shte trqbva da import tkinter, math (za button i za poziciqta na mishkata)
import os,pygame,math
import random


white = [255,255,255]

#display-a na koito se pokazva igrata, glavniq class(trqbva da sedi nai otgore)
class CardWar():
    def __init__(self):
        pass
        #1
        pygame.init()
        width, height = 400, 400
        #2
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("CardWar")
        #3
        self.clock=pygame.time.Clock()
    def update(self):
        self.clock.tick(60)

        self.screen.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        pygame.display.flip()

bg=CardWar()
while 1:
    bg.update()


from pygame.locals import *

from RandomCard import RandomCard
from Deck import Deck
from Player import Player

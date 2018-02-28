import random
import pygame

from pygame.locals import *

from Deck import Deck

#veche moje da vuvejdash yes,Y,Yes i go priema
class RandomCard:
	def random_pick():
		while(True):
			choice = input("Are you ready? Y/N:")
			if choice.lower() in ('y','yes'):
				card = random.randint(0,len(Deck)-1)
				print(Deck[card])
			else:
				print("Type Yes or Y when you are ready!")


	random_pick()

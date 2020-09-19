import pygame
from pygame.locals import *

# Initializiang Pygame
pygame.init()

# Screen
SCREEN_SIZE = 700
COLUMN = 3
BORDER = 10
IMG_SIZE = ( round((SCREEN_SIZE - BORDER) / 3) , round((SCREEN_SIZE - BORDER) / 3) )
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("TicTacToe")

IMG_X = pygame.transform.scale(pygame.image.load("images/x.png"),IMG_SIZE)
IMG_O = pygame.transform.scale(pygame.image.load("images/o.png"),IMG_SIZE)

BACKGROUND_IMAGE = pygame.image.load("images/background.png")
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (SCREEN_SIZE,SCREEN_SIZE))
BACKGROUND_COLOR = (0 , 0, 0)


def start_board():

	array_board = [
		[None,None,None],
		[None,None,None],
		[None,None,None]
	]

	x += BORDER
	y += BORDER
	for i in range(len(array_board)):
		for j in range(len(array_board[i])):

			array_board[i,j] = (x , y)

			x += BORDER + round((SCREEN_SIZE - (BORDER * COLUMN)) / 3)
		y += BORDER + round((SCREEN_SIZE - (BORDER * COLUMN)) / 3)
	return array_board


def click():
	pass


game_runing = True
#main part
while game_runing:
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()

		screen.blit(BACKGROUND,(0,0))


		pygame.display.update()
import pygame
from pygame.locals import *


''' Class responsible to set the board '''
class Board:
	def __init__(self,size = 500, column = 3, line = 3):
		self.size = size
		self.column = column
		self.line = line
		self.array_board = []



	def create_board(self):

		size_cel_x = self.size // self.column
		size_cel_y = self.size // self.line


		for i in range(self.line):
			self.array_board.append([])
			for j in range(self.column):
				self.array_board[i].append([None])
		print (self.array_board)


# Initializiang Pygame
pygame.init()

# Screen
SCREEN_SIZE = 500
IMG_SIZE = ( round(SCREEN_SIZE / 3) , round(SCREEN_SIZE / 3) )
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("TicTacToe")

IMG_X = pygame.transform.scale(pygame.image.load("images/x.png"),IMG_SIZE)
IMG_O = pygame.transform.scale(pygame.image.load("images/o.png"),IMG_SIZE)

BACKGROUND_IMAGE = pygame.image.load("images/background.png")
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (SCREEN_SIZE,SCREEN_SIZE))
BACKGROUND_COLOR = (0 , 0, 0)


board = Board()
board.create_board()


################################### main part ###################################
game_runing = True
while game_runing:
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
	screen.blit(BACKGROUND,(0,0))






	pygame.display.update()
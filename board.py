import pygame
from pygame.locals import *


''' Class responsible to set the board '''
class Board:
	def __init__(self,size = 500, column = 3,margin = 10):
		self.board_size = size
		self.column = column
		self.margin = margin
		self.array_board = []
		self.border = ((self.column + 1) * self.margin)
		self.element_size = (self.board_size - self.border) // self.column
		self.create_board()

	# Function responsible to create the board and define the elements inside of then.
	def create_board(self):
		coordx = self.margin
		coordy = self.margin

		width,height = ((self.element_size,self.element_size))

		for i in range(self.column):
			self.array_board.append([])
			for j in range(self.column):
				self.array_board[i].append( [0, (coordy,coordx)] )
				coordx += (width+self.margin)
			coordx = self.margin
			coordy += (height+self.margin)

	# Function responsible to plot the elements in the board
	def plot_board(self, screen, IMG_X, IMG_O):
		# get coordenates((x , y)) -> print (self.array_board[0][0][0])
		# plot the image -> screen.blit(IMG_O, (0,0))
		pygame.draw.line(screen, (100,100,100), [170, 0], [170,500], 11)
		pygame.draw.line(screen, (100,100,100), [330, 0], [330,500], 11)
		pygame.draw.line(screen, (100,100,100), [0, 170], [500,170], 11)
		pygame.draw.line(screen, (100,100,100), [0, 330], [500,330], 11)


		for x in range(len(self.array_board)):
			for y in range(len(self.array_board[x])):
				cordx,cordy = self.array_board[y][x][1]
				if (self.array_board[x][y][0]) == 1:
					screen.blit(IMG_O, (cordx,cordy))
				elif (self.array_board[x][y][0]) == 2:
					screen.blit(IMG_X, (cordx,cordy))

	# Function responsible to set a element inside of the board for a player
	# Obs: if the value referent to the player is not inform the function set the board to 0
	def set_element(self, coordxy, player = 0):
		#coordx,coordy = coordxy
		#self.array_board[coordx][coordy][0] = player
		print (f"Coordenada X Y = {coordxy}")
		print (f"Jogador = {player}")
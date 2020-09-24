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

	'''
	def create_board(self):
		width, height = (( round((self.board_size) // self.column) , round((self.board_size) // self.column) ))
		coordx = 0
		coordy = 0
		for i in range(self.column):
			self.array_board.append([])
			for j in range(self.column):
				self.array_board[i].append( [0 , (coordy,coordx)] )
				coordx += width
			coordx = 0
			coordy += height
		print (self.array_board)
	'''
	def create_board(self):
		coordx = self.margin
		coordy = self.margin

		width,height = ((self.element_size,self.element_size))

		for i in range(self.column):
			self.array_board.append([])
			for j in range(self.column):
				self.array_board[i].append( [0, (coordy,coordx)] )
				coordx += (width+self.margin)
			coordx = 0
			coordy += (height+self.margin)


	def set_element(self, coordxy):
		pass
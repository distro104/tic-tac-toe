import pygame
from pygame.locals import *

''' Class responsible to create bottons '''
class Button:
	def __init__(self, screen = None,  dimension = (30,50), position = (0,0), text = None, color = (68,24,20)):
		self.screen = screen
		self.dimension = dimension
		self.position = position
		self.color = (68, 24, 20)
		self.text = text
		self.text_style = None
		self.text_color = (68, 24, 20)
		self.text_display = None
		self.text_coordenate = position
		self.active = False

	def set_style(self, font='Comic Sans MS', color=None, size=50):
		if color == None:
			color = self.text_color
		self.text_style = pygame.font.SysFont(self.text, size)
		self.text_display = self.text_style.render(self.text, False, color)

	def text_ajust_xy(self, ajust=None):
		if ajust != None:
			ajust_x, ajust_y = ajust
			position_x, position_y = self.position
			ajust_x += position_x
			ajust_y += position_y
			self.text_coordenate =  ((ajust_x, ajust_y))
		else:
			self.text_coordenate = self.position

	def draw(self):
		pygame.draw.rect(self.screen, self.color,((self.position), (self.dimension)))
		self.screen.blit(self.text_display, self.text_coordenate)

	def click(self, mouse_position):
		mouse_position_x, mouse_position_y = mouse_position
		button_position_x, button_position_y = self.position
		button_size_x, button_size_y = self.dimension
		if mouse_position_x in range(button_position_x, button_position_x+button_size_x):
			if mouse_position_y in range(button_position_y, button_position_y + button_size_y):
				print(f'Area buttom press {mouse_position}')
				return True
			else:
				return False
		'''
		# Button Start
		button1_dimension = (250,50)
		button1_position = (0, 500)
		button1_color = (0,50,50)
		button1_color_text = (10,10,0)
		#Text Button
		text = 'Start Game'
		myfont = pygame.font.SysFont('Comic Sans MS', 50)
		
		pygame.draw.rect(screen, button1_color,((button1_position),(button1_dimension)))
		
		textsurface = myfont.render(text, False, (10, 10, 10))
		screen.blit(textsurface,((35, 510)))

		#board1.array_board[0][0][0] = 2
		#board1.array_board[0][1][0] = 1
		#board1.array_board[0][2][0] = 1
		#board1.array_board[1][0][0] = 2
		#board1.array_board[1][1][0] = 1
		#board1.array_board[1][2][0] = 1
		#board1.array_board[2][0][0] = 2
		#board1.array_board[2][1][0] = 1
		#Sboard1.array_board[2][2][0] = 2
		'''
import pygame
from pygame.locals import *


''' Class responsible to create the menu bottons '''
class Button:
	def __init__(self, screen = None,  dimension = (30,50), position = (0,0), text = None, color = (68,24,20)):
		self.screen = screen
		self.dimension = dimension
		self.position = position
		self.color = (68,24,20)
		self.text = text
		self.text_style = None
		self.text_color = (68,24,20)
		self.text_display = None
	



	def set_style(self, font = 'Comic Sans MS', color = None, size = 50):
		if (color == None):
			color = self.text_color
		self.text_style = pygame.font.SysFont(self.text, size)
		self.text_display = self.text_style.render(self.text, False, color)
		
	def text_ajust_xy(self,ajust = None):
		if (ajust != None):
			ajust_x, ajust_y = ajust
			position_x, position_y = self.position
			ajust_x += position_x
			ajust_y += position_y
			return ((ajust_x,ajust_y))
		else:
			return self.position

	def draw(self):
		pygame.draw.rect(self.screen, self.color,((self.position),(self.dimension)))
		self.screen.blit(self.text_display, self.text_ajust_xy((80,10)))

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
	'''
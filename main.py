import pygame, random, sys, time
from pygame.locals import *
from board import Board
from button import Button

# Initializiang Pygame
pygame.init()

# Screen
SCREEN_SIZE = 500

board1 = Board(SCREEN_SIZE)

IMG_SIZE = ( board1.element_size , board1.element_size )
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE + 50))
pygame.display.set_caption("TicTacToe")

IMG_X = pygame.transform.scale(pygame.image.load("images/x.png"),IMG_SIZE)
IMG_O = pygame.transform.scale(pygame.image.load("images/o.png"),IMG_SIZE)

BACKGROUND_IMAGE = pygame.image.load("images/background.png")
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (SCREEN_SIZE,SCREEN_SIZE))

button_dimension = (250,50)
button_position = (0, 500)
button_color = (0,50,50)
button_start = Button(screen, button_dimension, button_position, 'Start!!', button_color)


################################### main part ###################################
program_runing = True

while program_runing:
	
	player_turn = 1 # need implement rand
	if (player_turn == 1):
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				program_runing = False
				sys.exit()

			if(event.type == pygame.MOUSEBUTTONDOWN):
				mouse_position = pygame.mouse.get_pos()
				board1.set_element(mouse_position,1)
				print(f'Jogador clicou na posicao: {mouse_position}')
				player_turn = 2
				
	elif(player_turn == 2):
		print('Turno da maquina!!')
		player_turn = 1

	#board1.array_board[0][0][0] = 2
	#board1.array_board[0][1][0] = 1
	#board1.array_board[0][2][0] = 1
	#board1.array_board[1][0][0] = 2
	#board1.array_board[1][1][0] = 1
	#board1.array_board[1][2][0] = 1
	#board1.array_board[2][0][0] = 2
	#board1.array_board[2][1][0] = 1
	#Sboard1.array_board[2][2][0] = 2
	
	screen.blit(BACKGROUND,(0,0))

	button_start.set_style('Comic Sans MS',(0,0,50))
	button_start.draw()
	
	board1.plot_board(screen, IMG_X, IMG_O)
	
	'''
	# Button Start
	button1_dimension = (250,50)
	button1_position = (0, 500)
	button1_color = (0,50,50)
	button1_color_text = (10,10,0)
	#Text Button
	text = 'Start Game'
	myfont = pygame.font.SysFont('Comic Sans MS', 50)
	
	textsurface = myfont.render(text, False, (10, 10, 10))

	pygame.draw.rect(screen, button1_color,((button1_position),(button1_dimension)))
	screen.blit(textsurface,((35, 510)))
	'''
	pygame.display.update()
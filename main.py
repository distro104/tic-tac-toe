import time
import pygame
from pygame.locals import *
from board import Board


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
SQUARECOLOR = (255,100,100)

BACKGROUND_IMAGE = pygame.image.load("images/background.png")
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (SCREEN_SIZE,SCREEN_SIZE))

################################### main part ###################################
turn = True
game_runing = True
while game_runing:
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()

		if (turn == True):
			print("Player Turn!!!")
			if (event.type == pygame.MOUSEBUTTONDOWN):
				mouse_position = pygame.mouse.get_pos()
				print( mouse_position )
				board1.set_element(mouse_position,1)
				turn = False
		elif (turn == False): 
			print("Machine Turn!!!")
			time.sleep(2)
			turn = True

	#Proting images
	screen.blit(BACKGROUND,(0,0))

	#pygame.draw.line(screen, (100,100,100), [170, 0], [170,500], 11)
	#pygame.draw.line(screen, (100,100,100), [330, 0], [330,500], 11)
	#pygame.draw.line(screen, (100,100,100), [0, 170], [500,170], 11)
	#pygame.draw.line(screen, (100,100,100), [0, 330], [500,330], 11)

	#board1.array_board[0][0][0] = 2
	#board1.array_board[0][1][0] = 1
	#board1.array_board[0][2][0] = 1
	#board1.array_board[1][0][0] = 2
	#board1.array_board[1][1][0] = 1
	#board1.array_board[1][2][0] = 1
	#board1.array_board[2][0][0] = 2
	#board1.array_board[2][1][0] = 1
	#board1.array_board[2][2][0] = 2


	board1.plot_board(screen, IMG_X, IMG_O)

	
	pygame.display.update()
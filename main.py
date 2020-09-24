import time
import pygame
from pygame.locals import *
from board import Board


# Initializiang Pygame
pygame.init()

# Screen
SCREEN_SIZE = 500
IMG_SIZE = ( round(SCREEN_SIZE / 3) , round(SCREEN_SIZE / 3) )
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("TicTacToe")

IMG_X = pygame.transform.scale(pygame.image.load("images/x.png"),IMG_SIZE)
IMG_O = pygame.transform.scale(pygame.image.load("images/o.png"),IMG_SIZE)
SQUARECOLOR = (255,100,100)

BACKGROUND_IMAGE = pygame.image.load("images/background.png")
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (SCREEN_SIZE,SCREEN_SIZE))


board1 = Board(SCREEN_SIZE)


turn = True

# Function responsible to plot the elements in the board
def plot_board():
	# get coordenates((x , y)) -> print (board1.array_board[0][0][0])
	# plot the image -> screen.blit(IMG_O, (0,0))
	for x in range(len(board1.array_board)):
		for y in range(len(board1.array_board[x])):
			cordx,cordy = board1.array_board[y][x][1]
			if (board1.array_board[x][y][0]) == 1:
				screen.blit(IMG_O, (cordx,cordy))
			elif (board1.array_board[x][y][0]) == 2:
				screen.blit(IMG_X, (cordx,cordy))


################################### main part ###################################
game_runing = True
while game_runing:
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()

		if (turn == True) and (event.type == pygame.MOUSEBUTTONDOWN):
			mouse_position = pygame.mouse.get_pos()
			print( mouse_position )
			turn = False
		elif (turn == False): 
			time.sleep(3)
			print("Hello its my turn!!!")
			turn = True




	#Proting images
	screen.blit(BACKGROUND,(0,0))

	board1.array_board[0][0][0] = 1
	board1.array_board[1][1][0] = 1
	board1.array_board[2][2][0] = 1

	print(board1.array_board[2][1])


	plot_board()

	
	pygame.display.update()
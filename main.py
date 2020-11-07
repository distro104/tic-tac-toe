import pygame
import sys
from pygame.locals import *
from board import Board
from button import Button

# Initializing Pygame
pygame.init()

# Screen
SCREEN_SIZE = 500

board1 = Board(SCREEN_SIZE)

IMG_SIZE = (board1.element_size, board1.element_size)
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE + 50))
pygame.display.set_caption("TicTacToe")

IMG_X = pygame.transform.scale(pygame.image.load("images/x.png"), IMG_SIZE)
IMG_O = pygame.transform.scale(pygame.image.load("images/o.png"), IMG_SIZE)

BACKGROUND_IMAGE = pygame.image.load("images/background.png")
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (SCREEN_SIZE, SCREEN_SIZE))

button_dimension = (250, 50)
button_position = (0, 500)
button_color = (0, 50, 50)
button_start = Button(screen, button_dimension, button_position, 'Start!!', button_color)

# main part
running = True
while running:
    player_turn = 1  # need implement rand
    if player_turn == 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                running = False
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                board1.set_element_player(mouse_position, 1)
                print(f'Player mouse position: {mouse_position}')
                board1.set_element_player(mouse_position, 1)
                player_turn = 2
                board1.is_winner(1)
    elif player_turn == 2:
        print('Machine turn!!')
        player_turn = 1

    screen.blit(BACKGROUND, (0, 0))

    button_start.set_style('Comic Sans MS', (0, 0, 50))

    button_start.draw()
    button_start.text_ajust_xy((80, 10))
    board1.plot_board(screen, IMG_X, IMG_O)

    pygame.display.update()

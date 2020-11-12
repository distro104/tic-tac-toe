# Class responsable to machide decisions in  game
from random import *


class Machine:
    def __init__(self, board=[]):
        pass

    def play(self, board):
        while True:
            rand_x = randint(0, 2)
            rand_y = randint(0, 2)
            if board[rand_x][rand_y][0] == 0:
                return rand_x, rand_y
                break

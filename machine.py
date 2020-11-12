# Class responsable to machide decisions in  game
import random


class Machine:
    def __init__(self, board=[]):
        self.board = board

    def play(self):
        while True:
            rand_x = random.randint(0, 2)
            rand_y = random.randint(0, 2)
            if 0 == self.board[rand_x][rand_y][0]:
                return rand_y, rand_y
                break


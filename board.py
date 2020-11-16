import pygame

''' Class responsible to set the board '''


class Board:
    def __init__(self, size=500, column=3, margin=10):
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
        width, height = self.element_size, self.element_size
        for i in range(self.column):
            self.array_board.append([])
            for j in range(self.column):
                self.array_board[i].append([0, (coordy, coordx)])
                coordx += (width + self.margin)
            coordx = self.margin
            coordy += (height + self.margin)

    # Function: plot the elements in the board
    # Obs: Need to fix the lines in the board, in this case they are fixed and need to follow the size of the board!!!!
    def plot_board(self, screen, IMG_X, IMG_O):
        # get coordinates((x , y)) -> print (self.array_board[0][0][0])
        # plot the image -> screen.blit(IMG_O, (0,0))
        pygame.draw.line(screen, (100, 100, 100), [170, 0], [170, 500], 11)
        pygame.draw.line(screen, (100, 100, 100), [330, 0], [330, 500], 11)
        pygame.draw.line(screen, (100, 100, 100), [0, 170], [500, 170], 11)
        pygame.draw.line(screen, (100, 100, 100), [0, 330], [500, 330], 11)
        for x in range(len(self.array_board)):
            for y in range(len(self.array_board[x])):
                coordx, coordy = self.array_board[y][x][1]
                if (self.array_board[x][y][0]) == 1:
                    screen.blit(IMG_O, (coordx, coordy))
                elif self.array_board[x][y][0] == 2:
                    screen.blit(IMG_X, (coordx, coordy))

    # Function: Set an element X or O in the board for a player
    # Obs: if the player parameter is not passed the function set the element with 0 (No player)
    def set_element_player(self, coordxy_mouse, player=0):
        coordx_mouse, coordy_mouse = coordxy_mouse
        for i, line in enumerate(self.array_board):
            for j, element in enumerate(line):
                if coordx_mouse in range(element[1][0], element[1][0] + self.element_size):
                    if coordy_mouse in range(element[1][1], element[1][1] + self.element_size):
                        if self.array_board[j][i][0] == 0:
                            self.array_board[j][i][0] = player
                            return True
                        else:
                            return False

    def set_machine_choice(self, coord_x, coord_y):
        self.array_board[coord_x][coord_y][0] = 2

    # Function: Verify the elements on board searching the player winner condicton is True.
    def is_winner(self, player):
        is_winner = False
        if self.array_board[0][0][0] == player and self.array_board[0][1][0] == player and self.array_board[0][2][
            0] == player:
            is_winner = True
        if self.array_board[1][0][0] == player and self.array_board[1][1][0] == player and self.array_board[1][2][
            0] == player:
            is_winner = True
        if self.array_board[2][0][0] == player and self.array_board[2][1][0] == player and self.array_board[2][2][
            0] == player:
            is_winner = True
        if self.array_board[0][0][0] == player and self.array_board[1][0][0] == player and self.array_board[2][0][
            0] == player:
            is_winner = True
        if self.array_board[0][1][0] == player and self.array_board[1][1][0] == player and self.array_board[2][1][
            0] == player:
            is_winner = True
        if self.array_board[0][2][0] == player and self.array_board[1][2][0] == player and self.array_board[2][2][
            0] == player:
            is_winner = True
        if self.array_board[0][0][0] == player and self.array_board[1][1][0] == player and self.array_board[2][2][
            0] == player:
            is_winner = True
        if self.array_board[0][2][0] == player and self.array_board[1][1][0] == player and self.array_board[2][0][
            0] == player:
            is_winner = True
        return is_winner

    def is_full(self):
        is_full = False
        for i in self.array_board:
            if 0 == i[0][0]:
                is_full = True
        return is_full

    def clean(self):
        for i, list in enumerate(self.array_board):
            for j, list2 in enumerate(list):
                self.array_board[i][j][0] = 0
                print('Board cleaned!!')

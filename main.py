#!/bin/env python3
# ! -*- coding: utf-8 -*-

THINKING_DEPTH = 4


class Color(object):
    EMPTY = 0
    WHITE = 1
    BLACK = 2

    @classmethod
    def invert(cls, color):
        if color == cls.EMPTY:
            return color
        return cls.BLACK if color == cls.WHITE else cls.WHITE


class Empty(object):
    color = Color.EMPTY
    CODE = 'empty'

    def get_moves(self, board, x, y):
        return None

    def rate(self, board, x, y):
        return None

    def __str__(self):
        return ' '


class ChessMan(object):
    IMG = None

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return self.IMG[0 if self.color == Color.WHITE else 1]

    def get_left_up(self, board, x, y):
        # left+up, right+down
        moves = []
        for j in (-1, 1):
            rl = x + j
            ud = y + j
            while 0 <= rl <= 7 and 0 <= ud <= 7:
                color = board.get_color(rl, ud)
                if color == self.color:
                    break
                moves.append([rl, ud])
                if color != Color.EMPTY:
                    break
                rl += j
                ud += j
        return moves

    def get_right_up(self, board, x, y):
        # right+up, left+down
        moves = []
        for j in (-1, 1):
            rl = x + j
            ud = y + (-j)
            while 0 <= rl <= 7 and 0 <= ud <= 7:
                color = board.get_color(rl, ud)
                if color == self.color:
                    break
                moves.append([rl, ud])
                if color != Color.EMPTY:
                    break
                rl += j
                ud += -j
        return moves

    def get_horizont(self, board, x, y):
        ## on horizontally
        moves = []
        for j in (-1, 1):
            i = x + j
            while 0 <= i <= 7:
                color = board.get_color(i, y)
                if color == self.color:
                    break
                moves.append([i, y])
                if color != Color.EMPTY:
                    break
                i += j
        return moves

    def get_vertical(self, board, x, y):
        ## on vertically
        moves = []
        for j in (-1, 1):
            i = y + j
            while 0 <= i <= 7:
                color = board.get_color(x, i)
                if color == self.color:
                    break
                moves.append([x, i])
                if color != Color.EMPTY:
                    break
                i += j
        return moves


class Pawn(ChessMan):
    IMG = ('♟', '♙')
    CODE = 'pawn'
    VALUE = 10

    def get_moves(self, board, x, y):
        moves = []

        #### BLACK
        if self.color == Color.BLACK and y < 7 and board.get_color(x, y + 1) == Color.EMPTY:
            moves.append([x, y + 1])
        if self.color == Color.BLACK and y == 1 and board.get_color(x, y + 1) == Color.EMPTY and board.get_color(x,
                                                                                                                 y + 2) == Color.EMPTY:
            moves.append([x, y + 2])
        if self.color == Color.BLACK:
            for i in range(8):
                for j in range(8):
                    if abs(y - i) == abs(x - j) and i > y and j < (x + 2) and j > (x - 2):
                        if board.get_color(j, i) == Color.WHITE:
                            moves.append([j, i])

        #### WHITE
        if self.color == Color.WHITE and y > 0 and board.get_color(x, y - 1) == Color.EMPTY:
            moves.append([x, y - 1])
        if self.color == Color.WHITE and y == 6 and board.get_color(x, y - 1) == Color.EMPTY and board.get_color(x,
                                                                                                                 y - 2) == Color.EMPTY:
            moves.append([x, y - 2])
        if self.color == Color.WHITE:
            for i in range(8):
                for j in range(8):
                    if abs(y - i) == abs(x - j) and i < y and j < (x + 2) and j > (x - 2):
                        if board.get_color(j, i) == Color.BLACK:
                            moves.append([j, i])

        return moves

    def rate(self, board, x, y):
        return self.VALUE + 1 * (8 - y if self.color == Color.WHITE else y)


class King(ChessMan):
    IMG = ('♚', '♔')
    CODE = 'king'
    VALUE = 100

    def get_moves(self, board, x, y):
        moves = []

        for i in range(8):
            for j in range(8):
                if ((x == j) and ((y < (i + 2) and y > (i - 2)))) or ((y == i) and x > (j - 2) and x < (j + 2)) or (
                        abs(y - i) == abs(x - j) and (j < (x + 2) and j > (x - 2))):
                    if board.get_color(j, i) != self.color:
                        moves.append([j, i])

        return moves

    def rate(self, board, x, y):
        return self.VALUE


class Queen(ChessMan):
    IMG = ('♛', '♕')
    CODE = 'queen'
    VALUE = 75

    def get_moves(self, board, x, y):
        moves = []

        m1 = self.get_left_up(board, x, y)
        m2 = self.get_right_up(board, x, y)
        m3 = self.get_horizont(board, x, y)
        m4 = self.get_vertical(board, x, y)
        moves += m1 + m2 + m3 + m4

        return moves

    def rate(self, board, x, y):
        return self.VALUE


class Bishop(ChessMan):
    IMG = ('♝', '♗')
    CODE = 'bishop'
    VALUE = 50

    def get_moves(self, board, x, y):
        moves = []
        m1 = self.get_left_up(board, x, y)
        m2 = self.get_right_up(board, x, y)
        moves += m1 + m2

        return moves

    def rate(self, board, x, y):
        return self.VALUE


class Rook(ChessMan):
    IMG = ('♜', '♖')
    CODE = 'rook'
    VALUE = 50

    def get_moves(self, board, x, y):
        moves = []
        m1 = self.get_horizont(board, x, y)
        m2 = self.get_vertical(board, x, y)
        moves += m1 + m2
        return moves

    def rate(self, board, x, y):
        return self.VALUE


class Knight(ChessMan):
    IMG = ('♞', '♘')
    CODE = 'knight'
    VALUE = 25

    def get_moves(self, board, x, y):
        moves = []
        for i in range(1, 9):
            if i == 1 and x + 2 <= 7 and y - 1 >= 0:
                color = board.get_color(x + 2, y - 1)
                if color != self.color:
                    moves.append([x + 2, y - 1])
            elif i == 2 and x + 2 <= 7 and y + 1 <= 7:
                color = board.get_color(x + 2, y + 1)
                if color != self.color:
                    moves.append([x + 2, y + 1])
            elif i == 3 and y + 2 <= 7 and x + 1 <= 7:
                color = board.get_color(x + 1, y + 2)
                if color != self.color:
                    moves.append([x + 1, y + 2])
            elif i == 4 and y + 2 <= 7 and x - 1 >= 0:
                color = board.get_color(x - 1, y + 2)
                if color != self.color:
                    moves.append([x - 1, y + 2])
            elif i == 5 and x - 2 >= 0 and y + 1 < 7:
                color = board.get_color(x - 2, y + 1)
                if color != self.color:
                    moves.append([x - 2, y + 1])
            elif i == 6 and x - 2 >= 0 and y - 1 >= 0:
                color = board.get_color(x - 2, y - 1)
                if color != self.color:
                    moves.append([x - 2, y - 1])
            elif i == 7 and x - 1 >= 0 and y - 2 >= 0:
                color = board.get_color(x - 1, y - 2)
                if color != self.color:
                    moves.append([x - 1, y - 2])
            elif i == 8 and y - 2 >= 0 and x + 1 <= 7:
                color = board.get_color(x + 1, y - 2)
                if color != self.color:
                    moves.append([x + 1, y - 2])

        return moves

    def rate(self, board, x, y):
        return self.VALUE


class Board(object):
    next_move = 1

    def __init__(self):
        self.board = [[Empty()] * 8 for y in range(8)]
        for x in range(8):
            self.board[1][x] = Pawn(Color.BLACK)
        for x in range(8):
            self.board[6][x] = Pawn(Color.WHITE)

        self.board[0][3] = King(Color.BLACK)
        self.board[7][3] = King(Color.WHITE)

        self.board[0][4] = Queen(Color.BLACK)
        self.board[7][4] = Queen(Color.WHITE)

        self.board[0][2] = Bishop(Color.BLACK)
        self.board[0][5] = Bishop(Color.BLACK)
        self.board[7][2] = Bishop(Color.WHITE)
        self.board[7][5] = Bishop(Color.WHITE)

        self.board[0][0] = Rook(Color.BLACK)
        self.board[0][7] = Rook(Color.BLACK)
        self.board[7][0] = Rook(Color.WHITE)
        self.board[7][7] = Rook(Color.WHITE)

        self.board[0][1] = Knight(Color.BLACK)
        self.board[0][6] = Knight(Color.BLACK)
        self.board[7][1] = Knight(Color.WHITE)
        self.board[7][6] = Knight(Color.WHITE)

    def clone(self):
        cb = Board()
        cb.board = [self.board[i][:] for i in range(8)]
        return cb

    def get_color(self, x, y):
        return self.board[y][x].color

    def set_color(self, color):
        return '\033[%sm' % color

    def get_moves(self, x, y):
        return self.board[y][x].get_moves(self, x, y)

    def move(self, xy_from, xy_to):
        captured = self.board[xy_to[1]][xy_to[0]]
        self.board[xy_to[1]][xy_to[0]] = self.board[xy_from[1]][xy_from[0]]
        self.board[xy_from[1]][xy_from[0]] = Empty()
        return captured

    def get_chessman(self, x, y):
        return self.board[y][x]

    def rate(self, color):
        res = 0
        pawn_x_position = []
        for y in range(8):
            for x in range(8):
                if self.get_color(x, y) != color:
                    continue
                chessman = self.get_chessman(x, y)
                res += chessman.rate(self, x, y)
                if chessman.CODE == 'pawn':
                    pawn_x_position.append(x)
        # double pawns reduce the rate
        p = pawn_x_position
        res += 2 * (len(set(p)) - len(p))
        # alone pawn reduce the rate
        for i in range(1, 6):
            if i in p and (i - 1) not in p and (i + 1) not in p:
                res -= 2
        return res

    def __str__(self):
        colors = [0, 45]
        res = ''
        i = 0

        for y in range(8):
            for x in range(8):
                res += self.set_color(colors[i]) + str(self.board[y][x]) + ' '
                i = 1 - i
            i = 1 - i
            res += self.set_color(0) + "\n"
        return res


class AI(object):
    def __init__(self, my_color, depth):
        self.my_color = my_color
        self.enemy_color = Color.invert(my_color)
        self.depth = depth

    def do(self, board, depth=0):
        enemy = bool(depth % 2)
        color = self.enemy_color if enemy else self.my_color
        if depth == self.depth:
            return board.rate(self.my_color) - board.rate(self.enemy_color) * 1.1
        rates = []
        for y in range(8):
            for x in range(8):
                if board.get_color(x, y) != color:
                    continue
                xy_from = [x, y]
                for xy_to in board.get_moves(x, y):
                    new_board = board.clone()
                    target_cell = new_board.move(xy_from, xy_to)
                    captured = target_cell.CODE != 'empty'
                    if captured and target_cell.CODE == 'king':
                        rate = -1000 if enemy else 1000  # king capturing
                    else:
                        rate = self.do(new_board, depth + 1)
                        if rate is None:
                            continue
                        if captured and not enemy:
                            rate += self.depth - depth  # a little more aggression
                    if depth:
                        rates.append(rate)
                    else:
                        rates.append([rate, xy_from, xy_to])
        if not depth:
            return rates
        if not rates:
            return None
        rate = min(rates) if enemy else max(rates)
        return rate


### START GAME
b = Board()
print(b)

while True:
    p = input(":> ")
    if p == "exit" or p == "quit":
        print("By by", p)
        exit()
    try:
        coor_from, coor_to = p.split()
    except:
        continue
    from_y, from_x = 8 - int(coor_from[1]), ord(coor_from[0]) - 97
    to_y, to_x = 8 - int(coor_to[1]), ord(coor_to[0]) - 97

    moves = b.get_moves(from_x, from_y)
    if moves is None:
        print("Invalid move, try again!")
        continue

    if [to_x, to_y] in moves:
        # if b.get_color(from_x, from_y) == b.next_move:
        #     b.next_move = 1 if b.next_move == 2 else 2
        # else:
        #     print(f"move is {'white' if b.next_move == 1 else 'black'}")
        #     continue

        if b.get_color(from_x, from_y) != Color.WHITE:
            print("You move is white")
            continue

        b.move([from_x, from_y], [to_x, to_y])
        print(b)
        # print(moves)

        ### move is black AI
        color = Color.BLACK
        max_rate = -9999
        xy_from = xy_to = None
        rates = AI(color, THINKING_DEPTH).do(b)
        for rate in rates:
            if rate[0] < max_rate:
                continue
            max_rate, xy_from, xy_to = rate
        if not xy_from:
            print('end')
            exit()
        b.move(xy_from, xy_to)
        print(b)

    else:
        print("Invalid move, try again!")



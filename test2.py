#!/usr/bin/python3

import random

coor = input(":> ")
y, x = 8 - int(coor[1]), ord(coor[0]) - 97

EMPTY = '☐'
board = [[EMPTY] * 8 for _ in range(8)]

# a[n][m] = 'K'
board[y][x] = "K"


## Knight все возможные ходы конем
# for i in range(1,9):
#     if i == 1 and x + 2 <= 7 and y - 1 >= 0:
#         board[y - 1][x + 2] = '*'
#     elif i == 2 and x + 2 <= 7 and y + 1 <= 7:
#         board[y + 1][x + 2] = '*'
#     elif i == 3 and y + 2 <= 7 and x + 1 <= 7:
#         board[y + 2][x + 1] = '*'
#     elif i == 4 and y + 2 <= 7 and x - 1 >= 0:
#         board[y + 2][x - 1] = '*'
#     elif i == 5 and x - 2 >= 0 and y + 1 < 7:
#         board[y + 1][x - 2] = '*'
#     elif i == 6 and x - 2 >= 0 and y - 1 >= 0:
#         board[y - 1][x - 2] = '*'
#     elif i == 7 and x - 1 >= 0 and y - 2 >= 0:
#         board[y - 2][x - 1] = '*'
#     elif i == 8 and y - 2 >= 0 and x + 1 <= 7:
#         board[y - 2][x + 1] = '*'

def get_moves(x, y):
    moves = []
    for i in range(1, 9):
        if i == 1 and x + 2 <= 7 and y - 1 >= 0:
            # board[y - 1][x + 2] = '*'
            if board[y - 1][x + 2] == EMPTY:
                moves.append([x + 2, y - 1])
        elif i == 2 and x + 2 <= 7 and y + 1 <= 7:
            # board[y + 1][x + 2] = '*'
            if board[y + 1][x + 2] == EMPTY:
                moves.append([x + 2, y + 1])
        elif i == 3 and y + 2 <= 7 and x + 1 <= 7:
            # board[y + 2][x + 1] = '*'
            if board[y + 2][x + 1] == EMPTY:
                moves.append([x + 1, y + 2])
        elif i == 4 and y + 2 <= 7 and x - 1 >= 0:
            # board[y + 2][x - 1] = '*'
            if board[y + 2][x - 1] == EMPTY:
                moves.append([x - 1, y + 2])
        elif i == 5 and x - 2 >= 0 and y + 1 < 7:
            # board[y + 1][x - 2] = '*'
            if board[y + 1][x - 2] == EMPTY:
                moves.append([x - 2, y + 1])
        elif i == 6 and x - 2 >= 0 and y - 1 >= 0:
            # board[y - 1][x - 2] = '*'
            if board[y - 1][x - 2] == EMPTY:
                moves.append([x - 2, y - 1])
        elif i == 7 and x - 1 >= 0 and y - 2 >= 0:
            # board[y - 2][x - 1] = '*'
            if board[y - 2][x - 1] == EMPTY:
                moves.append([x - 1, y - 2])
        elif i == 8 and y - 2 >= 0 and x + 1 <= 7:
            # board[y - 2][x + 1] = '*'
            if board[y - 2][x + 1] == EMPTY:
                moves.append([x + 1, y - 2])

    return moves


n = 1
p = [[x, y]]


# for line in board:
#     print(*line)

# m = get_moves(p[0][0] ,p[0][1])
# print(m)


# while n <= 64:
#     p = get_moves(x, y)
#     if len(p) == 0:
#         break
#     m = random.randrange(len(p))
#     x, y = p[m][0], p[m][1]
#     board[y][x] = n
#     n += 1

# for line in board:
#     print(*line)

# print(f"число ходов: {n}")

def ppp(depth, message):
    print(' ' * depth + message)


def do(is_me, depth):
    if depth == 3:
        return random.randint(0, 100)
    rates = []
    for i in ('ход 1', 'ход 2'):
        ppp(depth, ('Мой' if is_me else 'Противник') + ' ' + i)
        rate = do(not is_me, depth + 1)
        ppp(depth, 'Позииция оценена %d' % rate)
        rates.append(rate)
    ppp(depth, 'Из оценок %s выбираем %s' % (rates, 'лучшую' if is_me else 'худшую'))
    return max(rates) if is_me else min(rates)


print(do(True, 0))
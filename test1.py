#!/usr/bin/python3

from time import sleep


### BISHOP
size = 8
amount = 1
def print_board(board):
    for lines in range(size):
        print(*board[lines])
    print("")

board = [['☐'] * 8 for _ in range(8)]
board_2 = [['☐'] * 8 for _ in range(8)]

coor = input(":> ")
y, x = 8 - int(coor[1]), ord(coor[0]) - 97


board[y][x] = "B"


board[2][6] = "R"


moves = []
# лево+верх, право+низ
# for j in (-1, 1):
#     rl = x + j
#     ud = y + j
#     while 0 <= rl <= 7 and 0 <= ud <= 7:
#         # color = board[y][i]
#                 # if color == "R":
#                 #     break
#         board[ud][rl] = '*'
#         # moves.append([i, y])
#         # if color != '☐':
#         #     break
#         rl += j
#         ud += j
#         sleep(1)
#         for line in board:
#             print(*line)

# право+верх, лево+низ
for j in (-1, 1):
    rl = x + j
    ud = y + (-j)
    while 0 <= rl <= 7 and 0 <= ud <= 7:
        color = board[ud][rl]
        if color == "R":
            break
        board[ud][rl] = '*'
        # moves.append([i, y])
        # if color != '☐':
        #     break
        rl += j
        ud += -j
        sleep(1)
        for line in board:
            print(*line)

# for i in range(8):
#     for j in range(8):
#         if (board[i][j] != '☐' ):
#             n = 1
#             while 1 <= n <= 7:
#             # for n in range(1,8):
#                 color = board[i][n]
#                 if color == 'R':
#                     print("RRRRRRRRRRRRRRRRR")
#                     break
#                 if ((j+n < 8) and (i+n < 8)):
#                     board_2[i+n][j+n]="*"
#                 if ((j-n >= 0) and (i+n < 8)):
#                     board_2[i+n][j-n]="*"
#                 if ((j+n < 8) and (i-n >= 0)):
#                     board_2[i-n][j+n]="*"
#                 if ((j-n >= 0) and (i-n >= 0)):
#                     board_2[i-n][j-n]="*"
#                 n += 1
#                 for lines in range(8):
#                     print(*board_2[lines])
#                 sleep(1)
# print_board(board_2)

# zero=0
# for row in range(size):
#     zero = zero + board_2[row].count(0)

# print(zero)

# input()

import random
name=input("What is your name?")
boards = [[
         [3, 0, 6, 5, 0, 8, 4, 0, 0],
         [5, 2, 0, 0, 0, 0, 0, 0, 0],
         [0, 8, 7, 0, 0, 0, 0, 3, 1],
         [0, 0, 3, 0, 1, 0, 0, 8, 0],
         [9, 0, 0, 8, 6, 3, 0, 0, 5],
         [0, 5, 0, 0, 9, 0, 6, 0, 0],
         [1, 3, 0, 0, 0, 0, 2, 5, 0],
         [0, 0, 0, 0, 0, 0, 0, 7, 4],
         [0, 0, 5, 2, 0, 6, 3, 0, 0]
],
[
         [5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 8, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
]

matrix=random.choice(boards)

def solveSudoku(bo):
    find = findEmpty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solveSudoku(bo):
                return True
            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    box_n = pos[0] // 3
    box_r = pos[1] // 3

    for i in range(box_n*3, box_n*3 + 3):
        for j in range(box_r * 3, box_r*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

def findEmpty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)

    return None

def print_matrix(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - - - -")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = ' ')

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end = ' ')

print(name + ", this is the solved sudoku! ;D")
print_matrix(matrix)
solveSudoku(matrix)
print("_________________________________")
print_matrix(matrix)


#EXTRA MATRIX TO ADD ON..
# [
#          [3, 0, 0, 8, 0, 1, 0, 0, 2],
#          [2, 0, 1, 0, 3, 0, 6, 0, 4],
#          [0, 0, 0, 2, 0, 4, 0, 0, 0],
#          [8, 0, 9, 0, 0, 0, 1, 0, 6],
#          [4, 0, 0, 0, 0, 0, 0, 5, 1],
#          [7, 0, 0, 0, 0, 0, 4, 0, 9],
#          [0, 0, 0, 5, 0, 9, 0, 0, 0],
#          [9, 0, 4, 0, 8, 0, 7, 0, 5],
#          [6, 0, 0, 1, 0, 7, 0, 0, 3]
# ]
